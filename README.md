# SOPGuard-Eval

**A paired-outcome research benchmark for evaluating LLM safety, SOP adherence, numerical validity and appropriate abstention in complete blood count (CBC) interference management.**

**Status: protocol development / NOT FOR CLINICAL USE.** This public repository does not contain patient data, approved laboratory SOPs, clinical software, or validated rules.

## Research question

When laboratory specimens produce analytically unreliable CBC measurements, can a language model recommend the correct SOP-constrained response without unsafe calculations, missed verification steps, or suppression of real pathology? How does it compare with a deterministic SOP engine and qualified biomedical scientists?

We will test rather than assume that an LLM adds value. Correctly declining to calculate or release a result is a valid and often necessary response.

## Intended study

- Retrospective, paired-outcome evidence: initial result and independently documented post-action result **where appropriate**, plus original flags, specimen metadata and local SOP version.
- Independent expert adjudication of permitted actions, affected parameters, reporting restrictions and the need to refer, withhold or recollect.
- Comparator arms: deterministic rules (R), unaided qualified scientists (H, subset), plain LLM (L0), SOP-RAG (L1), oracle-SOP LLM (L2) and tool-constrained LLM (L3).
- Primary endpoint: proportion of cases with at least one independently adjudicated **safety-critical recommendation error**, with case-level confidence intervals.
- Secondary endpoints: correct abstention and escalation, SOP adherence, arithmetic and analytic validity, negative-control errors, repeatability, robustness and human factors.
- First clinical scope: **one partner laboratory, one analyser family**, with clinically justified interference categories selected by the laboratory. A second lab/model is an independent later validation question, not an assumed capability.

## Hard boundaries

1. No live clinical advice, clinical deployment, instrument/LIS integration, patient-result authorization or specimen correction automation.
2. No patient-level data, identifiable metadata, licensed IFUs or restricted SOPs may be committed to this public repo.
3. No clinical-rule implementation is considered validated until the laboratory SOP owner and independent specialists approve it and governance gates are satisfied.
4. Post-action results support verification but are not automatically sufficient ground truth; incomplete, persistently interfered or unresolvable cases can require abstention.
5. We do not assume rule-engine perfection or numerical consistency equals analytical validity.
6. Model reviews by Gemini, Grok, Mistral and Claude are brainstorming inputs, **not** clinical expert review or peer review.

## Research documentation

- [Research charter](docs/RESEARCH_CHARTER.md)
- [Draft protocol](docs/PROTOCOL_DRAFT.md)
- [Reference-standard and adjudication charter](docs/ADJUDICATION_CHARTER.md)
- [Data dictionary and provenance specification](docs/DATA_DICTIONARY.md)
- [Statistical analysis plan - draft](docs/STATISTICAL_ANALYSIS_PLAN_DRAFT.md)
- [Exploratory paired endpoint pilot guide](docs/PAIRED_STATISTICS_PILOT_GUIDE.md)
- [Partner laboratory and governance requirements](docs/LAB_PARTNERSHIP.md)
- [Laboratory partner collaboration brief](docs/PARTNER_BRIEF.md)
- [Ethics and data access draft](docs/ETHICS_AND_DATA_ACCESS_TEMPLATE.md)
- [Blank clinical adjudication form](docs/CLINICAL_REVIEW_FORM_TEMPLATE.md)
- [Feasibility pilot and go/no-go plan](docs/FEASIBILITY_AND_GO_NOGO_PLAN.md)
- [Research decisions](docs/OPERATING_DECISION_LOG.md)
- [Preliminary prior-art search log](docs/PRELIMINARY_LITERATURE_SEARCH_LOG.md)
- [Prior-art comparison matrix](docs/PRIOR_ART_MATRIX.md)
- [Targeted October 2026 literature update](docs/TARGETED_LITERATURE_UPDATE_2026-10-11.md)
- [Updated research-positioning decisions](docs/LITERATURE_METHODS_DECISIONS.md)
- [Literature search and novelty audit protocol](docs/LITERATURE_SEARCH_PROTOCOL.md)
- [Reproducible PubMed metadata search snapshot](docs/PUBMED_SEARCH_SNAPSHOT.md)
- [Executed 11 Oct 2026 PubMed retrieval](docs/PUBMED_RUN_2026-10-11.md)
- [Literature screening handoff](docs/SCREENING_WORKPLAN.md)
- [PubMed metadata worksheet: screened by humans, no abstract redistribution](docs/PUBMED_METADATA_SCREENING.md)
- [Public PMID deduplication script](scripts/deduplicate_pubmed_pmids.py)
- [Eligibility and sampling safeguards](docs/ELIGIBILITY_AND_SAMPLING.md)
- [Evaluation data contracts](docs/EVALUATION_CONTRACT.md)
- [Model-view leakage prevention](docs/MODEL_VIEW_FIREWALL.md)
- [Evidence register](docs/EVIDENCE_REGISTER.md)
- [External AI review synthesis](docs/AI_REVIEW_SYNTHESIS.md)
- [Go/no-go gates](docs/GO_NO_GO_GATES.md)
- [Contribution guidance](CONTRIBUTING.md) and [security/data handling](SECURITY.md)

The repository includes three public **research metadata schemas**, 11 fictional-data contract tests and GitHub Actions static checks. These are not validated medical data models, clinical correction algorithms, or clinical safety tests.

## Current next step

Obtain collaboration with an accredited laboratory and its haematology lead for site-approved, version-controlled SOPs, paired de-identified cases, sample availability estimates, independent adjudicators, and ethics/privacy permissions. Targeted literature discovery has expanded to relevant September 2026 laboratory-safety and July 2026 SOP benchmarks, but a reproducible full database novelty search remains outstanding. Work on bibliography, protocol drafts and governance can proceed while laboratory collaboration is sought.

## Publication and reproducibility

The initial intended output is **one pre-registered, safety-first comparative study**, not a production clinical application. Plan to log model IDs, versions, prompts, parameters, retrieval corpus hashes and blinded scoring. Follow relevant [TRIPOD-LLM reporting guidance](https://www.nature.com/articles/s41591-024-03425-5); confirm other reporting standards with the eventual journal.

For prior art and authoritative literature see [evidence register](docs/EVIDENCE_REGISTER.md).
