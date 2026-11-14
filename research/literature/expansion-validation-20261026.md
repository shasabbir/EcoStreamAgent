# Validation of the 30-paper literature expansion

**Date:** 2026-10-26. Scope: requested literature additions and rebuilt working PDF, not submission certification.

## Passing artifact checks

- Exactly 15 additional records; 30 bibliography entries, 30 unique keys and 30 unique published DOIs.
- All 30 papers cited in substantive literature-review prose after excluding the comparison tables from the coverage check. No unknown or unused citation keys.
- Original 15 BibTeX entry dictionaries unchanged. SHA-256 comparisons confirm that the original standalone Markdown review and its PDF are byte-for-byte unchanged.
- Thirty rows and thirty distinct DOI identities in the source/access ledger. Fifteen new dated metadata records; all registry types are journal-article. PVLDB's journal-style proceedings status is separately qualified.
- No arXiv/preprint bibliography entry and no new arXiv support URL. Existing historical reading locators for the original papers are preserved.
- Fresh-output-directory pdfLaTeX/BibTeX build completed. The delivered PDF has six pages and no undefined citation/reference warnings.
- All thirty visible DOIs checked against the corresponding numbered reference, not merely searched somewhere in the PDF. All passed after whitespace normalization for line wraps.
- All thirty distinct expected DOI URL targets present as clickable PDF links.
- All six final rendered pages visually inspected. Both comparison tables fit on page 3 within the literature section; references begin on page 5 and continue without table interruptions. No visible clipped text, missing glyphs, overlapping objects, or overflowing table cells.
- Final verified PDF copied to paper/main.pdf. SHA-256: `27896d375482e66dd67b52388acc6cc32c9e17b11e4638f6c690217603a2edcb`.

The build and render files are in `tmp/manuscript-30-check-20261026/`; pre-edit copies are in `tmp/literature-expansion-baseline-20261026/`. They are diagnostic working files, not a publication package.

## Warnings and unresolved evidence

The reference-audit helper was run with online registry checks. It reports 30 pending records and a failed readiness gate because correction/retraction checks are incomplete, several support/final-version checks remain pending, and Nature Energy's issue year differs from registry dates. These findings were not cleared by successful compilation. Its rendered check was not run; the separate per-reference DOI and visual checks above supply the artifact verification.

The final LaTeX log retains the template's two 9.27-point title-box warnings and some underfull-box warnings. Their rendered locations were checked and showed no visible clipping. Shell escape is disabled; the epstopdf warning is non-blocking because no EPS conversion was required.

TAMO has identity/title-level support only. Scarf has a publisher-deposited abstract, not an inspected final full PDF. Other abstract/manuscript/indexed-passage limits and two author-name reconciliation issues are listed in expansion-20261026.md and the ledger. Published identity is not a completed method, notice, code or quartile audit.

No implementation, live benchmark, energy measurement, empirical gain, novelty approval, Q1 ranking certification, or clean extracted-package/Overleaf build was produced or claimed by this update.
