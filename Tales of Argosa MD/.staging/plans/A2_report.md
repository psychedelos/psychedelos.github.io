# Batch A2 report (PDF 57-92: chapters 9-14)

## Table notes written (12)

| note | PDF pages | die header | inferred? |
| --- | --- | --- | --- |
| 9. Equipment/9.3.1. Common Gear.md | 58 | d66 | inferred (11-66 numbering; no die printed) |
| 9. Equipment/9.15.1. Masterforged Weapon.md | 64 | d8 | inferred (entries 1-2 ... 8; no die printed) |
| 9. Equipment/9.15.2. Masterforged Armour.md | 64 | d6 | inferred (entries 1-6; no die printed) |
| 11. Encounters/11.1.1. Reaction.md | 68 | 2d6 | from prose ("roll 2d6", p.68) |
| 11. Encounters/11.2.1. Activity.md | 68 | d6 | from prose ("Activity Die ... d6") |
| 12. Combat/12.5.1. Chase Events.md | 75-76 | d20 | from prose ("rolls 1d20 on the Chase Event table", p.74) |
| 13. Injury & Death/13.1.1. Injuries & Setbacks.md | 85-86 | d20 | from prose ("1d20 roll on the Injuries & Setbacks table") |
| 13. Injury & Death/13.2.1. Blade Trauma.md | 86-87 | d12 | copied byte-for-byte from samples/ |
| 13. Injury & Death/13.2.2. Blast Trauma.md | 87 | d12 | inferred: prose says "Rolls tend to vary from 1d6 to 1d12 depending on the attack"; entries run 1-12 |
| 13. Injury & Death/13.2.3. Blunt Trauma.md | 87-88 | d12 | from prose ("Roll 1d12") |
| 13. Injury & Death/13.2.4. Missile Trauma.md | 88-89 | d12 | from prose ("Roll 1d12") |
| 13. Injury & Death/13.2.5. Toxin Trauma.md | 89 | d12 | from prose ("Roll 1d12") |

Every row was checked against the page image (crops in scratch/A2). Trauma/Injuries tables continue across columns/pages (Blade 9 on p86, 10-12 on p87; Blunt 1-4 p87, 5-12 p88; Missile 1-9 p88, 10-12 p89; Injuries 1-12 p85, 13-20 p86) and were joined into one table each in roll order. gmscripts fidelity_check: no word/emphasis/number issues other than the bracketed icon words and inter-row source text from facing columns (expected). table_check flags were all checked by eye: they come from identical text repeated in several tables ("Damaged Gear", the severed-limb rows) and from the icon words; no real misplacements. Typographic-punctuation grep: nothing found.

## Possible roll tables left as ref-tables / prose (Phase C) -- please confirm
- **Melee Weapons (p61, numbered 1-20 + "-" Lance), Ranged Weapons (p62, 1-6), Animals (p63, 1-8), Vehicles & Ships (p63, 1-8)**: each has a leading number column usable as a random roll (d20/d6/d8; merged rows like "6 7 Great Axe, Great Sword"). Treated as ref-tables as the batch notes say (weapon/gear/price lists), inside their rules notes. If Max wants them rollable, they can be promoted later.
- **Common Gear (p58)** is also a gear list, but it is numbered purely as a d66 with no cost/stat columns, so I treated it as a roll table (9.3.1). Judgement call against the batch note's "gear lists are ref-tables".
- Inline roll lists printed in prose, not set as tables (left in their rules notes): Rare Gear "For random items roll 1d20: 1 Acid, 2-3 Antitoxin ..." (p58); Uncommon Gear numbered list 1-13 with no die named (p58); "For random armour roll 1d6: 1-2 Light, 3 Medium, 4 Heavy, 5-6 Shield" (p63); Minor Exploits "For random NPC exploits, roll 1d6: (i) Grab ... (vi) Blind" (p80). Special Metals 1-4 (p60) is a numbered list, not rolled.
- Non-roll reference tables: Supply (p57), Armour (p63), ATT/GS/TF (p66), Melee Modifiers and Ranged Modifiers (p79).

## Suspected source typos/errors (kept verbatim)
- p58 Common Gear: two rows numbered **44** ("44 Pickaxe", "44 Pole, 10 ft"); 45 is missing -- "Pole, 10 ft" is presumably 45. Both rows kept as printed.
- p75 Chase Events #5(i): "makes a Perc (Det) check to notice to loss" (presumably "the loss").
- p76 Chase Events #15: "split themselves.This may require" -- no space after the full stop (visible on the image too).
- p88 Blunt Trauma #6: "3d6 days of rest mends the injury" -- no final full stop.
- p89 Toxin Trauma #3: "pre occupation" (line-end split with no hyphen on the image; kept as two words, consistent with the book's "non functional", "self heal").
- Inconsistent colon in limb sub-rolls, as printed: "1-3 hand, 4-5: below elbow" vs "1-3: foot, 4-5: below knee" (Injuries #18, Blast #10, Blunt #10, Missile #10, and Blade #10 in the sample). Blast #11 prints "1d6: 1-3: foot" without "Roll".
- p63 Animals "Snake (poison #1 p.226)" and p61 Lance "(Blade Trauma #3)" -- fine, noted only for later linking.

## Judgement calls
- **Masterforged Weapon/Armour**: the name is printed in its own column (bold) separate from the effect, unlike the trauma tables, so these notes use three columns (`| d8 | | |`), with empty header cells as nothing is printed.
- **Activity**: printed column titles kept (STATUS / INTELLIGENT CREATURE / OTHER CREATURES); the STATUS header covers the number column too, so the roll column header is `d6` and STATUS is the second column.
- **Chase Events #5**: the "Roll 1d6:" sub-list i-vi is joined with `<br>` inside the row (its own printed list).
- **Combat section names**: PDF 79 has no title bar (it follows ACTION). I named the note `12.7. Melee & Ranged Attacks_` (from its first two headings) covering Melee Attacks, Ranged Attacks, Damage, Critical Hits, Fumbles, Nat 19s, Dodge and both modifier tables. Rescues kept inside `12.8. Exploits_` (the book calls them Rescue Exploits). Charge/Intercept/Withdrawing/Stand Up/Blocking/Falling kept as `###` inside `12.3. Move_` (MOVE title bar).
- **Equipment**: Animals and Vehicles & Ships have title bars but no prose; each gets a small rules note holding its ref-table (`9.13.`, `9.14.`), in printed order (Animals above Vehicles & Ships on p63; the text layer has them reversed).
- **Reaction**: the paragraph "For those times when the GM would prefer a more evenly balanced reaction range, use the below chart..." sits under the Activity Die prose but introduces the REACTION table; planned for 11.1. Reaction Roll_.
- Roll numbers are bold in print but written plain, matching the approved sample.

## Icons replaced by words
- 11.2.1. Activity: STATUS cells carry the Activity Die icons, which the prose refers to ("see icons below"): `[dagger icon]` (Threat), `[group of people icon]` (Socialising), `[drumstick icon]` (Eating), `[shovel icon]` (Working), `[footprint icon]` (Traveling), `[campfire icon]` (Resting).

## Chapter boundaries
All as in BRIEF: Equipment 57-64, Doing Things 65-67, Encounters 68-70 (70 = art), Combat 71-84, Injury & Death 85-90 (90 = art), Healing & Recovery 91-92 (92 = art). No corrections. Chapters 10 and 14 have no roll tables, so their folders are not created in out/A2 (Phase C only).
