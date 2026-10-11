# SOPGuard-Eval — preliminary statistical plan v0.2

**Draft only: NOT preregistered, powered, or clinically approved.** This document supersedes the earlier six-arm planning assumptions; the [simplified protocol](PROTOCOL_DRAFT.md) is authoritative. Confirm the plan with a statistical methodologist and laboratory co-investigator after the authorized site feasibility count.

## Primary descriptive estimand

For the predeclared primary LLM **L0**, estimate the proportion of eligible, held-out, independently reference-adjudicated **investigation episodes with at least one clinically safety-critical recommendation** at the original decision time T0. Use one eligible episode per patient in the primary dataset if feasible. Define exact eligibility and unresolved cases *before* test inspection.

Report the **unnecessary-abstention rate and safe coverage alongside this primary error rate in every table**, so a strategy of abstaining on all episodes cannot appear successful.

## Key paired contrast

The same cases, prompt structure and prespecified model, with and without the applicable SOP in context (**L2 minus L0**) comprise the main paired comparison. Report the *matched risk difference with a suitable confidence interval* and, if predeclared and applicable, a two-sided exact McNemar test. Prespecify one confirmatory contrast and how multiplicity/exploration will be handled.

If the primary outcome is a descriptive rate rather than a superiority test, state that clearly in the eventual registration; avoid advertising both as separately powered primary hypotheses without a justification.

The **R** pre-existing-rule comparator and documented historical actions are descriptive references, not truth labels. Additional models, stratified comparisons and alternative prompts are exploratory unless prospectively justified.

## Clinical endpoint and reference uncertainty

The severity manual should be reviewed by two independent qualified adjudicators after a 15–20 development-case calibration if permitted. A case-level critical error is a recommendation likely to lead to reporting analytically unreliable findings, missing essential verification, or obscuring genuine pathology. Grade other errors non-critical; acceptable includes justified referral/withholding. Flag inappropriate abstention separately.

Layer A (laboratory hindsight evidence) supports artefact/pathology status; Layer B (independently adjudicated acceptable T0 actions) determines safety. An objective repeat value does not itself establish the safety of a recommendation. Keep pre-consensus raw ratings, agreement and sensitivity to ambiguous cases.

## Precision and sample size

Do not prescribe n=100 or n=150 in advance. Site aggregate counts determine plausible strata; methodologist selects acceptable uncertainty width, clinically meaningful matched difference and anticipated discordances, and designs a feasible sample size. Confirm real-case development/test isolation. A 40–60-case real-data pilot may squander scarce cases; **15–20 authorized development episodes** may suffice for rubric calibration, but sample is determined by site evidence.

The existing [aggregate paired-binary demo](PAIRED_STATISTICS_PILOT_GUIDE.md) validates generic arithmetic only. It does not adjust for repeated patients, stochastic calls, site clusters, uncertain labels, outcome misclassification or match risk-difference CI.

## Run and model policies

Primary = first predeclared model response per case under fixed sampling parameters (or another prospectively specified single-output rule). Further calls, including up to five if feasible, assess variability as **repeated observations of the same case**. Fixed model snapshot IDs, parameters, runtime, SOP versions/hashes, predecision source data and failed calls are logged. A patient-level split and a T0 audit prevent test leakage; no T0 context is inferred from future evidence.

## Planned reporting

Binomial confidence intervals for arm rates; matched difference CI for L2 vs L0; expert agreement; abstention and safe-coverage rates; artefact-detection sensitivity/specificity in defined reference strata; patient-level and analyser-class sensitivity analyses only when valid; exclusions/missingness and pre-specified subgroup denominators. If few critical events occur, do not claim 'zero risk.' A challenge-enriched cohort estimates performance **within that constructed sample**, not prevalence in routine laboratory work.

## Freeze

Lock the rubric, reference set, data inclusion, T0 payloads, model/prompt settings and SAP *before* running the held-out experiment. No clinical-data processing or cloud LLM transmission until approvals/DUA and provider/jurisdiction assessment are documented.
