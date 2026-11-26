# Transcription brief -- Tales of Argosa (Phase A: roll tables + chapter plan)

## Authorization context
The user (Max) owns this PDF (legitimately purchased) and placed it in his workspace for this purpose. The book's text is also published under CC BY-SA 4.0 (credits page). The destination is his personal, local Obsidian vault "Tales of Argosa MD" -- a GM reference layer over a book he owns; nothing is published or redistributed. Proceed with the transcription.

## What Phase A is
The vault will eventually hold the whole book. Phase A does two things for your page range:
1. **Transcribe every roll table** into its own note, at the path where it will live in the finished vault.
2. **Write the chapter plan** (`_plan.md`): every note the finished vault will need for your pages, in order, so a later Phase C agent can fill in the prose without renumbering anything.

A **roll table** is any table (or table-like list) whose rows are chosen by a die roll or roll result: d4-d100, 2d6, d66, percentile ranges (`01-05`), result bands of a check, "roll 1d6: 1-3 ..., 4-5 ..." lists set as a table. Include generator step tables, name/trait/personality tables, encounter tables, trauma/injury tables, events, treasure, trinkets, mutations, monster trait tables, everything rollable. If in doubt, include it and say so in the report.
**Not** Phase A (leave for Phase C, but list them in `_plan.md`): non-random reference tables -- class attack-bonus/progression tables, weapon/armour/gear/price lists, skill lists, XP tables, ship stat lists, ritual component lists that are not rolled, etc.

## Your inputs (ROOT = /home/claude/toa)
- Typing source, per PDF page: `ROOT/fm/toa/pNNN.md` -- the PDF's own text with **bold** / *italic* / ***both*** already applied from the font data. Display-size headings (title bars) appear plain. WARNING: the reading order in pNNN.md does not always follow the printed columns (a table's rows can be interleaved with another table's rows from the facing column). Always place rows by the page image.
- Page images: `ROOT/pages/toa/pNNN.png` (200 DPI, 1700x2200) and `pNNN.txt` (pdftotext -layout). NNN = PDF page. **PDF page = printed page + 2.**
- Approved sample (the model for every table note): `ROOT/samples/13.2.1. Blade Trauma.md`.
- Batch plan: `ROOT/batches.tsv` (your row: id, PDF pages, chapters you own, numbering).

## Method (font-assisted, mandatory)
- Find the tables in your range from `pNNN.md`/`pNNN.txt` first; open the page image of **every page that has any table** (crop/zoom with PIL into your scratch folder for dense tables -- full pages are 1700x2200). Pure prose pages need no image in Phase A (use their text for the plan).
- Type each cell from `pNNN.md`: keep its emphasis exactly, instance by instance -- never add or remove bold/italic by category. Never paraphrase or tidy wording; verbatim, including the book's spelling (armour, disad, etc.) and its typos (report typos, don't fix them).
- Re-join line-end hyphenation (`jump-` / `ing` -> `jumping`), but keep real compounds and **numeric ranges**: `4-` / `5: below knee` is `4-5: below knee`.
- Known text-layer glitches: a few words may be glued or split (`roof 's`, `"Thief ! Thief !"`): write what the image shows. Icons (dice symbols, sun/skull) are not in the text layer: if a cell shows an icon that carries meaning, write it in words in square brackets, e.g. `[sun icon]`, and report it.
- Escape literal asterisks (`\*`) and pipes inside cells (`\|`).
- Plain keyboard punctuation only: straight quotes `' "`, `...`, `--` for em dash, `-` for en dash/minus, `x` for the multiplication sign. Never typographic glyphs. (pNNN.md is already plain.)

## Vault structure (fixed -- all batches use these chapter folders)
Vault root: `Tales of Argosa MD/`. Chapter folders (book order; front matter, credits, contents and index are not transcribed):
```
1. What Is Tales of Argosa      (PDF 6-9: What is ToA, Core Features, How to Play)
2. Character Creation           (PDF 10-12, incl. Backgrounds)
3. Attributes                   (PDF 13-14, incl. Luck)
4. Races                        (PDF 15-16)
5. Classes                      (PDF 17-45)
6. Party Bonds                  (PDF 46)
7. Unique Features              (PDF 47-53)
8. Skills & Rerolls             (PDF 54-56)
9. Equipment                    (PDF 57-64)
10. Doing Things                (PDF 65-67)
11. Encounters                  (PDF 68-70)
12. Combat                      (PDF 71-84)
13. Injury & Death              (PDF 85-90)
14. Healing & Recovery          (PDF 91-92)
15. Sorcery                     (PDF 93-114)
16. Downtime                    (PDF 115-130)
17. GM Tools                    (PDF 131-157)
18. Hirelings                   (PDF 158-161)
19. Madness                     (PDF 162-163)
20. Mass Battle                 (PDF 164-167)
21. Monsters                    (PDF 168-209)
22. Naval Combat                (PDF 210-213)
23. Oracle Tools                (PDF 214-215)
24. Rival Adventurers           (PDF 216-217)
25. Solo Rules                  (PDF 218-223)
26. Traps                       (PDF 224-230)
27. Treasure                    (PDF 231-261)
28. Variant Rules               (PDF 262-263)
```
Check the chapter boundaries against the images; if a boundary above is wrong by a page, follow the book and report it.

Inside a chapter (Knave-style numbering; **every number segment ends with a period**):
- `X.N. Name_.md` -- a rules/prose section (trailing underscore marks rules notes). Sections follow the book's own headings (the contents page and the big headings); a minor sub-heading stays a `###` heading inside its section note rather than becoming its own note. Aim for notes a GM would look up (e.g. `13.1. Injury & Death_`, `13.2. Trauma Tables_`).
- `X.N.M. Name.md` -- a roll table belonging to section X.N, numbered in book order. A table group with no prose section of its own is fine (`17.5.1. ...` under a `17.5. Encounter Tables_` note that may be short).
- Per-entry collections (spells, monsters, magic items, rival adventurers if one note each makes sense): a subfolder `X.N. Name/` holding one note per entry, named as printed in Title Case (e.g. `15.5. Spells/Lightning Bolt.md`). A roll table that belongs to one entry of a collection lives in that subfolder, named by its printed title (e.g. `21.4. Bestiary/Terror Traits.md`).
- Filenames: the printed title in Title Case (`BLADE TRAUMA` -> `Blade Trauma`), keeping the book's words; `/` and `:` become ` - `; no `?`. If two tables share a title, add the parent section's word ("Carousing - Complications" style) and report it.

## Table note format (match the sample)
- The note holds only the table, plus any text printed **inside the table's frame** (a caption line under the title bar, a key/footnote line directly under the table, a "Roll ..." line printed in the bar). Prose above the table that explains it belongs to the section's rules note (Phase C) -- do not copy it into the table note. The title bar becomes the filename, not a heading. No H1.
- First column = the roll. Header row: only printed words. The die column header is the die, taken from the page (`d12` when the prose says "Roll 1d12", `d100`, `2d6`); if nothing prints it, infer it from the entries and say so in the report. Other header cells stay empty unless the book prints column titles (then use them exactly).
- Rows in numeric order; die results verbatim (`1-2`, `01-05`, `00`, `13`, `20+`). A row's cell = all its printed lines joined with single spaces. Where a cell prints separate paragraphs or its own bullet list, join them with `<br>`.
- One table, not two: a table printed in two side-by-side halves, or continued in the next column/page, becomes one table in roll order. A table whose title bar covers several parallel columns (e.g. OVERLAND / UNDERGROUND / VOYAGE sharing one roll column) is one table with those column headers.
- Two genuinely separate tables under separate title bars are separate notes, even when they sit side by side.
- Keep cross-references verbatim, including page references (`(p.66)`, `*Blunt Trauma*`). **No wiki-links in this pass.**
- If a table's rows are themselves split into sub-tables by a printed sub-heading (e.g. a d100 Encounter table split into "Aerial", "Desert" ... under one chapter), each printed title bar = its own note.

## The chapter plan (`_plan.md`, mandatory)
For every chapter you own, list **every note the finished vault will need**, in book order, as a markdown table:
`| path (vault-relative) | kind | PDF pages | status | contents |`
- kind: `folder`, `rules`, `table`, `entry` (one per-entry note), `ref-table` (a non-roll table that will sit inside the named rules note -- give the rules note path in contents).
- status: `written` (you wrote it) or `phase-C`.
- contents: the printed headings / entry names it covers (for per-entry collections list every entry name as printed, one row each).
Every printed page of your range must be accounted for (art-only pages: list them once as `art` rows so nothing looks missing). Phase C will follow this plan exactly, so make the numbering final.

## Page boundaries
You own every chapter listed in your batch row. Tables that start on your pages are yours; read past your last page to finish a table if needed. Don't write notes for chapters you don't own.

## Output
Write notes under `ROOT/out/<BATCH>/Tales of Argosa MD/...` mirroring the vault path. Write only inside your batch folder. Working files (crops, scripts) only in `ROOT/scratch/<BATCH>/`.
Write `ROOT/out/<BATCH>/_plan.md` (above) and `ROOT/out/<BATCH>/_report.md`: table notes written (path <- PDF pages, die header and whether inferred), anything you were unsure was a roll table, suspected source typos/errors (verbatim quote + PDF page), judgement calls, icons replaced by words, chapter-boundary corrections.
Before finishing, self-check every table note: the row count and roll ranges cover the die with no gaps/duplicates (or the gap is printed), every row's cell was checked against the image, no typographic punctuation (`grep -P "[\x{2018}\x{2019}\x{201C}\x{201D}\x{2013}\x{2014}\x{2026}\x{00D7}]"` finds nothing).
Final reply: batch id, table-note count, 3-6 lines of judgement calls/problems. Don't paste notes.
