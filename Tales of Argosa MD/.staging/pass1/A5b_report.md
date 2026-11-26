# A5b report -- 17. GM Tools, section 17.5 (PDF 142-157)

## Table notes written (12)
All under `Tales of Argosa MD/17. GM Tools/`. Every row of every table was checked against the page image (each page viewed as left and right column crops at full resolution).

| note | PDF pages | die header | inferred? |
| --- | --- | --- | --- |
| 17.5.1. Aerial.md | 142 | d20 | yes |
| 17.5.2. City, Town, Village.md | 143-145 | d100 | yes |
| 17.5.3. Deserts.md | 145-146 | d20 | yes |
| 17.5.4. Jungles.md | 147 | d20 | yes |
| 17.5.5. Forests.md | 148 | d20 | yes |
| 17.5.6. Mountains & Hills.md | 149-150 | d20 | yes |
| 17.5.7. Oceans, Lakes, Rivers.md | 150-151 | d20 | yes |
| 17.5.8. Plains & Grasslands.md | 151-152 | d20 | yes |
| 17.5.9. Roads & Trails.md | 152-153 | d20 | yes |
| 17.5.10. Snow & Ice.md | 154-155 | d20 | yes |
| 17.5.11. Swamps.md | 155-156 | d20 | yes |
| 17.5.12. Underground.md | 156-157 | d20 | yes |

Die headers: no die is printed on any of these tables. d20 comes from the prose on PDF 141 (A5a's pages): "For most tables roll **1d20 during the day** or **1d12+8** at night". The intro on PDF 142 also says the other tables "have twenty encounters". City, Town, Village prints paired results 1-2 ... 99-00 (fifty entries), so its header is d100.

Self-check: every table covers its die with no gaps or duplicates (20 rows, or 50 paired rows for d100). There is no typographic punctuation (grep is clean), and the bold/italic markers are balanced in every row. `fidelity_check.py` shows only expected noise: the title becomes the filename, the added die header, page numbers, and rows reordered from the text layer's out-of-column order on PDF 144 and 155-156. It shows no emphasis issues. `table_check.py` flags "cell-spans-rows" and "text-between-rows" on most rows. That is a known false positive here: each cell wraps over several lines and the roll number is centred vertically. There were no misplaced or swapped cells, and the image pass confirmed every row.

## Unsure whether roll tables
- None at table level. Some cells contain small inline sub-rolls (Roads & Trails 5: "Roll 1d8 (i) cloth, ..."; Roads & Trails 12 and 15: "1d6: (i) ...", "1d8: (i) ..."). I kept them verbatim inside their cells and did not split them into separate tables.

## Suspected source typos/errors (kept verbatim)
- p144, City 51-52: "(player draws from the *Deck of Signs*: If a sun, ... or if a moon they lose 1 *Luck* instead." -- the parenthesis is never closed.
- p144, City 67-68: "etc for discrete clientele" (probably "discreet").
- p145, City 73-74: "staggers in a cluttered ally" (alley).
- p146, Deserts 7: "unearthed a humanoid statute with a beetle like head" (statue).
- p146, Deserts 19: "They are guardians of a scared site" (sacred).
- p147, Jungles 2: "causing nails to emit yellow puss" (pus).
- p147, Jungles 4: "A 15 ft stone statute,in the likeness of" (statue; missing space after the comma).
- p151, Oceans 11: "A *Blue Hag* (as *Hag*, but amphibious and Spells (3) ... *Blast of Frozen Ruin.*" -- the opening "(as" is never closed.
- p152, Roads & Trails 5: "(vi) tools, (vii) wheat, (iv) iron." -- the 8th item is numbered (iv) instead of (viii).
- p153, Roads & Trails 15: "with a carriage or textiles wagons, secreting transporting, 1d8:" (garbled wording).
- p153, Roads & Trails 14: "The undertaker might be *Doppelganger*" (missing article; minor).
- p156, Swamps 14: "(as *Giant Serpent* but Swim Close, and electric shock (*Luck* (Con) save or *Stunned* instead of poison) emerge" -- the outer parenthesis is never closed.

## Judgement calls
- Text-layer glitch: City 71-72 has `"Thief ! Thief !"` in the text layer. The image shows "Thief! Thief!", so I wrote `*"Thief! Thief!"*`.
- Line-end hyphens: I kept real compounds: "non-poisonous" (p145), "non-magical" (p156), "to-ings and fro-ings" (p153). "Inquisitive 11-" / "12 Amicable" (p146) is a numeric range and became "11-12".
- Italic spans that break across lines were merged into one span (e.g. `*Eggbert "sell me own mother" Cruthers*`, `*Tax Collector Cruxus*`, the Orb quotation, `*Deck of Signs*`). Each one matches the image.
- Emphasis follows the font data exactly, even where it looks inconsistent: "**Oleg Arkoza,**" (the comma is bold, no separate title word), "**Snuffling**, cracking ..." (Mountains 13), "**Stinging** insect swarm" (Swamps 9), "**Webs** are strung" (Underground 6), "**Wildfire** erupts" (Plains 1), "**Fog** (50% light ..." (City 81-82), "*Madame Eshorri,*", "*Gaze of Beguilement.*", "*Near Blind,*", "*Off Turn Attacks,*", and `"*How much ya got?"*` (the opening quote is roman).
- Filenames: `CITY, TOWN, VILLAGE` -> `City, Town, Village` and `OCEANS, LAKES, RIVERS` -> `Oceans, Lakes, Rivers` (commas kept as printed). No duplicate titles in this section.
- The "ENCOUNTER TABLES" intro paragraph on PDF 142 is planned as `17.5. Encounter Tables_.md` (phase-C). I copied none of it into the Aerial note.

## Icons replaced by words
- None. No icons appear in these tables.

## Chapter boundary
- Confirmed: section 17.5 ends at the bottom of PDF 157 (Underground 20). PDF 158 begins chapter 18, Hirelings ("ROLES", "COST & NAMES"). No correction needed.
