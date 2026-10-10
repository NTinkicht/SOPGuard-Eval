# Research evaluation contract (v0.1)

This contract defines **metadata and research outputs only**. It is not an executable clinical SOP, model prompt, validated inference rule, or patient result.

## Inputs

Use `schemas/benchmark_episode.schema.json` in a **restricted research environment** for case episodes and provenance. JSON Schema validation checks fields/types, not their truth, permissible use or medical reliability. Real patient-derived episodes must **never be uploaded to this public repo**.

Each episode contains:
- synthetic/research case ID, anonymized grouping key retained only privately, selected analyser/software/SOP applicability metadata;
- source measurement array with numeric values, original and normalized units, method/provenance and availability labels;
- analyser flags and contextual evidence;
- outcome evidence about corrective actions and repeat values **where meaningful**;
- locked adjudication label, including ambiguous / must refer / no reporting.

## Model output contract

`schemas/research_output.schema.json` encodes a candidate **research recommendation**, never instructions for a laboratory operator. Its fixed high-level actions include `NO_ACTION`, `REANALYZE_PER_SOP`, `REQUEST_ALTERNATIVE_MEASUREMENT`, `WITHHOLD_OR_RECOLLECT`, `REFER_FOR_REVIEW`, `REPORT_WITH_CONDITIONS` and `ABSTAIN_INSUFFICIENT_EVIDENCE`.

Outputs must identify `sop_version_used` if used, evidence references, which measurements were used, requested verification and a transparent reason for no recommendation. A calculated value is only hypothetical research output, and may be present only in a nested provisional field marked `not_reportable: true`. **A typed field cannot make a clinical calculation valid.**

## Dataset and prediction separation

The case JSON (restricted) must never include adjudication reference labels in a model's prompt payload. Construct separate explicit prompt views stripped of `adjudication`, follow-up evidence when prospective visibility would be improper, and private metadata. No post-correction results leaked into model inputs unless the evaluation task explicitly calls for retrospective interpretation of those results.

## Scoring

- One episode's **maximum adjudicated severity** determines the primary critical-error indicator.
- `S4` errors are unsafe recommendations that could plausibly lead to wrong result release, concealment of pathology or skipped mandatory safety action.
- Incorrect, unsupported or unnecessary abstention is measured separately; do not automatically classify every abstention as S4.
- Arithmetic and unit errors are graded by clinical consequence, not cosmetic display.
- Blinded raters assess candidate outputs; an LLM judge cannot establish the primary reference standard.

## Provenance and protected controls

Do not infer that a source quantity is reliable merely because it is marked `MEASURED`. Distinguish *origin* (measured, derived, validated alternative) from *reliability* (trusted, unreliable, unavailable, uncertain). This corrects the conflation in the original five-label shorthand.

## Post-action outcomes

Post-action measurements can be supplementary empirical reference but may remain interfered; model cannot simply match a target number on every case. Include explicit `valid_as_numerical_reference` and an expert rationale outside model view.

## Pilot-only calculations and documentation

Before clinical validation, any calculation test is a non-clinical type/unit demonstration. No patient results, laboratory correction algorithms, or real model outputs are produced until research governance gates are satisfied.
