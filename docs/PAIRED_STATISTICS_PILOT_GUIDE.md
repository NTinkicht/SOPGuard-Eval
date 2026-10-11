# Paired binary safety endpoint: pilot planning guide (v0.1)

**Nonclinical research-methods utility. NOT a clinical model, registered statistical analysis plan, powered sample-size determination, real study result, or validated diagnostic procedure.** The code operates on *four aggregate counts only*, with fictional inputs in tests.

## The intended matched comparison

For a pre-specified LLM arm and deterministic rule baseline R, evaluate **the same eligible episodes**, each with exactly one selected output per arm for the preliminary primary binary endpoint: "at least one clinically adjudicated S4 safety-critical action". Do **not** treat multiple LLM runs or related episodes as independent observations.

| | LLM: no S4 | LLM: S4 |
| --- | --- | --- |
| Rule: no S4 | **neither** | **llm_only** |
| Rule: S4 | **rule_only** | **both** |

`N = neither + rule_only + llm_only + both`

- Rule error rate = `(rule_only + both) / N`
- LLM error rate = `(llm_only + both) / N`
- Matched rate difference (LLM minus rule) = `(llm_only - rule_only) / N`
- Exact two-sided McNemar test uses only the **discordant** `rule_only` and `llm_only` counts, conditional on total discordance.
- Wilson 95% intervals reported for each *marginal arm rate* are not a confidence interval for the **paired difference**.

## Built-in exploratory utility

```bash
python scripts/paired_binary_summary.py --neither 80 --rule-only 2 --llm-only 8 --both 10
```

Those numbers are **fictional mathematical input**, **not observations, expected event rates, power assumptions, or results from any laboratory**. The utility emits JSON descriptive counts/rates, separate marginal Wilson intervals and an exact paired McNemar p-value. It takes no case rows, clinical measurements, model prompts or SOP data.

The tool is not an alternative to statistician approval, a protocol-specified statistical model, or an independently blinded reference standard.

## Critical constraints before pilot use

1. Secure partner laboratory, ethics approval/waiver and DUA for case-level research.
2. Complete clinical adjudication and S4 severity taxonomy **without viewing model outputs**.
3. Predefine the one LLM arm used for primary comparison and first-run/replicate selection policy.
4. Define treatment of uncertain cases and eligible denominators, including controls and missing outcomes.
5. Account for patient/site clustering and repeated stochastic model runs in a prespecified inferential method; this simple utility does **not**.
6. Pilot discordance estimates are only planning information. Do not treat exploratory p-values as confirmatory or select comparisons after examining favorable results.
7. Have a statistician calculate formal matched-pair sample size and clinically justified safety margin, then pre-register the SAP before test-set evaluation.
8. Report per-stratum uncertainty and exact case selection; a balanced challenge benchmark is not a population-prevalence sample.

## Sources and methods

- McNemar, Q. 1947. *Note on the sampling error of the difference between correlated proportions or percentages*. Psychometrika 12:153–157.
- Wilson, E. B. 1927. *Probable inference, the law of succession, and statistical inference*. Journal of the American Statistical Association 22:209–212.

These generic statistical methods do not establish a valid clinical endpoint. The clinical interpretation and allowable error decision remain solely with qualified laboratory experts.

## Unresolved design choices for the statistician

- Which single primary LLM comparator and what inferential direction/margin?
- How will one selected output per episode be chosen, with sensitivity to run-to-run disagreement?
- What is the target matched-pair difference, expected discordant counts, and desired confidence interval precision?
- What is the correct sampling frame (consecutive clinical episodes versus deliberately enriched test cases)?
- Is one laboratory cluster sufficient for external validity? Are patient-level repeats rare or common?
- How to handle multiple acceptable action sequences and adjudicator disagreement?
