# Executed PubMed search snapshot — 2026-10-11

**Status: successful, public ESearch API results from GitHub Actions. This is a targeted bibliographic retrieval, NOT a systematic/scoping review, eligibility screening or unique eligible-study count.**

## Provenance

- **GitHub Actions run:** https://github.com/NTinkicht/SOPGuard-Eval/actions/runs/38119265189
- **Artifact (PMID export and manifest):** https://github.com/NTinkicht/SOPGuard-Eval/actions/runs/38119265189/artifacts/11694389255
- **UTC start:** `2026-10-11T06:48:42.719930+00:00`.
- **Git revision that ran the queries:** `1cf122fd5daa25e8021d09a46e9f5423387a1642`.
- **Official source:** NCBI ESearch, `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi`.
- **Immutable versioned manifest copy:** [search_manifest.json](../literature/pubmed/2026-10-11/search_manifest.json).
- **Workflow result:** succeeded; export artifact uploaded. Logs show the NCBI-reported counts and query translations. Artifact retention is 90 days; download/retain the CSV under normal scholarly governance.

## Actual search results

| Query | Scope | NCBI reported hits | Exported PMIDs | Export status |
| --- | --- | ---: | ---: | --- |
| A_CBC_INTERFERENCE | CBC interference, artefacts, hemolysis, agglutinins and autoverification | 1727 | 1727 | Complete within exact ESearch query |
| B_LLM_LABORATORY | LLMs/ChatGPT/generative AI in CBC or laboratory medicine | 40 | 40 | Complete within exact ESearch query |
| C_MEDICAL_LLM_SAFETY | Medical LLMs: safety, abstention, SOP and medical calculations | 403 | 403 | Complete within exact ESearch query |

**Verified raw-artifact deduplication (2026-10-11):** The original `pmid_export.csv` was downloaded from workflow artifact #11694389255 and deduplicated by exact PMID. There are **2,170 occurrences, 2,145 unique PMID identifiers and 25 duplicate occurrences**. Intersections: A∩B=0; A∩C=0; B∩C=25; all three=0. Only 15 of B's 40 records were absent from C. The downloaded ZIP's SHA-256 is `3d0812d533c8f270add9d62f5c3d72a436f557103e5af6eb7eea9186e5ebc190`, matching the GitHub Actions upload log. This check counts **unique PubMed identifiers, not screened eligible publications**. We have not retrieved, reviewed or excluded individual abstracts or full texts.

## What still needs doing before a literature-based novelty claim

1. Preserve the original PMID CSV artifact and the **verified deduplication counts**. A portable [deduplication script](../scripts/deduplicate_pubmed_pmids.py) and future workflow runs will generate `unique_pmid_export.csv` with provenance memberships.
2. Assign two qualified reviewers or otherwise transparently report single-screening limitations. Screen titles/abstracts and full texts with reasons and resolution of disagreements.
3. Add broader database coverage through institutional Scopus/Web of Science and computing literature indexes, plus citation chasing; the three ESearch queries are deliberately scoped and may miss important work.
4. Independently audit closest 2025–2026 articles at full-text and supplementary-material level, including comparison arms, reference-standard provenance and analyser dependence.
5. Update the evidence register and novelty claim **based on observed studies**, not the number of initial search hits.
6. In parallel, secure laboratory partnership, locally applicable SOPs, ethics permission and expert adjudication before any patient data work.

## Reproducibility note

This snapshot **does not** represent prospective preregistration of literature review methods. [The search protocol](LITERATURE_SEARCH_PROTOCOL.md) remains a draft for a wider, possibly systematic search. The archived JSON retains the PubMed query translations, which may differ from the authored raw queries, and the timestamp needed to reproduce the API response.
