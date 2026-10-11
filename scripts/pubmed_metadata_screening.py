#!/usr/bin/env python3
"""Create a public, unscreened PubMed bibliographic worksheet from ESearch PMIDs.

No patient data. NCBI EFetch PubMed XML is used to collect title, journal,
year, DOI, type, and abstract-PRESENT flags. Abstract TEXT is never exported:
PubMed abstracts may be copyrighted by publishers. The resulting worksheet
contains no automated eligibility verdict. This is not a systematic review.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

ENDPOINT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
SELECTED_QUERY = "B_LLM_LABORATORY"
MAX_IDS = 100
MAX_RETRIES = 3
PUBLIC_COLUMNS = [
    "pmid", "pubmed_url", "title", "journal", "year", "doi",
    "publication_types", "abstract_available",
    "reviewer_a_decision", "reviewer_b_decision",
    "conflict", "consensus", "full_text_status",
    "exclusion_reason", "screening_notes",
]


def text_content(element) -> str:
    if element is None:
        return ""
    return " ".join("".join(element.itertext()).split())


def parse_pubmed_xml(xml_bytes: bytes) -> dict[str, dict]:
    root = ET.fromstring(xml_bytes)
    if root.tag != "PubmedArticleSet":
        raise ValueError("Unexpected PubMed XML response root")
    found: dict[str, dict] = {}
    for item in root.findall("./PubmedArticle"):
        pmid = text_content(item.find("./MedlineCitation/PMID"))
        if not pmid.isdecimal() or pmid in found:
            raise ValueError("Missing, invalid or repeated PMID in EFetch response")
        article = item.find("./MedlineCitation/Article")
        if article is None:
            raise ValueError(f"Missing Article section for PMID {pmid}")
        title = text_content(article.find("./ArticleTitle"))
        if not title:
            raise ValueError(f"Missing article title for PMID {pmid}")

        journal = (text_content(article.find("./Journal/ISOAbbreviation"))
                   or text_content(article.find("./Journal/Title")))
        year = (text_content(article.find("./Journal/JournalIssue/PubDate/Year"))
                or text_content(article.find("./ArticleDate/Year")))
        if not year:
            md = text_content(article.find("./Journal/JournalIssue/PubDate/MedlineDate"))
            matched = re.search(r"\b(?:18|19|20)\d{2}\b", md)
            year = matched.group(0) if matched else ""

        doi = ""
        for identity in item.findall("./PubmedData/ArticleIdList/ArticleId"):
            if identity.attrib.get("IdType", "").lower() == "doi":
                doi = text_content(identity)
                break
        if not doi:
            for identity in article.findall("./ELocationID"):
                if identity.attrib.get("EIdType", "").lower() == "doi":
                    doi = text_content(identity)
                    break

        article_types = sorted({
            text_content(x) for x in article.findall("./PublicationTypeList/PublicationType")
            if text_content(x)
        })
        found[pmid] = {
            "pmid": pmid,
            "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
            "title": title, "journal": journal, "year": year,
            "doi": doi, "publication_types": "; ".join(article_types),
            "abstract_available": (
                "yes" if article.find("./Abstract/AbstractText") is not None else "no"
            ),
            "reviewer_a_decision": "", "reviewer_b_decision": "",
            "conflict": "", "consensus": "", "full_text_status": "",
            "exclusion_reason": "", "screening_notes": "",
        }
    return found


def request_xml(pmids: list[str], *, opener=urlopen, sleeper=time.sleep) -> bytes:
    """Bounded single PubMed GET request; no arbitrary URLs or patient data."""
    if not pmids or len(pmids) > MAX_IDS or any(not p.isdecimal() for p in pmids):
        raise ValueError("Expected 1-100 numeric PubMed identifiers")
    params = {
        "db": "pubmed", "id": ",".join(pmids), "retmode": "xml",
        "tool": "SOPGuardEvalBibliography",
    }
    url = ENDPOINT + "?" + urlencode(params)
    req = Request(url, headers={"User-Agent": "SOPGuardEvalBibliography/0.1 (public-metadata-only)"})
    for attempt in range(MAX_RETRIES):
        try:
            with opener(req, timeout=40) as response:
                return response.read()
        except (HTTPError, URLError, TimeoutError) as exc:
            if isinstance(exc, HTTPError) and exc.code not in (429, 500, 502, 503, 504):
                raise
            if attempt == MAX_RETRIES - 1:
                raise RuntimeError("PubMed EFetch unavailable after bounded retries") from exc
            sleeper(2 ** attempt)
    raise RuntimeError("unreachable")


def read_query_pmids(csv_path: Path, manifest_path: Path, query: str = SELECTED_QUERY) -> list[str]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    hits = [x for x in manifest["results"] if x.get("query_id") == query]
    if len(hits) != 1:
        raise ValueError("Expected exactly one query in search manifest")
    hit = hits[0]
    if not hit.get("complete_pmid_export"):
        raise ValueError("Query PMID export was truncated; refusing to prepare screening")
    ids: list[str] = []
    seen: set[str] = set()
    with csv_path.open("r", encoding="utf-8-sig", newline="") as inp:
        reader = csv.DictReader(inp)
        if reader.fieldnames != ["query_id", "pmid"]:
            raise ValueError("Expected only query_id,pmid CSV columns")
        for row in reader:
            if row["query_id"] != query:
                continue
            pmid = row["pmid"]
            if not pmid.isdecimal() or pmid in seen:
                raise ValueError("Invalid or duplicated PMID within target query")
            ids.append(pmid)
            seen.add(pmid)
    if len(ids) != hit["retrieved_count"] or len(ids) != hit["reported_count"]:
        raise ValueError("Manifest count disagrees with input PMID export")
    if not 0 < len(ids) <= MAX_IDS:
        raise ValueError("Query class exceeds bounded metadata exporter capacity")
    return ids


def generate(csv_path: Path, manifest_path: Path, output_dir: Path, *,
             requester=request_xml) -> dict:
    pmids = read_query_pmids(csv_path, manifest_path)
    xml_data = requester(pmids)
    rows_by_id = parse_pubmed_xml(xml_data)
    if set(rows_by_id) != set(pmids):
        missing = sorted(set(pmids) - set(rows_by_id))
        extra = sorted(set(rows_by_id) - set(pmids))
        raise ValueError(f"PubMed metadata mismatch; missing={missing}, extra={extra}")
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "lab_llm_screening_unscreened.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=PUBLIC_COLUMNS)
        writer.writeheader()
        for pmid in pmids:
            writer.writerow(rows_by_id[pmid])
    summary = {
        "source": "Public PubMed EFetch bibliographic metadata",
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "input_pmid_csv_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        "input_esearch_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "query_id": SELECTED_QUERY, "expected_pmids": len(pmids),
        "exported_rows": len(rows_by_id),
        "abstract_present_count": sum(
            x["abstract_available"] == "yes" for x in rows_by_id.values()
        ),
        "abstract_text_exported": False,
        "screening_decisions_made": 0,
        "automated_study_eligibility": False,
        "note": (
            "Public bibliographic worksheet only, not eligible studies. "
            "Abstracts may have publisher copyright; consult original PubMed links. "
            "Titles and metadata may require verification and correction by screeners."
        ),
    }
    (output_dir / "metadata_export_manifest.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Public bibliographic metadata; NO patient data")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(generate(args.input, args.manifest, args.output), indent=2))
    except Exception as exc:
        print(f"ERROR: PubMed metadata export FAILED: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
