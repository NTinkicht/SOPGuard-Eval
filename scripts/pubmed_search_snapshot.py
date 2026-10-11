#!/usr/bin/env python3
"""Reproducible public PubMed metadata discovery. No clinical/patient data.

Uses NCBI ESearch via HTTPS to produce a dated JSON manifest and CSV of PMIDs.
A targeted metadata search is NOT a systematic review or independent screening.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ENDPOINT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
SEARCHES = {
    "A_CBC_INTERFERENCE": (
        '("Blood Cell Count"[MeSH Terms] OR "complete blood count"[Title/Abstract] '
        'OR "full blood count"[Title/Abstract] OR MCHC[Title/Abstract]) AND '
        '(interference[Title/Abstract] OR "cold agglutinin"[Title/Abstract] '
        'OR lipemia[Title/Abstract] OR lipaemia[Title/Abstract] '
        'OR hemolysis[Title/Abstract] OR haemolysis[Title/Abstract] '
        'OR autoverification[Title/Abstract])'
    ),
    "B_LLM_LABORATORY": (
        '("Blood Cell Count"[MeSH Terms] OR "complete blood count"[Title/Abstract] '
        'OR "laboratory medicine"[Title/Abstract]) AND '
        '("large language model"[Title/Abstract] OR "large language models"[Title/Abstract] '
        'OR ChatGPT[Title/Abstract] OR "generative AI"[Title/Abstract])'
    ),
    "C_MEDICAL_LLM_SAFETY": (
        '("large language model"[Title/Abstract] OR "large language models"[Title/Abstract]) '
        'AND (abstention[Title/Abstract] OR "patient safety"[Title/Abstract] '
        'OR "standard operating procedure"[Title/Abstract] '
        'OR "medical calculation"[Title/Abstract] OR "laboratory medicine"[Title/Abstract])'
    ),
}
MAX_EXPORT = 2000
PAGE_SIZE = 200
REQUEST_PAUSE_SECONDS = 0.4
MAX_RETRIES = 3


def request_json(params: dict[str, str | int], opener=urlopen, sleeper=time.sleep) -> dict:
    url = ENDPOINT + "?" + urlencode(params)
    if not url.startswith("https://eutils.ncbi.nlm.nih.gov/"):
        raise ValueError("Unexpected API destination")
    req = Request(url, headers={"User-Agent": "SOPGuard-Eval-research-search/0.1 (public metadata)"})
    for attempt in range(MAX_RETRIES):
        try:
            with opener(req, timeout=40) as response:
                data = json.load(response)
            if not isinstance(data, dict) or "esearchresult" not in data:
                raise ValueError("Unexpected NCBI ESearch response; cannot report hit counts")
            return data["esearchresult"]
        except (HTTPError, URLError, TimeoutError) as error:
            if isinstance(error, HTTPError) and error.code not in (429, 500, 502, 503, 504):
                raise
            if attempt >= MAX_RETRIES - 1:
                raise RuntimeError("NCBI ESearch unavailable after bounded retries") from error
            sleeper(2 ** attempt)
    raise AssertionError("unreachable")


def search_one(query_id: str, term: str, *, fetch=request_json, pause=time.sleep,
               limit: int = MAX_EXPORT) -> dict:
    if not 0 < limit <= MAX_EXPORT:
        raise ValueError("Requested limit outside controlled maximum")
    ids = []
    result_count = None
    translated_query = None
    start = 0
    while True:
        batch = min(PAGE_SIZE, limit - start)
        if batch <= 0:
            break
        result = fetch({
            "db": "pubmed", "term": term, "retmode": "json",
            "retstart": start, "retmax": batch, "sort": "pub date"
        })
        try:
            count = int(result["count"])
            returned = list(result["idlist"])
        except (KeyError, ValueError, TypeError) as error:
            raise ValueError("NCBI response is missing count or idlist") from error
        if count < 0 or any(not str(pmid).isdigit() for pmid in returned):
            raise ValueError("Invalid result count or PMID")
        if result_count is None:
            result_count = count
            translated_query = result.get("querytranslation")
        elif result_count != count:
            raise RuntimeError("Search count changed during pagination; rerun snapshot")
        ids.extend(str(pmid) for pmid in returned)
        start += len(returned)
        if start >= count or start >= limit or not returned:
            break
        pause(REQUEST_PAUSE_SECONDS)
    if len(ids) != len(set(ids)):
        raise RuntimeError("Duplicate PMIDs returned during pagination")
    if result_count is None or (result_count <= limit and len(ids) != result_count):
        raise RuntimeError("Incomplete ESearch response; refusing to call export complete")
    return {
        "query_id": query_id, "query": term, "query_translation": translated_query,
        "database": "pubmed", "reported_count": result_count,
        "retrieved_count": len(ids), "complete_pmid_export": len(ids) == result_count,
        "pmids": ids,
    }


def run_snapshot(output: Path, *, searches=SEARCHES, fetch=request_json,
                 pause=time.sleep, limit=MAX_EXPORT) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc).isoformat()
    results = []
    for query_id, term in searches.items():
        results.append(search_one(query_id, term, fetch=fetch, pause=pause, limit=limit))
        pause(REQUEST_PAUSE_SECONDS)
    manifest = {
        "provenance": "PubMed ESearch public bibliographic metadata only",
        "search_date_utc": started,
        "git_sha": os.environ.get("GITHUB_SHA", "not-recorded"),
        "endpoint": ENDPOINT, "query_scope": "targeted, NOT systematic/exhaustive",
        "unfiltered_search": True, "export_limit_per_query": limit,
        "note": ("'reported_count' is returned by NCBI on this date. "
                 "If complete_pmid_export is false, PMID export is TRUNCATED. "
                 "No deduplication between query classes or dual independent screening performed."),
        "results": [
            {key: value for key, value in result.items() if key != "pmids"}
            for result in results
        ],
    }
    (output / "search_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    with (output / "pmid_export.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["query_id", "pmid"])
        for result in results:
            for pmid in result["pmids"]:
                writer.writerow([result["query_id"], pmid])
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return manifest


def main():
    parser = argparse.ArgumentParser(
        description="Public PubMed query snapshot. Never send patient data or private SOPs.")
    parser.add_argument("--output", type=Path, default=Path("pubmed-search-output"))
    parser.add_argument("--max-export", type=int, default=MAX_EXPORT)
    args = parser.parse_args()
    try:
        run_snapshot(args.output, limit=args.max_export)
    except Exception as error:
        print(f"ERROR: PubMed search snapshot FAILED: {type(error).__name__}: {error}",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
