# Draft study protocol - NOT REGISTERED

Version: 0.1, 2026-10-11. Every element remains conditional on a partner laboratory, expert review and ethics assessment.

## Study design

Retrospective, single-analyser-family, paired-outcome, comparative safety evaluation. Primary evaluation cases are real de-identified laboratory records after appropriate ethics/data-use authorization. An original instrument run may be paired with a repeat after permitted warming, plasma replacement, dilution, alternative channel measurement or recollection **when such a comparison is clinically meaningful**. Neither a repeat nor a rule engine is automatically declared ground truth.

### Population / sampling frame

Consecutive or systematically sampled records flagged for investigation over a declared look-back period, together with verified negative controls. Record site, exact analyser model/software, flag export capabilities, SOP applicability, look-back limits, selection mechanism and excluded cases. Count unique specimens and patients to avoid pseudo-replication.

### Scope proposed for partner selection

- Initial focus: cold agglutination and lipaemia, if the selected lab can supply sufficient validated cases.
- Mandatory negative controls: true red-cell disease, neonatal cases where available, genuine abnormalities not caused by interference, ordinary non-interfered cases.
- Special safety strata: in-vitro versus potentially in-vivo haemolysis, unresolved agglutination, warm agglutinin suspicion, other raised-MCHC causes, multiple interferences. If clinical context is insufficient, the correct label can be *uncertain: refer/withhold*.
- Add icterus or other interferences only with validated site evidence and a justified analysis plan.

### Unit of analysis

One pre-defined specimen investigation **episode** is the primary unit. Related repeated runs, multiple specimens and multiple LLM stochastic runs must be linked to prevent accidental independence assumptions.

## Decision support comparator arms

| ID | Arm | Purpose |
| --- | --- | --- |
| R | Deterministic SOP engine with unit/provenance enforcement and explicit abstention | Strong baseline, not ground truth |
| H | Qualified biomedical scientist, unaided, on an independently planned case subset | Human comparison |
| L0 | LLM without SOP access | Unconstrained baseline |
| L1 | LLM with approved applicable SOP retrieval | Retrieval effect |
| L2 | LLM given the correct SOP excerpt (oracle passage) | Isolate retrieval from reasoning failure |
| L3 | LLM with SOP context, structured output, and deterministic arithmetic tool | Assess safeguards, not direct clinical operation |

Use at least two model families if feasible, frozen model IDs/settings and recorded prompts. Pre-specify number of repeats and primary aggregation; repeated calls are not independent patient cases. All model outputs are research suggestions only.

## Reference standard

A blinded independent panel assigns permissible actions, parameters that may be reported, invalid measurements, mandatory verification, comments and abstention/recollection. The adjudication charter controls provenance, disagreements, uncertainty and grading. Post-action measurements provide independent supporting evidence when valid.

## Primary endpoint

Case-level **Safety-Critical Error Rate (SCER)**: proportion of episodes with at least one candidate action classified as critically unsafe under the locked adjudication policy. Pre-specify whether a repeated LLM invocation counts via first run, majority action, or run-aggregated error. Report run-to-run variability separately.

Examples: recommending release of an invalid result; calculations from invalid inputs; missing required recollection; treating genuine disease as specimen artifact; recommending a contraindicated procedure; claiming unsupported alternate measurement reliability.

## Secondary endpoints

- Correct SOP-constrained pathway and action-set agreement.
- Sensitivity and specificity for clinically required withhold/refer/recollect actions.
- Unnecessary abstention rate and safe case coverage.
- Numeric accuracy **conditional on permitted calculation**, plus agreement with appropriately valid post-action reference values.
- Unit and measurement-provenance errors, wrong-SOP selection, explanation quality scored by humans, repeated-run consistency.
- Outcomes by interference, model family, missingness and clinical control group.

## Controls and bias management

Independent source of labels, separate rule authors from adjudicators, development/test isolation, blinded model-output scoring, frozen cases, and explicit eligibility exclusions. Synthetic counterfactual transformations (unit swaps, expired SOP, wrong-analyser SOP, missing flags, comment injection) are **stress tests only**, not estimates of clinical frequency or primary safety rate.

## Analysis and reporting

Pilot the discordant-pair probabilities; use a pre-specified paired primary comparison with uncertainty intervals and multiplicity strategy. Treat repeated runs as clustered. Record failures and abstention denominators. Avoid describing absence of observed errors as proof of zero clinical risk. Specify any external-validation site separately.

## Ethics and registration gates

No ingestion of patient data before ethics approval/waiver, DUA and a compliant infrastructure plan. No external LLM processing without explicitly approved transfer and vendor arrangements. Register the locked protocol and analysis plan before running the frozen test set. Follow relevant TRIPOD-LLM items and laboratory reporting guidance.
