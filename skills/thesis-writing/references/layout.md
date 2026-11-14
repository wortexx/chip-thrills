# Layout defaults

**The institution's template and regulations take precedence over everything in this file.** Use these only when the user has no template, or to fill gaps the template leaves open. Don't rewrite an existing preamble toward these values.

## Page and font (fallback defaults)

- Single column, A4 (210 × 297 mm). Submitted as PDF (PDF/A where required for archiving).
- Margins: binding/inner 4.0 cm, outer 2.0 cm, top and bottom 2.5 cm. (One-sided printing for short theses; two-sided is reasonable above ~80 pages.)
- Body: 12 pt, line spacing 1.5, 6 pt after each paragraph. Sans-serif (Arial) was the reference guide's choice; serif (Times, Latin Modern, TeX Gyre Termes) reads better in long printed text — follow the template.
- Abstract: 10–11 pt, single spacing, justified and hyphenated, indented paragraphs.
- Page numbers in the outer top corner (or as the template places them). Front matter after the title page in Roman numerals starting with the abstract (i, ii, …); Arabic numbering starts at the Introduction (page 1). The running header may show the chapter title in the inner corner, but not on a chapter's first page.

## Chapters and headings

- **At most three heading levels** (e.g. 4.4.2). If you need a fourth, restructure or use run-in paragraph headings (`\paragraph`).
- **No lone subsections**: if a chapter has subsections, it has at least two (6.1 and 6.2).
- A chapter or subsection has at least two paragraphs; keep chapters balanced in length.
- A paragraph has more than one sentence and covers one theme (or the relation between two).
- Headings: ≤ 5–6 words, summarise the topic, catch interest. Avoid vague ones ("Theory", "Other", "Results 2").
- Major (chapter) headings start a new page.
- No heading as a widow at the bottom of a page — at least two lines of text must follow it (LaTeX usually handles this; check the PDF).
- Heading sizes larger than body text with vertical space around them (reference: chapters 18 pt with ~42 pt above/below; subheadings 14 pt with 18 pt above and 12 pt below).
- Refer to chapters by number: "in Chapter 2", "in Section 3.1" (use the template's term — Section or Subchapter — consistently), except "in this chapter" / "in the following chapter". In LaTeX: `Chapter~\ref{ch:method}` or `\cref{ch:method}` with cleveref.
- Never start a chapter or section with a figure, table or list — put introductory text first.

## Front and back matter order

Title page → Abstract (→ abstract in a second language if the institution requires) → Preface → Contents → List of abbreviations and symbols (→ lists of figures/tables if many) → chapters → References → Appendices. Contents, abbreviations, references and each appendix start on a new page.

## Practical file hygiene

- Use the official template from day one, not at the end.
- Version control (git) for LaTeX sources; tag or name versions sent to the supervisor (e.g. `v03`, `lastname_topic_msc_v03_2026-11-14.pdf`).
- Back up on more than one medium/location.
- Generate TOC, lists, cross-references and bibliography automatically — never type figure/section numbers by hand.
- Non-breaking spaces before references and units: `Figure~\ref{…}`, `[\cite{…}]` → `text~\cite{…}`, `100~MHz`.
- Long URLs: `\usepackage{xurl}`; long words with no hyphenation point: `\-` or `\discretionary{}{}{}`.
