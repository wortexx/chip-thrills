# Thesis structure: what each part is for

Contents: Title · Title page · Abstract · Preface · Contents · Abbreviations/symbols/lists · Introduction · Background / literature review · Methodology and materials · Results and discussion · Conclusions · References · Appendices · Thesis types

General rules:
- The canonical chapter titles (Background, Methodology, Results) are placeholders — replace them with headings that say what the chapter contains. Keep "Introduction" and "Conclusions".
- Add chapters and subchapters as needed. If one chapter opens with a short introduction, all should. Chapters may end with a short summary or summary table.
- Typical length: BSc 18–28 pages, MSc 55–75 pages (check local rules).

---

## Title

- Brief, accurate, attention-catching, and containing the keywords someone would search for.
- Avoid unnecessary abbreviations, company names and brand names.
- Evaluative adjectives (efficient, fast, low-power, energy-efficient) are claims: only use them if the thesis substantiates them with measurements.
- The working title can change; finalising it after the thesis is written is often easiest. It must still clearly reflect the topic.

## Title page

University logo, author name, thesis title (and optional subtitle), thesis type (Master's thesis / Bachelor's thesis), faculty/programme, and the submission date (month and year). Use the institution's template.

## Abstract

A **self-contained** summary that fits on **one page**, readable by someone outside the topic.

Contains, in this order:
1. Context and problem — why this matters (1–2 sentences).
2. Objectives / research questions.
3. Materials and key methods.
4. Main results — **with numbers** ("reduces area by 18 % at 50 MHz"), not "significant improvement".
5. Conclusions and recommendations, including for further research.

Rules:
- Nothing that isn't in the body. No references, no quotations, no figures, no tables, no equations needing definitions.
- Plain paragraphs, no headings, same font as the body, single spacing.
- Header block (if the template requires it): faculty; author: title; thesis type; month and year.
- Follow with 3–5 **keywords** in order of importance, most important first.
- A journal-style abstract is 70–250 words; a thesis abstract may use the full page but should still answer "what was the problem, what was done, what was the result".
- Write it after the conclusions and before the final introduction.

## Preface (acknowledgements)

- General information about the thesis process; who supervised/instructed and how; acknowledgements.
- If the work was done in a group or a company project, state the author's own contribution.
- Do not criticise anyone. One page maximum. Finish with place and date (the date after which the text was not revised) and the author's name.
- The preface is the one place where "I" is natural.

## Contents

Starts on a new page. Generated automatically (LaTeX `\tableofcontents`, Word TOC field) so that headings match the text exactly. Includes all numbered headings after it; preceding front matter may be omitted.

## Abbreviations, symbols, list of figures/tables

- Lists all notations, symbols, units, abbreviations and terms used. Title it after what it contains ("List of Symbols and Abbreviations").
- Group into categories (abbreviations, then symbols), each in alphabetical order; explanation tab-aligned. SI units are not listed.
- The list does not replace first-use definitions in the body.
- Lists of figures/tables only if there are many; if a list would be a stub of a few items, leave it out.

## Introduction (typically 2–4 pages)

Job: catch interest, establish the topic, and prepare the reader for what follows. The reader does not yet know the terminology — unlike in the conclusions.

Must contain:
1. **Motivation** — convince the reader the problem matters (context, gap, consequences).
2. **Objectives and research questions** — what the thesis attempts to resolve, and by what methods (one or two sentences on method, not a methods chapter).
3. **Placement in prior work** — short references showing the work builds on existing research (details come later).
4. **Contribution** — if part of a larger project, the author's own contribution stated clearly. A good pattern is a list of the 2–4 most important things achieved.
5. **Structure** — what each following chapter covers and how they connect (from chapter 2 onwards).

Optional but effective: a first figure that orients the reader — the system studied, its main inputs/outputs/interfaces, with the author's contribution highlighted.

Must not contain: detailed methodology, results, conclusions or future-work recommendations.

Write it last (after conclusions and abstract) so it promises exactly what the thesis delivers.

## Theoretical background / problem setting / literature review

Job: give the reader exactly the background needed to understand the problem and the solution — and to judge its quality.

- **State the research problem and why it matters clearly**, plus the criteria by which a solution should be judged. Many papers fail here and leave readers wondering why the work was done.
- Define all concepts carefully. A new term often needs only a few words and a reference.
- Assume an engineer in the field who is not a specialist in this topic: skip textbook basics, explain topic-specific material.
- A thorough literature review prevents reinventing the wheel and avoids known pitfalls. Compare sources, don't just summarise them one by one: similarities, differences, gaps, and where this thesis fits.
- When the chapter surveys several similar items (e.g. six microprocessors, five interface standards), end with a **summary/comparison table**.
- Company/industry context (existing products, the system being replaced, standards to follow, internal practices, the wider project) is included in as much detail as needed to justify the choices made — and only with permission for internal information.
- Delete everything irrelevant. The chapter must form a coherent whole with the rest of the thesis: every concept introduced here should be used later.
- A figure showing the topic in its broader system, with the thesis scope highlighted, is very effective.

## Research methodology and materials

Job: let the reader judge reliability and **reproduce** the work.

- Choice of method follows from the research questions. Present alternative methods and justify the choice.
- Describe materials (data sets, devices, tools and versions, software, benchmarks, configurations, interview subjects…) so there is no doubt about their origin and nature.
- Describe methods in enough detail for another researcher to reproduce the study and reach similar conclusions. Mathematical bases of new results are shown in enough detail that readers can follow without long calculations of their own. Ideally, data and source code are openly available (give the repository/commit).
- Well-known methods: a brief reference suffices. Unusual or self-developed methods: describe thoroughly.
- Qualitative methods must also be described as clearly as possible.
- There must be a visible link from the background chapter to the method — and the novelty of the work must be clear.
- Design/construction theses: this chapter usually gives the general system description.
- May span several chapters; give each a descriptive heading.

Technical-field specifics worth including: tool versions and settings, hardware platform, random seeds, measurement setup and conditions, number of repetitions, how noise/variance was handled, what was held constant in comparisons.

## Results and discussion

Job: present the most important results, their reliability, and their relevance.

- Present results briefly and accurately, using figures and tables. Graphs for trends, correlations and deviations; tables for exact numbers and lists. Extra data goes to appendices.
- Must be partly self-contained: a reader jumping here should understand the results without reading every earlier page.
- Design theses: first the details of the solution, then the results (possibly separate chapters).
- **Discuss, don't just list.** Compare against the prior work from the background chapter. For tables, answer in the text: what are the similarities, main differences, deficiencies, most common approach, recommended approach, trends?
- Address **sources of error, deviations from expected results, validity and reliability**. Say whether the objectives were met and the research questions answered.
- Emphasise what is new or significant; reflect on scientific and practical importance.
- Do not rely on results to "speak for themselves" — state their value explicitly. Be fair, precise and objective; no marketing language.

## Conclusions (typically 2–4 pages)

The most important chapter: many readers read only the introduction, the conclusions and the figures/tables.

- Summarise the main results and **discuss their importance** — don't re-list individual results. Repeat a few of the most important numbers.
- Answer the research questions explicitly.
- Give concrete recommendations for practical application (for the commissioning company, other researchers, society) and their limitations.
- Assess the quality and limitations of the thesis itself, and the need for further research.
- No new results, no new references for the first time ideally, no new terminology.
- A summary table can be very effective: objective, methods, key results/numbers, strengths, weaknesses, effort, costs.

Example summary table rows: Topic · Adjusted/measured variable · Hardware/software (size, memory, lines of code) · Strengths · Weaknesses · Time spent · Costs.

## References

- Title "References". Starts on a new page. Same font and spacing as the body, with extra space between entries.
- Contains **only** works cited in the text — and every cited work.
- One style, applied consistently. Details in `referencing.md`.

## Appendices

- For material that is needed for the whole but is not core or doesn't fit in the body: long derivations, long code or algorithms (>1 page), input/output listings, standard excerpts, user manuals, survey results, drawings, circuit diagrams, detailed measurement reports.
- Every appendix is referred to in the body. Each starts with a heading and a short description, since readers may browse appendices on their own.
- Ask "is this really necessary?" before appending.

## Thesis types

- **Experimental / empirical**: the default structure above.
- **Design / implementation (common in IT, hardware)**: Introduction → background and requirements → system overview (replacing methodology) → detailed design and implementation → evaluation/results and analysis → conclusions. Evaluation must still be quantitative where possible and compared to alternatives.
- **Literature review**: chapters after the introduction are thematic, titled after their content; method = how literature was searched and selected; end with synthesis and comparison tables.
- Agree non-standard structures with the supervisor before writing.
