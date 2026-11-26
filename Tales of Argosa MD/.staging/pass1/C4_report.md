# Batch C4 report (PDF 75-92: 12. Combat from PDF 75, 13. Injury & Death, 14. Healing & Recovery)

## Notes written (11)

| note | PDF pages |
| --- | --- |
| 12. Combat/12.6. Action_.md | 77 |
| 12. Combat/12.7. Melee & Ranged Attacks_.md (incl. ref-tables Melee Modifiers, Ranged Modifiers) | 79 |
| 12. Combat/12.8. Exploits_.md | 80-81 |
| 12. Combat/12.9. Fighting Styles_.md | 82 |
| 12. Combat/12.10. Miscellaneous Factors_.md | 83 |
| 12. Combat/12.11. Conditions_.md | 84 |
| 13. Injury & Death/13.1. Injury & Death_.md (embeds 13.1.1) | 85 |
| 13. Injury & Death/13.2. Trauma Tables_.md (embeds 13.2.1-13.2.5) | 86-89 |
| 14. Healing & Recovery/14.1. Short Rest_.md | 91 |
| 14. Healing & Recovery/14.2. Sleep_.md | 91 |
| 14. Healing & Recovery/14.3. Long Rest_.md | 91 |

Pages opened: 75-92 (all). PDF 75-76 hold only the Chase Events table (already written, embedded by C3's 12.5. Chases_ note -- not touched). PDF 78, 90, 92 are full-page art; 76, 81, 82, 84, 86, 87 (header art), 89, 91 carry partial art (no text). No `written` rows were rewritten.

## Plan rows not followed
None. All phase-C rows in scope written with the plan's filenames.

## Suspected source typos/errors (kept verbatim)
- p84 Conditions / Burning: "*Cosmetic Scarring* become *Serious Scarring* instead" -- "becomes"; also the Injuries & Setbacks table entry 1-3 is titled "Scarring", not "Cosmetic Scarring".
- p77 Action: "during other character's turns" (characters').
- p79 Melee/Ranged Modifiers: "66% miss chance*" -- the asterisk has no footnote on the page (points to p.82 presumably); kept as `\*`.
- p84 Prone: "(eg Dex (Acrobatics*))" -- stray asterisk with no footnote; kept as `\*`.
- p91 Long Rest: "predominately" (predominantly).
- Page refs kept verbatim; note p79 "Injury & Death section ... (p.83)" and "Nat 19 ... see p.58" use printed page numbers (PDF = +2).
- p88 text layer starts with a stray "." not visible on the image; ignored.

## Judgement calls
- Title bars / first headings equal to the note title (ACTION, EXPLOITS, FIGHTING STYLES, MISCELLANEOUS FACTORS, CONDITIONS, INJURY & DEATH chapter title, SHORT REST, SLEEP, LONG REST) not repeated. HEALING & RECOVERY chapter title (p91) is folder-level only; not written.
- 12.6: COMMON ACTIONS under the ACTION title bar written as `### Common Actions`.
- 12.7: Melee Attacks, Ranged Attacks, Damage, Critical Hits, Fumbles, Nat 19s, Dodge as `###`; the two modifier tables' red title bars as `#### Melee Modifiers` / `#### Ranged Modifiers` placed where they print (after their attack section). The tables print no column titles, so header row is empty `| | |`. "Target in Cover" cell holds two diamond-bullet items -> `- ...<br>- ...`.
- Shaded worked-example boxes (Fighter p79, Kruncor/wolves p80, Giant Scorpions p81, Kruncor/Lyssa lightning p81, invisible sorcerer p83, Kruncor Short Rest p91) -> untitled `> [!example]`.
- 12.9 / 12.10 subheads (bold serif, e.g. "Single Weapon Fighting", "Cover") written as `###` per plan.
- Numbered steps (Major Exploit 1-4, Rescue 1-5): printed number+label is bold; written as markdown `1. **label**` (number cannot carry bold in a list).
- 13.2. Trauma Tables_ has no printed "Trauma Tables" heading; it holds `### Blade/Blast/Blunt/Missile/Toxin Trauma` (the red section heads) each with its intro paragraph followed by the embed. The table title bars of the same name were not duplicated as extra headings.
- 13.1: Injuries & Setbacks embed placed at the end of the note (table prints in the right column beside the prose, continuing to p86).
- gmscripts fidelity_check: no words/emphasis/table-number issues (only the printed page number "79" and filename heading words). It reports 13.2 intros as "not-in-text-layer" because the intros are separated by tables in the PDF; checked by hand against p86-89 fm text and images -- verbatim.
- No icons in these pages. No hard line breaks used. Typographic-punctuation grep: nothing found.

## Left out
Running heads, page numbers, art. Nothing else.
