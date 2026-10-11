# Research positioning decisions after October 2026 targeted discovery

**Status: methodology discussion; requires statistician and laboratory clinician sign-off.**

## A. The novelty claim has narrowed

Broad claims are no longer tenable in light of published LLM laboratory medicine safety evaluations (Diagnostics 2026), SOP execution benchmarks (SOP-Maze 2026, SOP-Bench project) and medical abstention benchmarks (MedAbstain 2026). The research is **not** about inventing SOP-following, an abstention option or another CBC chatbot.

The key empirical question is:

> In retrospective real-world episodes of suspected CBC analytical interference, how frequently do LLM workflows propose a safety-critical action compared with independently adjudicated reportability/action decisions and an approved SOP-encoded deterministic comparator?

This question remains conditional on real data and permission and has not been shown to be unstudied.

## B. Independent reference standard takes precedence

The reference standard **cannot** simply be the deterministic rule's own output. It must be built by qualified laboratory experts independently of system outputs, with SOP version and supporting evidence, including follow-up results *when they are valid*. Discordant expert decisions must be retained and resolved transparently.

## C. New risk of metric conflation

The 2026 Diagnostics study used expert-rated unsafe or guideline-discordant recommendations in a text-based educational benchmark. Our proposed primary endpoint is **case-level independently adjudicated potentially safety-critical action**, not directly comparable to published percentages without harmonized case definition, unit, actions, adjudication, and severity. Do not create an artificial numerical 'beat 2%' benchmark.

Also distinguish:
- one model answer vs multiple stochastic runs;
- scenario-level action safety vs generic clinical-management quality;
- true justified withholding vs unjustified abstention;
- measured vs derived parameter origin vs reliability status;
- numeric consistency vs analytic validity;
- benchmark composition vs population prevalence.

## D. Sensitivity analyses and design upgrades

1. **Case-mix:** report stratified by initial flag pathway, plausible true pathology, missing data and interference category. Rare strata should not be concealed in pooled results.
2. **External validity:** explicitly identify single-lab, single analyser, unit conventions, software versions, and SOP revision; only test other labs with permission and independent evidence.
3. **Fair comparison:** each arm receives clearly logged information available by decision time T0; L1 retrieval vs L2 oracle passage must not inadvertently reveal a reference answer.
4. **Adjudication:** independent pre-consensus labels and blinded response scoring. Make adjudicator ambiguity itself an analyzable phenomenon.
5. **Statistical analysis:** clinical critical-error rate prespecified; paired difference from rule comparator; repeated runs clustered; pilot-derived sample size. No claim of zero risk from zero observed S4 events.
6. **Negative controls:** true elevated MCHC pathology, neonates where eligible, other artefacts/mimics; do not overfit the benchmark to treat every flagged case as artefact.
7. **Out-of-scope:** no direct patient report decisions, experiment API calls using patient data, unsupported correction formulas, full four-vendor tool.

## E. Reporting standards

TRIPOD-LLM supports transparent reporting of LLM evaluation. STARD-AI may be additionally applicable if the final protocol includes a diagnostic accuracy claim with an appropriate index test/reference standard. Select the actual study design first and document justification; multiple checklists do not compensate for invalid ground truth.

## F. Gating

Research preparation and bibliography can proceed in this public repository. Any real retrospective extraction, paired case validation, clinical SOP encoding, cloud model calls or clinical findings remain gated by named laboratory collaborator, ethics/data-use approvals, SOP permissions, independent adjudicators and locked protocol.
