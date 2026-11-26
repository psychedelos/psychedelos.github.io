# A5a report -- 17. GM Tools 17.1-17.4 (PDF 131-141)

## Table notes written (9)
All under `Tales of Argosa MD/17. GM Tools/`. Every row was checked against the page image (p132-141 all opened).

| note | PDF pages | die header | source of die |
| --- | --- | --- | --- |
| 17.2.1. Diseases.md | 132-133 | d12 | printed ("roll 1d12", p132) |
| 17.2.2. Parasites.md | 133 | d3 | **inferred** (3 entries, no die printed) |
| 17.3.1. Fancy Meeting You Here.md | 134 | d6 | printed ("roll 1d6") |
| 17.3.2. Dungeon Event.md | 135 | 2d6 | printed ("roll 2d6"); rows 2-3, 4, 5, 6-8, 9, 10, 11-12 |
| 17.4.1. Fortune Die Examples.md | 137 | d8 | **inferred** (8 numbered entries) |
| 17.4.2. Weather Shift.md | 138 | d12 | printed ("modified each day by 1d12") |
| 17.4.3. Exploring.md | 138 | d20 | printed ("roll 1d20", Exploring a Hex) |
| 17.4.4. Travel Events.md | 138-140 | d20 | printed ("roll 1d20", Travel Procedure step 5, p136) |
| 17.4.5. Back to Base.md | 141 | 2d6 | printed ("roll 2d6"); rows 2, 3-4, 5, 6, 7, 8, 9, 10, 11-12 |

Self-check: roll ranges cover each die with no gaps/duplicates; emphasis markers balanced; no typographic punctuation (grep clean).

## Unsure whether roll tables
- **Fortune Die Examples** (p137): a numbered 1-8 list of example Fortune results (with "Use the opposite for Misfortunes"); not explicitly rolled, but numbered like a d8 table, so written as a table note (d8 inferred).
- **Watches** (p136): numbered 1-6 (Day Shift 1-3, Night Shift 4-6) but these are watch ordinals, not roll results -> treated as ref-table inside 17.4. Hexploration_.
- **Exploring and Travel** (p136): watch-cost reference -> ref-table.
- Small inline rolls inside prose/cells (Travel Roles Guide "roll 1d6 for direction", Back to Base 8 "Roll 1d6 (i-ii)...") stay inline.

## Judgement calls
- **Travel Events** (d20, three columns OVERLAND / UNDERGROUND / VOYAGE): many rows print one cell spanning all three columns (2-5, 7-9, 11, 12, 14-17, 19), and rows 6 and 20 print one cell spanning OVERLAND+UNDERGROUND with a separate VOYAGE cell. Markdown has no colspan, so the spanning text is **repeated in every column it spans** (no words added). Row 1 VOYAGE's own (i)-(vi) list is joined with `<br>`.
- **Fortune Die Examples** caption "Use the opposite for Misfortunes" (printed bold in the title bar) kept as a bold line above the table.
- Two-half tables (Weather Shift 1-6/7-12, Exploring 1-10/11-20, Fortune 1-4/5-8) merged into one table in roll order.
- Diseases continues from p132 (rows 1-7) to p133 left column (rows 8-12); the p133 text layer interleaves Parasites 1-3 before Diseases 8-12 -- placed by image.
- Literal skill asterisks escaped (`Apothecary\*`, `Lore\*`, `Watercraft\*`).
- Random Encounters (PDF 141, big heading) kept as a `###` inside 17.4. Hexploration_ per the batch row (no 17.5+); Starting Distances and Back to Base likewise.

## Formatting not representable
- p140 Travel Events row 20 (Perfect Campsite): the word "or" in "one *Reroll*, or one point of *Luck*" is **underlined** in print; written plain.

## Suspected source typos / oddities (kept verbatim)
- p133 Greyscale Blight: "chaffing feet" (chafing).
- p133 Slough Pox: "(patients as Str zero die)" (at).
- p133 Throat leeches: "vocal chords" (cords); entry name "Throat leeches" lowercase l unlike the other entries.
- p139 Travel Events 4: "ill fated prophesy" (prophecy).
- p140 Travel Events 16: "one of the Lair's outer sentries have detected" (has).
- p141 Back to Base 6: "which ever occurs first" (whichever).

## Icons
None in the tables of this range.

## Chapter boundaries
GM Tools starts on PDF 131 as planned (PDF 130 is a full-page art plate ending ch. 16). 17.4 Hexploration runs 136-141; Encounter Tables start on 142 (A5b). No corrections.
