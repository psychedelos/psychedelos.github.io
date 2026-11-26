# Transcription brief -- Tales of Argosa (Phase C: everything that is not a roll table)

## Authorization context
The user (Max) owns this PDF (legitimately purchased) and placed it in his workspace for this purpose. The book's text is also published under CC BY-SA 4.0 (credits page). The destination is his personal, local Obsidian vault "Tales of Argosa MD" -- a GM reference layer over a book he owns; nothing is published or redistributed. Proceed with the transcription.

## What Phase C is
Phase A already wrote every **roll table** as its own note (verified row by row against the page images -- do not change them). Phase C writes every other note the vault needs -- rules sections, reference tables inside them, per-entry notes (classes' gods, spells, monsters, magic items...) -- exactly as listed in the chapter plan. The plan's numbering is final.

## Your inputs (ROOT = /home/claude/toa)
- Your batch row: `ROOT/batches_c.tsv` (id, PDF pages, plan file, scope).
- The chapter plan: `ROOT/out/<A-batch>/_plan.md` -- every note, its kind, PDF pages and contents. Write every row with status `phase-C` (and every `ref-table` row inside its rules note) that falls in your scope. Rows with status `written` already exist in `ROOT/merged/Tales of Argosa MD/` -- read them, don't rewrite them.
- The Phase A report for the same pages: `ROOT/out/<A-batch>/_report.md` (judgement calls, typos, icons -- useful context).
- Typing source, per PDF page: `ROOT/fm/toa/pNNN.md` -- the PDF's own text with **bold** / *italic* / ***both*** already applied from the font data. Display-size headings appear plain. WARNING: the reading order in pNNN.md does not always follow the printed columns, and boxed sidebars can sit anywhere in it. Always follow the page image for order and layout.
- Page images: `ROOT/pages/toa/pNNN.png` (200 DPI, 1700x2200). **Open the image of every page you transcribe** (crop/zoom with PIL into your scratch folder; full pages are large). NNN = PDF page. **PDF page = printed page + 2.**

## Method (font-assisted, mandatory)
- Type every paragraph from `pNNN.md`: keep its emphasis exactly, instance by instance -- never add or remove bold/italic by category. Never paraphrase, summarize or tidy wording; verbatim, including the book's spelling (armour, disad, etc.) and its typos (report typos, don't fix them). Never invent text (no intro sentences, captions or headings the page doesn't print).
- Compare every page image with its `pNNN.md` and type anything printed but missing (art text, icons). Icons that carry meaning are written in words in square brackets, e.g. `[sun icon]`, `[d6 icon]`, and reported.
- Re-join line-end hyphenation (`jump-` / `ing` -> `jumping`), but keep real compounds and numeric ranges (`4-` / `5` -> `4-5`).
- Known text-layer glitches: a few words may be glued or split (`roof 's`, `mayonly`): write what the image shows.
- Escape literal asterisks (`\*`); escape `|` inside table cells (`\|`).
- Plain keyboard punctuation only: straight quotes `' "`, `...`, `--` for em dash, `-` for en dash/minus, `x` for the multiplication sign. Never typographic glyphs (pNNN.md is already plain).
- Skip: running heads, page numbers, art, art credits, the contents and index pages.

## Note format
- No H1. The filename carries the section title. If the note's first printed heading is the section title, don't repeat it.
- Printed headings inside a note: `###` for the headings directly under the section (the red/large headings), `####` for minor headings under those. Never skip levels upward, never invent headings.
- Term labels and inline headings keep the source's own bold/italic and punctuation (`**Luck Rolls**`, `**Nat 19.**`), as the font data shows.
- Bullets (the book's diamond bullets) become `- `; numbered steps stay numbered as printed (`1.`); lettered or roman sub-items keep their printed markers.
- **Sidebars and boxes** become callouts with the printed box title: `> [!note] Designer's Thoughts`, `> [!example]` for worked examples / examples of play printed in a box (title = printed title, else no title), `> [!tip] Optional` for printed optional rules, `> [!note] <Title>` for any other titled box. The body keeps the source's emphasis. Place a sidebar where it sits in the reading flow; if it interrupts a list or a run of subheads, put it at the end of that section.
- **Reference tables** (non-random tables listed as `ref-table` in the plan) go inside their rules note at the place they print, as markdown tables: header row = the printed column titles exactly (empty cells where nothing prints), rows in printed order, a multi-line cell joined with spaces, `<br>` only for printed separate paragraphs/list items inside a cell. A table title bar becomes a `###`/`####` heading above the table (printed title only).
- **Roll tables that Phase A wrote as their own notes**: at the place the table prints, put an embed line on its own: `![[13.2.1. Blade Trauma]]` (basename only, no `.md`). Do not copy the table's rows into the rules note.
- Paragraphs: one printed paragraph = one markdown paragraph (lines joined). Use hard line breaks (two trailing spaces) only where the print sets separate short lines (e.g. stat lines of a spell header).
- **No wiki-links** in this pass apart from the embeds above. Keep cross-references and page references verbatim (`(p.66)`, `*Blunt Trauma*`).

### Per-entry notes
- **Spells** (one note per spell): the spell's printed header lines first (e.g. `**Range:** Close` / `**Duration:** ...`, exactly as printed, each on its own line with a hard break), then the description paragraphs. The spell name is the filename (Title Case of the printed name).
- **Monsters** (one note per printed monster heading): the description paragraphs, then every printed stat block as **one paragraph each** (all its printed lines joined, bold/italic from the font data -- e.g. `**DRAGON (BOSS)** #1 **AC** 22 **HD** 20+8 ...`), then any further paragraphs/boxes that belong to the entry. Extra stat blocks printed under the same heading (young/elder variants) stay in that note. Group intro text (DEMONS, GIANTS ...) goes in the group-intro note the plan names.
- **Magic items, gods, unique features, rival adventurers, etc.**: printed name = filename, then the entry's text exactly as printed; per-item power tables (1st/2nd/3rd/Special) are reference tables inside the item note.
- Classes: follow the plan (one rules note per class with its attack-bonus table as a reference table).

## Filenames
Exactly as the plan gives them. If the plan is clearly wrong (a heading it missed, a note it merged that the page splits), follow the page, keep the plan's numbering for everything else, and report the change -- never renumber notes that already exist.

## Page boundaries
You own every plan row in your scope. A note whose text starts on your pages and continues past your last page is yours: read on and finish it. Skip text that belongs to a note starting before your first page (the previous batch finishes it).

## Output
Write notes under `ROOT/out/<BATCH>/Tales of Argosa MD/...` mirroring the vault path. Write only inside your batch folder. Working files (crops, scripts) only in `ROOT/scratch/<BATCH>/`.
Write `ROOT/out/<BATCH>/_report.md`: notes written (path <- PDF pages), plan rows you could not follow and why, suspected source typos/errors (verbatim quote + PDF page), judgement calls (callout choices, heading levels, icons), anything printed you left out and why.
Before finishing, self-check: every plan row in your scope has its note; every page in your range was opened; no typographic punctuation (`grep -P "[\x{2018}\x{2019}\x{201C}\x{201D}\x{2013}\x{2014}\x{2026}\x{00D7}]"` finds nothing); hard line breaks survived where you used them.
Final reply: batch id, note count, 3-6 lines of judgement calls/problems. Don't paste notes.
