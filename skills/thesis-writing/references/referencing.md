# Referencing

Contents: Why references · Source reliability · Numeric vs name-year · In-text citation patterns · Quotations · Secondary sources · Bibliography content · Entry examples · Common mistakes · Copyright and reuse

---

## Why references

Citing credits the original author and places the primary responsibility for the content on them. References show familiarity with the field, let the examiner judge the quality and reliability of the work, justify the author's choices, and allow background to be presented compactly. Taking credit for others' work is the most serious mistake a thesis writer can make.

References are most dense in the background chapter and when comparing results with others.

## Source reliability

The author is responsible for judging each source: who wrote it, who published it, what it cites, how accurate it is.

Rough order of preference:
1. Peer-reviewed journal articles, conference papers, books from academic publishers.
2. Standards, specifications, datasheets, official documentation (cite with document ID and version/revision).
3. Theses, technical reports, preprints (arXiv — note that it is not peer-reviewed; cite the published version when one exists).
4. Company websites, project repositories, blogs — with discretion and an access date.
5. Forums and Q&A sites — generally unreliable.

Wikipedia is not cited in an academic thesis (use it only to find primary sources). Prefer primary sources over secondary ones. Back "common"/"widely used" claims with several sources.

## Numeric vs name-year

| | Numeric (Vancouver / IEEE) | Name-year (Harvard / APA-like) |
|---|---|---|
| In text | [1], [2, p. 23], [6–18] | (Weber 2001), Weber (2001, p. 230) |
| Bibliography order | alphabetical by first author, or order of first citation (IEEE) | alphabetical by first author |
| Typical fields | engineering, CS, electronics (IEEE) | industrial management, information management, architecture |
| Pros/cons | compact; numbers meaningless without the list | longer, more special cases; reader sees who/when |

Pick one, follow the institution's/supervisor's choice and the field's convention, and **never mix them**. In LaTeX, set it once with biblatex (`style=ieee`, `style=numeric-comp`, `style=authoryear`) or a BibTeX `.bst`; don't hand-format.

## In-text citation patterns

Placement: as close as possible to the cited claim, normally inside the sentence before the full stop: "… is widely used [3]."

Extent: the position signals what the citation covers. A citation after the final full stop of a paragraph ("… platform. [100]") can mark the whole paragraph as cited — but it's ambiguous. Clearer: cite in the first sentence and phrase the following sentences so it's obvious they come from the same source ("The same study also reports …").

One source:
- Weber argues that … [1].
- Cattaneo et al. introduce in their study [2] a new …
- The result is … [1, p. 23].
- In accordance with the presented theory … (Weber 2001).
- Weber (2001, p. 230) has stated …

Rules:
- A numeric citation can replace the name of a source but must **not begin a sentence**: ✗ "[2] proposed …" → ✓ "Cattaneo et al. [2] proposed …".
- Give page numbers when citing a specific passage; omit when citing the whole work.
- Name-year with more than two authors: first author + "et al." in text; all authors in the bibliography. Two authors: both names (Smith & Braun 1994).
- Same author, same year: 2001a, 2001b — also in the bibliography.
- Unknown author (name-year): use the first words of the title or the corporate author: (Raw Materials Manual 2002).

Multiple sources: numeric in ascending order [1, 3, 5] or [1][3][5]; ranges with an en dash [6–18]. Name-year ordered by year: (Weber 2001; Kaunisto 2003; Cattaneo et al. 2004). Don't let long citation lists bury the message — and don't cite ten papers for one trivial claim.

Figures and tables from other sources: citation goes in the caption ("… in 2003–2005 [15]."); if redrawn or modified, "adapted from [15]".

## Quotations

Direct quotations are rare in engineering — paraphrase and cite instead. When quoting:
- Exact words in quotation marks, followed by the reference with page: "…" [7, p. 3].
- Omitted parts marked with "…"; clarifications in square brackets: "This [academic misconduct] includes …".
- Errors in the source kept and marked "(sic)".
- Quotations must be offset/marked, not too long, not misleading, verbatim, and relevant to the author's own argument — they must not drown out the author's voice.

## Secondary sources

Always try to locate and read the primary source. If impossible, make the second-hand nature explicit:
- "… is 0.0615 cm²/g [1, see 2]."
- "According to Shleinen et al. [1], as cited in Pöllänen [2], …"
- "(Shleinen et al. 1998, cited in Pöllänen 2003)"

List the original in the bibliography only if you actually read it.

## Bibliography content

Every entry needs enough to find the source:

| Numeric | Name-year |
|---|---|
| 1. authors | 1. authors |
| 2. title | 2. (year) |
| 3. publisher / journal / conference | 3. title |
| 4. year | 4. publisher / journal / conference |
| 5. pages | 5. pages |
| 6. URL / DOI if applicable | 6. URL / DOI if applicable |

- List **all** authors in the bibliography (or follow the style's truncation rule consistently).
- Volume/issue/pages when available; DOI strongly recommended.
- Online material: URL **and access date**; readers must be able to find it again from the other details if the URL dies. Test whether a search engine finds it from the details given. Don't randomly truncate long URLs (LaTeX: `\url{}` with the `url`/`xurl` package breaks them properly).
- Datasheets/standards: document number and revision.
- Accepted-but-unpublished articles: "accepted for publication, year".
- Write journal and conference names in full and in **one consistent form** — preference: "in Proc. IEEE International Symposium on Circuits and Systems (ISCAS)" > "In Proceedings of ISCAS" > "In ISCAS" > "Proc. ISCAS".
- Author names in one consistent form ("K. Keutzer" or "Keutzer, K.").
- Use a reference manager (BibTeX/biblatex + Zotero/JabRef, Mendeley, RefWorks) — each reference is typed once and formatted automatically. Still check the generated `.bib` fields: tools often import wrong capitalisation, missing pages, or "arXiv" as the venue for published papers. In BibTeX, protect acronyms in titles with braces: `title = {A {RISC-V} Coprocessor for {SHA-3}}`.

## Entry examples (numeric style)

```
[1] M.J. Weber, Handbook of Lasers, CRC Press, Boca Raton, FL, USA, 2001, 300 p.                         (book)
[2] S. Cattaneo, E. Vuorimaa, H. Lemmetyinen, M. Kauranen, Advantages of Polarized Two-beam
    Second-harmonic Generation in Precise Characterization of Thin Films, Journal of Chemical
    Physics, Vol. 120, Iss. 19, 2004, pp. 9245–9252.                                                     (journal)
[4] W. Li, M. Pessa, T. Jouhti, C.S. Peng, E.-M. Pavelescu, GaInNAs Quantum Well Lasers, in:
    H.S. Nalwa (ed.), Encyclopedia of Nanoscience and Nanotechnology, Vol. 3, American Scientific
    Publishers, California, USA, 2004, pp. 719–730.                                                      (chapter in compilation)
[5] F. Wai-ling Ho-Ching, J. Mankoff, J.A. Landay, Can you see what I hear?: The Design and
    Evaluation of a Peripheral Sound Display for the Deaf, Proceedings of the SIGCHI Conference on
    Human Factors in Computing Systems, Ft. Lauderdale, FL, USA, April 5–10, 2003, ACM Press,
    pp. 161–168.                                                                                         (conference)
[6] A. Puhakka, Weakest Congruences, Fairness, and Compositional Process-algebraic Verification,
    dissertation, Tampere University of Technology, 2004, 176 p. Available: http://…                    (thesis)
[8] OMAP4430 Multimedia Device Data Manual, Texas Instruments, Literature Number SWPS041D,
    Dec 2012, 443 p. Available: http://www.ti.com/lit/gpn/omap4430                                      (datasheet)
[11] Intel Timeline: A History of Innovation, Intel Corporation, website. Available (accessed
    24.6.2013): http://www.intel.com/…                                                                   (website)
[16] Y. Pan, G. Dong, T. Zhang, Error Rate-Based Wear-Leveling for NAND Flash Memory at Highly
    Scaled Technology Nodes, IEEE Trans. VLSI Systems, accepted for publication, 2013.                  (accepted)
[21] V. Miettinen, MSc (Tech), CEO, Company Ltd. Interview on 25.5.2005.                                (interview)
```

Name-year form of a journal article:
```
Keutzer, K., Newton, A.R., Rabaey, J.M. & Sangiovanni-Vincentelli, A. (2000). System-level design:
  orthogonalization of concerns and platform-based design. IEEE Transactions on Computer-Aided Design
  of Integrated Circuits and Systems, 19(12), pp. 1523–1543.
```

The source type never changes the order or formatting of fields — completely different sources are written consistently. Alphabetising: lower-case name prefixes are ignored (van der Sar → S), upper-case ones are not (De Niro → D).

## Common mistakes

1. **Assuming something is common knowledge.** "Better, faster, cheaper" needs a reference and a magnitude (1 cent, EUR 1 or EUR 100?).
2. **Single-source background.** Use several authors, compare their theories and results, note where terms are used differently. "Commonly" needs several references.
3. **Not positioning the work.** State the similarities and differences between this work and others, and its novelty.
4. **Drifting from the sources' facts.** Cross-check background facts in several sources. Record full bibliographic info when taking notes.
5. **Inconsistent formatting** of names, months, venue names, field order.
6. **Orphans**: bibliography entries not cited in the text (often left after edits) — and citations with no entry.
7. **Copying the sources' mistakes** — unclear or missing information in a source shouldn't propagate.
8. **Losing track of numbers.** Note exactly which number came from which source and page.
9. **Making your own work hard to cite.** Any document you produce (reports, slides, memos) should carry author, title, date, publisher.

## Copyright and reuse

- Quoting text is allowed when credited, marked, verbatim, of reasonable length, non-misleading and relevant (see Quotations). Always credit even when no permission is needed.
- Reproducing figures: ordinary graphs and block diagrams (e.g. from datasheets) are rarely original works of authorship, but must still be cited. Photographs and creative illustrations usually are protected — redraw from the data, use CC-licensed material, or request permission (IEEE and other publishers offer permission links per article).
- Copyright law follows the country of origin; the US has a "fair use" doctrine for criticism, teaching, scholarship and research, but other jurisdictions are stricter. Check the institution's guidance when publishing the thesis online.
- Creative Commons material can usually be reused for research — check the specific licence terms (attribution, non-commercial, no-derivatives, share-alike).
- Company-internal information needs the company's permission before it goes into a public thesis.
