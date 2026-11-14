# EcoStream-Agent manuscript

This is an **unpublished pre-experiment working draft**, not a finished or submission-ready study.

## Files

- `main.tex`: main manuscript, using the official IEEE Access class.
- `sections/literature-review.tex`: thematic literature review and two comparison tables covering 30 published papers.
- `references.bib`: 30 distinct published references with DOI fields and visible DOI URLs; the 15 additions contain no arXiv/preprint entries.
- `main.pdf`: compiled working draft, generated after source/citation checks.
- `title-and-15-paper-review.md` and `.pdf`: the earlier standalone review, preserved unchanged.
- `additional-15-paper-review.md`: additions 16-30, with summaries, comparative roles and access qualifications. Fourteen are conventional journal articles and one is a PVLDB journal-style proceedings article.
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

Publication metadata and access qualifications are recorded in `../research/literature/doi-metadata.json`, `doi-metadata-additional-20261026.json`, and `reference-ledger.csv`. The integration/expansion notes list unfinished checks. Some full texts and final-version comparisons remain unavailable, and the notice audit is incomplete. TAMO's published identity is verified but only title-level scope is used because its final methods were inaccessible. Scarf uses the publisher-deposited abstract; several other additions have abstract- or author-manuscript-level support. Issue years are retained where they differ from online-first or DOI years, including Nature Energy, the stream-evolution survey, and MA-RCA. No current quartile classification is certified by this bibliography update.

The abstract and non-literature sections are a minimal proposed-study framework or clearly marked pending sections. No code execution, calibrated controller, experiment, resource saving, physical-energy reduction, or final contribution is claimed.
