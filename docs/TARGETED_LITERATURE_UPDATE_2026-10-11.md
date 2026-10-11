# Targeted literature update — 2026-10-11

**Status: executed targeted public-web discovery and source verification, NOT a systematic review or a PubMed/MEDLINE database-search run.** Search results can vary over time and provider ranking. There are no claimed database hit counts, exhaustive screening totals, or independent second screener.

## What was actually done

On 2026-10-11, broad discovery searches were carried out using general web search, followed by checks against PubMed, journal/publisher and ACL Anthology pages where accessible. One direct PubMed E-utilities search attempt could not be accessed in the available browsing environment. No publication or result-count statistics are inferred from that failure. Access to institutional Scopus/Web of Science and IEEE/ACM search interfaces was not established here.

### Executed search phrases (verbatim thematic searches, no database-specific Boolean syntax)

1. `complete blood count analytical interference large language models SOP evaluation hemolysis lipemia 2025 2026 benchmark`
2. `2026 2025 large language model laboratory medicine analyser flags CBC interpretation safety performance research`
3. `GFHC 2025 "Breaking Free From MCHC Interferences" clinical decision trees`
4. `Clinical laboratory auto-verification rules GPT large language model hematology SOP benchmark 2024 2025 2026`
5. `STARD AI TRIPOD-LLM CONSORT-AI 2025 reporting guidelines laboratory decision support validation`
6. `"CBC" "interference" "large language model" "safety" benchmark clinical 2026`
7. `"laboratory medicine" "standard operating procedure" "large language model" evaluation 2025 2026`
8. `CBC auto verification AI middleware lipemia haemolysis machine learning 2026 study`
9. `"MedAbstain" healthcare benchmark abstention paper 2026`
10. `research laboratory quality control LLM benchmark SOP adherence real reports 2026`

These queries are NOT equivalent to running the planned PubMed searches A/B/C in [LITERATURE_SEARCH_PROTOCOL.md](LITERATURE_SEARCH_PROTOCOL.md). Study selection was targeted, not exhaustive or dual-screened.

## Newly identified and checked against source pages

| Study | Date/status | Design and objective from source | Closest overlap | Unresolved distinction |
| --- | --- | --- | --- | --- |
| Ulutaş and Pekmezci, *Laboratory Medicine Decision Support—Beyond Exam Passing* | *Diagnostics* 2026;16(18):3030; 18 Sep 2026; DOI 10.3390/diagnostics16183030 | 100 **text-based educational clinical pathology/lab medicine cases**, three LLMs, two blinded expert reviewers; management and safety ratings; unsafe/guideline-discordant recommendations reported at 2%, 4%, 5% | **Directly challenges any claim that laboratory-medicine LLM safety benchmarking is novel** | No evidence in the abstract of analyser-specific CBC interference workflow, partner-lab SOP decisions or original-to-post-correction specimen pairs. Full case/materials check still needed. |
| Wang et al., SOP-Maze | Findings ACL 2026 (July); DOI 10.18653/v1/2026.findings-acl.715 | 397 instances, 3,422 subtasks from 23 **business** SOP scenarios; measures branching/SOP following and calculation errors | General SOP comprehension benchmark already exists | Clinical CBC analytical validity, reportability and human laboratory adjudication are not its target tasks. |
| Amazon Science SOP-Bench | Public repository, 2026; **publication/acceptance status not independently confirmed** | Repository describes >2,000 tasks across 12 industrial areas including healthcare intake, complex SOP execution and LLM agents | General multi-step SOP benchmarking is not a new idea | Do not equate SOP-based simulated tasks with validated clinical lab SOP outcomes; no direct CBC interference equivalence established. |
| Machcha et al., MedAbstain | EACL 2026 (paper and code); arXiv 2601.12471 | Medical multiple-choice QA benchmark for abstention, perturbation and uncertainty/conformal prediction | **Medical LLM abstention benchmarking already exists** | Action-level laboratory withholding/recollect/referral and empirical post-action results remain a distinct proposed task. |
| Sounderajah et al., STARD-AI | *Nature Medicine* Sep 2025; DOI 10.1038/s41591-025-03953-8 | Consensus reporting guidance for AI diagnostic accuracy studies | Potential companion reporting checklist | Applicability depends on whether the final claim is diagnostic-test accuracy or SOP-action safety; not itself validation evidence. |
| Ye et al., LLM CBC interpretation | *JMIR* 2026;28:e87802; DOI 10.2196/87802 | 100 **real CBC reports** in haematological disease; GPT-5, Grok 4, DeepSeek R1, 4 blinded laboratory physicians, analyser-alert processing among tasks | Closest CBC model comparison | Reference primarily diagnostic/interpretation, not necessarily adjudicated interference corrective action with paired specimen outcomes. |

### Direct publicly accessible sources

- [Diagnostics 2026, article and abstract](https://www.mdpi.com/2075-4418/16/18/3030), [PubMed PMID 42793815](https://pubmed.ncbi.nlm.nih.gov/42793815/).
- [SOP-Maze, ACL Anthology](https://aclanthology.org/2026.findings-acl.715/).
- [SOP-Bench, Amazon Science GitHub](https://github.com/amazon-science/SOP-Bench) (repository claims are project self-descriptions, not proof of clinical validation or final venue status).
- [MedAbstain, EACL paper](https://aclanthology.org/2026.eacl-long.291/), [source repository](https://github.com/sravanthi6m/MedAbstain).
- [STARD-AI, Nature Medicine](https://www.nature.com/articles/s41591-025-03953-8).
- [Ye et al., JMIR](https://www.jmir.org/2026/1/e87802/).
- [GFHC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12426809/).

## Research-positioning consequence

**Do not claim** first LLM laboratory benchmark, first clinical numerical safety benchmark, first SOP benchmark, or first medical abstention benchmark. Existing works already directly cover these general claims.

The still-proposed contribution is the *intersection* of analyser-specific CBC analytical interference and reportability, expert adjudication independent of the encoded rule engine, original/post-intervention evidence when clinically relevant, appropriate action abstention, and comparison to the **local SOP-deterministic reference baseline**. The absence of prior work on this exact intersection is **not yet proven**.

The project should aim for a scientifically useful negative result: if existing rules remain safer and LLMs offer no measurable gain, report that conclusion with uncertainty and clearly scoped generalizability.

## Next literature actions

1. Obtain database-specific search result exports and dates from PubMed and institutional Scopus/Web of Science, with full strings and counts; apply two-reviewer screening if pursuing a systematic/scoping novelty claim.
2. Read *Diagnostics* 2026 supplementary cases and methods to assess safety taxonomy overlap; do not infer methods from abstract alone.
3. Read the full SOP-Maze and MedAbstain evaluation and identify transferable metrics without copying their dataset content.
4. Check whether independent after-action specimen results were used in previous lab AI studies, beyond title/abstract search.
5. Update target-journal reporting plans with TRIPOD-LLM and STARD-AI (if applicable), maintaining case-level primary endpoint and independent clinical reference.

## Limitations

Search engine results can be incomplete; accessible publisher pages may return access/rate-limit errors. Bibliographic metadata and abstract results are sufficient to register candidates, **not** to claim an exhaustive review or full-text verification in every case. This update does not use any patient data or laboratory-specific SOP.
