# Manuscript integration verification

**Checked:** 2026-10-26  
**Scope:** Finish integrating the selected 15-paper review into the EcoStream manuscript. This check does not complete the research study or certify the bibliography for submission.

## Completed checks

- Rebuilt `paper/main.tex` with pdfLaTeX, BibTeX, and two further pdfLaTeX passes in a fresh output directory, without using the previous `.aux` or `.bbl` files.
- Confirmed 15 bibliography entries with 15 unique DOIs, all cited in the literature-review narrative before the comparison table. No uncited entries or undefined citation keys were found.
- Confirmed that the four-page PDF contains 15 distinct clickable DOI targets, matching the bibliography.
- Extracted the bibliography column by column and checked each DOI within its own numbered reference after removing only layout whitespace. All 15 passed.
- Rendered and visually inspected all four rebuilt pages, including the full comparison table and references. No visible clipping or overlapping content was found.
- Confirmed that the rebuilt PDF's extracted text matches the previously prepared manuscript PDF. No manuscript prose, study claims, or reference identities were changed during this continuation.
- Preserved the earlier standalone review Markdown and PDF.

This is a fresh-output-directory build, not a separate-machine, Overleaf, or clean source-archive reproduction test.

## Reference-by-reference rendered DOI checks

The numbering below follows citation order in the compiled manuscript, not the reading order of the standalone review. Each row passed both the visible-DOI check within the correct reference and the clickable-target check.

| PDF reference | Paper | DOI | Result |
|---|---|---|---|
| 1 | Phoebe | 10.1109/icws55610.2022.00041 | Pass |
| 2 | Demeter | 10.1145/3629526.3645048 | Pass |
| 3 | Daedalus | 10.1145/3629526.3645042 | Pass |
| 4 | STREAMLINE | 10.1016/j.iot.2025.101731 | Pass |
| 5 | MUDAP/RASK | 10.1109/tsc.2026.3711142 | Pass |
| 6 | Ra-Stream | 10.1016/j.future.2025.108119 | Pass |
| 7 | SAP-DPO | 10.1016/j.future.2026.108520 | Pass |
| 8 | CAOM | 10.1109/tcc.2025.3538512 | Pass |
| 9 | DRRS | 10.1109/icde65448.2025.00286 | Pass |
| 10 | RCAgent | 10.1145/3627673.3680016 | Pass |
| 11 | ORACL | 10.1109/tsc.2026.3707982 | Pass |
| 12 | SciToolAgent | 10.1038/s43588-025-00849-y | Pass |
| 13 | BioMedAgent | 10.1038/s41551-026-01634-6 | Pass |
| 14 | ESSA/TTCLB-EA | 10.1016/j.future.2024.107681 | Pass |
| 15 | Grid-interactive AI data centres | 10.1038/s41560-025-01927-1 | Pass |

## Interpretation of the earlier audit

The automated report in `reference-audit/audit.md` flagged some DOIs as absent from rendered text. Those are line-wrap/column-extraction false positives: the per-reference checks above establish that the DOI text is present and associated with the correct reference. The original automated report is retained unchanged so its limitations remain visible; its flags must be interpreted together with this follow-up.

Other pending findings are **not** cleared by the rendering check. Final journal-version reconciliation for ORACL and MUDAP, incomplete correction/retraction checks, and the documented Nature Energy online-first versus issue-year distinction remain as recorded. Source metadata from 2026-10-13 were not refreshed or relabelled as newly verified in this continuation.

## Build warnings

The rebuilt log has no undefined citations/references or missing PDF destinations. Two 9.27-point title-block box warnings and underfull-box warnings remain; the rendered pages were inspected and have no visible clipping. These layout warnings do not establish scientific validity or invalidate the pending source checks.

## Source identities checked

SHA-256 before final PDF replacement:

```text
paper/main.tex
ccc0c000d14c4c736b943df82733712211b1a8b18e3eebddd0ae7851104204d6

paper/sections/literature-review.tex
10e9639a03b20dc3269cf8e076bcdc1b16090a2cb094ac6cec0e0cc1bfc75c39

paper/references.bib
91607d1fcecf2867da3d8aeb952a36052eb02067bfadc5cb6531783f6911734e
```

**Outcome:** The requested literature integration is complete as a pre-experiment manuscript artifact. Method implementation, experiments, and final evidence-backed conclusions remain unfinished.
