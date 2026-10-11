"""Offline tests of public bibliographic metadata extraction; no NCBI calls or clinical data."""
import csv
import json
import tempfile
import unittest
from pathlib import Path

from scripts.pubmed_metadata_screening import (
    generate, parse_pubmed_xml, read_query_pmids, request_xml,
)

SYNTHETIC_XML = b"""<?xml version="1.0" encoding="utf-8"?>
<PubmedArticleSet>
 <PubmedArticle><MedlineCitation><PMID>101</PMID>
 <Article><Journal><JournalIssue><PubDate><Year>2026</Year></PubDate></JournalIssue>
 <ISOAbbreviation>Toy Res</ISOAbbreviation></Journal>
 <ArticleTitle>Purely <i>fictional</i> study number one</ArticleTitle>
 <Abstract><AbstractText>Copyrighted fictitious test abstract NEVER EXPORT ME.</AbstractText></Abstract>
 <PublicationTypeList><PublicationType>Journal Article</PublicationType></PublicationTypeList>
 </Article></MedlineCitation><PubmedData><ArticleIdList>
 <ArticleId IdType="doi">10.0000/fictional-test</ArticleId></ArticleIdList></PubmedData></PubmedArticle>
 <PubmedArticle><MedlineCitation><PMID>202</PMID>
 <Article><Journal><JournalIssue><PubDate><MedlineDate>2025 Fall</MedlineDate></PubDate></JournalIssue>
 <Title>Mock Journal</Title></Journal><ArticleTitle>Another imaginary article</ArticleTitle>
 </Article></MedlineCitation></PubmedArticle>
</PubmedArticleSet>"""


class MetadataScreeningTests(unittest.TestCase):
    def _inputs(self, root: Path):
        csvfile = root / "pmids.csv"
        csvfile.write_text(
            "query_id,pmid\nB_LLM_LABORATORY,101\nA_CBC_INTERFERENCE,999\n"
            "B_LLM_LABORATORY,202\n", encoding="utf-8"
        )
        manifest = root / "manifest.json"
        manifest.write_text(
            json.dumps({"results": [{
                "query_id": "B_LLM_LABORATORY", "retrieved_count": 2,
                "reported_count": 2, "complete_pmid_export": True
            }]}), encoding="utf-8"
        )
        return csvfile, manifest

    def test_xml_metadata_and_title_inline_markup(self):
        r = parse_pubmed_xml(SYNTHETIC_XML)
        self.assertEqual(set(r), {"101", "202"})
        self.assertEqual(r["101"]["title"], "Purely fictional study number one")
        self.assertEqual(r["101"]["doi"], "10.0000/fictional-test")
        self.assertEqual(r["202"]["journal"], "Mock Journal")
        self.assertEqual(r["202"]["year"], "2025")
        self.assertEqual(r["101"]["abstract_available"], "yes")
        self.assertEqual(r["202"]["abstract_available"], "no")
        self.assertNotIn("Copyrighted fictitious", repr(r))

    def test_generate_never_exports_abstract_text_or_screening_verdicts(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            inp, manifest = self._inputs(root)
            out = root / "output"
            provenance = generate(inp, manifest, out, requester=lambda _: SYNTHETIC_XML)
            self.assertEqual(provenance["exported_rows"], 2)
            self.assertFalse(provenance["abstract_text_exported"])
            self.assertEqual(provenance["screening_decisions_made"], 0)
            raw = (out / "lab_llm_screening_unscreened.csv").read_text()
            self.assertNotIn("Copyrighted fictitious", raw)
            with (out / "lab_llm_screening_unscreened.csv").open(newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual([r["pmid"] for r in rows], ["101", "202"])
            self.assertTrue(all(r["reviewer_a_decision"] == "" for r in rows))
            self.assertTrue(all(r["reviewer_b_decision"] == "" for r in rows))
            self.assertTrue(all(r["consensus"] == "" for r in rows))

    def test_manifest_count_mismatch_refused(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            inp, manifest = self._inputs(root)
            manifest.write_text(json.dumps({"results": [{
                "query_id": "B_LLM_LABORATORY", "retrieved_count": 3,
                "reported_count": 3, "complete_pmid_export": True
            }]}))
            with self.assertRaises(ValueError):
                read_query_pmids(inp, manifest)

    def test_truncated_manifest_refused(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            inp, manifest = self._inputs(root)
            manifest.write_text(json.dumps({"results": [{
                "query_id": "B_LLM_LABORATORY", "retrieved_count": 2,
                "reported_count": 4, "complete_pmid_export": False
            }]}))
            with self.assertRaises(ValueError):
                read_query_pmids(inp, manifest)

    def test_unexpected_pmid_refused(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            inp, manifest = self._inputs(root)
            with self.assertRaises(ValueError):
                generate(inp, manifest, root / "out",
                         requester=lambda _: SYNTHETIC_XML.replace(b"<PMID>202</PMID>", b"<PMID>303</PMID>"))

    def test_non_pubmed_root_refused(self):
        with self.assertRaises(ValueError):
            parse_pubmed_xml(b"<error>bad</error>")

    def test_no_private_columns_accepted(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            inp, manifest = self._inputs(root)
            inp.write_text("query_id,pmid,patient_id\nB_LLM_LABORATORY,101,private")
            with self.assertRaises(ValueError):
                read_query_pmids(inp, manifest)

    def test_duplicate_pmid_refused(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            inp, manifest = self._inputs(root)
            inp.write_text("query_id,pmid\nB_LLM_LABORATORY,101\nB_LLM_LABORATORY,101")
            with self.assertRaises(ValueError):
                read_query_pmids(inp, manifest)

    def test_missing_title_refused(self):
        with self.assertRaises(ValueError):
            parse_pubmed_xml(SYNTHETIC_XML.replace(b"Another imaginary article", b""))

    def test_request_rejects_non_numeric_ids_without_network(self):
        with self.assertRaises(ValueError):
            request_xml(["accession-HOSPITAL"])

    def test_no_abstract_decisions_in_generated_metadata(self):
        rows = parse_pubmed_xml(SYNTHETIC_XML)
        self.assertEqual(rows["101"]["screening_notes"], "")
        self.assertEqual(rows["101"]["full_text_status"], "")
        self.assertEqual(rows["202"]["conflict"], "")


if __name__ == "__main__":
    unittest.main()
