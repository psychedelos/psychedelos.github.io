# Table image-check brief -- Tales of Argosa MD (Phase A verification)

## Context and authorization
Max owns this PDF (legitimately purchased; its text is also CC BY-SA 4.0) and the vault is his personal GM reference over it. Tables are a crucial part of his play, so every row of every table is checked against the printed page. You review roll-table notes written by transcription agents and propose exact, minimal patches. You do NOT edit the notes -- you write a patch file; the orchestrator applies it.

## Inputs (ROOT = /home/claude/toa)
- Your group file: `ROOT/tri/<GROUP>.json` -- `{note path: {"pages": [PDF pages], "table_check_issues": [...], "fidelity_issues": [...]}}`. The automated flags are hints only: this book sets each row's die number vertically centred beside a narrow multi-line cell, and reading order across columns is interleaved, so most `cell-spans-rows` / `text-between-rows` / `cell-cut-short` / `row-unlocated` / `words replace|insert` flags are layout noise. Use them to find rows to look at first; the image decides.
- Notes (read-only): `ROOT/merged/Tales of Argosa MD/<note path>`.
- Page images: `ROOT/pages/toa/pNNN.png` (200 DPI, 1700x2200). Font-tagged text with the PDF's own bold/italic: `ROOT/fm/toa/pNNN.md`. NNN = PDF page (= printed page + 2).
- Conventions: `ROOT/BRIEF.md` (read the "Method" and "Table note format" sections) and the sample `ROOT/samples/13.2.1. Blade Trauma.md`.

## What to do
For EVERY table row of every note in your group: open the page image (crop and zoom with PIL into `ROOT/scratch/<GROUP>/` -- read dense tables at full resolution, a column at a time) and compare the note's row with the printed row cell by cell:
- the die range exactly as printed (`1-2`, `01-05`, `00`), no missing or duplicated rows (unless the print itself duplicates/skips -- keep the print and note it);
- every word and number in order -- no dropped, added, swapped or paraphrased words, no text that belongs to the row above/below, no cell cut short; signs (`+1`/`-1`);
- emphasis: bold/italic exactly as printed (the `pNNN.md` font data is authoritative for bold/italic; the image for layout);
- header row: die header and any printed column titles (only printed words; an inferred die is acceptable and must not be "fixed" to something unprinted).
Also check that nothing printed in the table's frame is missing (a footnote or key line), and that the note doesn't contain prose that is printed outside the table.
Source typos stay verbatim (don't fix them; list them). Plain keyboard punctuation only.
Never guess unreadable text.

## Patch rules (strict)
One patch per change; `old` must occur exactly once in the note (short, but long enough to be unique); change only the wrong words/markers; never touch filenames; no reflowing. Patches to the same file apply in list order.

## Output -- `ROOT/patches/TABLES-<GROUP>.json`
```
{"patches": [{"file": "<note path>", "old": "...", "new": "...", "why": "pNNN: what the print shows"}],
 "confirmed": [{"file": "<note path>", "note": "all N rows match"}],
 "rows_checked": {"<note path>": <number of rows you compared>},
 "source_typos": [{"file", "quote", "page"}],
 "questions": [{"file", "question"}],
 "notes": "..."}
```
Reply with: group id, patch count, rows checked, 3-5 lines on what you found. Don't paste the patches.
