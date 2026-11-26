# C12 report -- PDF 210-230 (22. Naval Combat, 23. Oracle Tools, 24. Rival Adventurers, 25. Solo Rules, 26. Traps)

19 rules notes written (every phase-C row and all 4 ref-tables in A8's plan). Every page 210-230 was opened as an image (half-page crops, plus zooms of the p214 icons); 219 and 230 are full-page art with no text. Self-checks: the typographic-punctuation grep finds nothing. All 39 embed targets exist in `merged/`. `gmscripts/fidelity_check.py` was run (config/output in `scratch/C12/`). Its flags are expected noise only: embedded tables counted as missing text, the bracketed icon words, section titles carried by filenames, the repeated header on p217, and the card-diagram description. There are no real word or emphasis mismatches. No hard line breaks were used.

## Notes written (path <- PDF pages)
22. Naval Combat/
- 22.1. Naval Combat_ <- 210
- 22.2. Ships_ <- 210 (prose + `### Ships` ref-table)
- 22.3. Artillery_ <- 210-211 (prose, embed 22.3.1, `### Repairs`)
- 22.4. Ramming_ <- 212
- 22.5. Boarding_ <- 212-213 (prose, embed 22.5.1, `### Crew vs Crew` prose p213, embed 22.5.2)
- 22.6. Withdrawing_ <- 212
- 22.7. Blackpowder Weapons_ <- 213 (ref-table only)

23. Oracle Tools/
- 23.1. Oracle Tools_ <- 214
- 23.2. Consult the Bones_ <- 214
- 23.3. Read the Signs_ <- 215

24. Rival Adventurers/
- 24.1. Rival Adventurers_ <- 216-217 (prose + class ref-table, p216 and p217 joined into one table)

25. Solo Rules/
- 25.1. Solo Rules_ <- 218
- 25.2. Lone Wolf_ <- 218
- 25.3. Published Adventures_ <- 218
- 25.4. Dungeon Generator_ <- 220-223 (prose + embeds 25.4.1-25.4.12 where each table prints)

26. Traps/
- 26.1. Traps_ <- 224 (### Simple vs Complex / Mechanical vs Magical / Rarity)
- 26.2. Where & How_ <- 224
- 26.3. Three Second Trigger_ <- 224 (Designer's Thoughts callout)
- 26.4. Simple Traps_ <- 225-229 (### Danger Level, Triggers & Counters, Mode of Attack, Bypasses, Purchasing Traps + `#### Cost` ref-table; embeds 26.4.1-26.4.24; Magic and Poison roll lead-ins on p228)

## Plan rows not followed
- None. All filenames and numbering are as planned.

## Judgement calls
- **Icons** (none of them are in the text layer):
  - p214 Judgment and Twins dice: Yes/No glyphs written as `[Yes rune icon]` / `[No rune icon]`. The two dice use different rune shapes, but both are written the same way.
  - p214 and p218 Fortune die: `[sun icon]` / `[skull icon]`.
  - p214 "Fortune [sun icon], Misfortune": the text layer has a comma here that the icon hides in the image. I kept it.
- **p215 labelled card diagram:** written as one bracketed description line at the end of 23.3. It names the printed labels (bold, as in the font data) and the card words they point to (REBEL / direction arrow / DEFYING / sun / OUTSPOKEN / UNSTABLE). It is not a table or a heading, because the page prints neither.
- **Numbered lists:** the font data bolds the number together with the label (`**1. Artillery**`). In markdown the list marker is plain: `1. **Artillery** ...`. The same applies in 22.1, 26.1, 26.2, 26.3 and 26.4.
- **Ships table:**
  - The first column (row numbers 1-8) has no printed title, so its header is empty.
  - In the NAME cells the ship name and its smaller type line (e.g. Rowboat) are separate printed elements, joined as `**Skiff**<br>Rowboat`.
  - In the CREW cells the two bold lines are merged into one span: `**1d4 (1-6)**`.
  - The header "COST (sp)" is joined onto one line.
- **Blackpowder Weapons:** the title bar is the note title, so no heading is repeated. The row-number column header is empty.
- **Rival Adventurers table:**
  - The p217 repeat of the header row is dropped (one table).
  - Each class takes 3 rows. The class cell (bold name + stat lines, joined with `<br>` because they are separate printed lines) sits in the first row, and the class cell is empty in rows 2-3.
  - Headers are uppercase as the image shows. The text layer has mixed case ("claSS lvl").
  - "MAGIC USER" is printed over two lines and joined.
- **Example boxes:** p214 (Urgot) and p215 (Thuel tribe) are untitled boxes, written as `> [!example]` and placed where they sit in the column flow.
- **26.4 order:** this follows the print column order:
  - After `### Purchasing Traps` and its `#### Cost` table come the trap-mode embeds Acid ... Spear, Spikes. These have no heading of their own, so in the outline they fall under the Purchasing Traps heading.
  - The Magic lead-in (p228) comes right before the Magic embed. The Poison lead-in comes after Pit and before the Poison embed, as printed.
  - If Max prefers, the 20 mode embeds could move up under `### Mode of Attack`.
- **Cost table:** a `####` heading (title bar "COST") under `### Purchasing Traps`. No column titles are printed, so the header cells are empty, matching how A8 handled the trap tables.
- **Crew vs Crew** (black minor heading, p213): goes in 22.5 as `###`, as the plan says, even though it prints after WITHDRAWING (22.6).
- **25.4:** the bullets under "Roll 1d20 for a room's contents." print between that lead-in and the ROOM CONTENTS table, so the embed follows the bullets. In the same way, the Rooms & Corridors embed comes before its bullets.

## Suspected source typos / errors (left as printed)
- p210 "**Navel Combat** is divided" (Naval).
- p210 "between ship statistics may **may result in modifiers**" (doubled "may").
- p212 "To reflect his, **one PC** rolls" (this).
- p215 "The cards also includes a small **compass symbol**".
- p218 "light sleeper, etc).This is a bonus Travel Role" (missing space after the period).
- p220 "Alternatively, to **create a map** as you go see p.220" (no final period).
- p222 "place **secret door** or hatch" (missing "a").
- p216/217 "*Sever Arcarnum*" (also in the Phase A tables, consistently spelled; check against chapter 15).
- p224 "everyone at the table gets to linger" / "squees of delight": as printed, not an error.

## Left out
- Running heads, page numbers, art and art signatures. This includes the full-page art on p219 and p230, the p221 card-fan art (its card words ALIEN / CULTIST / PREACH... / MUTANT / CHANGING are illustration only), and the p215 illustration apart from the labelled card.
- p216: a stray "WEAPON" token at the top of p216.md is not visible on the page (hidden text-layer residue). Omitted.

## Possible memory note
- None.
