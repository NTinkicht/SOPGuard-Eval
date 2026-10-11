# Reproducible PubMed ESearch snapshot

**Status:** Public bibliography discovery utility. No patient or protected medical data, clinical SOP text or model prompts. This is **not** a systematic/scoping review on its own.

**First successful run:** [2026-10-11 results and counts](PUBMED_RUN_2026-10-11.md), with [archived exact query manifest](../literature/pubmed/2026-10-11/search_manifest.json). Subsequent runs may return different counts as PubMed indexing changes.

## Why

The prior targeted search identified relevant 2025–2026 CBC, laboratory LLM safety, SOP-reasoning, and abstention literature, but did not collect reproducible PubMed hit counts or PMID lists. A bounded ESearch workflow records the actual NCBI response (counts, query translation, PMIDs, run date and GitHub SHA), without inventing results.

## Exact source and scope

- Public NCBI [ESearch](https://www.ncbi.nlm.nih.gov/books/NBK25499/) API, `db=pubmed`, `retmode=json`, fixed three query strings versioned in [the script](../scripts/pubmed_search_snapshot.py).
- A: CBC analytical interference, haemolysis, lipaemia, agglutinins, autoverification.
- B: CBC or laboratory medicine and LLM/generative AI.
- C: LLMs in medical safety, SOPs, abstention or medical calculation.
- No language/date filters. Count is from NCBI ESearch **when the run executes**.
- A maximum of **2,000 PMID exports per class**. If NCBI finds more, `complete_pmid_export=false` and the CSV is expressly incomplete, although the count is still reported.
- These are **three partial topical searches, not a librarian-approved comprehensive strategy**. We still need additional systematic queries, citation chasing and institutional bibliographic databases.

## Run methods

**GitHub Actions:** select **PubMed literature search snapshot** in Actions and **Run workflow**. The workflow also triggers once when its YAML is initially merged to `main` (path-filtered), producing an artifact if NCBI is available. Repeated runs are manually invoked, not scheduled.

**Local:** `python scripts/pubmed_search_snapshot.py --output pubmed-search-output`.

## Outputs

- `search_manifest.json`: UTC timestamp, exact query strings, NCBI-reported counts, translated query, number of PMIDs actually retrieved, truncation status and Git commit SHA.
- `pmid_export.csv`: `query_id,pmid` rows, **public bibliographic identifiers only**, not screened papers or patient data.
- GitHub Actions artifact retention: 90 days. Download and archive approved literature records before expiration if they will support a manuscript methods section.

## Limitations and checks

1. Search results are time-sensitive; preserve exact dates, query strings, versions and counts.
2. The source's `querytranslation` is stored because PubMed may transform search syntax.
3. Counts can change during pagination; script fails rather than treating shifting counts as a complete export.
4. A complete PMID export is not deduplicated across query classes. Deduplication, dual screening and detailed extraction are separate work.
5. If the external NCBI API is blocked, job should **fail**, never fabricate counts or silently fall back to guessed bibliographic numbers.
6. If any query exceeds 2,000 entries, it is explicitly flagged as truncated. Expand the planned strategy safely to obtain complete screening lists, subject to research methodologist review.
7. Always follow NCBI E-utilities policies, bounded rate-limits and request retry limits. No API key is needed at this scale.

## Next research decisions

A completed public ESearch snapshot will support issue #3, but **will not close it** without screening, deduplication and other databases. Only update evidence logs with data actually observed from a successful run.
