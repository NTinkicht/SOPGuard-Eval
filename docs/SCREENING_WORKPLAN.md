# SOPGuard-Eval literature screening handoff (bibliography prepared; screening not yet executed)

## Scope

The first reproducible PubMed targeted search on 2026-10-11 yielded **1727** CBC-interference hits, **40** LLM-laboratory hits and **403** medical-LLM-safety hits. Their verified PMID union is **2,145 unique identifiers**, with 25 duplicate occurrences (all B/C overlap); neither number represents eligible studies. See [executed snapshot](PUBMED_RUN_2026-10-11.md).

The 2026-10-11 GitHub workflow **successfully generated an unscreened 40-record B-query bibliographic worksheet (34 abstracts available, no abstract text exported and no eligibility decisions)**; see [executed verified run](PUBMED_METADATA_RUN_2026-10-11.md). The workflow prepares an **unscreened B-query bibliographic worksheet** with title, journal, DOI, year and abstract-availability flags only. See [copyright and workflow guidance](PUBMED_METADATA_SCREENING.md). No automated inclusion/exclusion decisions are made.

## Reviewer workflow

1. Retrieve `pmid_export.csv` from [GitHub run artifact](https://github.com/NTinkicht/SOPGuard-Eval/actions/runs/38119265189/artifacts/11694389255) and archive it with the versioned [manifest](../literature/pubmed/2026-10-11/search_manifest.json).
2. Use the new [deduplication utility](../scripts/deduplicate_pubmed_pmids.py) to reproduce 2,170 raw occurrences, 2,145 unique PMIDs and cross-query membership using the archived original CSV. The automatic workflow now produces a `unique_pmid_export.csv` in new runs. Preserve timestamped query-to-PMID provenance; counts may change with reindexing.
3. Obtain titles, journals, years, DOIs, publication types and abstract-availability flags from the public B-query worksheet. Read original abstracts at their PubMed links under publisher/institutional rights; do not redistribute bulk abstract text in GitHub artifacts.
4. Prioritize the **40 B-query citations** for full overlap with prior laboratory-LLM work, but do not treat them as the only relevant papers.
5. Predefine inclusion/exclusion taxonomy from [literature protocol](LITERATURE_SEARCH_PROTOCOL.md), including separately tagged consensus guidelines, vendor documents, preprints and primary empirical studies.
6. Use two independent human screeners when possible; preserve raw screening decisions, resolved conflicts, full-text exclusions and reasons. Never allow an LLM-only judge to certify the clinical evidence base.
7. Hand-code extraction of device, specimen cases, repeat outcomes, expert adjudication, action-level harm taxonomy, abstention, numerical validation and cross-vendor generalization.
8. Review newest papers again just before submission; publication indexing and evidence evolve.

## Output table to produce (no fake rows)

Use [blank evidence extraction template](evidence_log_template.csv), plus a screening log with fields: PMID, query_sources, study_title, abstract_available, decision_reviewer_A, decision_reviewer_B, conflict, consensus, full_text_status, exclusion_reason, reviewer_initials and evidence_verification_date.

The project has completed **PMID-level exact deduplication only**, not title/abstract or full-text screening. The presence of public PMIDs in an artifact is not evidence of eligibility.

## Clinical boundaries

Do not upload patient data, accession records, local lab SOPs or manufacturer manuals to a screening platform or this public repository. Screens use only lawful public bibliographic metadata and approved licensed documents.
