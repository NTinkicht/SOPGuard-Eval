# Reference-standard and adjudication charter - draft

**Not an approved SOP.** Local medical and laboratory experts must adopt or revise this before any case is scored.

## Independence

Target three qualified adjudicators from laboratory medicine/haematology, independent from deterministic-rule authorship. Conduct calibration on development records, then independent blinded labeling. Preserve raw ratings before consensus and report inter-rater agreement where estimable. An unresolved case must not be silently converted into a definite label.

## What adjudicators receive

De-identified original analyzer outputs, instrument flags, specimen characteristics, eligibility-limited clinical context, exact lab SOP/IFU version, and documented corrective actions plus valid downstream measurements, as applicable. **No candidate system output during reference labeling.**

## Required ground-truth fields

- Evidence sufficiency: sufficient / insufficient / disputed.
- Suspected cause: candidate categories, including no interference, true pathology, multiple and undetermined.
- Per-parameter reliability/provenance and expected source of evidence.
- Permitted action set: reanalyze under approved procedure, validated alternative measurement, report with restriction/comment, withhold/recollect, refer for additional review; each with prerequisites.
- Required vs optional verification actions (smear, plasma appearance, clinical history, delta review, other relevant checks).
- Explicitly reportable and non-reportable outputs, correct rounding/unit policy where confirmed.
- Allowed abstention state with reason, plus potentially dangerous contraindicated actions.
- Clinical evidence provenance: original specimen, repeat specimen, microscopy, additional context and adjudicator rationale.

## Grading output proposals

Grade **per action** then per case (most severe action determines safety-critical indicator). Draft hierarchy:

- S4: potentially safety-critical, plausibly leading to invalid reporting or masked pathology.
- S3: serious pathway error, likely caught by competent review but risks delay/unnecessary work.
- S2: minor presentation or non-safety numerical detail error that cannot affect reportability.
- S1: cosmetic/explanatory weakness.
- A-: unsupported or unnecessary abstention on an otherwise resolvable case (track separately).

Severity of any unit/arithmetical mistake depends on **potential downstream consequence**, not automatically S2. Do not downgrade an omitted mandatory review step merely because a human might notice it. Require examples and inter-rater testing before locking severity rules.

## Adjudication workflow

1. Two or three experts independently annotate the same development set.
2. Compare disagreements; revise the annotation manual, not test labels.
3. Freeze the manual and panel protocol.
4. Independently label held-out cases without seeing any model or rule-engine outputs.
5. Resolve via documented discussion and, where needed, an additional independent expert.
6. Separate blinded scoring panel scores candidate outputs against the locked reference; retain raw grades, consensus and dissent.

## Methodology warning

Neither the deterministic engine nor the post-correction measurement is automatically ground truth. A repeat can remain interfered; an appropriate action can be *do not report*, even when no corrected value exists. Avoid hiding ambiguity by forcing a single incorrect answer.
