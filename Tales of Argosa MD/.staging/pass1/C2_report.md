# C2 report -- PDF 32-56 (5. Classes Fighter-Rogue, 6. Party Bonds, 7. Unique Features, 8. Skills & Rerolls)

## Notes written (50)
All paths under `Tales of Argosa MD/`.

| note | PDF pages |
| --- | --- |
| 5. Classes/5.6. Fighter_.md (incl. Fighter Attack Bonus & Abilities ref-table; embeds 5.6.1) | 32-34 |
| 5. Classes/5.7. Magic User_.md (incl. Magic User Attack Bonus & Abilities ref-table) | 35-36 |
| 5. Classes/5.8. Monk_.md (incl. Monk Attack Bonus & Abilities ref-table; embeds 5.8.1) | 37-39 |
| 5. Classes/5.9. Ranger_.md (incl. Ranger Attack Bonus & Abilities ref-table, Wolf/Viper/Owl stat blocks; embeds 5.9.1) | 40-42 |
| 5. Classes/5.10. Rogue_.md (incl. Rogue Attack Bonus & Abilities ref-table; embeds 5.10.1) | 43-45 |
| 6. Party Bonds/6.1. Party Bonds_.md (embeds 6.1.1) | 46 |
| 7. Unique Features/7.1. Unique Features_.md | 47 |
| 7. Unique Features/7.2. Example Unique Features/ -- 41 entry notes, exactly the plan's filenames (Pilfer Pouch embeds `Pilfer Pouch - d100 Table`) | 47-52 |
| 8. Skills & Rerolls/8.1. Skills_.md (incl. SKILLS ref-table, p55) | 54-55 |
| 8. Skills & Rerolls/8.2. Rerolls_.md (incl. REROLLS ref-table) | 54 |

Every page 32-56 was opened as an image (art pages 53 and 56: no text, nothing written). `fidelity_check.py` run on all 50 notes: the only flags are the embedded roll-table lists (expected -- rows live in the Phase A notes), page numbers, the embed lines themselves, and the Rerolls table that p054.md reads after "Backgrounds" (placed by the image, after the Rerolls intro). 0 emphasis issues in the transcribed text. No typographic punctuation. Hard line breaks are present in the class stat-label blocks.

## Plan rows not followed
None. All phase-C rows in scope have their note; folder and art rows need no note.

## Judgement calls
- **Class header labels** (Key Attribute(s), Hit Points, Weapons, Armour & Shields, Class Starting Gear, Skills): printed as small black bold labels with the value on the next line. I wrote them as `**Label**` + hard line break + value (not headings), since they sit above the first red heading and a `####` would skip a level. Class Starting Gear keeps its two printed lines (hard break) where the print sets two lines.
- **Magic User "Spellbook"**: same black-bold style but sits under the red SPELLCRAFT heading, so it became `#### Spellbook`.
- **Display headings** (Estus font, all-caps in print, mixed case in the text layer like "Deadly StrikeS") written in Title Case: `### Deadly Strikes`, `### Beyond 9th Level`, `### Relevant vs Required` (the print has lower-case "vs").
- **Attack Bonus tables**: title bar -> `### <Class> Attack Bonus & Abilities`; 9 printed columns `LEVEL | AB | ABILITY` x3; two-line cells joined with a space ("Adaptable, Deadly Strikes"); "**Level N**" kept bold as the font shows.
- **Kruncor example box** (Fighter, p33): untitled box -> `> [!example]`.
- **Beast Companion stat blocks** (Ranger, p41): printed in an untitled box -> `> [!example]` (the text calls them "examples"), one paragraph per beast, emphasis from the font data; the Reac lines stay inline as printed.
- **Designer's Thoughts** (p54) -> `> [!note] Designer's Thoughts`, placed at the end of the Skills material (before the SKILLS table), where it sits in the left column.
- **SKILLS table** title "SKILLS" kept as `### Skills` even though the note's filename is Skills (it is the table's own title bar). **REROLLS table** has no printed column titles -> empty header row; title bar -> `### Rerolls`.
- **Unique Feature tier tables**: no printed column titles -> empty header row, tier numbers bold as printed (`**1**`). Untiered UFs are plain paragraphs. Poisoner keeps its two printed paragraphs.
- **Rogue**: the "Generally speaking..." paragraph follows the Tricks & Techniques embed, as printed.
- Line-split italic/bold runs were re-joined into one run (e.g. `**one use of this ability per level.**`, `*Gaze of Beguilement*`, `*Dire Wolf, Griffon, Giant Lizard*,`, `**Int (Arcane Lore\*)**`).
- Literal asterisks escaped: `Int (Arcane Lore\*)` (Magic User, Runesmith), `Int (Apothecary\*)` (Skills).

## Suspected source typos/errors (kept verbatim)
- PDF 32 Fighter Skills: "(vii) General Lore (viii) Persuasion, (ix) Watercraft (x) Stealth" -- missing commas after "General Lore" and "Watercraft". Similar missing commas in the Magic User (PDF 35: "(ii) Deception (iii)", "(vi) General Lore (vii)", "(viii) Watercraft (ix)") and Ranger (PDF 40: "(ix) Watercraft (x)") skill lists.
- PDF 40 Ranger: "a brave woodsmen" (singular article + plural noun).
- PDF 41 Ranger Wolf: "extra +1 to attack when outnumber foe".
- PDF 41 Rangercraft intro: "Traveling" (US spelling in a UK-spelling book).
- PDF 43 Rogue table: Level 5 lists "Backstab Boost", which has no heading of its own (it is the 5th-level line in Backstab).
- PDF 48 Born to Loot 2: "an Int (Perception) check" (already reported by A1).
- PDF 49 "INJURY ADAPTION" (Adaptation?) and "MONK TECHNIQUES (CROSS CLASS)" spelled differently from the other "(CROSSCLASS)" headings -- filenames follow the plan.
- PDF 54 Rerolls: "only one of the results are rerolled"; Backgrounds: "identify weak points on rooftop".
- PDF 55 Skills table: "Specialized" (US spelling).
- Class notes say "See p.15 and 45." -- printed p.15 is PDF 17 (Classes) and p.45 is PDF 47 (Unique Features); correct, kept verbatim.

## Text-layer glitches fixed from the image
- p052.md "THIEVES ' GRACE" -> filename already "Thieves' Grace" (plan); no heading written (filename carries it).

## Left out
- Running heads, page numbers, art, art credits; the Party Bonds art captions ("Caravan Attack", "Prison Cell Mates", "Muscle for Crime Boss") are illustration labels, per the plan.
- Entry headings of the UF boxes are not repeated inside the notes (the filename carries them).

## Icons
None.
