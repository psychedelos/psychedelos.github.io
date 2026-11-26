# Linking pass brief -- Tales of Argosa MD (pass 2)

## Context and authorization
Max owns this book (legitimately purchased; text also CC BY-SA 4.0); the vault is his private Obsidian GM reference. Pass 1 (verbatim transcription) is finished and verified. This pass ONLY adds wiki-links. Proceed.

## Inputs (ROOT = /home/claude/toa/link)
- Working copy you edit in place: `ROOT/work/` (vault-relative paths). The untouched baseline: `ROOT/orig/` (never edit).
- Every note and its headings: `ROOT/index.txt` (`path :: heading | heading`).
- Printed page -> notes (+ headings on that page): `ROOT/pagemap.json` (`{"toa": {"66": [{"note", "share", "headings"}]}}`). The book prints page references as `p.66`, `(p.66)`, `p.229`, `see p.220`. Printed page = PDF page - 2 (the map is already in printed pages).
- Checker: `python3 /home/claude/toa/gmscripts/link_verify.py ROOT/orig ROOT/work --rules ROOT/rules.json --files <your notes, vault-relative, no .md>` -- run it on your own notes until 0 ERROR lines.

## The rules
1. Linking never changes the displayed text. Strip every link back to its alias and the note must read exactly as before. The only removable text is a print-layout page reference the link consumes (`(p.66)`, `p.229`) plus at most one preposition that only worked with the page number.
2. **Link only what the text phrases as a reference**: a page reference; "see X"; "the X table / the X chart / roll on X"; an *italic* name that is the book's own cross-reference marker -- italic spell names, monster names, magic item names, table names (*Blunt Trauma*), conditions (*Prone*, *Stunned*, *Helpless*, *Blind*... -> the condition's heading in `12. Combat/12.11. Conditions_`), *Consult the Bones* / *Read the Signs* (-> 23.2 / 23.3), *Boss* / *Heavy* (-> monster special traits) when a note exists. A bare rule word in running prose stays plain. Do NOT link *Luck* (it marks the Luck save/stat hundreds of times) or attribute names.
3. A page reference that points at a named thing: link the name, drop the page ref: `the Activities table (p.66)` -> `the [[11.2.1. Activity|Activities]] table`. A page reference that names nothing: keep the page text as the alias: `use p.229` -> `use [[27.1. Treasure_|p.229]]`. A page ref whose page holds several candidate notes: use the name to pick; if still ambiguous, leave it as printed and list it.
4. Link format: basename targets (no folders; every basename in this vault is unique), always with an alias: `[[13.2.3. Blunt Trauma|Blunt Trauma]]`, `[[12.11. Conditions_#Prone|Prone]]`, `[[Doppelganger|Doppelganger]]`. Anchors must be real headings of the target (see index.txt). Never a self-link (same-note references to a heading: `[[#Heading|text]]` only if it helps; otherwise leave). Never link inside a heading. Never touch `![[embed]]` lines.
5. Emphasis wraps the link: `*[[13.2.3. Blunt Trauma|Blunt Trauma]]*`, `***[[Hellblast|Hellblast]]***`. A span of emphasis holding several references stays one span. In table rows escape the pipe: `[[13.2.3. Blunt Trauma\|Blunt Trauma]]`.
6. By note type: rules notes (`_` suffix) and roll-table notes -> every reference per rule 2; per-entry notes (spells, monsters, items, gods, unique features) -> italic names with notes and page references only. Plural/inflected names may link with the printed word as alias (list them).
7. Ambiguous target, or the target is not in the vault (e.g. a spell name that isn't a note, a printed page that holds only art) -> leave as printed and list it. Never guess: if the printed name doesn't match a note, don't link it to a similar note.

## Output
Edit only your group's notes in `ROOT/work/`. Write `ROOT/reports/<GROUP>.md`: notes changed, link count, page refs consumed, preposition swaps, every reference you left unlinked and why (ambiguous / no target), inflected aliases. Run the checker on your notes until 0 ERROR lines. Reply with counts and 3-5 lines of judgement calls.
