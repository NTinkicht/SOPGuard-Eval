# Literature search and novelty audit protocol — v0.1

**Created 2026-10-11. PROTOCOL ONLY: search strings below have not yet been run as complete database queries, screened or deduplicated.** Do not call the current [targeted evidence matrix](PRIOR_ART_MATRIX.md) a systematic review. The literature review is intended to test the provisional novelty claim and to identify existing deterministic and LLM-based methods.

## Objectives and scope

Question A (laboratory baseline): What methods, middleware and manufacturer/analyser-specific procedures already identify, investigate, suppress or report CBC measurements affected by cold agglutination, lipaemia, icterus, haemolysis or genuine pathological mimics?

Question B (LLM safety): Which published evaluations of generative LLMs, retrieval or neuro-symbolic methods have examined CBC analytical interferences, laboratory SOP adherence, numerical error, abstention, or laboratory reporting safety, and what independent reference standards did they use?

Question C (methodological transfer): Which validated evaluation, bias, reporting and selective prediction approaches can reasonably be adopted without claiming that they establish clinical safety?

Separate evidence for A, B and C; do not conflate decision-tree guidance with comparative LLM experiments.

## Planned information sources

- PubMed/MEDLINE (clinical and haematology).
- Scopus **or** Web of Science (citation tracking and broader coverage, subject to institutional access).
- IEEE Xplore and/or ACM Digital Library (technical safety benchmarks and expert systems).
- Manufacturer publications and CLSI/ICSH/EFLM or ISO guidance **only to the extent publicly/legally available**, tagged separately from peer-reviewed primary studies.
- Backward/forward citations of GFHC 2025, Henry 2022, Barnes 2005, and Ye 2026.

A librarian or information specialist should review the strategy and determine whether a formal scoping-review methodology and registration are warranted. Google/web targeted lookups are *supplementary*, not a substitute for reproducible database searches.

## Draft PubMed strategy (NOT EXECUTED)

Use three separately logged searches, adjusting MeSH and field tags after librarian review. No fabricated hit counts.

**A — laboratory processes**

```text
("Blood Cell Count"[Mesh] OR "complete blood count"[tiab] OR "full blood count"[tiab] OR "hematology analyz*"[tiab] OR "haematology analys*"[tiab] OR MCHC[tiab])
AND
(interferen*[tiab] OR agglutinin*[tiab] OR lipemi*[tiab] OR lipaemi*[tiab] OR icter*[tiab] OR hemolys*[tiab] OR haemolys*[tiab] OR autoverif*[tiab] OR "review rules"[tiab])
```

**B — LLM and generative AI in laboratory result interpretation**

```text
("complete blood count"[tiab] OR "Blood Cell Count"[Mesh] OR haematolog*[tiab] OR hematolog*[tiab] OR "laboratory medicine"[tiab])
AND
("large language model*"[tiab] OR "generative AI"[tiab] OR ChatGPT[tiab] OR "retrieval augmented generation"[tiab] OR LLM[tiab] OR "neuro-symbolic"[tiab])
AND
(interpreta*[tiab] OR analy*[tiab] OR SOP[tiab] OR error*[tiab] OR safe*[tiab] OR abstain*[tiab])
```

**C — safety and methodology transfer (broader medical AI)**

```text
("large language model*"[tiab] OR ChatGPT[tiab] OR "generative artificial intelligence"[tiab])
AND
("patient safety"[tiab] OR abstain*[tiab] OR "selective prediction"[tiab] OR "clinical numeracy"[tiab] OR "medical calculation"[tiab] OR "benchmark"[tiab])
```

The starred terms, field tags, spelling variants and expression validity must be verified in PubMed's query builder before execution. Run no undisclosed date/English-only filter; if restrictions become necessary, document rationale and exclusions.

## Adaptation to other databases

Translate the concepts rather than mechanically pasting PubMed `[tiab]` syntax. Maintain one saved, database-specific query per concept, exact interface/version if visible, search date, applied filters and unfiltered/filter counts. Do not invent Scopus/Web of Science hit counts when institutional access is unavailable.

## Eligibility and screening

Include: peer-reviewed original clinical evaluation, prospective/retrospective method comparison, consensus guidelines directly defining relevant procedures, formal diagnostic software validation, and healthcare LLM benchmarks with applicable numeric/SOP/abstention endpoints.

Separate categories: narrative reviews, guidance, software/vendor marketing, preprints and editorial/opinion. They can inform context but must not be represented as independent clinical validation.

Exclude with a logged reason: unrelated analytes, purely patient-facing education without evaluated laboratory actions, general model performance without a comparable endpoint, duplicates, inaccessible evidence that cannot substantiate a claim.

Two independent screeners are preferred for title/abstract and full text; store conflict resolutions and adjudication. Track publication date and review date to avoid treating an older preprint as more recent than its peer-reviewed article.

## Extraction and evidence strength

For each study record: ID/DOI/PMID; publication date; review status; setting/location; sample/unit of analysis; study design; exact analyser and software; interference type; reference standard and independence; number of cases and controls; comparison arms; safety and abstention outcomes; confidence intervals; methodological limitations; direct novelty overlap; citation URL; licensing/access notes.

Clinical recommendations and numerical corrections must be checked at the exact device/SOP level. A model-generated paper summary is never accepted as a source.

## Evidence log schema and process

Use [evidence_log_template.csv](evidence_log_template.csv) as a blank template; there are intentionally **no study records or fake search hits**. For each executed database search also record in a separate dated retrieval log: database, search string, search timestamp/timezone, filters, hit count, exports, deduplication and first/second screening counts. Track references to source PDFs externally under allowed licensing, not in public Git history.

## Primary novelty outcome

At the completion of the search, document:
1. Closest studies and exact differences in action-level reference standards and paired-post-intervention data.
2. Whether an independently adjudicated CBC interference LLM safety benchmark already exists.
3. Unresolved overlap and whether the primary hypothesis should change.
4. What can legitimately be described as new **without** a blanket first-of-kind claim.

## Relevant confirmed anchor works

- [GFHC review, Girard et al. 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12426809/): decision trees and true pathology differentiation.
- [Ye et al. 2026, JMIR](https://www.jmir.org/2026/1/e87802/): LLM CBC interpretation including analyser alerts.
- [TRIPOD-LLM 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12104976/): LLM research reporting checklist.
