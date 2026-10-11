# SOPGuard-Eval — simplified study protocol (v0.2, for clinical review)

**Working title:** *Artefact or Disease? Safety of Large Language Models Interpreting Analytically Invalid Complete Blood Counts*

**Research-only. NOT REGISTERED OR APPROVED.** Adopted as the working design after an independent October 2026 review; subject to laboratory, ethics, and statistical consultation. No patient-level records, internal SOPs, clinical decisions, or intervention are authorized by this document.

## Scientific question and boundaries

When a CBC result is affected by an analytical artefact, will an LLM mistake it for genuine disease or recommend an unsafe result-reporting action? Does providing the **applicable, approved SOP in context** reduce such errors without encouraging unnecessary abstention?

The study investigates **reasoning at the original decision point**, not whether an LLM replaces a haematology analyser, its middleware, or a biomedical scientist. We will publish meaningful negative as well as positive results. We do not claim novelty for generic laboratory LLM safety, RAG, SOP reasoning or abstention.

## First study: minimal design

- **Setting:** one cooperating clinical laboratory, one precisely identified analyser family/software version, one or two interference classes chosen *after a site feasibility count*. Initial candidates include cold agglutination and lipaemia; neither is guaranteed.
- **Cases:** independently documented proven interference episodes **plus** genuine-pathology mimics and abnormal/non-interfered controls. Retain unresolved/insufficient-evidence episodes in a separate exploratory safety stratum, rather than mislabeling them as proven artefacts.
- **Unit:** one prespecified investigation episode per patient in the primary evaluation when feasible. Document the eligibility window and selection process; do not claim a challenge-set rate is routine laboratory prevalence.
- **T0:** the real decision time, before corrective investigation. Model inputs include only values/units, flags, observation data, analyser/method identifiers and context that were available by T0. Each field needs source/time provenance before any real-patient experiment.
- **Reference evidence:** laboratory documentation after T0, which neither LLM arm sees: where valid, corrected/repeat/alternative measurements, smear and specimen findings, and independently supported clinical diagnosis. These are evidence, **not** automatic truth (a repeat may still be interfered).
- **SOP availability:** the local SOP must be applicable at T0 and licensed/approved for research use. No confidential SOP is posted publicly or sent to an unapproved model provider.

### Arms and hypotheses

| Arm | Model view | Purpose | Study status |
| --- | --- | --- | --- |
| **L0** | One prespecified LLM, neutral interpretation prompt, **no SOP** | Primary descriptive estimate of critical error rate | Primary |
| **L2** | **Same** model/settings and T0 case, with applicable SOP text in context | Paired effect of SOP grounding | Key paired secondary comparison |
| **R** | Pre-existing laboratory middleware decision rules, or externally published flowchart frozen before test | Non-LLM comparator, **never ground truth** | Descriptive, only if accessible/valid |
| **Historical action** | Documented action the laboratory originally took | Real-practice context, potentially imperfect | Descriptive |

Two additional models (preferably one open-weights), fixed-version repeatability trials, or broader interference categories are optional descriptive extensions **only if the feasible case volume and processing permission justify them**. Do not build L1/RAG, tool-constrained L3, or a separate human-performance arm in Study 1. Their previous designs remain in Git history as superseded exploratory alternatives.

**Primary endpoint:** episode-level percentage of L0 recommendations containing **at least one independently adjudicated clinically critical error**, with a confidence interval. Examples: unqualified disease attribution despite analytical invalidity; suggesting release of an unreliable result; treating genuine pathology as mere artefact; or omitting a mandatory verification/safety action. These examples are *candidates for a clinician-approved manual*, not an unreviewed executable rule set.

**Mandatory companion endpoint, shown alongside the primary everywhere:** inappropriate withholding / unnecessary abstention on episodes adjudicated safely resolvable, plus overall safe coverage. A system that abstains on everything cannot be considered safe/useful merely because it avoids critical actions.

**Key paired comparison:** L2 versus L0 episode-level difference in critical-error risk, supported by an appropriate matched confidence interval and, if pre-specified, a paired hypothesis test. Diagnostic artefact recognition sensitivity/specificity, analytical-provenance errors, subtype outcomes and model instability are secondary/exploratory.

## Reference standard: two evidence layers, no circularity

**Layer A — evidence-supported episode classification:** a documented real-world outcome (proven artefact, genuine abnormality/non-interfered, or unresolved) plus parameter-specific analytical validity. Only valid hindsight measurements/smears/clinical evidence support classification. A case does not become 'proven' because a SOP/middleware rule flagged it.

**Layer B — acceptable decision-time actions:** two qualified biomedical scientists, experienced with the chosen analyser, independently specify action sets, reportability restrictions, mandatory checks and whether withholding/referral was justified. They see the reference evidence but **not** candidate model outputs or frozen rule-baseline predictions during reference labeling. Document raw disagreement; resolve by discussion and escalate persistent disputes to a qualified clinical co-investigator who did not write the rule baseline. Preserve ambiguous cases when no justifiable consensus exists.

The laboratory co-investigator should own case feasibility, SOP permissions, case curation and reference-evidence assessment, but **should not serve as one of the two initial action adjudicators** if a separate qualified pair is feasible. Reference classification is not identical to safe decision-time recommendation: post-correction measurements alone do not make the latter objective. Following reference lock, the same two experts may perform blinded free-text output grading with recorded decisions and conflicts; a separate permanent scoring panel is not presumed.

**Working severity rubric:** acceptable / non-critical error / potentially safety-critical error. Separately encode excessive abstention and insufficient-evidence handling. Lock criteria and examples after calibration, not before qualified clinical participation.

## Sampling, controls and information leakage

Before extraction, establish the case source population, lookback dates, one-patient/episode grouping, positive and negative case retrieval, how investigation was triggered, missingness, and exclusions. Investigating only middleware-flagged cases risks incorporation/selection bias; including only valid repeated samples risks verification bias. Record separate strata. The artificially enriched challenge set **cannot** estimate real-world prevalence.

Build a T0-only model view and an independent locked reference dataset. Never show post-action results, expert labels, answer keys, later notes or clinical diagnosis unavailable at T0 to any arm. Preserve source/time stamps within a restricted institutional environment and audit the actual model payloads. JSON Schema name filters alone are insufficient.

## Pilot, statistics and preregistration

- **Before partner data:** published case reports may be used for a clearly labeled *exploratory harness/prompt* pilot, with manual verification of source evidence, possible training-set contamination, case selection bias and rights checks. No published-case result is a clinical safety estimate.
- **After institutional permission:** if enough cases, use about **15–20 real development episodes** for adjudicator calibration and T0 validation; do not use them in the locked test.
- **Sample size:** determined after site aggregate counts and qualified methodological consultation. No fixed 100/150-case target or arbitrary effect assumed. Choose desired error-rate precision and a clinically justified paired comparison; document achievable uncertainty if the number is limited.
- **Analysis:** per-arm binomial confidence intervals; a paired L2–L0 difference interval; exact McNemar only when its independent-pair assumptions fit. One predeclared output per episode defines the primary result; additional stochastic calls are sensitivity/reliability data, not extra patient observations. Report adjudicator agreement and label-uncertainty sensitivity.
- **Freeze:** SAP, exact model ID/settings, prompts, input cutoffs, reference manual, split and output scoring procedures **before** access to the held-out evaluation results. Preregister when scientifically/ethically ready.

## Smallest practical team

PI (AI methods, software, writing), **one clinical haematology laboratory co-investigator** (site access, SOP, case evidence/feasibility), **two independent qualified haematology biomedical-scientist adjudicators**, and a statistical methodologist consulted for design and analysis. A research assistant can help with literature and nonclinical implementation. Recruit adjudicators *after* laboratory feasibility is confirmed.

## Scientific gates (simplified management, NOT exemptions)

1. **Partner:** written agreement in principle, named clinical lead and exact analyser family. **Review checkpoint: 15 January 2027**; if absent, re-evaluate after a bounded outreach extension and consider a published-case-only research paper with transparent limitations.
2. **Volume:** an institution-authorized **aggregate-only** feasibility count supports the chosen case-mix and desired statistical precision; otherwise narrow, extend the lookback, seek another permitted site or limit to descriptive study.
3. **Processing:** explicit ethics approval/waiver and lawful, institution-approved data/model processing route. If an external API is not approved, assess approved local/open-weight options, not unpermitted transfer.

**Additional required steps before any real case-level research:** signed data permission/DUA as appropriate, secure environment, independent adjudication, frozen externally sourced rule baseline, adjudication calibration, audited T0 payloads and preregistered analysis. Simplifying the *management* gates does **not** remove these requirements.

## Immediate priorities

1. Approach two or three prospective haematology lab partners with the one-page [collaboration brief](PARTNER_BRIEF.md), requesting a conversation, not data.
2. Rebuild a high-recall targeted literature search and include [Spies et al. (2023)](https://academic.oup.com/jalm/article/8/6/1092/7272601); do not screen all 2,145 PMIDs by default.
3. Optionally prepare a very small, openly sourced published-case pilot for workflow feasibility; defer new frameworks, data contracts and RAG engineering.
4. Freeze most repository engineering until partner feasibility and approved processing are clear.

**Status on 2026-10-11:** no laboratory partner, no approved local SOP access, no authorised patient data, no signed clinical reference labels, no registered analysis, and no study results.
