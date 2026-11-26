# Batch C3 report (PDF 57-74: 9. Equipment, 10. Doing Things, 11. Encounters, 12. Combat 12.1-12.5)

All pages 57-74 opened (full page + top/bottom crops in scratch/C3). PDF 70 and 73 are full-page art; no text.

## Notes written (32)

| note | PDF pages |
| --- | --- |
| 9. Equipment/9.1. Equipment_.md (incl. SUPPLY ref-table) | 57 |
| 9. Equipment/9.2. Encumbrance_.md | 57 |
| 9. Equipment/9.3. Common Gear_.md (embeds 9.3.1) | 58 |
| 9. Equipment/9.4. Uncommon Gear_.md | 58 |
| 9. Equipment/9.5. Rare Gear_.md | 58-59 |
| 9. Equipment/9.6. Food & Board_.md | 59 |
| 9. Equipment/9.7. Services_.md | 59 |
| 9. Equipment/9.8. Lifestyle_.md | 59 |
| 9. Equipment/9.9. Weapons_.md (incl. MELEE WEAPONS, RANGED WEAPONS ref-tables) | 60-62 |
| 9. Equipment/9.10. Armour_.md (incl. ARMOUR ref-table) | 63 |
| 9. Equipment/9.11. Shields_.md | 63 |
| 9. Equipment/9.12. Repairs & Crafting_.md | 63 |
| 9. Equipment/9.13. Animals_.md (ref-table only) | 63 |
| 9. Equipment/9.14. Vehicles & Ships_.md (ref-table only) | 63 |
| 9. Equipment/9.15. Masterforged Gear_.md (embeds 9.15.1, 9.15.2) | 64 |
| 10. Doing Things/10.1. Doing Things_.md | 65 |
| 10. Doing Things/10.2. Attribute Checks_.md | 65-66 |
| 10. Doing Things/10.3. Great Success & Terrible Failure_.md (incl. ATT/GS/TF ref-table) | 66 |
| 10. Doing Things/10.4. Opposed Checks_.md | 66 |
| 10. Doing Things/10.5. Group Checks_.md | 67 |
| 10. Doing Things/10.6. Representative Checks_.md | 67 |
| 10. Doing Things/10.7. Retries_.md | 67 |
| 10. Doing Things/10.8. Montages_.md | 67 |
| 10. Doing Things/10.9. Random Checks_.md | 67 |
| 11. Encounters/11.1. Reaction Roll_.md (embeds 11.1.1) | 68 |
| 11. Encounters/11.2. Activity Die_.md (embeds 11.2.1) | 68 |
| 11. Encounters/11.3. Influencing NPCs_.md | 69 |
| 12. Combat/12.1. Initiative & Turn Order_.md | 71 |
| 12. Combat/12.2. Morale_.md | 71 |
| 12. Combat/12.3. Move_.md | 72 |
| 12. Combat/12.4. Party Retreat_.md | 74 |
| 12. Combat/12.5. Chases_.md (embeds 12.5.1; the table on 75-76 ends the section) | 74 |

Every plan row with status phase-C in scope has its note; all `written` table notes are embedded, not copied.

## Plan rows not followed exactly
- **12.1 "### Delay & Ready Action"**: printed as a titled parchment box at the foot of the Initiative column, so written as `> [!note] Delay & Ready Action` (brief: boxes become callouts) instead of a `###` heading.
- **9.9 "### Second Rank Weapons"**: it is a minor (black serif) heading under the red PROPERTIES AND NAT 19S heading, so written as `####` under `### Properties and Nat 19s`.

## Suspected source typos/errors (kept verbatim)
- p58 Common Gear prose: "available in most villages ." (space before the full stop).
- p63 Repairs & Crafting: "might be able perform their own repairs" (missing "to").
- p74 Chases step 1: "until all allies have lead a first leg" (presumably "led").
- p72 Stand Up From Prone / Falling: "Dex (Acrobatics*)" -- an asterisk with no footnote on the page (kept, escaped `\*`).
- p58 Common Gear prose "Arrows typically use Ammo rolls* p.58" -- asterisk kept (escaped); it matches "Arrows (20*)" in the table.

## Judgement calls
- Display headings (all-caps/small-caps in print) written in Title Case as in the plan; the section title bar / first heading is not repeated (filename carries it). Chapter title words (EQUIPMENT, DOING THINGS, ENCOUNTERS, COMBAT) are not written as headings.
- Example boxes -> `> [!example]` (Lothar p60, Lyssa p66 x2, gate guards p69, Giant Rat p72).
- The two untitled parchment boxes holding inline item lists (Uncommon Gear 1-13, Rare Gear "For random items roll 1d20", p58) -> untitled `> [!note]` callouts. The Encumbrance, Food & Board/Services/Lifestyle, and Attribute Checks parchment panels are whole sections with their own notes, so no callout.
- Table title bars -> heading above the table: `#### Supply` (under `### Supply`), `### Melee Weapons`, `### Ranged Weapons`, `### Armour`. Animals and Vehicles & Ships are notes whose only content is the titled table, so the title is the filename and not repeated.
- Melee/Ranged Weapons: the unlabelled number column gets an empty header cell. Rows that print two weapons/numbers stacked ("6 / 7", "Hammer, Heavy / Mace, Heavy") use `<br>`; NAT 19 cells ("1d8+4 / Blade Trauma") joined with a space. In PROPERTIES, `<br>` only where the print deliberately breaks a short line before a new sentence (Hammer/Mace Heavy, Spear, Sword Bastard/Long, Sword Short); other wraps joined.
- Armour table: name/description, supply/cost and AC/penalty print as separate stacked lines in each cell -> `<br>`. Animals/Vehicles: the small roll numbers print inside the TYPE column, kept there; paired values (costs, supply) for merged rows joined with `<br>`.
- ATT/GS/TF (p66): printed as two side-by-side halves (5-12, 13-20) under repeated headers; written as one 3-column table, rows 5-20 in reading order. No title bar printed, so no heading.
- 11.1 includes the "For those times when the GM would prefer a more evenly balanced reaction range..." paragraph (right column, above REACTION table) before the embed, as planned.
- Numbered steps: the print bolds the step number with the label ("**1. Surprise**"); markdown ordered lists cannot bold the marker, so the label alone is bold.
- No icons in the Phase C text of these pages (Activity icons are inside the already-written 11.2.1 table). No hard line breaks used.

## Left out
- Running heads/page numbers, art (p62 lower half, 64 lower half, 65, 66, 67, 68, 69 sides, 70, 73, 74), art credits/signatures.

## Self-check
- Typographic-punctuation grep: nothing found.
- fidelity_check.py (config pointed at out/C3): no emphasis or table-number issues; remaining flags are page numbers, filename-carried headings, embed lines and the two-half ATT table reorder. Token-count comparison of fm pages 57-74 against the notes + embedded tables: only missing words are the headings carried by filenames and the repeated ATT/GS/TF header.
