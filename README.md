# chip-thrills

A collection of agents and skills for ASIC and FPGA design, inspired by Awesome Copilot.

## Skills

| Skill | What it does |
|---|---|
| [systemverilog-style](skills/systemverilog-style/) | Write, refactor and review SystemVerilog/Verilog RTL and testbenches in the lowRISC Comportable style: naming, ports, `always_ff`/`always_comb` split, FSMs, case statements, widths and X-avoidance. Follows the existing codebase's convention where it differs. |
| [thesis-writing](skills/thesis-writing/) | Plan, draft, review and polish a Master's or Bachelor's thesis in a technical field: structure, scientific style, figures, tables, equations, code listings, citations and layout. Includes a checker script for LaTeX and Markdown drafts. |

## Install

### Claude Code (plugin)

```
/plugin marketplace add wortexx/chip-thrills
/plugin install chip-thrills@chip-thrills
```

### Any agent that reads `SKILL.md` folders

Copy a skill folder into your skills directory, for example:

```bash
git clone https://github.com/wortexx/chip-thrills.git
cp -R chip-thrills/skills/thesis-writing ~/.claude/skills/
```

## thesis-writing

The skill picks what to do from what you ask:

- **Planning:** turns a topic into a chapter outline with page budgets, research questions and the author's contribution.
- **Drafting:** writes a section in your existing style and citation keys. It never invents sources or numbers; gaps become bold `[CITATION NEEDED]`, `[VALUE]` or `[CHECK]` markers that show in the PDF.
- **Reviewing:** runs `scripts/check_thesis.py`, then reviews the draft from structure down to wording, and ends with questions to expect at the defence.

The checker runs on its own too:

```bash
python3 skills/thesis-writing/scripts/check_thesis.py main.tex          # follows \input/\include
python3 skills/thesis-writing/scripts/check_thesis.py draft.md
```

Your institution's template and rules always take precedence over the skill's defaults.

**Source.** The skill is a condensed adaptation of Tampere University's *Guide to Writing a Thesis in Technical Fields: Instructions for Master of Science and Bachelor of Science theses* (January 2019). Rules that apply only to Finnish students or to Tampere University's own systems are left out.

## systemverilog-style

Used when writing new RTL (modules, FIFOs, FSMs, bus interfaces, register files) or reviewing `.sv`/`.v` code. Reviews group findings by severity and give the rule, why it matters, and a corrected snippet.

**Source.** A condensed adaptation of the [lowRISC Verilog Coding Style Guide](https://github.com/lowRISC/style-guides/blob/master/VerilogCodingStyle.md), © lowRISC contributors, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The skill condenses and reorganises the guide and defaults enum value names to `ALL_CAPS` where the guide allows either style.

## License

[MIT](LICENSE), except where a skill notes a different licence for adapted material (see systemverilog-style above).
