#!/usr/bin/env python3
"""Deduplicate *public bibliographic IDs* exported by PubMed ESearch.

No clinical data, author/contact metadata, patient records, SOPs or LLM inference.
Produces cross-query memberships and checksummed audit metadata. This is not
study eligibility screening or a comprehensive literature search.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

EXPECTED_QUERIES = {"A_CBC_INTERFERENCE", "B_LLM_LABORATORY", "C_MEDICAL_LLM_SAFETY"}


def deduplicate(input_path: Path, output_dir: Path) -> dict:
    raw = input_path.read_bytes()
    groups: dict[str, set[str]] = defaultdict(set)
    occurrences = 0
    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["query_id", "pmid"]:
            raise ValueError("Expected only public query_id,pmid CSV columns")
        for row in reader:
            query_id, pmid = row["query_id"], row["pmid"]
            if query_id not in EXPECTED_QUERIES or not pmid.isdecimal() or not pmid:
                raise ValueError("Unexpected query class or non-numeric PMID")
            if pmid in groups[query_id]:
                raise ValueError("Duplicate PMID in same query export; integrity failure")
            groups[query_id].add(pmid)
            occurrences += 1
    if not groups:
        raise ValueError("Empty PMID export")
    union = set().union(*groups.values())
    membership = {pmid: sorted(query for query, members in groups.items() if pmid in members)
                  for pmid in union}
    query_names = sorted(EXPECTED_QUERIES)
    overlaps = {f"{a} + {b}": len(groups[a] & groups[b])
                for i, a in enumerate(query_names) for b in query_names[i + 1:]}
    summary = {
        "source_csv_sha256": hashlib.sha256(raw).hexdigest(),
        "processed_utc": datetime.now(timezone.utc).isoformat(),
        "source": "public PubMed ESearch bibliographic IDs",
        "method": "exact PMID string deduplication, preserving per-query membership",
        "original_occurrences": occurrences,
        "unique_pmids": len(union),
        "duplicate_occurrences": occurrences - len(union),
        "query_membership_counts": {q: len(groups[q]) for q in query_names},
        "pairwise_overlap_counts": overlaps,
        "all_queries_overlap": len(set.intersection(*(groups[q] for q in query_names))),
        "note": "Bibliographic identity only. No title/abstract/full-text eligibility or clinical review."
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "unique_pmid_export.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["pmid", "query_memberships"])
        for pmid in sorted(union, key=int):
            writer.writerow([pmid, ";".join(membership[pmid])])
    (output_dir / "deduplication_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return summary


def main():
    parser = argparse.ArgumentParser(description="Deduplicate public PubMed PMIDs only")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(deduplicate(args.input, args.output), indent=2))


if __name__ == "__main__":
    main()
