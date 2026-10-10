# Benchmark data dictionary - draft (NO REAL RECORDS IN REPO)

This is a proposed metadata specification, not a clinical inference schema or actual data dump. Site privacy staff and haematology leads must approve the eventual fields and redaction strategy.

| Field | Type | Meaning / requirement |
| --- | --- | --- |
| episode_id | Pseudonymous string | Research episode key, no accession number |
| site_code | Pseudonymous string | Site grouping for analyses; keep mapping offline |
| analyser_vendor, model, software_version | Strings | Exact machine/software recorded at the time |
| sop_id, sop_version, effective_date | Strings/date | Locally approved SOP applicable at episode time |
| source_run_id / repeat_run_id | Pseudonymous strings | Link originals to relevant downstream measurements |
| parameter_code, value, unit | String/decimal/string | Preserve original notation and normalized unit separately |
| parameter_method | Categorical | Site-confirmed measurement/derivation method; do not infer from vendor alone |
| provenance | Categorical | MEASURED / DERIVED / VALIDATED_ALTERNATIVE / UNRELIABLE / UNAVAILABLE |
| analyser_flag | String/coded | Exact documented flag or masked code, plus dictionary |
| specimen_context | Categorical/text | Plasma appearance, appropriate sample characteristics, artifacts |
| clinical_context_available | Boolean/controlled fields | Only minimally necessary and approved context |
| action_taken | Controlled enum | Repeat, investigate, refer, withhold, recollect, alternate measurement etc. |
| action_evidence | Controlled fields | How follow-up action/result was validated |
| reportability_label | Controlled enum | Allowed, disallowed, conditional, unknown with rationale |
| adjudication_status | Categorical | Independent, consensus, unresolved |
| adjudicated_action_set | Structured array | Permitted actions and mandatory prerequisites |
| linkage_group | Pseudonymous | Groups related episodes/runs without releasing identifiers |
| split | Enum | Development / locked test / external validation |

## Unit rules

Store source unit and a separately versioned normalized unit; never overwrite the original. For standard arithmetic demonstrations only (not analytical correction): with RBC expressed in 10^12/L, MCV in fL, Hb in g/L, Hct% = RBC*MCV/10, MCH(pg) = Hb/RBC, and MCHC(g/L) = 100*Hb/Hct(%). With Hb in g/dL, MCH(pg) = 10*Hb/RBC and MCHC(g/dL) = 100*Hb/Hct(%). These identities **do not validate any source measurement**. Specific analyser methods and rounding must be checked with the local laboratory.

## Patient privacy requirements

Never commit real CBC records, accession numbers, exact timestamps, patient names, lab employee notes, raw SOP text, proprietary manuals or linkage salts to this public repository. Even de-identified data require governance and release authorization. Avoid unrestricted cloud APIs unless separately approved.

## Benchmark split safeguards

Split by linked patient/episode, not individual repeat run; document site/time partitions and duplicates. Do not use held-out cases to author rules, prompts, severity rubric or SOP adaptations. Release synthetic demonstrations only when clearly labeled and validated as examples.
