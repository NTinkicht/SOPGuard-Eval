# SOPGuard-Eval — draft independent clinical reference standard v0.2

**For review by a partner laboratory. No clinical SOP, medical approval or case labels are established here.** Supersedes the proposed standing three-person panel and separate permanent scoring panel.

## Team and independence

The preferred minimum for Study 1 is **one clinical haematology laboratory co-investigator** plus **two independently labeling experienced biomedical-scientist adjudicators** familiar with the partner's analyser family. The co-investigator secures SOP applicability, coordinates authorized case curation and assesses whether clinical records support reliable post-action evidence. The co-investigator should not be one of the two initial action adjudicators if feasible, and must not be the author of a comparator whose predictions define ground truth.

A third clinical expert is *on call* only to resolve persistent disputes. After the reference is locked, the two original adjudicators may also **blindly score candidate free-text recommendations** without establishing a separate panel. Record identities/roles, conflicts and all raw judgments privately.

## Two-layer reference

**Layer A — evidence about what happened.** Independent, clinically verified classifications: proven interference, genuine pathology/other noninterfered result, or unresolved; which parameters were unreliable; what hindsight measurements, smears, recollection, specimen context or diagnosis genuinely substantiate the category. No case is declared valid just because a published SOP or deterministic rule predicts a label. If the repeat remains affected, label unresolved rather than calling the new number corrected.

**Layer B — acceptable decisions at T0.** On separately recorded labels, both adjudicators identify the acceptable set of actions given the data *known at decision time*, mandatory investigations, reporting conditions, clinically important forbidden actions and justified referral/withholding. Several action sequences can be acceptable. Outcome evidence can inform truth but should not be silently treated as an action that was obvious at T0.

A decision-time mandatory check **must be justified by prospective evidence and the site SOP**, not retrospectively required only because later results uncovered the problem. Such distinctions guard against hindsight bias.

## Labels and consequences

Use **acceptable / non-critical error / potentially safety-critical error**, with a separate inappropriate-abstention flag. The definitions require exemplar development cases, clinical consequence, disagreement review and explicit preservation of unclear records. Do not assign cosmetic grading labels whose inter-rater agreement is unlikely to matter to the primary endpoint.

Core safety examples to validate locally:
- confidently treating a confirmed invalid measurement as reportable;
- disease attribution that ignores credible signals of analytical invalidity;
- dismissing genuine pathology as artefact without adequate evidence;
- omitting an essential test/review when necessary to avoid erroneous reporting;
- calculations from invalid inputs presented as repaired CBC results.

Explanatory weakness alone does not make an error critical. Do not infer reportability from measurement *origin* alone: measured, derived and alternative-channel methods require a separate reliability determination.

## Calibration and frozen adjudication

1. Establish ethical data authority and a linked episode register; select only authorized development episodes for training on the rubric (about 15–20 if feasible).
2. Adjudicators independently label without seeing model predictions, historical reference predictions or the deterministic comparator's outputs.
3. Review disagreements and change the *manual*, not held-out test answers; freeze it.
4. On held-out episodes, collect independent ratings and preserve disagreement; resolve by discussion with an on-call expert if needed.
5. Only after reference lock, evaluate model responses using blinded grading by qualified reviewers; document disagreements, agreement statistics and sensitivity to alternate raw labels.

Clinical adjudication cannot be performed by AI reviewers, students, the PI's prompts, or the lab's rules alone.

## Exception handling

Unresolved episodes remain a distinct uncertainty/safe-handling stratum. Cases with insufficient evidence for critical-error classification should not be forced into a definitive primary binary label. Decisions to exclude require predeclared reasons, reported counts, and assessment of selection bias.

**No patient data, restricted SOPs or case-level expert notes in the public repository.**
