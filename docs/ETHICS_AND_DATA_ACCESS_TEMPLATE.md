# SOPGuard-Eval: draft ethics / data-access submission pack

**Template only. Not submitted, approved, or an institutional legal opinion.** Institutional research ethics, laboratory governance, and legal/privacy officers must adapt and approve this text before any data access.

## 1. Project identity
- Working title: *When to Abstain: A Paired-Outcome Safety Benchmark of Large Language Models for Complete Blood Count Interference Management*.
- Sponsor/institution: **TO BE COMPLETED BY INSTITUTION**.
- PI and co-investigators: **TO BE APPROVED**.
- Participating haematology laboratory and accreditation: **NOT YET CONFIRMED**.
- Jurisdiction, data custodian, accountable controllers/processors: **TO BE DETERMINED**.

## 2. Background and rationale

Published consensus decision trees and analyser-specific handling procedures for unreliable CBC measurements provide an established deterministic reference. LLMs may produce unsupported interpretations and numerical errors. This retrospective research project asks whether candidate AI workflows produce safety-critical recommendations compared with an independently adjudicated reference standard and a local deterministic SOP implementation. **No patient result may be influenced by any candidate output.**

## 3. Objectives

**Primary:** Estimate the case-level proportion of at least one adjudicated safety-critical recommendation error by evaluation arm in offline retrospective episodes.

**Secondary:** Proper withholding/recollection/referral; false intervention on real pathology; SOP adherence; numeric accuracy only for SOP-permitted calculations; repeatability; reliability/provenance classification; subgroup differences.

Hypotheses and primary comparator will be locked in a statistical analysis plan *after* pilot feasibility and before held-out analysis. No effect size, sample size or safety rate is asserted here.

## 4. Design and cohort

- Retrospective, de-identified/pseudonymized data under an institutionally approved method.
- Initial one analyser family/site; evaluated specimen-investigation episodes and legitimate non-interference controls.
- Inclusion/exclusion/sampling and duplicate patient handling: [eligibility draft](ELIGIBILITY_AND_SAMPLING.md).
- Paired original/follow-up data only where meaningful; valid 'abstain/withhold/recollect' episodes may have no numerical target.
- No recruitment, changes to clinical care, sample treatment, device integration, or patient contact in phase 1.
- Feasibility counts and a development pilot precede confirmatory sample-size determination.

## 5. Data minimization worksheet

Proposed fields subject to independent necessity/permissions review:
- Pseudonymous episode linkage (not an accession identifier).
- Instrument model/software, flag categories, raw/derived CBC values with original units.
- Applicable approved SOP identifier and revision (licensed full text kept restricted).
- Limited specimen context, available pre-decision observations, clinically essential age bands/conditions, and approved follow-up evidence.
- Separate adjudicator action/reportability labels and later reference measurements.

**Not requested for public release:** names, contact information, exact dates of birth, addresses, original accession identifiers, patient-level notes containing identifiers, uncontrolled free-text or linkage keys.

Describe institutional lawful basis; waiver/consent decision; extraction queries; minimization; small-cell aggregation protections and governance sign-offs before use.

## 6. Security and model-processing boundary

- Institution-approved restricted environment for working data.
- Re-identification linkage, if allowed, stored separately under the data custodian.
- Named authorized roles, access logs, encrypted transit/storage, key controls and retention/deletion schedule to be filled and approved.
- No raw or pseudonymous patient records in GitHub, public issues, CI logs, public artifact stores or external analytics.
- No patient-derived prompts to a cloud model/API unless the institution expressly approves vendor, jurisdiction, data-processing terms, retention and security. Consider an authorized local model when cloud use is forbidden.
- Model inputs are separated from adjudication and post-decision evidence using [model view](MODEL_VIEW_FIREWALL.md); schema tests alone do not prevent semantic leakage.

## 7. Expert adjudication and conflicts

At least two qualified independent clinical adjudicators, ideally three, with an independently designated rule-author group. They will receive an approved reference package and assign acceptable action sets, contraindicated actions, reportability, and abstention. Preserve raw judgments and disagreements. Blinded second reviewers score system responses.

## 8. Risk and mitigation

| Potential risk | Mitigation proposed | Who must authorize |
| --- | --- | --- |
| Privacy breach | Approved minimization, secure storage, audit and release control | Institution privacy/security |
| Using invalid rules as ground truth | Independent adjudication and valid post-action evidence | Haematology lead |
| Model recommendation used in care | Offline evaluation with no LIS/instrument connectivity and clear research-only labels | Clinical governance |
| SOP/IFU IP leakage | Restricted documents, authorized extracts, publication check | Lab/vendor/legal owner |
| Clinical ambiguity masked in pooled score | Unresolved/abstain labels and stratified analysis | Clinical panel/statistician |
| Unapproved international data transfers | No external model calls before written processing authorization | Data controller/legal |

## 9. Outputs and dissemination

Proposed: peer-reviewed safety benchmark paper; documented evaluation harness, abstract data contracts, pre-registered analysis and synthetic toy examples. Any patient-derived data release requires an explicit separate approval (possibly controlled-access only); aggregate outputs must be privacy-reviewed.

## 10. Approval checklist — MUST BE FILLED

- [ ] Named PI, sponsor and clinical laboratory
- [ ] Local research ethics approval / written waiver, reference ID and dates
- [ ] Data use agreement with sharing/retention limitations
- [ ] Detailed de-identification and legal-basis assessment
- [ ] Vendor/cloud model terms approved or explicitly forbidden
- [ ] SOP/IFU use and derived-rule publication rights resolved
- [ ] Independent adjudicators confirmed
- [ ] Institution-approved secure infrastructure identified
- [ ] Study protocol, SAP and governance version controlled
- [ ] Public release review and incident response ownership assigned

**Current status of every approval item: unconfirmed. This document establishes no permission.**
