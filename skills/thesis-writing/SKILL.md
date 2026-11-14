---
name: thesis-writing
description: Guidance for planning, drafting, reviewing and polishing a Master's (or Bachelor's) thesis in a technical field — engineering, computer science, electronics, hardware design and similar — following established technical-thesis conventions (structure, scientific style, figures and tables, equations, code listings, citations, layout). Use this skill whenever the user is working on a thesis, dissertation chapter, thesis abstract, introduction, literature review, methodology, results or conclusions chapter, or asks to outline, write, rewrite, critique, proofread or check a thesis draft (LaTeX, Word or Markdown), even if they only say "my chapter", "the diploma", "MSc work" or paste a section without calling it a thesis. Also use it for thesis-like technical reports and seminar papers that follow the same structure.
---

# Technical thesis writing

This skill helps write a Master's thesis in a technical field the way examiners expect it to read: objective, reproducible, well-argued, well-referenced, and easy to skim. It distils Tampere University's *Guide to Writing a Thesis in Technical Fields* (January 2019) into working rules, leaving out the parts that only apply to Finnish students or to that university's own systems.

The thesis exists to show that the author can do research independently and report it to professionals. Every rule below serves one of three readers' needs: **understanding** (clear structure, defined terms), **trust** (evidence, references, reproducibility), and **speed** (a reader who only looks at the introduction, conclusions, headings, figures and tables should still get the story).

## First, find out where the user is

Look at what the user has given you and pick the matching mode. If there is a thesis source tree in the working directory (e.g. `main.tex`, `chapters/`, `*.bib`), read the relevant files before writing anything — the user's existing terminology, notation, citation keys and template come first.

| Situation | What to do |
|---|---|
| Choosing/narrowing a topic, planning, "where do I start" | Prewriting: answer the four planning questions, produce a preliminary table of contents with page budgets (see *Planning*) |
| Writing a specific chapter or section | Read `references/structure.md` for that section, then draft (see *Drafting*) |
| Reviewing, critiquing, proofreading a draft | Run the checker script, then review against `references/review-checklist.md` (see *Reviewing*) |
| Figures, tables, equations, numbers, units, code listings | `references/style.md` |
| Citations, bibliography, quoting, plagiarism, copyright, source reliability | `references/referencing.md` |
| Page layout, fonts, margins, headings, numbering | `references/layout.md` — but the user's institution template always wins |

Institution-specific rules (template, citation style, page limits, required sections, language) override the defaults here. When the repo already contains a template or formatting preamble, follow it silently and do not "fix" it toward these defaults.

## Planning

Before drafting, settle four questions with the user (briefly — don't interrogate if the answers are already evident from their files):

1. **Main message and goal** — what is the one thing the thesis shows, and why is it interesting?
2. **Scope** — what is in, what is deliberately out, and what is the author's own contribution versus prior or team work?
3. **Audience** — an engineer in the field who is not a specialist in this exact topic. Don't explain basics of the field; do define everything topic-specific.
4. **Schedule** — leave real time for revision. 1–3 good pages per day is excellent progress.

Then produce a **preliminary table of contents**: tentative chapter titles, 2–4 bullet points per chapter on what it argues, where the key figures and tables go, and a page budget per chapter (a typical MSc thesis is ~55–75 pages; introduction and conclusions ~2–4 pages each). The page budget forces decisions about emphasis: 0.5 vs 5 pages on background is a real choice.

The default experimental structure is:

```
Title page, Abstract, Preface, Contents, Abbreviations and symbols
1. Introduction
2. Theoretical background / literature review   (give it a descriptive title)
3. Research methodology and materials           (descriptive title)
4. Results and discussion                       (may be several chapters)
5. Conclusions
References, Appendices
```

Chapters 2–4 should get descriptive titles that say what they contain — "RISC-V Coprocessor Interfaces" beats "Theoretical Background". Keep the plain titles "Introduction" and "Conclusions"; readers look for them. Design/implementation theses usually replace chapter 3 with a general system description and chapter 4 with the detailed design, results and analysis. Literature-review theses title every chapter after its content.

## Drafting

Read `references/structure.md` for the section being written — each section has a distinct job, and most weak theses fail by mixing jobs (results in the introduction, new results in the conclusions, unreferenced claims in the background).

Working rules while drafting:

- **Don't write front to back.** Results and background are easiest to start with. Write **conclusions → abstract → introduction last**, in that order, distilling the message each time so the three stay consistent.
- **Draft directly, polish later.** Say what needs saying directly and briefly; spelling and micro-style come in revision.
- **Guide the reader**: start a chapter by saying what it covers and how it links to what came before; move from general to specific; end major chapters with a short summary or summary table when it helps. If one chapter gets an intro paragraph, give all of them one.
- **Never invent facts, numbers, results or references.** If a claim needs a number or a citation you don't have, leave a placeholder such as `\todo{cite: source for X}` or `\textbf{[CITATION NEEDED: …]}` / `\textbf{[VALUE: …]}` and list them for the user. Fabricated data or citations are research misconduct, and a thesis with them can be failed or revoked — a placeholder costs the user a minute.
- **Placeholders must show up in the compiled PDF**, not hide in `% TODO` comments: the user and supervisor read the PDF, and an invisible gap gets submitted. The same applies to facts you wrote from general knowledge rather than from a source the user has — mark them `[CHECK: …]` in the text instead of mentioning them only in your chat reply.
- **Keep the author's contribution visible.** When the work is part of a larger project or reuses others' code/designs, say precisely what the author did.
- **Write in the user's voice and format.** Match their LaTeX macros, citation commands (`\cite`, `\autocite`, …), label conventions (`fig:`, `tab:`), British/American spelling, and existing terminology.

Core style rules (details and examples in `references/style.md`):

- Short sentences, active verbs, established terminology, no marketing language ("revolutionary", "seamless", "cutting-edge", "state-of-the-art" without evidence).
- Avoid "I" outside the preface; use "we", passive voice, or "this work/this stage …".
- Define every abbreviation and symbol at first use, even if it is in the abbreviation list.
- Quantify: "3.2× faster (from 41 ms to 13 ms)", not "much faster". Comparative claims (better, faster, cheaper, commonly) need a number or a reference — usually both.
- Every figure and table is referred to and *discussed* in the text (what should the reader notice?), with a few of its numbers repeated in the prose.
- Numbered paragraphs of logic, not bullet dumps: lists are fine but sparingly, with parallel items, and always introduced by body text.

## Reviewing a draft

1. If the draft is in files, run the mechanical checker first — it catches the cheap problems so you can spend attention on argument and structure:

   ```bash
   python3 <skill-dir>/scripts/check_thesis.py path/to/main.tex      # follows \input/\include
   python3 <skill-dir>/scripts/check_thesis.py chapters/*.tex --bib references.bib
   python3 <skill-dir>/scripts/check_thesis.py draft.md
   ```

   It reports unreferenced figures/tables, chapters that begin with a float, lone subsections, over-deep headings, long headings, first-person "I", sentences starting with a citation or symbol, `.5`-style decimals, missing non-breaking spaces before units, citations in the abstract, uncited/missing bib entries, vague intensifiers and hype words, and placeholders left in. Treat its output as leads, not verdicts — verify each in context before reporting it.

2. Then review against `references/review-checklist.md`, which goes from big to small: research problem and contribution → structure and chapter jobs → argumentation and evidence → figures/tables/equations → references → language. Big problems first: a perfectly punctuated chapter that answers the wrong question is still wrong.

3. Report findings ordered by impact, each with location (file:line or section), the problem, why it matters to the examiner/reader, and a concrete fix or rewritten sentence. Don't rewrite the whole text unless asked; show before/after for representative cases.

4. End with **questions to expect at the defence** — 4–8 pointed questions an examiner would ask on the basis of this text (weak evidence, unjustified choices, missing comparisons, scope). They turn the review into preparation and often expose problems more vividly than a list of fixes.

## Good scientific practice (non-negotiable)

- Research must be **objective** (preconceptions don't drive interpretation), **valid** (it measures what it claims to) and **reliable/reproducible** (someone else can repeat it and get the same result). Methods are described in enough detail to reproduce; ideally code and data are available.
- Look for alternative explanations and contrary evidence; narrow or drop a claim when they are plausible. Don't generalise from limited observations, and don't claim causation from correlation.
- Misconduct: **fabrication** (invented data/results), **falsification** (selective or distorted results, omitting essential results), **plagiarism** (others' text, figures, ideas or translations without credit — including your own earlier published work), **misappropriation** (presenting others' ideas or results as yours). When helping, never generate text that would cross these lines; when paraphrasing a source for the user, keep the citation attached.
- AI-assisted writing: many universities require disclosing AI tool use. If the user's institution has such a rule, remind them once; it's their call how to comply.

## Reference files

- `references/structure.md` — job, content and length of each thesis part (title, abstract, preface, intro, background, methods, results, conclusions, references, appendices)
- `references/style.md` — text, argumentation, comparisons, lists, abbreviations, figures, tables, numbers and units, equations, code and algorithms (with LaTeX snippets)
- `references/referencing.md` — numeric vs name-year, in-text citation patterns, secondary sources, quotations, bibliography content, common mistakes, source reliability, copyright
- `references/layout.md` — default layout, headings and numbering rules when the institution gives none
- `references/review-checklist.md` — the full review checklist
- `scripts/check_thesis.py` — mechanical checker for LaTeX/Markdown drafts
