# Integration of the 15-paper review into the manuscript

**Date:** 2026-10-13  
**Last verification:** 2026-10-26  
**Requested scope:** Add literature review to the paper and include these 15 papers if absent.

## Baseline and changes

Inspection found no `.tex` manuscript or `.bib` bibliography in this fresh project. Only the standalone review and study plan existed. Accordingly, a new `paper/main.tex` manuscript framework was created using the official IEEE Access template, with `sections/literature-review.tex` included in the main text and 15 entries in `references.bib`. No discarded-project manuscript or saved memory was reused.

The literature section is organized by mechanism, not fifteen disconnected paper summaries. It includes all 15 papers in substantive discussion and a comparison table. The prior Markdown review and its PDF remain unchanged. The rest of the manuscript is explicitly pre-experiment and incomplete; the user's request did not authorize inventing results or claiming that the full paper is finished.

## Source and bibliography checks

- Retrieved all 15 DOI records from Crossref and preserved a dated metadata snapshot.
- Matched the selected paper identities to the earlier primary-source review.
- Used the published journal/conference versions; no ordinary preprints are bibliography entries.
- Preserved cited-version dates, including Ra-Stream 2026 and the Flink energy-aware paper 2025.
- Nature Energy is cited as 2026, volume 11, issue 2, pages 254-261, as directed by the publisher's citation. Crossref records online-first publication on 5 December 2025. The automated year check can therefore remain pending even though the reason is identified.
- Claims based on abstracts are limited to mechanism-level descriptions present in those abstracts; no unseen algorithm details, split sizes, or performance measurements are inferred.
- ORACL and MUDAP final journal-version reconciliation remains pending. Their ledger support/version flags are conservative.
- Correction/retraction checks remain incomplete for the full set. A null registry update field does not establish the absence of a notice.

## Narrative and novelty safeguards

The section acknowledges existing autonomous Flink diagnosis, diagnostic stopping, selective profiling, constrained numerical allocation, recovery-aware tuning, and migration-cost-aware execution. It positions decision-focused diagnostic acquisition as a proposed question, not a proved first contribution. Scientific-tool and power-orchestration papers have explicitly supporting roles rather than being presented as direct streaming baselines.

## Validation status

Completed for the delivered source/PDF version:

- Compiled locally with MiKTeX pdfLaTeX and BibTeX using the official IEEE Access class. The PDF has four pages.
- Confirmed 15 unique bibliography entries/DOIs and substantive citation of all 15 within the literature section. No unused entries or undefined citation keys were found.
- Confirmed the PDF contains all 15 distinct clickable DOI targets and the 15-paper comparison table.
- Rendered and visually inspected all four final PDF pages, including the full table and every reference. No visible clipping or overlap was found. The draft footer does not display the template's fictional volume/year.
- Ran the workflow reference-audit helper against the bibliography, source tree, ledger, registry cache, and extracted PDF text. The scientific/reference readiness gate remains pending: notice checks are incomplete, final-version support for ORACL and MUDAP is unresolved, and Nature Energy's publisher issue year differs from the registry online-first year.
- The final LaTeX log has no undefined citations or references and no missing PDF destination warning. Two 9.27-point title-block box warnings and some underfull-box warnings remain; the relevant pages were visually checked. No EPS conversion was required, so the disabled shell-escape warning does not prevent the build.

Compilation and visual checks establish document integrity, not study validity or submission readiness. A clean extracted package/Overleaf build was not requested or tested.

On 2026-10-26, a fresh-output-directory build, citation coverage check, per-reference rendered DOI check, and visual inspection of all four pages passed. The earlier helper's missing-DOI text flags were traced to layout wrapping, not omitted bibliography links. See [the dated verification record](integration-validation-20261026.md). Scientific source/version and notice checks remain pending; no substantive manuscript text or standalone review content was changed during this continuation.

## Remaining work

**Subsequent expansion, 2026-10-26:** Fifteen more published papers were added to the manuscript, bringing the live bibliography to 30. The original integration and validation above describe the earlier 15-reference version and are preserved as history. The additional reading notes, metadata snapshot, and `expansion-20261026.md` describe the new sources and their limitations. The original standalone review/PDF remain unchanged.

**Subsequent expansion, 2026-11-02:** Ten more published papers were added, bringing the live bibliography to 40. The manuscript was also restricted to exactly two top-level sections: Introduction and Literature Review. The background, problem, research questions and planned contributions are now within the introduction. See `expansion-20261102.md` and `expansion-validation-20261102.md`. The original standalone review/PDF remain unchanged.

1. Obtain unavailable final full texts and reconcile the nearest competitors' implementations and versions.
2. Complete notice checks and resolve any remaining metadata details before approving the bibliography for submission.
3. Specify and implement the controller, freeze the protocol, run the study, and write evidence-backed results.
4. Supply author identities and actual funding/availability/declaration facts.
5. Select the final venue and apply its current requirements after the study's evidence is stable.
