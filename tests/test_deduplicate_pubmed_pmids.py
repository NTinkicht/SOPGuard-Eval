"""Tests use fictional bibliographic identifiers; no network or patient data."""
import csv
import json
import tempfile
import unittest
from pathlib import Path
from scripts.deduplicate_pubmed_pmids import deduplicate


class DeduplicatePubMedTests(unittest.TestCase):
    def test_overlaps_and_membership_preserved(self):
        with tempfile.TemporaryDirectory() as dir_name:
            root = Path(dir_name)
            inp = root / "in.csv"
            inp.write_text(
                "query_id,pmid\n"
                "A_CBC_INTERFERENCE,100\n"
                "A_CBC_INTERFERENCE,200\n"
                "B_LLM_LABORATORY,200\n"
                "B_LLM_LABORATORY,300\n"
                "C_MEDICAL_LLM_SAFETY,300\n"
                "C_MEDICAL_LLM_SAFETY,400\n", encoding="utf-8")
            result = deduplicate(inp, root / "out")
            self.assertEqual(result["original_occurrences"], 6)
            self.assertEqual(result["unique_pmids"], 4)
            self.assertEqual(result["duplicate_occurrences"], 2)
            self.assertEqual(result["pairwise_overlap_counts"]["A_CBC_INTERFERENCE + B_LLM_LABORATORY"], 1)
            self.assertEqual(result["pairwise_overlap_counts"]["B_LLM_LABORATORY + C_MEDICAL_LLM_SAFETY"], 1)
            with (root / "out" / "unique_pmid_export.csv").open(newline="") as handle:
                records = list(csv.DictReader(handle))
            self.assertEqual(len(records), 4)
            self.assertEqual(records[1]["query_memberships"], "A_CBC_INTERFERENCE;B_LLM_LABORATORY")
            self.assertNotIn("patient", json.dumps(result).lower())

    def test_duplicate_within_one_query_rejected(self):
        with tempfile.TemporaryDirectory() as dir_name:
            root = Path(dir_name)
            p = root / "input.csv"
            p.write_text("query_id,pmid\nB_LLM_LABORATORY,4\nB_LLM_LABORATORY,4\n")
            with self.assertRaises(ValueError):
                deduplicate(p, root / "out")

    def test_invalid_pmid_rejected(self):
        with tempfile.TemporaryDirectory() as dir_name:
            root = Path(dir_name)
            p = root / "input.csv"
            p.write_text("query_id,pmid\nB_LLM_LABORATORY,NOT_A_PMID\n")
            with self.assertRaises(ValueError):
                deduplicate(p, root / "out")

    def test_unexpected_columns_rejected(self):
        with tempfile.TemporaryDirectory() as dir_name:
            root = Path(dir_name)
            p = root / "input.csv"
            p.write_text("query_id,pmid,patient_id\nB_LLM_LABORATORY,100,abc\n")
            with self.assertRaises(ValueError):
                deduplicate(p, root / "out")

    def test_unrecognized_query_rejected(self):
        with tempfile.TemporaryDirectory() as dir_name:
            root = Path(dir_name)
            p = root / "input.csv"
            p.write_text("query_id,pmid\nPRIVATE_HOSPITAL,100\n")
            with self.assertRaises(ValueError):
                deduplicate(p, root / "out")


if __name__ == "__main__":
    unittest.main()
