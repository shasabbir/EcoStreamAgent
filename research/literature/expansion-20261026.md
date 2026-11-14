# Literature expansion record - 2026-10-26

## Scope

User request: add 15 more papers, mostly journal papers, no arXiv. Added exactly 15 distinct published DOI records to the existing 15, with thematic discussion and a second comparison table. The 15 additions comprise 14 conventional journal papers and one journal-style PVLDB article; thirteen are method-oriented and two are surveys. Eleven issue years are 2024-2026; the remaining four are 2022-2023 foundations retained for direct relevance. No Q1 classification is certified here.

Files changed: paper/main.tex (draft date only), sections/literature-review.tex, references.bib, README.md, plan.md and reference-ledger.csv. New files: paper/additional-15-paper-review.md, this record, additional-references.bib (the new subset), and doi-metadata-additional-20261026.json. The original standalone review/PDF and Reference-papers were not edited. Pre-edit source copies are retained under tmp/literature-expansion-baseline-20261026.

## Search and selection

Primary-source searches covered: Flink multi-objective tuning; multi-model predictive streaming adaptation; straggler and near-source grouping; federated edge-cloud stream scheduling; local/fragment-based state recovery; agentic multimodal diagnosis; and surveys of runtime adaptation/evolution. IEEE, Elsevier, Springer Nature, ACM and PVLDB records were considered. Generic IoT prediction papers and weakly related application papers were not added to fill the quota. A paywalled older Flink scheduling candidate was replaced by the 2024 CEBFD paper, whose publisher abstract could be inspected.

All new DOI identities were retrieved from Crossref on 2026-10-26; the dated JSON records raw deposited metadata, issue/online dates and the evidence level. Each selected DOI is a journal-article registry record. PVLDB is explicitly qualified rather than counted without explanation as a conventional journal.

No new arXiv entry or arXiv-based support locator was added. Search results sometimes surfaced preprint versions; these were not used as the new reading sources. The bibliography cites published versions. Existing historical support locators for the original papers were preserved, not rewritten to imply new access.

## Access and integrity limits

- TAMO: identity and published title verified; IEEE access challenge prevented final abstract/method inspection. Only title-level scope is stated. Support and final-version flags remain false.
- Scarf: publisher-deposited abstract inspected through the DOI registry; final full PDF not retrieved. No detailed algorithm/evaluation or reproduction claim.
- Ns-Stream: indexed author-hosted published PDF passages inspected, including p. 3384; complete downloads timed out. Do not interpret this as a whole-paper audit.
- LocaleXpert: author-hosted manuscript inspected; final journal reconciliation pending. Its author spelling differs internally; the bibliography follows the deposited journal identity.
- ProOSStream: Crossref deposits the coauthor spelling "Rocioo Perez De Prado"; retained conservatively, with final-article name reconciliation pending.
- CEBFD, hierarchical autoscaling and runtime-adaptation survey: abstract-level support only; unseen evaluation details are not inferred.
- Issue dates intentionally differ from online-first/DOI years for several sources. MA-RCA is cited as 2026, the evolution survey as 2024, Ms-Stream as 2025 and ProOSStream as 2026. These are not inferred from DOI digits.
- Available registry update fields were null for the retrieved records. This is not proof of absence of corrections/retractions; all notice-check flags remain pending.
- Quartile/ranking verification and clean extracted-package/Overleaf builds are outside this literature-addition scope and are not claimed.

## Study implications

Scarf and MMP-SPS strengthen numerical comparators. TAMO, LocaleXpert and MA-RCA constrain broad claims about tools, multimodal telemetry, specialized agents or verification. CausalRCA provides a non-LLM diagnosis alternative. Recovery/scheduling papers require engine-appropriate transitions and supported incident/action pairs. The candidate distinction remains decision-focused diagnostic acquisition with collection, waiting and intervention costs. M1 novelty approval is still pending.

## Validation

Source/citation, DOI/link, compilation and rendered-page checks passed for the six-page PDF; see expansion-validation-20261026.md. All 30 papers have narrative citations and matching visible/clickable DOI links; original entries and standalone review files are preserved. The reference-readiness audit remains pending for scientific/source/notice checks. No study implementation, measurement, empirical gain, acceptance probability or submission readiness is claimed.

