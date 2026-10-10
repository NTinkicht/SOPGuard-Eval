# Eligibility, sampling and bias mitigation — draft

Status: v0.1, unapproved. The laboratory must define the sampling frame before extraction or intervention.

## Unit and anchor

An **episode** is a particular specimen investigation workflow triggered by the local laboratory, not each CBC run. Multiple original, warmed, centrifuged, alternate-channel or recollected runs may attach to the same episode. Link repeated specimens belonging to the same patient securely for splitting; do not publish identifiers or linkage salt.

The intended initial source population is **all consecutive or systematically sampled routine haematology specimens within a fixed period**, with stratified sampling for relevant investigated cases and independently assembled controls. Each clinical safety proportion is interpreted relative to its sampling frame; an intentionally balanced challenge set cannot estimate population-wide error prevalence.

## Eligibility candidates

- Known analyser family, software version, contemporaneous SOP version and enough original CBC data/flags for the task.
- Site-recorded investigation of suspected interference or defined non-interference control.
- Subsequent documented action/result evidence **when relevant and available**; an episode can have 'withhold/refer/recollect' as its correct end state without a corrected number.
- Minimum approved contextual evidence to distinguish interference suspicion from a genuine pathology or ambiguity.

## Exclusion and uncertainty

- Ineligible model/software or unknown SOP applicability.
- Patient-data governance limitations; lack of permission for research export.
- Irretrievably missing original source evidence needed to judge the workflow.
- Nonresolvable ambiguity should usually be **retained as an uncertain/abstain stratum**, not quietly deleted.

Create explicit exclusion counts by reason. Specify selection criteria *before* outcome adjudication and preserve uncertainty labels.

## Major biases and controls

| Bias | Mechanism | Mitigation |
| --- | --- | --- |
| Spectrum bias | Overrepresentation of dramatic raised-MCHC cases | Include true pathology, routine noninterfered and borderline cases; report strata |
| Verification bias | Only specimens re-tested provide numerical follow-up | Do not require repeat value for all safe-abstention outcomes; report missing follow-up by arm/stratum |
| Incorporation bias | Same SOP decision rules define both labels and baseline predictions | Separate rule authors and adjudicators; external clinical evidence; blind and independent ratings |
| Selection bias | Convenient available samples omit difficult or unresolved cases | Consecutive sampling when possible; refusal/exclusion accounting |
| Leakage | Same patient or episode runs across development/test | Group by episode/patient; time/site holdouts; frozen test hashes |
| Site dependence | Local SOP thresholds and instrument features vary | Report exact site/analyser/SOP revision; no unsourced cross-vendor claim |
| Reviewer bias | Experts know system origin when grading | Independently blinded candidate-output scoring |
| Clustering | Multiple cases per patient and repeated stochastic outputs | Explicit hierarchical analyses; runs never treated as independent patients |

## Pre-extraction feasibility counts

Record, under authorized institutional processes, total eligible episodes, per-class counts, number with intervention and follow-up evidence, missing fields, age-band availability (including neonates), true pathology controls, potentially warm agglutinins, potential in-vivo haemolysis, and duplicates by patient. These are restricted aggregate counts until release is approved.

## Clinical meaning of pairing

Paired samples are **evidence, not automatic truth**: repeat values can remain affected, a recollection can represent a different physiologic moment, and withholding a result has no numerical target. Expert action labels must distinguish these situations.

## Public sample restrictions

Only schema definitions, approved derived statistics and explicitly synthetic toy demonstrations belong in this repository. No real CBC row, laboratory SOP clause or row-level ground truth is presumed publicly releasable.
