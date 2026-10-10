# Laboratory feasibility pilot: operational plan (no data collected)

Status: 2026-10-11 proposal; G1 (partnership) and G2 (ethics/data permissions) remain **unmet**. This plan is not authority to extract or view any patient data.

## Sequence

**Phase 0 — prospective partner discussion:** confirm laboratory lead, analyser family/version, SOP availability, academic/research approvals, allowable data processing and which follow-up actions are actually recorded.

**Phase 1 — authorized aggregate count:** institution-controlled team queries number of eligible episode investigations, plausible analytical interference strata, available pre/post evidence, no-repeat outcomes, negatives, duplicate patients and missingness. Only governance-approved aggregate counts may leave the institution.

**Phase 2 — approved 40–60 case development pilot, if feasible:** independently adjudicate cases on the development split, estimate inter-rater disagreements, missingness and paired differences between candidate strategies. Size and conduct of pilot determined by access and approvals, not presumed in advance.

**Phase 3 — statistical freeze:** compute sample size from pilot discordance and stratum precision, name primary arm/comparator, define repeat-run estimand, pre-register and freeze test cases prior to evaluation.

**Phase 4 — confirmatory evaluation:** only after G1–G6. No clinical work-flow integration.

## Blank aggregate counting worksheet

[Feasibility template CSV](feasibility_count_template.csv) contains **only column names**, no lab records or example counts. Include dataset period start/end under approved internal format, count unique patients and investigation episodes separately, and record whether repeat values are valid reference evidence.

## Decision gates

| Decision | Pass condition | If not met |
| --- | --- | --- |
| Ethics/legal access | Approval/waiver, DUA and approved infrastructure | No individual record processing |
| SOP eligibility | Current laboratory SOP and exact analyser/software matched | No machine-executable clinical pathways |
| Paired case sufficiency | Numerically valid follow-ups and/or independently adjudicable abstain/refer outcomes; enough for planned precision | Narrow scope or seek second partner with new approvals |
| Reference independence | Independent clinical labels separate from rule engine | Redesign reference standard |
| Pilot precision / power | Scientifically defensible paired sample-size plan | Reframe as descriptive pilot, not a powered Q1 evaluation |
| Public artifact release | Institutional privacy/IP approval | Release only protocol, code and nonclinical synthetic metadata |

**No-go outcome is a legitimate research management decision.** Do not manufacture simulated clinical outcomes to make a target sample size look achievable.
