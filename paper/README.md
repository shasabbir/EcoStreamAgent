# EcoStream-Agent manuscript

This is an **unpublished pre-experiment working draft**, not a finished or submission-ready study.

## Files

- `main.tex`: main manuscript, using the official IEEE Access class. It contains exactly two top-level sections: an expanded introduction with background, problem definition, research questions and planned contributions, then the literature review. References follow directly.
- `sections/literature-review.tex`: thematic literature review of 41 published papers; one selective table positions the ten closest technical precedents, while the remaining foundation and cross-cutting papers are integrated in the prose.
- `references.bib`: 41 distinct published references with DOI fields and visible DOI URLs; no ordinary arXiv/preprint entry was added.
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

Publication metadata and access qualifications are recorded in `../research/literature/doi-metadata.json`, `doi-metadata-additional-20261026.json`, and `reference-ledger.csv`; the dated expansion notes list unfinished checks. Some full texts and final-version comparisons remain unavailable, and the notice audit is incomplete. TAMO's published identity is verified but only title-level scope is used because its final methods were inaccessible. The 2026 topology-aware scheduling paper is likewise used only for the mechanism established by its published title/metadata pending fuller access. Issue years are retained where they differ from online-first or DOI years. No current quartile classification is certified by this bibliography update.

The expanded introduction frames the background, problem, research questions and planned contributions; the literature review is followed directly by references. No code execution, calibrated controller, experiment, resource saving, physical-energy reduction, or completed contribution is claimed. AI drafting assistance remains recorded in the project history; any future submission must satisfy the selected venue's actual disclosure requirements.
