# Statistical analysis plan (SAP) - design template, NOT PREREGISTERED

Version 0.1. To be signed off by the study statistician and clinical panel **after feasibility/pilot data and before test execution**.

## Estimand and denominator

Primary estimand: per-episode proportion of safety-critical (S4) recommendation errors in each system arm, using the independently adjudicated action set and final locked severity taxonomy. The denominator is eligible held-out *episodes*, not repeated calls or individual calculated parameters. Define and pre-register the exact per-episode model-run selection rule.

## Primary comparison

Paired comparison of a designated LLM strategy against deterministic baseline R on the same held-out cases. Prespecify the chosen LLM arm, superiority/non-inferiority goal, one- or two-sided alpha, safety margin if applicable, and whether any co-primary outcome is used. Use an exact McNemar procedure for one paired binary decision per case where warranted; adjust for repeated episodes by patient/site and stochastic model runs using appropriate hierarchical or clustered analysis.

A [nonclinical paired-count pilot worksheet](PAIRED_STATISTICS_PILOT_GUIDE.md) is provided to illustrate the estimand; its aggregate arithmetic is not a full clustered/multiplicity-adjusted inferential SAP or a sample-size calculator.

## Uncertainty and robustness

Provide per-arm Wilson or exact confidence intervals; matched difference intervals where justified; stratify by interference class and true-pathology controls. Present both unadjusted results and planned sensitivity analyses. No assertion of 'zero risk' from zero observed events. Assess adjudicator uncertainty and misclassification.

## Sample-size planning

First obtain counts of eligible paired events by stratum and run a separate 40-60 episode development pilot **if cases permit**. Estimate discordant pair probabilities and target a clinically justified minimum difference/margin. Determine n using matched-pair power plus interval-precision and required-abstention-stratum precision; inflate for nonindependence and missing adjudicable labels. **No fixed 300/500-case requirement or predetermined effect size is scientifically justified yet.** Document the resulting calculation in the registered SAP.

## Other outcomes

Correct referral/withholding/recollection: sensitivity, specificity, appropriate/inappropriate abstention; SOP action set, numerical error on *permitted* calculations, provenance disagreement, paired post-action agreement only for clinically valid comparisons, run-to-run stability, and robustness under deliberately perturbed input. Use multiplicity correction for confirmatory secondary hypotheses; call other outcomes exploratory.

## Missingness and deviations

Pre-specify excluded/unresolved episodes, how to treat unavailable post-action values (not always an error), protocol deviations, model/API availability changes, and missing subgroup labels. Do not drop difficult cases post hoc or convert missing evidence into inferred clinical truth.

## Governance

Freeze and preregister before the first locked-test run. Hash data splits, SOP corpus, prompts, model IDs and evaluation configuration. Make de-identified summary outputs and allowed research code available, subject to clinical and legal review.
