# Validation of the 40-reference, two-section manuscript

**Date:** 2026-11-02  
**Artifact:** `paper/main.pdf`

## Checks completed

- Built from a clean temporary output directory with pdfLaTeX, BibTeX, then two further pdfLaTeX passes.
- Confirmed exactly two top-level `\\section` commands: Introduction and Literature Review.
- Confirmed 40 BibTeX entries and 40 unique citation keys in the manuscript.
- Confirmed that every bibliography entry is cited and that no cited key is missing.
- Confirmed 40 unique DOI link targets in the final PDF.
- Confirmed that the obsolete top-level headings “Background and Study Scope” and “Literature Review and Research Positioning” do not appear as section headings.
- Rendered all seven PDF pages at 150 DPI and visually inspected the title block, two-column flow, research questions, contribution list, both comparison tables, section transitions and all 40 references.

## Build result

The final log contains no undefined citation/reference, multiply-defined label or LaTeX error. The only overfull-box messages are the two 9.27-point title-block warnings inherited from the existing IEEE Access title layout; visual inspection of page 1 found no clipping or collision. Underfull-box messages are normal column-justification warnings and do not indicate missing content.

## Scientific status

Artifact checks establish source/PDF integrity only. They do not establish study novelty, Q1 acceptance, controller correctness or empirical effectiveness. The implementation and experiments remain pending. The reference ledger still records incomplete notice checks and source-access qualifications, including title/metadata-level use of the 2026 topology-aware scheduling paper.

The workflow reference-audit helper was also run online; its output is preserved in `reference-audit-40-20261102/`. The automatic scientific-readiness gate remains pending, chiefly because correction/withdrawal/retraction checks and several source-support/final-version checks are incomplete. Its “DOI not found in rendered text” flags are line-wrap artifacts: direct PDF annotation inspection found 40 distinct DOI targets. The registry-title flags for the Liu--Buyya survey and Scabbard reflect shorter Crossref titles; the authoritative published pages/PDFs support the fuller titles used in the bibliography. These qualifications are recorded rather than overriding publisher evidence to satisfy an exact-string check.
