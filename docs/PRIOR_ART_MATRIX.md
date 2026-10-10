# Prior-art comparison matrix — research extraction v0.2

Date: 2026-10-11. Targeted source examination; **not** a systematic review. These sources support feasibility and differentiate our question, but cannot substantiate a claim of the first-ever benchmark.

| Study/standard | Population and material | Existing method | Reference/outcome as reported | Difference from SOPGuard-Eval | Important caveat |
| --- | --- | --- | --- | --- | --- |
| Girard et al. GFHC 2025 (Int J Lab Hematol; DOI 10.1111/ijlh.14536) | Literature/expert synthesis of raised MCHC across artefacts and true pathology | Expert decision trees; differentiated reporting/management | Consensus guidance, not a head-to-head LLM experiment | Grounding and clinically significant negative control taxonomy | Device techniques differ; GFHC is not the selected laboratory's executable SOP |
| Henry et al. 2022 (Int J Lab Hematol; DOI 10.1111/ijlh.13951) | 65 historical confirmed interference cases; 901 unselected prospective samples; XN-10 | Optical/impedance comparator measurements and two flowcharts | 63/65 historical corrected (97%); 18 prospective results corrected | Strong device-specific rule comparator and feasibility example | Different study purpose; historical preselection may affect correction performance |
| Barnes et al. 2005 (Lab Hematol; PMID 16024331) | 13,298 samples in 15 laboratories for consensus hematology review criteria | 41 consensus review rules | Published validation of suggested criteria | Shows rules and manual CBC review long predate LLMs | Broad slide-review rules, not the same interference-specific endpoint |
| Ye et al. 2026 (JMIR; DOI 10.2196/87802) | 100 clinical CBC reports from hematologic disease patients at one center; Chinese prompts | GPT-5, Grok 4 and DeepSeek R1; five task dimensions including analyser alerts | Expert ratings, diagnostic concordance, and categorized model errors; GPT-5 12 hallucinations in alert processing | Closest public LLM-CBC evaluation; our differentiator is interference action safety against independent, episode-linked reference | Diagnosis-oriented, not a paired-after-intervention safety reference |
| Laboratory Medicine Decision Support—Beyond Exam Passing, Diagnostics Sep 2026 (DOI 10.3390/diagnostics16183030) | 100 educational, text-based clinical pathology/lab medicine cases | 3 LLMs, 2 blinded raters, management and safety scoring | Unsafe/guideline-discordant responses reported: 2%, 4%, 5% | Closest general laboratory-LLM safety benchmark; ours must be specifically CBC interference decision validity | Abstract-level verification; those percentages are not comparable to an independently adjudicated case-level S4 rate |
| Wang et al., SOP-Maze, Findings ACL Jul 2026 (DOI 10.18653/v1/2026.findings-acl.715) | 397 SOP instances, 3422 subtasks, 23 complex business scenarios | LLM procedural decision/routing and calculations | SOP-following errors classified | SOP adherence alone is not novel; clinical reportability/action reference needed | Business, not CBC lab workflows |
| Amazon Science SOP-Bench, public project 2026 | Project describes 2000+ tasks and 12 industrial domains | Human-expert-authored, complex executable SOP agent tasks | Public project research description | Another reason not to claim novelty for multi-step SOP benchmarking | Venue/peer-review status unverified; healthcare tasks not necessarily clinical laboratory result reporting |
| Machcha et al., MedAbstain, EACL 2026 | Medical multiple-choice QA with uncertainty and adversarial perturbations | Abstention and conformal prediction evaluation | Model ability to abstain under incomplete information | Abstention itself is not novel; clinically correct laboratory withholding is more specific | MCQA rather than patient specimen interference |
| Sounderajah et al., STARD-AI, Nat Med Sep 2025 | Consensus guideline, no patient study cohort | Reporting recommendations for AI diagnostic accuracy | Not performance data | Possible reporting framework if relevant to final study design | Not proof that our intended SOP decision evaluation is a diagnostic accuracy study |
| Khandekar et al. 2024 (NeurIPS, MedCalc-Bench) | Over 1,000 reviewed examples, 55 clinical calculators | LLM numerical/rule reasoning tasks | Entity extraction, formula choice and arithmetic errors | Supports deterministic numerical verification and explicit taxonomy | Not laboratory interference management or SOP-dependent reportability |
| CLSI AUTO10-A, published 2006 | Laboratory automation practice standard (not case dataset) | Design, implement, validate and customize autoverification rules | Normative validation framework | Appropriate general methodological comparator for SOP encoding | It does **not** prescribe clinical thresholds or parameter limits; archived guideline |
| CLSI AUTO15 (published 2019) | Discipline-specific autoverification framework | Guidance for laboratory discipline workflows | Not a model-comparison benchmark | Context for clinical rule validation | Confirm specific clauses from licensed standard before citing detailed requirements |

## Primary verified references

1. Girard S et al. [GFHC 2025, full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12426809/); [PubMed](https://pubmed.ncbi.nlm.nih.gov/40819933/).
2. Henry S et al. [XN-10 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9804823/); [PubMed](https://pubmed.ncbi.nlm.nih.gov/36053968/).
3. Barnes PW et al. [ISLH suggested rules](https://pubmed.ncbi.nlm.nih.gov/16024331/); [ISLH rules](https://islh.org/web/consensus_rules.php).
4. Ye X et al. [JMIR 2026 full article](https://www.jmir.org/2026/1/e87802/).
5. Khandekar N et al. [NeurIPS 2024 abstract](https://proceedings.neurips.cc/paper_files/paper/2024/hash/99e81750f3fdfcaf9613db2dbf4bd623-Abstract-Datasets_and_Benchmarks_Track.html).
6. CLSI [AUTO10](https://clsi.org/shop/standards/auto10/) and [AUTO15 announcement](https://clsi.org/about/press-releases/clsi-publishes-new-automation-and-informatics-document-auto15/).

## Critical novelty constraints

**Established:** Existing clinical decision trees, vendor workflows and CBC rule review; a recent GPT-5/Grok4/DeepSeek CBC interpretation comparison; general medical calculation LLM evaluation.

**Proposed, not established:** A benchmark joining expert-assessed SOP-action safety, empirically observed follow-up measurements when relevant, true-pathology controls, paired baseline comparison, and explicit appropriate abstention.

**Not verified:** Absence of earlier studies combining these dimensions. Comprehensive search and evidence extraction must precede any 'first' assertion.

## Search limitations and next stage

The searches above were targeted through online primary pages, not an exhaustively logged bibliographic database query. Complete PubMed, Embase/Scopus or Web of Science, IEEE/ACM queries with database date, full strings, result counts, duplicate removal, inclusion criteria, and title/abstract/full-text screening. Review newest papers before manuscript submission.

For the October 2026 additions, see [the targeted search log](TARGETED_LITERATURE_UPDATE_2026-10-11.md). General laboratory AI safety evaluation, SOP-benchmarks and medical abstention benchmarks predate SOPGuard-Eval. All claims of an unstudied **intersection** remain provisional until a full literature screen.
