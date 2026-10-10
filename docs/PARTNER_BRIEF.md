# SOPGuard-Eval: collaboration brief for accredited laboratory partners

**Research-only project concept. No live clinical software or patient-result authorization.**

## Why we are conducting this study

Instrument flags, genuine pathology and analytical interferences can complicate whether CBC-derived results can safely be reported. Laboratories have established analyser-specific SOPs, published expert decision trees and middleware workflows. We are **not** proposing to replace them. Instead, we intend to evaluate whether LLMs follow those existing practices safely, especially when results should be withheld or an additional investigation is needed.

## Scientific aim

An independent safety evaluation will compare deterministic SOP rules with several LLM configurations and qualified biomedical scientists on retrospective CBC interference episodes. The proposed primary endpoint is the percentage of episodes containing at least one safety-critical recommendation error. Cases would include original instrument values and follow-up actions/results **where available and appropriate**, with independent specialist adjudication.

## Proposed initial scope

One analyzer family selected by the partner, ideally covering investigated cold agglutination and lipaemia, supplemented by genuine-pathology negative controls, unresolved cases and other locally relevant safety branches. A secondary laboratory is optional for later external validation. No vendor-specific or correction procedure is assumed in advance.

## What we would request from the laboratory

1. A named haematology lead and institutional research liaison.
2. Identification of instrument model/software and applicable, currently approved laboratory SOPs, with terms governing permitted use of manufacturer instructions.
3. A feasibility assessment of retained CBC investigation episodes, including original/repeat values, recorded intervention, flags, exported alternative parameters, plasma/smear observations and specimen metadata.
4. Two or three qualified adjudicators independent from rule authorship, plus a method for documenting unresolved cases.
5. Assistance obtaining ethics approval or a waiver, legal data-use agreements and secure processing arrangements.
6. Agreement on authorship/contributions, publication rights, data retention and which abstractions can be openly shared.

## What the partner receives

A co-designed research protocol, reproducible evaluation method, clinical safety/error taxonomy, audited comparison against the partner's verified procedures, and the option to review resulting manuscript findings and allowed rule abstractions. **No promise of a production medical device or validated clinical workflow** is made.

## Information governance

The public GitHub repository contains no patient data, restricted SOP text or manufacturer manuals. Real data will only be processed in an authorized research environment after formal approval. No cloud LLM will receive patient-derived content unless that exact transfer is approved. Published data may be aggregate, synthetic demonstration-only or controlled-access depending on policy.

## Proposed collaboration sequence

Scoping discussion → access/feasibility review → ethics and data-use approval → clinician-owned adjudication charter → pilot and sample-size determination → pre-registration → locked retrospective benchmark → joint interpretation/publication.

## Scientific references

- GFHC raised-MCHC review (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12426809/
- XN-10 interference flowchart evaluation (2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9804823/
- TRIPOD-LLM reporting guidance (2025): https://www.nature.com/articles/s41591-024-03425-5

Contact and institutional details can be added once formally agreed; this brief intentionally does not identify or imply an existing partner.
