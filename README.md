# SOPGuard-Eval

**Artefact or Disease? Safety of Large Language Models Interpreting Analytically Invalid Complete Blood Counts**

**Current status: STUDY DESIGN / NOT FOR CLINICAL USE (11 October 2026).** This public project contains no patient data, approved laboratory SOP, institutionally authorized patient-data pipeline or validated clinical tool.

## Scientific purpose

Evaluate whether an LLM mistakes analytically invalid complete blood count (CBC) values for disease or recommends unsafe laboratory reporting actions, and whether providing the **applicable SOP in context** reduces these problems without promoting excessive abstention.

Following an independent scientific review, the working study is **one laboratory + one analyser family + one or two clinically supported interference classes**, with true-pathology mimics and negative controls. One prespecified model is tested **without (L0) and with (L2) relevant SOP text**, and independently assessed against documented laboratory evidence and qualified expert action labels. Existing laboratory rules and historical actions are descriptive comparators, **not ground truth**. The previous six-arm RAG/tool/human comparison is no longer planned for Study 1.

**No laboratory partner, case-volume feasibility count, permission to use patient-level data, signed adjudication or preregistration has yet been secured.** There are no empirical CBC safety results.

## Current, authoritative documents

- [Simplified protocol (v0.2, not registered)](docs/PROTOCOL_DRAFT.md)
- [Direct laboratory collaboration request](docs/PARTNER_BRIEF.md)
- [Laboratory response checklist](docs/LAB_COLLABORATION_ACTIONS.md)
- [Ready-to-send collaboration email](docs/LAB_COLLABORATION_EMAIL_DRAFT.md)
- [Aggregate feasibility template (blank)](docs/lab_aggregate_feasibility_template.csv)
- [Preliminary statistical analysis plan (v0.2)](docs/STATISTICAL_ANALYSIS_PLAN_DRAFT.md)
- [Clinical adjudication and reference standard (v0.2)](docs/ADJUDICATION_CHARTER.md)
- [Three feasibility go/no-go gates](docs/GO_NO_GO_GATES.md)
- [Operating research decision log](docs/OPERATING_DECISION_LOG.md)
- [Literature evidence register](docs/EVIDENCE_REGISTER.md)
- [Public bibliography run record](docs/PUBMED_METADATA_RUN_2026-10-11.md)

Earlier study-design and automation documents remain in Git history and the repository for traceability, but **the simplified protocol and documents above take precedence** when they conflict. Do not expand or implement the earlier six-arm design without a new decision and clinical review.

## Next action: laboratory feasibility

The PI already has receptive laboratory contacts and will send the **direct collaboration action request** and checklist to those laboratories. Ask for a written response identifying a clinical co-investigator, analyser/records availability, and the internal permission route for aggregate-only case counting; **an introductory meeting is not a prerequisite**. Request no patient-level results or restricted SOP text at this stage. Do **not** request patient-level results or restricted SOP copies at this stage. **Initial response target: about 7–10 working days if practical; partner feasibility review checkpoint: 15 January 2027.**

In parallel, correct the literature-search recall gap (including Spies et al. 2023), and, if useful, conduct a small **published-case research workflow pilot** with source verification and contamination disclosure. No real CBC experimental work before institutional approvals.

## Safety boundaries

- No clinical deployment, result release, integration into instruments/LIS or medical advice.
- No patient-level data, accessions, restricted SOPs, IFUs, credentials or unapproved clinical outputs in public GitHub, issues, Actions or external AI tools.
- Laboratory corrective outcomes are evidence but do not independently prove which recommendation was appropriate at the initial decision time (T0).
- Two qualified independent adjudicators review acceptable actions without seeing arm predictions; missing/unresolved cases are not forced into false certainty.
- Source, unit and time provenance matter; formula consistency cannot validate an analytically unreliable input.
- No invented sample sizes, simulated real-patient outcomes, blanket novelty claims or claims of regulatory/clinical approval.

### Technical assets (frozen, research-only)

Existing public metadata schemas, fictional-data tests, PubMed bibliographic scripts and paired-count demonstrations remain available for reproducibility, but **new frameworks, RAG pipelines and clinical algorithms are on hold until feasibility is demonstrated**.

This work aims to produce one credible scientific paper, including a negative result if the data support it. The scope and publication target will be confirmed after clinical and statistical feasibility review.
