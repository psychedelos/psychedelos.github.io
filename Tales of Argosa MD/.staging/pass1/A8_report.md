# A8 report -- PDF 210-230 (22. Naval Combat, 23. Oracle Tools, 24. Rival Adventurers, 25. Solo Rules, 26. Traps)

39 table notes written. Every table page was opened as an image (210-213, 216-217, 220-229); 214-215, 218-219, 224 and 230 were also viewed (prose/art). Self-checks: roll ranges cover each die with no gaps/duplicates; typographic-punctuation grep finds nothing; `gmscripts/fidelity_check.py` and `table_check.py` were run (configs/outputs in `scratch/A8/`). Their flags were all false positives: the die header, the title in the filename, prose next to the table, side-by-side halves read across columns, and repeated phrases (Mast/Main Sails, Drowning Moderate/Major). There are no word or emphasis mismatches.

## Table notes (path <- PDF page, die header)
22. Naval Combat/
- 22.3.1. Artillery <- 211, d20 (prose "Roll 1d20 for each Artillery strike")
- 22.5.1. Boarding <- 212-213 (rows 1-12 p212, 13-20 p213), d20 (prose: 1d20 above deck / 1d10 below)
- 22.5.2. Crew vs Crew <- 213, 2d6 (prose "2d6 roll")

25. Solo Rules/ (Dungeon Generator)
- 25.4.1. Dungeon Site <- 220, d20
- 25.4.2. Size <- 220, d20
- 25.4.3. Objective <- 220, d6 + printed column titles TASK / THING
- 25.4.4. Reward <- 220, d20
- 25.4.5. Main Opposition <- 221, d20
- 25.4.6. Special Leader <- 221, d20
- 25.4.7. Doors <- 222, d20
- 25.4.8. Rooms & Corridors <- 222, d20
- 25.4.9. Room Theme <- 222, d20
- 25.4.10. Room Contents <- 222, d20
- 25.4.11. Theme Items <- 223, header `| | d20 |` (see judgement calls)
- 25.4.12. Complications <- 223, d20

26. Traps/ (all under 26.4. Simple Traps_)
- 26.4.1. Danger Level <- 225, 2d6
- 26.4.2. Triggers & Counters <- 225, 2d6 + printed TRIGGER / COUNTER
- 26.4.3. Mode of Attack <- 225, d20 (prose: 1d8 containers / 1d20 spaces)
- 26.4.4. Bypasses <- 226, 2d6
- 26.4.5. Acid, 26.4.6. Alarm, 26.4.7. Arrows, Darts <- 226
- 26.4.8. Crushing Walls, 26.4.9. Deadfall, 26.4.10. Drowning, 26.4.11. Fire, Explosion, 26.4.12. Gas, 26.4.13. Lockdown <- 227
- 26.4.14. Magic <- 228, d12 (prose "For completely random roll 1d12")
- 26.4.15. Monster, 26.4.16. Needle, 26.4.17. Pit <- 228
- 26.4.18. Poison <- 228, d20 (prose "Random Poison 1d20")
- 26.4.19. Relocation, 26.4.20. Rolling Boulder, 26.4.21. Scything Blades, 26.4.22. Self Destruct, 26.4.23. Snare, 26.4.24. Spear, Spikes <- 229

The 20 attack-mode tables (Acid ... Spear, Spikes) are keyed Minor / Moderate / Major / Counter. They use the result band of the 2d6 Danger Level roll, not a die of their own. Both header cells are empty because nothing is printed there.

## Unsure whether roll tables
- **Ships** (p210) and **Blackpowder Weapons** (p213) have numbered rows (1-8 and 1-4), so they could be rolled with a d8/d4. No prose says to roll on them, and the brief names ship stat lists and weapon lists as ref-tables, so I left them for Phase C as ref-tables. Easy to promote if Max wants them rollable.
- **Rival Adventurers** class table (p216-217): stat lookup, not rolled. ref-table.
- **Cost** (Purchasing Traps, p226): price list by danger level. ref-table inside 26.4. Simple Traps_, even though the batch note says "every trap table".
- **Read the Signs -- Time** (p215: Light Sun = Morning, etc.): keyed by a drawn card, not a die. Left in rules note 23.3.
- 23. Oracle Tools and 24. Rival Adventurers have **no roll tables**.

## Judgement calls
- Side-by-side halves were merged into one table in roll order: Dungeon Site, Size, Reward, Main Opposition, Special Leader, Doors, Rooms & Corridors, Room Theme, Mode of Attack, Magic, Poison. Boarding continues across two pages and was also joined.
- Objective prints two parallel 1d6 columns ("Roll 1d6 twice"), each with its own repeated 1-6 numbers. I made them one table, `| d6 | TASK | THING |`.
- Theme Items is keyed by the Room Theme name, with d20 sub-ranges inline in each cell. The first column holds the theme name (bold, as printed) and the second the inline rolls. The header `| | d20 |` comes from the lead-in "roll 1d20 below". The "\*Also roll ..." footnote lines in Power/Respect/Awe and Valuables start on their own printed line, so I joined them with `<br>`. In Secure the footnote is printed inline, so it stays inline.
- Triggers & Counters: the title bar prints only the column titles TRIGGER / COUNTER. I took the filename from the section heading "Triggers & Counters".
- Danger Level has no title bar (a one-row strip under the DANGER LEVEL heading). I named it after that heading.
- Crew vs Crew is a minor heading inside the boarding flow, so its prose goes in 22.5. Boarding_ as `###` and the table is 22.5.2.
- Bypasses and Purchasing Traps are headings in the same style as Danger Level etc. under the SIMPLE TRAPS banner, so every Simple Traps table is numbered 26.4.x in book order (left column, then right, page by page). The trap-mode tables are therefore not alphabetical across pages (Arrows, Darts comes before Crushing Walls; Magic/Monster/Needle before Pit/Poison).
- Italic spans broken across printed lines were rejoined into one span (e.g. `*Glimpse the True Gods*`, `*Injuries & Setbacks*`, `*Gelatinous Cube*`). Emphasis was otherwise kept exactly as in pNNN.md, including trailing punctuation inside spans (`*Burning,*`, `*Silent Shroud.*`, `**1d12.**`).
- Double spaces in the source (Pit Minor "(Close).  *Luck*", Secure "Ward*.   *Also") were collapsed to one.

## Suspected source typos / errors (left as printed)
- p223 Theme Items "Secret" row: "Concealed **1-3** Info **4-9** Valuables B **10-13** Minor Magical Item, **14-17** Door **18-20** Special." It looks like "Concealed Door" (14-17) was split by layout, with "Concealed" pushed to the start of the cell. It is transcribed as printed.
- p227 Gas: "Poison p.222" (all three rows). Printed p.222 is the Traps opener; the Poison table is on printed p.226. The page reference looks wrong.
- p227 Drowning Major: "...before the room seals" has no final period. p227 Gas Major: "Poison p.222" has no final period. p228 Needle Minor: "(1d12)" has no period. p228 Pit Major: "(50/50)" has no period.
- p213 Boarding 17: "weighed net" (weighted?). p213 Boarding 20 ends without a period.
- p225 Triggers & Counters, p217 Rival Adventurers, p216 Cultist: "Sever Arcarnum". It is consistent across the book, so it may be the real spell name; check against chapter 15.
- Prose (Phase C, not in notes): p210 "Navel Combat", "may may result"; p212 "To reflect his"; p215 "The cards also includes".
- p220 Reward 7-8 "Gemstones Valuables B #61": transcribed as printed (it refers to a Valuables B entry).

## Icons replaced by words
- None in the table notes. Phase C will meet icons on p214 (Yes/No rune glyphs, Fortune sun and Misfortune skull) and p218 (Lone Wolf Fortune-die sun/skull). The text layer has only blanks there.

## Chapter boundaries
- All chapter boundaries match the brief. PDF 219 (printed 217) is a full-page illustration inside Solo Rules. PDF 230 (printed 228) is a full-page illustration (treasure hoard) at the end of the Traps range; it is listed as `art` in Traps, though it may visually open 27. Treasure.

## Possible memory note
- None.
