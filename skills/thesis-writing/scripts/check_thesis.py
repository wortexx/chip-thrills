#!/usr/bin/env python3
"""Mechanical checks for a technical thesis draft (LaTeX or Markdown).

Usage:
    check_thesis.py main.tex                 # follows \\input / \\include
    check_thesis.py chapters/*.tex --bib references.bib
    check_thesis.py draft.md

Findings are leads to verify in context, not verdicts.
"""
import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

HYPE = [
    "revolutionary", "seamless", "seamlessly", "cutting-edge", "cutting edge",
    "game-changing", "game changer", "groundbreaking", "ground-breaking",
    "best-in-class", "world-class", "unprecedented", "next-generation",
    "powerful", "amazing", "incredible", "perfect", "perfectly",
]
VAGUE = [
    "very", "really", "quite", "extremely", "huge", "massive", "significantly",
    "a lot of", "lots of", "a couple of", "it can be seen that",
    "it is obvious that", "obviously", "clearly", "in order to",
]
PLACEHOLDER_RE = re.compile(
    r"\\todo\b|\bTODO\b|\bFIXME\b|\bXXX\b|\bTBD\b|CITATION NEEDED|\[VALUE:|lorem ipsum|\?\?",
    re.I)
UNITS = (r"(?:[kMGT]?Hz|[mµun]?s|ns|ps|[mµunk]?m|[mµunpk]?W|[mµk]?V|[kMGT]?B|"
         r"[KMG]iB|bits?|°C|K|dB|dBm|LUTs?|FFs?|cycles|\\%)")
CITE_CMD = r"\\(?:[pP]aren|[tT]ext|[aA]uto|foot|full|[sS]mart)?cite[pt]?\*?"
CITE_RE = re.compile(CITE_CMD + r"(?:\[[^\]]*\]){0,2}\{([^}]*)\}")
NOCITE_RE = re.compile(r"\\nocite\{([^}]*)\}")
REF_RE = re.compile(r"\\(?:[cC]ref|[vV]ref|autoref|ref|pageref|eqref|nameref|[cC]pageref)\*?\{([^}]*)\}")
LABEL_RE = re.compile(r"\\label\{([^}]*)\}")
INPUT_RE = re.compile(r"\\(?:input|include|subfile)\{([^}]*)\}")
HEAD_RE = re.compile(r"\\(part|chapter|section|subsection|subsubsection|paragraph)\*?(?:\[[^\]]*\])?\{(.*)\}")
LEVELS = {"part": -1, "chapter": 0, "section": 1, "subsection": 2, "subsubsection": 3, "paragraph": 4}
FLOAT_START = re.compile(r"\\begin\{(figure|table|itemize|enumerate|description|lstlisting|algorithm|minted|longtable|sidewaystable|sidewaysfigure|wrapfigure)\*?\}")


HIDDEN_TODOS = []


class Line:
    __slots__ = ("file", "no", "text")

    def __init__(self, file, no, text):
        self.file, self.no, self.text = file, no, text

    def loc(self):
        return f"{self.file}:{self.no}"


def strip_tex_comment(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def load_tex(path, root_dir, seen, out):
    path = path.resolve()
    if path in seen or not path.exists():
        return
    seen.add(path)
    rel = path.relative_to(Path.cwd()) if path.is_relative_to(Path.cwd()) else path
    for no, raw in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        text = strip_tex_comment(raw)
        out.append(Line(str(rel), no, text))
        cm = re.search(r"(?<!\\)%.*", raw)
        if cm and PLACEHOLDER_RE.search(cm.group(0)):
            HIDDEN_TODOS.append(f"{rel}:{no}: {cm.group(0).strip()[:100]}")
        for m in INPUT_RE.finditer(text):
            name = m.group(1).strip()
            cand = root_dir / name
            if cand.suffix != ".tex":
                cand = cand.with_suffix(".tex") if not (root_dir / name).exists() else cand
            load_tex(cand, root_dir, seen, out)


def is_front(fname, words):
    low = fname.lower()
    return any(w in low for w in words)


def check(lines, md, bibs):
    findings = defaultdict(list)
    add = lambda key, ln, msg: findings[key].append(f"{ln.loc()}: {msg}")

    in_math = False
    env_stack = []
    labels = {}            # label -> (Line, env)
    refs = set()
    cites = set()
    nocite_all = False
    heads = []             # (level, title, Line)
    abstract_open = False

    for i, ln in enumerate(lines):
        t = ln.text
        st = t.strip()

        # --- environments (LaTeX) ---
        if not md:
            for m in re.finditer(r"\\(begin|end)\{([^}]*)\}", t):
                if m.group(1) == "begin":
                    env_stack.append(m.group(2))
                    if m.group(2) == "abstract":
                        abstract_open = True
                elif env_stack:
                    env_stack.pop()
                    if m.group(2) == "abstract":
                        abstract_open = False
            for m in LABEL_RE.finditer(t):
                env = next((e for e in reversed(env_stack) if e.rstrip("*") in ("figure", "table", "sidewaysfigure", "sidewaystable", "wrapfigure", "longtable", "lstlisting", "algorithm")), None)
                labels[m.group(1)] = (ln, env)
            for m in REF_RE.finditer(t):
                refs.update(k.strip() for k in m.group(1).split(","))
            for m in CITE_RE.finditer(t):
                cites.update(k.strip() for k in m.group(1).split(",") if k.strip())
            for m in NOCITE_RE.finditer(t):
                if "*" in m.group(1):
                    nocite_all = True
                cites.update(k.strip() for k in m.group(1).split(",") if k.strip() != "*")
            # also catch refs in label option of listings: label=...
            hm = HEAD_RE.search(t)
            if hm:
                heads.append((LEVELS[hm.group(1)], hm.group(2), ln, hm.group(1)))
        else:
            if st.startswith("```"):
                in_math = not in_math
                continue
            if in_math:
                continue
            hm = re.match(r"^(#{1,6})\s+(.*)", st)
            if hm:
                heads.append((len(hm.group(1)), hm.group(2), ln, "h"))

        in_verbatim = any(e.rstrip("*") in ("lstlisting", "verbatim", "minted", "equation", "align", "displaymath", "tikzpicture", "tabular", "tabularx") for e in env_stack)
        prose = st and not in_verbatim and not (not md and st.startswith("\\") and not st.startswith(("\\textit", "\\emph", "\\textbf")))
        in_abstract = abstract_open or is_front(ln.file, ["abstract"])
        in_preface = is_front(ln.file, ["preface", "acknowledg", "foreword"])

        if PLACEHOLDER_RE.search(t):
            add("placeholders / TODOs left in", ln, st[:100])

        if in_abstract and (CITE_RE.search(t) or re.search(r"\[\d+(?:[,–-]\s*\d+)*\]", t) and md):
            add("citation in abstract (abstracts have no references)", ln, st[:100])
        if in_abstract and not md and FLOAT_START.search(t):
            add("figure/table/list in abstract", ln, st[:100])

        if not prose:
            continue
        plain = re.sub(r"\$[^$]*\$", " MATH ", t)

        if not in_preface and re.search(r"(?<![~\w])(?<!Table )(?<!Figure )(?<!Part )(?<!Phase )\bI\b(?!/O|-|\.|~)|\b[Mm]y\b", re.sub(r"\\[a-zA-Z]+", " ", plain)):
            add("first person 'I/my' outside preface", ln, st[:100])

        # a line only starts a sentence if the previous prose line ended one
        prev = next((p.text.strip() for p in reversed(lines[:i]) if p.text.strip()), "")
        starts = r"(^|[.!?]\s+)" if (not prev or re.search(r"[.!?]\}?$", prev) or re.match(r"\\(begin|end|chapter|section|subsection|subsubsection|paragraph|label|item|centering|par|noindent)\b", prev)) else r"([.!?]\s+)"
        if re.search(starts + r"(" + CITE_CMD + r"|\[\d+)", st):
            add("sentence starts with a numeric citation", ln, st[:100])
        if re.search(starts + r"\$", st):
            add("sentence starts with a math symbol", ln, st[:100])

        for m in re.finditer(r"(?<![\w.\d])\.\d+\b", plain):
            add("missing leading zero (write 0.5, not .5)", ln, m.group(0))

        if not md:
            for m in re.finditer(r"\d\s" + UNITS + r"(?![\w])", plain):
                add("breakable space between number and unit (use ~ or \\qty/\\SI)", ln, m.group(0))
            for m in re.finditer(r"(Figure|Fig\.|Table|Chapter|Section|Equation|Eq\.|Appendix|Listing|Algorithm)\s\\(?:ref|eqref)\{", t):
                add("breakable space before \\ref (use Figure~\\ref{...})", ln, m.group(0))
            for m in re.finditer(r"\w\s(" + CITE_CMD + r")\{", t):
                add("breakable space before \\cite (use text~\\cite{...})", ln, m.group(0).strip())
            if re.search(r"\.\s*" + CITE_CMD + r"\{", t):
                add("citation after the full stop (place it before the period unless it deliberately covers several sentences)", ln, st[:100])
        else:
            for m in re.finditer(r"\d" + r"\s" + UNITS.replace(r"\\%", "%") + r"(?![\w])", plain):
                pass  # Markdown: spacing is fine; non-breaking handled by renderer

        lower = plain.lower()
        for w in HYPE:
            if re.search(r"\b" + re.escape(w) + r"\b", lower):
                add("marketing / hype word", ln, w)
        for w in VAGUE:
            if re.search(r"\b" + re.escape(w) + r"\b", lower):
                add("vague intensifier or filler (quantify or cut)", ln, w)
        if re.search(r"\b(e\.g\.|i\.e\.|etc\.)", lower):
            add("Latin abbreviation in running text (consider 'for example' / 'that is')", ln, re.search(r"(e\.g\.|i\.e\.|etc\.)", lower).group(1))

    # --- small-font commands when the body size was changed ---
    if not md:
        body = next((ln for ln in lines if re.search(r"\\renewcommand\{?\\normalsize\}?\s*\{\s*\\fontsize", ln.text)), None)
        resized = {m.group(1) for ln in lines for m in re.finditer(r"\\renewcommand\{?\\(small|footnotesize|scriptsize|tiny)\b", ln.text)}
        if body:
            for ln in lines:
                for m in re.finditer(r"\\(small|footnotesize|scriptsize|tiny)\b", ln.text):
                    if m.group(1) not in resized and "renewcommand" not in ln.text:
                        add(f"\\{m.group(1)} uses the class default size, but \\normalsize was redefined at {body.loc()} (text may be far smaller than the body font)", ln, ln.text.strip()[:80])

    # --- headings ---
    if heads:
        if md:
            base = min(h[0] for h in heads)
            # treat a single top-level H1 as the document title
            if sum(1 for h in heads if h[0] == base) == 1 and len(heads) > 1:
                base += 1
            norm = [(h[0] - base, h[1], h[2], h[3]) for h in heads if h[0] >= base]
        else:
            has_chapter = any(h[3] == "chapter" for h in heads)
            off = 0 if has_chapter else 1
            norm = [(h[0] + off, h[1], h[2], h[3]) for h in heads if h[3] not in ("part", "paragraph")]
        for lvl, title, ln, _ in norm:
            words = len(re.sub(r"\\[a-zA-Z]+|[{}$]", " ", title).split())
            if lvl >= 3:
                add("fourth heading level (max three levels, e.g. 4.4.2)", ln, title)
            if words > 6:
                add("long heading (> 6 words)", ln, f"{words} words: {title}")
        # lone subsections: count children per parent
        children = defaultdict(list)
        stack = []
        for idx, (lvl, title, ln, _) in enumerate(norm):
            while stack and norm[stack[-1]][0] >= lvl:
                stack.pop()
            parent = stack[-1] if stack else None
            children[(parent, lvl)].append(idx)
            stack.append(idx)
        for (parent, lvl), kids in children.items():
            if parent is not None and len(kids) == 1:
                k = norm[kids[0]]
                add("lone subsection (if you subdivide, use at least two)", k[2], k[1])

    # --- heading immediately followed by float/list ---
    for i, ln in enumerate(lines):
        is_head = (HEAD_RE.search(ln.text) if not md else re.match(r"^#{1,6}\s", ln.text.strip()))
        if not is_head or (not md and is_head.group(1) == "paragraph"):
            continue
        for nxt in lines[i + 1:i + 8]:
            s = nxt.text.strip()
            if not s or (not md and (s.startswith("\\label") or s.startswith("\\index"))):
                continue
            if (not md and FLOAT_START.search(s)) or (md and (s.startswith("![") or s.startswith("|") or re.match(r"^([-*+]|\d+\.)\s", s))):
                add("section starts with a figure/table/list (put text first)", nxt, s[:80])
            break

    # --- unreferenced floats ---
    if not md:
        for lab, (ln, env) in labels.items():
            if env and lab not in refs:
                add(f"{env.rstrip('*')} never referenced in text", ln, lab)
        for r in sorted(refs - set(labels)):
            findings["\\ref to undefined label"].append(r)

    # --- bibliography ---
    if bibs and not md:
        keys = {}
        for b in bibs:
            for no, raw in enumerate(Path(b).read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                m = re.match(r"\s*@(\w+)\s*\{\s*([^,\s]+)\s*,", raw)
                if m and m.group(1).lower() not in ("string", "preamble", "comment"):
                    keys[m.group(2)] = f"{b}:{no}"
        if not nocite_all:
            for k in sorted(set(keys) - cites):
                findings["bib entry never cited"].append(f"{keys[k]}: {k}")
        for k in sorted(cites - set(keys)):
            findings["cited key missing from bib"].append(k)

    return findings


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--bib", action="append", default=[], help=".bib file(s); auto-detected from \\addbibresource/\\bibliography")
    ap.add_argument("--no-follow", action="store_true", help="don't follow \\input/\\include")
    ap.add_argument("--max-per-check", type=int, default=25)
    args = ap.parse_args()

    md = all(f.endswith((".md", ".markdown", ".txt")) for f in args.files)
    lines = []
    if md:
        for f in args.files:
            for no, raw in enumerate(Path(f).read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                lines.append(Line(f, no, raw))
    else:
        seen = set()
        for f in args.files:
            p = Path(f)
            if args.no_follow:
                for no, raw in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    lines.append(Line(f, no, strip_tex_comment(raw)))
            else:
                load_tex(p, p.parent, seen, lines)
        if not args.bib:
            for ln in lines:
                for m in re.finditer(r"\\(?:addbibresource|bibliography)\{([^}]*)\}", ln.text):
                    for name in m.group(1).split(","):
                        base = Path(args.files[0]).parent
                        cand = base / name.strip()
                        if cand.suffix != ".bib":
                            cand = cand.with_suffix(".bib")
                        if cand.exists():
                            args.bib.append(str(cand))

    findings = check(lines, md, args.bib)
    if HIDDEN_TODOS:
        findings["TODO hidden in a comment (invisible in the PDF; use \\todo{} or a bold [..] marker)"] = HIDDEN_TODOS
    if not findings:
        print("No mechanical issues found. Now review argument, structure and evidence by hand.")
        return 0
    total = 0
    for key in sorted(findings, key=lambda k: -len(findings[k])):
        items = findings[key]
        total += len(items)
        print(f"\n## {key} ({len(items)})")
        for it in items[: args.max_per_check]:
            print(f"  {it}")
        if len(items) > args.max_per_check:
            print(f"  … {len(items) - args.max_per_check} more")
    print(f"\n{total} findings across {len(findings)} checks. Verify each in context before reporting.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
