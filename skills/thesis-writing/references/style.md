# Writing style: text, figures, tables, maths, code

Contents: 1 Text · 2 Argumentation · 3 Comparison · 4 Lists · 5 Abbreviations · 6 Figures · 7 Tables · 8 Numbers and units · 9 Equations · 10 Programs and algorithms

---

## 1. Text

**Think of the reader.** Text proceeds from general to specific; all terms are defined; it shows how the work builds on previous work; key points are highlighted.

**Signpost.** Tell readers what to expect, make the points, then sum up. Most readers first flip through headings, figures and tables — do the same with the draft and check the impression it gives. Emphasise key points by giving them their own section, a table or a figure. Page count signals importance.

**Sentences.**
- Avoid long sentences and nested structures. A full stop is the best way to end a sentence.
- Use active, concrete verbs.
- Avoid "I" except in the preface. Alternatives: "this stage included…", "we next…", or the passive ("the stage was completed…"). Pick one convention and keep it.
- Use established terminology and neutral language. Highlight key terms when they first appear — italics preferred over bold, bold over underline; don't overdo it.

**Cut wordiness and circumlocution.**
- ✗ "the identification and detection of the original author or group of authors who prepared the document or other equivalent material that served as a source for this piece of text" → ✓ "plagiarism detection"
- ✗ "The planning of the circuit board was accomplished in collaboration with the customer company" → ✓ "The circuit board was designed together with the customer company."
- ✗ "It can be seen that there is a tendency for the latency to increase" → ✓ "Latency increases …"

**No marketing jargon** anywhere: seamless, revolutionary, cutting-edge, game-changing, robust (without definition), powerful, best-in-class.

## 2. Argumentation

- Start a chapter from what the reader already knows, then introduce the new; summarise afterwards.
- Reason from stated premises to conclusions ("A holds, therefore B holds and C does not"). Delete or rephrase conflicting statements (one must be false for the other to be true).
- **A valid argument from a false premise gives a false conclusion.** Don't over-generalise from limited observations ("I saw only black dogs today, so all dogs are black"). "Always" and "never" statements are especially risky.
- **Define terms so they can be measured.** How is "efficiency", "usability", "performance" measured here? Undefined terms make unfalsifiable statements ("if the market responds favourably, the stock rises 2 %" — can never be wrong).
- Renaming doesn't change reality.
- **Causal claims need strong evidence.** Correlation (ice cream sales vs drownings) is not causation; look for a common cause (hot weather).
- Unlikely events happen by chance; don't infer a cause just because something was improbable after the fact.
- Showing a claim false doesn't make its opposite true.
- The truth of a claim doesn't depend on who said it — give evidence.
- Hypotheses must be falsifiable. Look for alternative explanations and contrary evidence; narrow or drop the claim if they are plausible. With limited data or a short study, confounders can't be isolated — say so.

## 3. Comparison

- Comparisons are the core of technical work. You *can* compare apples and oranges — on defined attributes (size, weight, price…) reported identically (with or without peel?).
- If several parameters change at once, you cannot tell which caused the difference. Controlled experiments change one variable at a time. In tool/flow comparisons: same inputs, same versions except the one under test, same constraints, same seeds; report noise bands.
- Prefer quantitative to qualitative. "X is 17.6 % better than Y but 24× more expensive" lets the reader decide; "X is superior but more expensive" doesn't. Define "better" precisely, case by case, and say whether bigger or smaller is better.
- For two variables, an x–y plot is usually the clearest presentation.

## 4. Lists

Use sparingly in formal writing. When used:
1. Order items deliberately (importance, chronology, category, size; alphabetical is rarely best).
2. Give all items parallel grammatical structure.
3. Keep items short and of similar length.
4. Prefer a numbered list when the count is mentioned in the text or items are referred to individually; sequential instructions are always numbered.

A list is always introduced by and connected to body text; it can't stand alone. Never start a chapter or section with a list.

## 5. Abbreviations

- Don't overuse. Write common Latin abbreviations (e.g., i.e., etc.) out in full in most running text ("for example", "that is").
- Define at first appearance: "Core-V eXtension Interface (CV-X-IF)" — or the reverse, "the file system FAT32". Mention the source language if not English and if relevant ("SI system (French Système international d'unités)").
- After definition, use either the abbreviation or the full term, as long as it's clear. Plain terms are often more readable than a wall of acronyms.
- Keep capitalisation consistent (e.g. "RISC-V", not "Risc-V" elsewhere).
- Very common abbreviations act as words (LED, CPU) and need no expansion in a technical thesis — but when in doubt, expand.
- In LaTeX, the `acronym` or `glossaries` package enforces first-use expansion and builds the list automatically.

## 6. Figures

Figures include drawings, photographs, charts, maps, block diagrams; lists, algorithms and code may also be presented as figures.

**Referencing and discussing**
- Every figure is referred to in the text, preferably before it or on the same page.
- Every figure is explained in the text: what should the reader notice? Mention some of its numbers and terms so the link is obvious. Example: "Figure 4 shows that the time of flight is 3.8–6.3 s (≈1.65× variation) and the height 16–55 m (up to 3.4×), depending on the departure angle. Increasing α by 10° raises the apex by about 10 m."
- The first figure of the thesis should introduce the topic without overwhelming detail.

**Preparation**
- Figures exported from analysis tools always need editing: remove unnecessary elements (e.g. meaningless negative axis ranges), label both axes with quantity and unit, place line labels next to the lines instead of a distant legend, use sensible tick spacing, adjust line widths.
- Text in figures must be readable: ideally body-text size, never below ~10 pt at print size. Use the thesis language in figure text.
- Axes show scales and units; scales generally start at zero so ratios (half, double) can be read. For log scales, say so in the label: "Frequency (log) [Hz]".
- Follow standard drawing conventions for the domain (circuit symbols, timing diagrams, block diagrams) and use them consistently.
- Colour is fine, but text in figures should be black and the figure must remain readable in greyscale (use line styles/markers, not colour alone).
- Photos and graphs get annotations: text boxes, arrows, scale bars. Flowcharts read left-to-right and top-to-bottom.
- Small icons can make diagrams more memorable.
- Prefer vector formats (PDF/SVG/TikZ/pgfplots) for diagrams and plots.

**Placement and captions**
- Figures and tables are numbered consecutively in separate sequences (either throughout the thesis or per chapter, e.g. Figure 3.2 — follow the template).
- Prefer the top of the page; wide figures/tables may be rotated 90°. Avoid several full-page figures in a row; move overflow to appendices.
- Figure captions go **below** the figure, on the same page. Consistently centred or left-aligned. Same font as body (often italic/smaller per template).
- The caption says what the reader should notice, even though the text also says it: "Figure 5. Cell area grows linearly with the number of SHA-3 rounds unrolled." rather than "Figure 5. Area results."
- **Never start a chapter or section with a figure, table or list** — there must be text first.
- A figure taken from elsewhere is cited in its caption; if modified, "adapted from [15]". See `referencing.md`.

LaTeX:
```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.8\textwidth]{figures/area_vs_rounds.pdf}
  \caption{Cell area grows linearly with the number of unrolled rounds.}
  \label{fig:area-rounds}
\end{figure}
... As Figure~\ref{fig:area-rounds} shows, ...
```

## 7. Tables

- Numbered and captioned; caption goes **above** the table, on the same page. Avoid tables splitting across pages.
- Every table is referred to in the text **and its content discussed**: "Table 2 compares … The largest differences are in X and Y: X is nearly 5× higher for TiO₂ because …".
- Variables, abbreviations and symbols in the table are defined in the text if needed.
- Good uses: lots of numbers concisely; making missing or divergent values visible; summarising background literature and the thesis's own results. Large numeric tables are often better as line or bar charts. Statistics (min, max, mean, std dev) belong here.
- Column headers clearly show quantity and unit; may be bold and separated by a double/heavier rule.
- **Order rows and columns deliberately**: group by type first (2–3 categories help a lot), then sort by the most important value. Alphabetical is rarely the best.
- **Don't box every cell.** Rule above and below the table and under the header (LaTeX `booktabs`: `\toprule`, `\midrule`, `\bottomrule`); add a light rule every 4–5 rows only if rows aren't grouped.
- Number rows in large tables if they're referred to.
- For comparisons, highlight the best (or worst) value in each column/row.
- Right-align numbers, ideally aligned on the decimal point (LaTeX `siunitx` `S` columns). Use a consistent power of ten within a column (15.0·10⁻⁵ next to 3.0·10⁻⁵, not 1.5·10⁻⁴), preferably moved into the column header. Use SI units and prefixes (m, µ, n…).

LaTeX:
```latex
\begin{table}[t]
  \centering
  \caption{Post-synthesis results for the three coprocessor variants.}
  \label{tab:synth}
  \begin{tabular}{lS[table-format=5.0]S[table-format=3.1]}
    \toprule
    Variant & {Cells} & {$f_\text{max}$ (MHz)} \\
    \midrule
    Baseline  & 18234 & 112.4 \\
    Unrolled  & 41120 & \bfseries 143.0 \\
    \bottomrule
  \end{tabular}
\end{table}
```

## 8. Numbers and units

- Technical writing uses numerals: "6 stages" rather than "six stages", and certainly not "a couple of stages". Spelling out 1–10 and large round numbers (hundred, million) is acceptable in prose; be consistent.
- Numerals are easier to scan for — that's why they're preferred.
- Use thousands separators for long numbers: 55 700 125 (thin space; LaTeX `\num{55700125}` with siunitx) — follow the template's convention.
- Never omit the leading zero: 0.5, not .5. English uses a decimal point.
- Abbreviate units: 3 m, 100 Hz, 25 %, 120.4 kg.
- Space between number and unit, never broken across lines: LaTeX `3~m`, `100~MHz`, or `\SI{100}{\mega\hertz}` / `\qty{100}{MHz}`; Word non-breaking space.
- Many values in running text → use a table or graph instead.
- Be precise and put numbers on a scale: ✗ "cost-effective [1,2,3] and fast [4,5] centrifuges" → ✓ "affordable (EUR 200–400, below 4 000 rpm) [1–3] and fast (over EUR 900, over 10 000 rpm) [4,5] centrifuges".
- Ranges use an en dash: 3.8–6.3 s (LaTeX `--`).
- "B is three times larger than A" is ambiguous (B = 3A or B = 4A?). Write it mathematically or as "B = 3A" / "B is 3× A".

## 9. Equations

- Display equations that are referred to are numbered, usually right-aligned in parentheses, numbered throughout ((1), (2)…) or per chapter ((2.1), (2.2)…) — follow the template. Simple formulas can sit inline unnumbered.
- **Equations are part of sentences** and get punctuation:
  ```
  Newton's second law is
      F = ma,                                  (1)
  where m is the mass of the object, a its acceleration and F the force.
  ```
- Define every variable at its first appearance.
- Prefer standard, well-known notation; minimise invented symbols. Never use one symbol for two meanings. Upper and lower case differ in meaning.
- Latin letters are often easier than Greek for your own variables, especially in figures.
- State units, and state whether bigger or smaller is better for any index, score or quality value.
- Define ratios explicitly: "let r = A/B", not "the ratio of A and B".
- Don't start a sentence with a symbol: ✗ "a is a real number…" → ✓ "Acceleration a is a real number…".
- Don't use "=" in place of a verb in prose. Sentences around equations must be grammatical.
- Variables in italics; functions and operators upright: sin(2x + y), grad T, div B, lim. (LaTeX math mode does this; use `\sin`, `\operatorname{div}`, `\mathrm{d}`.)
- Write logarithm bases: log₂(x), log₁₀(x); `ln` for natural log. Avoid `lg` (ambiguous).
- Pick one convention for vectors vs matrices/operators (e.g. bold upper-case operators, bold lower-case vectors, regular scalars) and keep it.
- Distinguish a function f from its value f(x). Use parentheses to remove ambiguity: sin(x² + y²) vs y² + sin(x²).
- Statements like Definition 1, Theorem 1 can label formal results.

## 10. Programs and algorithms

- Code and pseudocode use a monospaced font (LaTeX `listings`, `minted`, `algorithm2e`/`algorithmic` for pseudocode).
- **< ~10 lines and not referred to later**: inline as a display, like an equation.
- **Longer but under a page**: as a numbered float captioned "Program N." / "Listing N." / "Algorithm N.", numbered like figures.
- **Over a page**: appendix (or a repository link with commit hash).
- Add comments, indent consistently, number lines so the text can refer to them ("line 14 compares …"). Reserved words may be bold in listings but not in body text. Long parameter lists may be elided: `foobar(…)`.
- Outline in the text what the code does.
- Identifiers in body text: either italic or the code font (`\texttt{EXIT\_SUCCESS}`), spelled exactly as in the code; be consistent. Don't start a sentence with an identifier: "The return value `EXIT_SUCCESS` denotes …".
- For HDL (Verilog/SystemVerilog/VHDL), the same rules apply; show interfaces/ports and key FSMs rather than whole modules, and put full RTL in the repository.
