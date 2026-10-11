# Evidence register and novelty-check queue

Maintained as a scientific provenance ledger. Status as of 2026-10-11. 'Verified' means the bibliographic source and broad relevance were checked, **not** that every proposed clinical pathway has been validated locally.

| Work | Source / identifier | Status | Implication |
| --- | --- | --- | --- |
| Girard et al., GFHC raised-MCHC decision-tree review (2025) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12426809/ | Verified publication and scope | Existing practical decision trees constrain system novelty |
| Gulati et al., Unreliable Automated CBC Results (2022) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9057813/ | Prior-art candidate, verify each detail before use | Broad review of interference recognition/management |
| Henry et al., XN-10 interference management (2022) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9804823/ | Verified primary study; extraction summarized in prior-art matrix | XN-10 optical flowcharts: 63/65 retrospective and 18/901 prospective |
| CLSI AUTO10 | https://clsi.org/shop/standards/auto10/ | Verified scope | Framework for laboratory rule/autoverification validation |
| Gallifant et al., TRIPOD-LLM (2025) | https://www.nature.com/articles/s41591-024-03425-5 | Verified publication and checklist | LLM study transparency requirements |
| Ye et al., LLMs interpreting CBC reports (2026) | https://pubmed.ncbi.nlm.nih.gov/42247415/ | Verified full-article abstract/method overview; deeper overlap review pending | Potential overlap with LLM-CBC evaluation |
| Khandekar et al., MedCalc-Bench (2024) | https://proceedings.neurips.cc/paper_files/paper/2024/hash/99e81750f3fdfcaf9613db2dbf4bd623-Abstract-Datasets_and_Benchmarks_Track.html | Verified 55 tasks and >1000 reviewed evaluation instances | Numerical medical reasoning baseline |
| Laboratory Medicine Decision Support—Beyond Exam Passing (Diagnostics, Sep 2026) | https://doi.org/10.3390/diagnostics16183030 | PubMed abstract and journal metadata checked; supplementary cases not yet inspected | **Direct overlap with broad laboratory-LLM safety benchmarking**; 100 educational cases, 3 LLMs, safety scores |
| Wang et al., SOP-Maze (Findings ACL 2026) | https://doi.org/10.18653/v1/2026.findings-acl.715 | ACL Anthology metadata/abstract verified | General complex SOP reasoning benchmarks pre-exist |
| SOP-Bench (Amazon Science, 2026) | https://github.com/amazon-science/SOP-Bench | Public project README only; publication status unverified | Multi-step industrial SOP benchmark including healthcare-adjacent contexts |
| Machcha et al., MedAbstain (EACL 2026) | https://aclanthology.org/2026.eacl-long.291/ | Primary conference paper indexed | Medical LLM abstention testing pre-exists |
| Sounderajah et al., STARD-AI (Nat Med, 2025) | https://doi.org/10.1038/s41591-025-03953-8 | Reporting guideline verified | Apply conditionally when claiming diagnostic accuracy |
| Barnes et al., international CBC review rules (2005) | https://scholars.mssm.edu/en/publications/the-international-consensus-group-for-hematology-review-suggested-2/ | Relevant candidate, review methods | Strong conventional expert-system prior art |

## Clinical cautions to resolve from local sources

- Raised MCHC can reflect genuine pathology or analyser artifacts; the decision is not formula-only.
- Distinguish in-vitro and in-vivo haemolysis, and warm/cold agglutinin scenarios.
- Alternative channel outputs are model/software/SOP specific; measurement provenance must not be guessed.
- GFHC review, vendor procedures and site SOPs may differ: do not treat public thresholds as universal.
- A formula can be numerically correct while its inputs are analytically invalid.

## Unverified novelty claims: do not publish as fact

- 'First benchmark' / 'first paired-outcome evaluation' / 'no previous study' without a reproducible literature search.
- Any claimed zero-error rate of a deterministic engine.
- Q1 quartile status of specific journals for submission year and category.
- Manufacturer-specific alternative-channel capabilities beyond actually checked IFUs.
- Suitability of any named regulatory pathway for UAE deployment.

## Next evidence tasks

Build a reproducible search log (PubMed/Scopus/Web of Science/IEEE/ACM search strings, dates, exclusions); extract paper-by-paper population, devices, setting, labels, endpoints and limitations; obtain IFU-level parameter derivation table; request librarian and clinical specialist validation.

## Extracted comparison

See [verified prior-art matrix](PRIOR_ART_MATRIX.md) for study populations, comparator arms and the distinct proposed contribution. This is a targeted audit, **not** a completed systematic search.

## Research positioning revision (2026-10-11)

This targeted public-web update found 2026 laboratory decision-support, SOP-following and clinical abstention benchmarks absent from the four-AI review synthesis. See [targeted source update](TARGETED_LITERATURE_UPDATE_2026-10-11.md). Broad novelty claims must now be rejected; a complete systematic/scoping database search is still not complete.

## Public reproducibility utility

A bounded read-only [PubMed search snapshot](PUBMED_SEARCH_SNAPSHOT.md) can produce an artifact recording ESearch count, translated query and PMIDs for three **targeted** query classes. This does not complete the planned systematic evidence screening or any IFU verification.
