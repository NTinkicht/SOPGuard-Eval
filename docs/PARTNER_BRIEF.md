# SOPGuard-Eval — Immediate laboratory collaboration action request

**Working study:** *Artefact or Disease? Safety of Large Language Models Interpreting Analytically Invalid Complete Blood Counts*

**Research lead:** Higher Colleges of Technology, UAE (computer science / applied AI).
**Status:** Research concept for co-design; no clinical approval, patient data, signed partnership, approved SOP access or study results.

## Purpose of the collaboration

We aim to evaluate whether an LLM mistakenly treats analytically unreliable CBC results as disease or recommends unsafe reporting, and whether provision of a relevant laboratory SOP changes that risk. Study 1 is intentionally narrow: **one analyser family**, one or two empirically feasible interference pathways, plus genuine-pathology mimics and non-interfered controls. We propose an **offline, retrospective** study with independent clinical reference labels; we will not alter patient care or deploy a clinical decision system.

## What we ask the laboratory to do now

**Please reply in writing rather than scheduling an introductory meeting.** The attached [collaboration action checklist](LAB_COLLABORATION_ACTIONS.md) allows a designated representative to return a brief response using information already known to the laboratory.

1. **Nominate a clinical co-investigator**: the haematology section lead, senior biomedical scientist or clinical laboratory specialist responsible for CBC interference workflow, plus a contact for ethics/data governance.
2. **Identify the analyser family**: vendor, model, software version (if known), and where relevant existing validated middleware or interference review rules.
3. **Confirm records and available evidence**: whether original flagged results, documented laboratory corrective investigations, repeat/alternative measurements, final reporting decisions, smear observations, and relevant genuine-pathology control records are retained; include available historical lookback and limitations. Indicate **availability, not actual patient-level information**.
4. **Indicate potential case categories**: which interference pathways are seen locally, which are documented well enough for an independent reference, and whether genuine mimics/non-interfered controls exist. The laboratory should choose the clinical focus based on what it actually handles; we do not require cold agglutinins and lipaemia specifically.
5. **Establish the feasibility/ethics path**: say whether an **aggregate-only count**, prepared by authorized laboratory staff, can be approved internally, and identify the committee/privacy office that would authorize any later retrospective data use and AI-model processing.

**Suggested response:** return the brief [action checklist](LAB_COLLABORATION_ACTIONS.md) within approximately **7–10 working days**, or indicate when the laboratory can realistically reply. A written agreement in principle and a named contact can arrive first; do not delay that acknowledgment because counting requires permissions.

## What happens only after authorization

Once the laboratory identifies a lawful route for internal aggregate counting, its staff can prepare counts by selected interference / genuine-mimic categories, valid follow-up evidence, unique patient/episode counts and missingness using the [blank feasibility worksheet](lab_aggregate_feasibility_template.csv). The laboratory determines whether sharing even aggregate counts is permissible.

If volume and governance support the study, we will jointly define the protocol; confirm SOP use rights, secure processing, ethics approval/waiver and any data-use agreement; recruit **two independent experienced haematology biomedical-scientist adjudicators**; and freeze the analysis before any held-out experiment.

## Data protection and workload

**Do not email or upload** patient values, accession numbers, identifiable details, screenshots of real CBC results, restricted SOP/IFU copies, case narratives, or record-level extracts. No cloud LLM receives patient-derived data without documented institutional approval. At this stage we request **availability information and authorized aggregate counts only**; expert labeling is **not yet requested**.

The immediate work is an inventory and a short response, not a full data extraction or project implementation. Co-investigators and substantial contributors would have publication roles considered under normal institutional/authorship criteria; participation is subject to institutional agreement.

**Please send back:** a named clinical lead, brief analyser/records availability answers, aggregate-count approval pathway, and the proposed next administrative action.

Project and current research protocol: https://github.com/NTinkicht/SOPGuard-Eval

*Working document, 13 October 2026. No existing partner agreement is implied.*
