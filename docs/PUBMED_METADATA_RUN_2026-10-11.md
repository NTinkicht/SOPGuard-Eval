# Executed laboratory-LLM PubMed bibliography export — 2026-10-11

**Status: ESearch/EFetch bibliographic extraction completed and verified. Not screened, not eligible-study selection, not a systematic review.** No laboratory records or confidential procedures involved.

## Provenance (observed from actual GitHub Actions and downloaded artifact)

- [GitHub Actions run #38121808146](https://github.com/NTinkicht/SOPGuard-Eval/actions/runs/38121808146): `pubmed-public-metadata` job succeeded on main commit `b67111bf5eb34ef714c38059c2144b36c4a4c02b`.
- [Artifact #11695771749](https://github.com/NTinkicht/SOPGuard-Eval/actions/runs/38121808146/artifacts/11695771749): `pubmed-literature-snapshot`, including `pmid_export.csv`, `unique_pmid_export.csv`, `search_manifest.json`, `lab_llm_screening_unscreened.csv`, `metadata_export_manifest.json` and deduplication summary.
- Metadata retrieved (UTC): `2026-10-11T07:34:24.203754+00:00`.
- Archive ZIP SHA-256 (verified after download): `caf812ba8deacd77d916239a5a5bdf44c6044b0ac2241d090920472d3a2a61ef`.
- PMID input CSV SHA-256: `c32eb6385d9b9840710feafabc504666c18f2268450410313fc43721ac784cb0`.
- ESearch manifest SHA-256: `de51746b5c674b712a8b4fcf304dc8808a6a562e5456e14077b1bc0180c7b9bd`.
- Full run manifest is also preserved as [machine-readable metadata](../literature/pubmed/2026-10-11/metadata_export_manifest.json).

## Verified counts

| Measure | Observed |
| --- | ---: |
| B_LLM_LABORATORY PMIDs requested | 40 |
| EFetch PubMed records exported | 40 |
| With abstract available (presence flag only) | 34 |
| Without abstract flag | 6 |
| Full abstract text exported | **0** |
| Reviewer A or B eligibility decisions made | **0** |
| Judged eligible clinical studies | **Not determined** |
| All-queries PMID union from same workflow | 2,145 unique PMIDs of 2,170 query occurrences |

**Interpretation:** 40 is a query-generated *bibliography*, not 40 eligible or evaluated papers. No claims of full-text screening, empirical clinical results, systematic-review completion or novel first-of-kind methods follow from these counts.

## Source-grounded manual screening priorities (NOT inclusion decisions)

The following records were checked against the downloaded **bibliographic titles/DOIs** and selected because their titles plausibly overlap laboratory LLM evaluation or SOP-compliance research. These are *title-priority prompts for two independent reviewers*, not relevance scores or evidence of eligibility.

| PMID | Year | Title/subject | Why reviewers should examine it |
| --- | --- | --- | --- |
| [42793815](https://pubmed.ncbi.nlm.nih.gov/42793815/) | 2026 | Laboratory medicine decision support: 100-case safety benchmark (*Diagnostics*) | Closest general laboratory-LLM safety baseline; inspect S4 definition and case selection |
| [42247415](https://pubmed.ncbi.nlm.nih.gov/42247415/) | 2026 | GPT-5, Grok 4 and DeepSeek R1 interpreting CBC reports (*JMIR*) | Closest CBC-specific comparison; check analyser-alert handling |
| [41244595](https://pubmed.ncbi.nlm.nih.gov/41244595/) | 2025 | Retrieval-augmented generation for clinical laboratory regulations (*J Pathol Inform*) | Closest source-grounded laboratory procedure/regulation Q&A, but not sample correction |
| [40023838](https://pubmed.ncbi.nlm.nih.gov/40023838/) | 2025 | LLM chain-of-thought reasoning in clinical laboratory case interpretation (*CCLM*) | Related laboratory-case evaluation; no abstract listed in PubMed, full text may be needed |
| [40823482](https://pubmed.ncbi.nlm.nih.gov/40823482/) | 2025 | DeepSeek-R1 for multidisciplinary laboratory decision support | Inspect clinical references and safety task |
| [37083166](https://pubmed.ncbi.nlm.nih.gov/37083166/) | 2023 | EFLM ChatGPT understanding of laboratory medicine test results | Foundational cautionary comparison for lab result interpretation |
| [41506176](https://pubmed.ncbi.nlm.nih.gov/41506176/) | 2026 | LLM mapping of laboratory observation names/codes | Relevant to semantic normalization; indirect to interference routing |
| [39787612](https://pubmed.ncbi.nlm.nih.gov/39787612/) | 2025 | ChatGPT classification of normal/abnormal blood-cell morphology | Related negative controls and morphology but distinct task |

The table uses descriptive summaries, not bulk article titles or abstracts, and does not assert that any study is in-scope.

## Full-source cross-check for one previously omitted comparator

[**Nanua et al., *Retrieval-augmented generation for interpreting clinical laboratory regulations using large language models* (2025)**](https://pmc.ncbi.nlm.nih.gov/articles/PMC12616094/) evaluated the Raven system on **103 synthetic laboratory regulatory questions**, including **88 explicitly addressed by 42 CFR Part 493**. The paper reports **92.0% totally complete and correct responses** among those 88, assessed against manually generated answers by a board-certified pathologist. The remaining cases emphasize uncertainty when policy did not cover a question.

This is material SOP/source-grounding prior art. It **does not** provide independent paired specimen corrections or a CBC-interference reporting endpoint. The current project must cite it and avoid asserting that an SOP-RAG laboratory assistant is new.

## Next reviewer work

1. Archive artifact (90-day retention), verify SHA and connect each screening row to its PubMed DOI/metadata.
2. Two independent human screeners complete the **40 B-query** title/abstract decisions using the exported blank columns; record disagreements and adjudication.
3. Check the source full texts and supplements for laboratory actions, valid after-correction reference, analyser specifics, deterministic baseline, abstention and harm taxonomy.
4. Extend screening to A and C query records and institutional bibliographic indexes without pretending that the B tranche alone is comprehensive.
5. Update [systematic search workplan](SCREENING_WORKPLAN.md) and evidence register only as independently verified.

NLM notes that abstracts may be subject to copyright. See [metadata-only export design](PUBMED_METADATA_SCREENING.md). This report contains no protected abstracts or patient information.
