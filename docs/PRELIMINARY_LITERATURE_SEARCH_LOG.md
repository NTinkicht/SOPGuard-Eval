# Preliminary targeted prior-art search log

**Search date:** 2026-10-11. **Purpose:** initial background verification only; NOT a complete systematic/scoping review or PRISMA-compliant search. A trained librarian/researcher should validate reproducibility, additional databases, Boolean strings and selection rules before novelty claims are made.

See the [executed October 2026 targeted public-web update](TARGETED_LITERATURE_UPDATE_2026-10-11.md) (not a systematic database search). See the [prospective literature search protocol](LITERATURE_SEARCH_PROTOCOL.md) and [blank extraction template](evidence_log_template.csv). The search strategy is not yet systematically executed.

See also [reproducible PubMed ESearch snapshots](PUBMED_SEARCH_SNAPSHOT.md) for date-stamped public PMID/count metadata once GitHub Actions successfully retrieves it. Do not infer counts before such a run.

## Search plan

Starting search sources: general scholarly web indexing used to resolve primary PMC/PubMed/journal pages and publisher standards pages. Future systematic phase must search PubMed/MEDLINE, Scopus and/or Web of Science, IEEE Xplore and ACM Digital Library, with deduplication, screening and a retained audit trail. This log documents only the limited searches actually carried out.

Representative queries executed (free-text, not reproducible database search syntax):

- "Girard Berda Haddad 2025 Breaking free MCHC interferences GFHC review PMC"
- "CLSI AUTO10 autoverification clinical laboratory test results guidance"
- "TRIPOD LLM reporting guideline Nature Medicine 2025"
- "optimizing management analytical interferences affecting red blood cells XN-10 Henry 65 901"
- "ISLH 41 rules hematology review 2005 13298 15 laboratories"
- "GPT-5 Grok DeepSeek blood count 2026 instrument alerts"
- "MedCalc-Bench NeurIPS 2024 medical calculation evaluation"

## Verified primary or authoritative items

| Citation | Core verified observation | Why it matters / what it does NOT establish |
| --- | --- | --- |
| Girard S et al. Int J Lab Hematol 2025;47:798–807. DOI 10.1111/ijlh.14536. https://pmc.ncbi.nlm.nih.gov/articles/PMC12426809/ | GFHC synthesized methods and management decision trees for raised MCHC across artefacts and true pathology. Article notes MCHC determination may be measured or calculated depending on platform. | Strong prior art; not a validated local laboratory SOP. |
| Henry S et al. Int J Lab Hematol 2022;44:1068–1077. DOI 10.1111/ijlh.13951. https://pmc.ncbi.nlm.nih.gov/articles/PMC9804823/ | XN-10 optical-parameter flowcharts retrospectively corrected 63/65 historical cases, and corrected 18 results among 901 unselected prospective samples; paper notes cases requiring repeat sample despite optical channel. | Existing comparator; its observed correction performance is not a universal benchmark score. |
| Barnes PW et al. Lab Hematol 2005. PMID 16024331. https://pubmed.ncbi.nlm.nih.gov/16024331/ and https://islh.org/web/consensus_rules.php | International group consolidated 83 consensus suggestions to 41 rules after evaluation at 15 labs / 13,298 samples. | Broad CBC review/autoverification prior art; not our target LLM safety task. |
| Ye X et al. J Med Internet Res 2026;28:e87802. DOI 10.2196/87802. https://pubmed.ncbi.nlm.nih.gov/42247415/ | Comparative retrospective study of GPT-5, Grok 4 and DeepSeek R1 for CBC report interpretation in haematologic diseases. | Closest LLM CBC paper; detailed analysis of analyser alerts and validity needed before exact novelty claims. |
| Khandekar N et al. MedCalc-Bench, NeurIPS 2024 Datasets and Benchmarks. https://proceedings.neurips.cc/paper_files/paper/2024/hash/99e81750f3fdfcaf9613db2dbf4bd623-Abstract-Datasets_and_Benchmarks_Track.html | Over 1,000 reviewed examples across 55 medical calculators, documenting errors in extraction, formula selection and arithmetic. | General numerical benchmark; does not on its own test CBC interference SOP compliance. |
| Gallifant J et al. Nat Med 2025;31:60–69. DOI 10.1038/s41591-024-03425-5. https://www.nature.com/articles/s41591-024-03425-5 | TRIPOD-LLM reporting checklist, 19 main items and 50 subitems. | Reporting framework, not proof of clinical safety. |
| CLSI AUTO10-A (2006). https://clsi.org/shop/standards/auto10/ | Guideline covers developing, implementing and validating laboratory autoverification rules. | Check current local accreditation/standard adoption; do not copy license-restricted content. |

## Implications for novelty wording

Acceptable working claim: "We will test the incremental safety of LLM SOP reasoning against established laboratory decision procedures on independently adjudicated CBC interference episodes."

Not established: "first paired-outcome benchmark", "no previous safety study", "models outperform/underperform the rule engine", or "cross-platform validated". A completed search and extracted comparison table are required.

## Next actions under issue R02

- Form database-specific Boolean search strategies and save returned counts, search dates and screening decisions.
- Extract clinical case definitions, source method, gold standard, sample sizes, failure endpoints and limitations.
- Map reported CBC optical/derived methods against exact partner analyser software and approved SOPs.
- Audit claims about warm agglutinins, in-vitro/in-vivo haemolysis, alternative measurement availability and device regulation with clinical experts.
