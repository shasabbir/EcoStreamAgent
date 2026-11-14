# EcoStream-Agent manuscript

This is an **unpublished pre-experiment working draft**, not a finished or submission-ready study.

## Files

- `main.tex`: main manuscript, using the official IEEE Access class.
- `sections/literature-review.tex`: thematic literature review and comparison table covering all 15 requested papers.
- `references.bib`: 15 distinct published references with DOI fields and visible DOI URLs.
- `main.pdf`: compiled working draft, generated after source/citation checks.
- `title-and-15-paper-review.md` and `.pdf`: the earlier standalone review, preserved unchanged.
- `ieeeaccess.cls`, `IEEEtran.cls`, `IEEEtran.bst`, fonts, maps, and required logo assets: copied without modification from the official template.

The official template was retrieved on 2026-10-13 from the [IEEE Access author page](https://ieeeaccess.ieee.org/authors/preparing-your-article/). Its linked LaTeX archive is `ACCESS_latex_template_20260513-1-1.zip`. Vendor class/font files are unchanged; the main source replaces publication-volume footers with an explicit draft footer and does not invent a manuscript DOI, authors, or funding.

## Build

Run in `paper/` with a LaTeX installation providing pdfLaTeX and BibTeX:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -output-directory=build main.tex
bibtex build/main
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -output-directory=build main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -output-directory=build main.tex
```

Create `build/` first if needed. Copy the final `build/main.pdf` to `main.pdf` after checks. On Overleaf, upload the files together with `sections/` and select `main.tex` as the main document. An Overleaf build has not been tested.

## Evidence status

Publication metadata and access qualifications are recorded in `../research/literature/doi-metadata.json` and `reference-ledger.csv`. The integration notes list unfinished checks. Some full texts and final-version comparisons remain unavailable, and the notice audit is incomplete. The Nature Energy citation follows the publisher's 2026 issue record, although Crossref's online-first date is 2025; this difference is explicitly recorded rather than silently changing the citation.

The abstract and non-literature sections are a minimal proposed-study framework or clearly marked pending sections. No code execution, calibrated controller, experiment, resource saving, physical-energy reduction, or final contribution is claimed.
