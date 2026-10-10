# Research charter (v0.1 - for review)

Date: 2026-10-11. Status: **proposed**. No scientific, ethics or clinical approval implied.

## Working title

**When to Abstain: A Paired-Outcome Safety Benchmark of Large Language Models for Complete Blood Count Interference Management**

## Objective

Quantify how often LLM-based recommendations on potentially interfered CBC results are unsafe, inappropriate or unsupported by applicable laboratory SOPs, using real independently adjudicated cases and (where valid) post-intervention measurements. Compare with a strong deterministic baseline and qualified biomedical scientists.

## Target contribution

1. A traceable case-level clinical reference standard, including *legitimate withholding/referral* as successful outcomes.
2. A prespecified taxonomy of potentially safety-critical recommendations.
3. A paired comparison across deterministic, plain LLM, retrieved-SOP, oracle-SOP and tool-constrained approaches.
4. Empirical characterization of measurement provenance, abstention and errors on true-pathology negative controls.
5. Reproducible, ethically shareable research artifacts; clinical cases only under permitted access.

A high-performing rule baseline or a negative LLM result is informative. We do not pre-commit to promoting any architecture.

## Out of scope for Study 1

Four-vendor clinical deployment; live patient decisions; claims of manufacturer-equivalent corrections; model-generated reportable values; automatic SOP interpretation without owner approval; multicenter cross-vendor generalization; real-time productivity claims; claims that a numerical formula repairs an interfered measurement.

## Scientific uncertainties

- Which locally validated alternative methods are available and exportable?
- What action labels can be reliably adjudicated independently of SOP-encoded rules?
- Do post-action measurements adequately resolve each case?
- Are rare-interference strata sufficiently represented?
- Is an LLM helpful for explanation or narrative-to-rule formalization without compromising safety?

## Approval checkpoints

Clinical scope requires signed-off SOPs and analyser/IFU version. Case extraction and cloud/API processing require governance review and approval/waiver. The reference standard requires independent adjudication and a locked data specification. Analysis requires pilot-informed statistical justification and a sealed test split. No clinical use is authorized by this repository.
