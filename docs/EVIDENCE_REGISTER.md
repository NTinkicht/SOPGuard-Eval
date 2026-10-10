# Evidence register and novelty-check queue

Maintained as a scientific provenance ledger. Status as of 2026-10-11. 'Verified' means the bibliographic source and broad relevance were checked, **not** that every proposed clinical pathway has been validated locally.

| Work | Source / identifier | Status | Implication |
| --- | --- | --- | --- |
| Girard et al., GFHC raised-MCHC decision-tree review (2025) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12426809/ | Verified publication and scope | Existing practical decision trees constrain system novelty |
| Gulati et al., Unreliable Automated CBC Results (2022) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9057813/ | Prior-art candidate, verify each detail before use | Broad review of interference recognition/management |
| Henry et al., XN-10 interference management (2022/2023 indexing) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9804823/ | Prior-art candidate, full methods extraction pending | Platform-specific flowcharts and evaluation |
| CLSI AUTO10 | https://clsi.org/shop/standards/auto10/ | Verified scope | Framework for laboratory rule/autoverification validation |
| Gallifant et al., TRIPOD-LLM (2025) | https://www.nature.com/articles/s41591-024-03425-5 | Verified publication and checklist | LLM study transparency requirements |
| Ye et al., LLMs interpreting CBC reports (2026) | https://pubmed.ncbi.nlm.nih.gov/42247415/ | Relevant candidate, full method/difference audit pending | Potential overlap with LLM-CBC evaluation |
| Khandekar et al., MedCalc-Bench (2024) | https://proceedings.neurips.cc/paper_files/paper/2024/hash/99e81750f3fdfcaf9613db2db623-Abstract.html | Relevant candidate, verify benchmark scope | Numerical medical reasoning baseline |
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
