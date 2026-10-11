# PubMed metadata-assisted independent screening: first B-query tranche

**Research-only, public bibliographic metadata.** This procedure is **not** a systematic review, an automatic screening model, or evidence of eligible publications.

## Aim and provenance

The successful October 11, 2026 PubMed ESearch retrieved 40 PMIDs from query `B_LLM_LABORATORY` plus larger, separate CBC interference and medical-LLM-safety lists. Previous work performed exact PMID deduplication across 2,170 occurrences to 2,145 unique identifiers. This new step generates an **unreviewed, 40-record bibliographic screening worksheet**.

The source workflow reruns the public searches, then verifies each B-query PMID against the ESearch manifest. It calls the official NCBI EFetch PubMed XML endpoint, stores a SHA-256 of the source PMID CSV and manifest, and refuses to issue a complete export if any PMID is missing, duplicated or unexpected. Retrieval is bounded to 100 identifiers, with limited retries.

**Important:** The GitHub-run worksheet represents the query performed **in that run**, not necessarily the exact IDs from the October 11 snapshot. PubMed can update and re-index. The original dated manifest remains the historical record.

## Public worksheet fields

`pmid,pubmed_url,title,journal,year,doi,publication_types,abstract_available,reviewer_a_decision,reviewer_b_decision,conflict,consensus,full_text_status,exclusion_reason,screening_notes`

The reviewer and consensus cells are **empty**, and no study is called eligible merely because PubMed returned it.

## Copyright and review boundaries

NLM warns that PubMed abstracts may carry journal or author copyright and that NLM does **not** own their rights. Therefore, this repository and public GitHub Actions artifacts export **no abstract text**. `abstract_available` is only a boolean; reviewers can read source abstracts using their PubMed links and follow their institution's lawful access/reuse policies.

Sources: [NCBI policies](https://www.ncbi.nlm.nih.gov/home/about/policies/), [PubMed XML EFetch](https://www.ncbi.nlm.nih.gov/entrez/query/static/efetch_help.html), [NLM data copyright](https://www.nlm.nih.gov/databases/download.html).

## Running the next retrieval

1. Run the **PubMed literature search snapshot** GitHub Action using authorized repository controls (the workflow also runs when its workflow file changes on `main`).
2. Download its `pubmed-literature-snapshot` artifact, including fresh `search_manifest.json`, `pmid_export.csv`, `unique_pmid_export.csv`, and the new `lab_llm_screening_unscreened.csv` plus `metadata_export_manifest.json`.
3. Archive the original source files and their SHA-256 values according to research governance.
4. Assign **two actual human screeners** to B-query citations, following [screening workplan](SCREENING_WORKPLAN.md). Record decisions and disagreements; do not ask a single LLM to certify eligibility.
5. Broaden to A/C queries, Scopus/Web of Science/IEEE/ACM as permitted, and citation tracking before claiming comprehensive novelty coverage.

Do not commit PDF full texts, bulk abstract text, proprietary SOPs or any patient data.

## Study status

The utility does **not** evaluate CBC records, generate clinical correction instructions or score model safety. It only prepares bibliographic metadata. Its unit tests use fictional PMIDs and fabricated article titles.
