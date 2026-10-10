# Model-view firewall and information leakage prevention

**Research-only design, pending institutional authorization.** No clinical processing system is implemented.

## Why this matters

The restricted full research episode record may contain expert labels, known interference status, intervention decisions, repeat results and reliability annotations. None of these may automatically appear in a model's input. The *model-visible view* is a separate, allowlisted contract with no `adjudication`, `reportability_label`, `action_taken`, follow-up measurements, expert outcome rationale or post-correction numerical targets.

## Public schemas

- [Full restricted episode metadata](../schemas/benchmark_episode.schema.json) describes record fields available to adjudicators and evaluators (not directly used as a model prompt).
- [Model-visible input](../schemas/model_view.schema.json) describes only permitted predecision evidence.
- [Research-only candidate output](../schemas/research_output.schema.json) describes nonclinical suggestions.

The repository's unit tests validate schema rejection of nested forbidden fields using fictional placeholders. They do **not** detect meaning-based leakage hidden in free text, nor prove patient privacy.

A schema alone cannot prevent leakage; an authorized, audited offline preparation process and review against original laboratory timelines are required before any data processing.

## Before finalizing an inference arm

1. Define the real-world decision time **T0**, available patient/specimen context and which analyser flags and local SOP versions existed at T0.
2. Use independent review to classify each field as: predecision-visible, reference-only, private linkage, or excluded.
3. Include unit and known analyser method information only if it genuinely existed at T0; never include `TRUSTED` / `UNRELIABLE` if determined by retrospective adjudication.
4. Create independent SOP context policies:
   - L0: no retrieved SOP excerpt; describe standard task without revealing correct action.
   - L1: retrieve from appropriately approved corpus only; freeze corpus, retrieval configuration and relevance scoring.
   - L2: give correct applicable SOP passage (oracle context) without exposing the reference action for this episode.
   - L3: same governed SOP information plus declared deterministic tools; no actual instrument action.
5. Partition related runs by patient/episode **before** any prompts, tuning or rule development. Avoid using a repeat value as input when its availability postdates T0.
6. Inspect all model-visible payloads for accidental identifiers, later values, answer keys, institution-restricted text and injection-bearing free-text sources.
7. Record approved model provider, data jurisdiction, hashed configuration and arm-specific context. Never commit payloads containing patient-derived data.

## Study scoring and limitations

Keep reference labels in a separate controlled evaluation dataset with independent adjudicators. Reveal them to an evaluator only after the output is frozen. A case with no later numerical reference may still have an adjudicated correct action (e.g., withhold/refer). A model that copies an action label by leakage has **not** demonstrated SOP reasoning.

## Current implementation boundary

This repository currently provides *schemas and static checks only*. It does not include a patient-data extraction pipeline, RAG index, LLM API integration, calculated patient results, validated clinical software or executable laboratory SOPs.
