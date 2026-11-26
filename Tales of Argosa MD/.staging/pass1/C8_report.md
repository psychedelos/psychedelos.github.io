# C8 report -- 17. GM Tools, phase-C notes (PDF 131-157)

## Notes written (5)
All under `Tales of Argosa MD/17. GM Tools/`.

| note | PDF pages | contents |
| --- | --- | --- |
| 17.1. GM Tools_.md | 131 | intro paras, untitled box (3 paras) as `> [!note]`, closing 2 paras |
| 17.2. Diseases & Parasites_.md | 132 (133 opened) | intro 2 paras + embeds 17.2.1, 17.2.2 |
| 17.3. Dungeon Crawling_.md | 134-135 | intro; ### Marching Order; Readied Gear (box -> callout); ### Who's Got the Light?; ### Dead Adventurers + embed 17.3.1; ### Dungeon Events (numbered 1-3) ; #### Consult the Bones; Designer's Thoughts callout; embed 17.3.2 |
| 17.4. Hexploration_.md | 136-141 | intro; ref-tables ### Watches and ### Exploring and Travel; mixed terrain para; ### Injured or Encumbered; Travel Procedure (box -> callout, steps 1-7 with sub-bullets); ### Travel Roles (7 bullets); ### Night Shift + embed 17.4.1; ### Weather + embed 17.4.2; ### Rivers; ### Exploring a Hex + embeds 17.4.3, 17.4.4; ### Random Encounters; ### Starting Distances; ### Back to Base + embed 17.4.5 |
| 17.5. Encounter Tables_.md | 142 (143-157 opened) | intro paragraph + embeds 17.5.1-17.5.12 in print order |

Every page 131-157 was opened (131-142 full page + crops; 143-157 as page grids to confirm they hold only the Phase A tables and art -- no prose, boxes or ref-tables there).

## Plan rows not followed / changes
- None renumbered. `### Consult the Bones` in the plan written as `#### Consult the Bones`: it prints as a small bold serif subhead under the red DUNGEON EVENTS heading (brief: minor headings = ####).
- Plan's "### Readied Gear (boxed)" and "### Travel Procedure (boxed)": each prints with its heading *inside* a parchment box, so per the brief they are callouts `> [!note] Readied Gear` / `> [!note] Travel Procedure` in their reading-flow position (not ### headings). They therefore do not appear in the Obsidian outline.
- Random Encounters (PDF 141, printed in the black-box section-title style like DUNGEON CRAWLING) kept as `###` inside 17.4 per plan; Starting Distances and Back to Base also `###` (siblings), per plan.

## Judgement calls
- p131 box has no printed title -> `> [!note]` with no title.
- Watches ref-table: header `|  | DAY SHIFT |  | NIGHT SHIFT |` (number column, then name+hours column per shift); name and hours joined with a space (`**Morning** 6am - 10am`). Exploring and Travel prints no column titles -> empty header cells.
- Table title bars (Watches, Exploring and Travel) became `###` because they sit directly under the section intro.
- Travel Procedure: printed bold step labels "**1. New Day**" written as Markdown ordered list `1. **New Day** ...` (the list marker cannot carry bold). Sub-diamonds under steps 4 and 6 are nested `-` bullets.
- Travel Roles: each role name prints on its own line above its description -> `- **Look Out**` + hard line break + indented paragraph (7 hard breaks). Guide's second paragraph ("Tracking a quarry ...") is an indented paragraph inside the Guide bullet.
- Embed placement follows printed column order: on p135 the Dungeon Event table (right column) is embedded after the Designer's Thoughts box (bottom of left column); on p138 Weather Shift after the Weather para, Exploring after Exploring a Hex, Travel Events (full-width, 138-140) after that; Fortune Die Examples after Night Shift (p137 bottom right).
- Bold spans broken by a line end in the text layer were merged where the image shows continuous bold (e.g. `**Int (Apoth\*) Great Success**`, `**Int or Perc (Wilderness Lore\*)**`, `**random encounters are "unbalanced" by design**`, `**night shift**`).
- Literal asterisks escaped (`Lore\*`, `Stealth\*`, `Apoth\*`).
- Page refs kept verbatim, incl. unparenthesised ones: "**light sources** p.55", "*Monster by HD* chart p.167".

## Suspected source typos / oddities (kept verbatim)
- p134: "there's a few things the GM and party should consider" (there are) -- minor.
- p141: "a series of tables ... adventurers are limited by their torches, lantern, etc" (lanterns) -- minor.
No other errors found in the prose of 131-142.

## Fidelity check
`fidelity_check.py` on the 5 notes: no emphasis or word issues in the prose; only expected noise (embed lines not in text layer, section titles carried by filenames, embedded table text absent from the note, ref-table reordering). Typographic-punctuation grep clean.

## Left out
Running heads, page numbers, art. The display-size section titles (GM TOOLS, DISEASES & PARASITES, DUNGEON CRAWLING, HEXPLORATION, ENCOUNTER TABLES) are carried by the filenames. No icons in this range.
