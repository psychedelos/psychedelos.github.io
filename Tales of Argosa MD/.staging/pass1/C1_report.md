# C1 report -- PDF 6-31 (chapters 1-4, chapter 5 up to and including the Cultist)

## Notes written (18)
All paths under `Tales of Argosa MD/`.

| note | PDF pages |
| --- | --- |
| 1. What Is Tales of Argosa/1.1. What Is Tales of Argosa_.md | 6 |
| 1. What Is Tales of Argosa/1.2. Core Features_.md | 7 |
| 1. What Is Tales of Argosa/1.3. How to Play_.md | 8-9 |
| 2. Character Creation/2.1. Character Creation_.md | 10 (embeds 2.1.1. Backgrounds) |
| 3. Attributes/3.1. Attributes_.md | 13 (incl. ref-table Attribute Modifiers) |
| 3. Attributes/3.2. Luck_.md | 14 |
| 4. Races/4.1. Races_.md | 15-16 |
| 5. Classes/5.1. Classes_.md | 17 |
| 5. Classes/5.2. Artificer_.md | 18-21 (incl. ref-table; embeds 5.2.1, 5.2.2) |
| 5. Classes/5.3. Barbarian_.md | 22-23 (incl. ref-table) |
| 5. Classes/5.4. Bard_.md | 24-25 (incl. ref-table) |
| 5. Classes/5.5. Cultist_.md | 26-28 (incl. ref-table; embeds 5.5.1, 5.5.2; Tenets & Favour; Example Gods intro) |
| 5. Classes/5.5. Example Gods/Argona (The Starmaiden).md | 28 |
| 5. Classes/5.5. Example Gods/Baal (Lord of Crows).md | 28-29 |
| 5. Classes/5.5. Example Gods/Graxus (The Iron God).md | 29 |
| 5. Classes/5.5. Example Gods/Shennog.md | 29-30 |
| 5. Classes/5.5. Example Gods/Soliri (The World Tree).md | 30 |
| 5. Classes/5.5. Example Gods/Wodon.md | 30 |

Every page 6-31 was opened as an image (12 and 31 are full-page art with no text; 11 is the rest of the Backgrounds table, already written in Phase A). Every note was machine-checked word by word against its pNNN.md (only differences: heading case, the known glyph glitches below, and table rows that are embedded rather than copied) and emphasis was checked word by word (only differences: bold list numerals, the bold table header row, and the Barbarian source's unescaped `AC*` asterisk). No typographic punctuation. Hard line breaks are used only in the class stat blocks (label + value) and survived.

## Plan rows not followed
None. All phase-C rows in scope have notes; all six god filenames are the plan's (the book prints "Argona (the Starmaiden)" with lower-case "the"; the plan's "The" was kept).

## Suspected source typos/errors (not fixed)
- PDF 8: "pain... <the GM rolls a Dex check, which fails> .., and he topples" -- the stray ".." is printed; kept.
- PDF 18 (Artificer skills): "(ix) Watercraft (x) Sleight of Hand" -- missing comma; also PDF 24 (Bard) "(viii) Stealth (ix) Watercraft". Kept.
- PDF 15: "Five races are provided below" -- five including Humans; fine, but note the Halfling heading is singular ("HALFLING") where the others are plural.
- PDF 28: "Five deities ... are provided below" but six gods follow (already noted by A1).
- PDF 29 (Baal): "Add the following to Spell like Blessing:" singular (already noted by A1).
- PDF 27: "*Sever Arcarnum*" is in the embedded Phase A table, not retyped here.

## Text-layer glitches fixed from the image
- PDF 8 "roof 's" -> "roof's"; PDF 25 "mayonly" -> "may only"; PDF 9 "ten-" / "sided" -> kept as "ten-sided" (the hyphen is a real compound hyphen; other dice in the same sentence are written "six sided", "twelve sided" unhyphenated, so this is the book's own inconsistency).
- PDF 23: the Sixth Sense body text sits at the end of p023.md; placed under its heading as the image shows.

## Judgement calls
- **Class stat block** (Key Attribute, Hit Points, Weapons, Armour & Shields, Class Starting Gear, Skills): written as bold labels with a hard break before the value, not as headings, to match batch C2's Fighter/Ranger notes and avoid a heading level below no parent. Two-line starting gear (Bard, Cultist) keeps its printed line break.
- **Red headings** inside each note -> `###`; the Game Dice sub-head "Exploding Dice" (black, smaller) -> `####`; table title bars -> `###` (class tables) or `####` (Attribute Modifiers, under the Modifiers heading). Headings are in Title Case (the book prints them in small caps).
- **Attack Bonus tables**: header row is the printed LEVEL / AB / ABILITY x3 (9 columns, as printed); "Level N" cells bold as printed; two-line ability cells joined with a space.
- **Attribute Modifiers**: no printed column titles, so an empty 6-cell header row; the printed dash for 9-12 is `-`.
- **Callouts**: the boxed hp example (PDF 17) and the Priestess of Argona example (PDF 28) -> `> [!example]` with no title; Designer's Thoughts boxes (PDF 14, 17) -> `> [!note] Designer's Thoughts`; the Artificer OPTIONAL box (PDF 20) -> `> [!tip] Optional`, keeping its printed inline label "**OPTIONAL:**" and entry "13. **Poison**" inside the box.
- **Example of play** (PDF 8-9) is not boxed in the print, so it is plain paragraphs. The angle-bracket asides (`<Tom rolls his attack and damage>` etc.) are escaped as `\<...>` so Obsidian does not swallow them as HTML tags.
- **Numbered steps** (Character Creation 1-17): the list numbers print bold; markdown list numbers can't be bold, so they are plain list markers with the bold step label after them.
- **God entries**: "Related Activities", "Common Phrases", "Icons" stay inline bold labels; "Tenets" and "Patron Benefits" are bold label lines followed by bullet lists, as printed. Graxus's Common Phrases and Icons are each printed over two short lines ("No Quarter! / With me Brothers! Blessed Iron!"; "Anvil and skull. Iron fist. / Crossed swords with a central eye."); joined as one paragraph each (could be hard breaks if preferred). Tenet bullets wrapped over two lines were joined.
- Blessings: the line "All cultists may learn the following blessings:" stays in the Cultist note directly above the 5.5.1 embed; 5.5.2 is embedded right after (it prints beside the 7-12 row).
- Escaped literal asterisks: Barbarian "Hide (+3 AC\*)" and "+3 AC\* instead of +1 AC".

## Left out
- Art and art credits/signatures; the handwritten pseudo-script annotations on the clockwork-arm sketch (PDF 21) are illegible art, not text.
- Page 12 and 31: full-page art, no text.

## Icons
None (diamond bullets -> `- `).
