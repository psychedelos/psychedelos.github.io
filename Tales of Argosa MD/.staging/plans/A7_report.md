# A7 report -- 21. Monsters (PDF 168-209, printed 166-207)

## Table notes written (6)
All under `Tales of Argosa MD/21. Monsters/`. Every row checked against the page image (full-res crops in `scratch/A7/`) and machine-checked against `fm/toa/pNNN.md` (plain-text match, all rows pass). No typographic punctuation (grep clean). Roll column plain (as in the sample), cell emphasis kept per instance.

| note | PDF pages | die header | inferred? | rows |
| --- | --- | --- | --- | --- |
| `21.2.1. Monsters by HD.md` | 169 | `HD` (printed column head of the left-hand table) | n/a -- see below | 14 HD bands, <1 to 17+, no gaps |
| `21.3.1. Heavy Abilities.md` | 171 | `d20` | no -- "choose or **roll 1d20**" printed above the table | 1-20 |
| `21.4. Bestiary/Terror Traits.md` | 175 | `d12` | no -- "according to the **1d12** table below" | 1-12 |
| `21.4. Bestiary/Ooze Traits.md` | 196 | `d10` | no -- "Roll **1d10** to determine a particular ooze's special trait" (Ooze, Sentient) | 1-10 |
| `21.4. Bestiary/Shrieker Traits.md` | 200 | `d6` | no -- "Some fungi have a means of defence (roll 1d6)" | 1-6 |
| `21.4. Bestiary/Mutations.md` | 204-205 | `d20` | **yes** -- Urgot prose says only "Roll on the *Mutations Table*"; die inferred from the 20 entries | 1-20 (rows 18-20 continue at the top of p.205) |

## Unsure whether roll tables
- **Monsters by HD (p.169)**: each HD band holds a numbered list (1 Bat, 2 Bird ... 11 Xornling) -- clearly meant for picking/rolling a random monster of a given HD (1d11, 1d16, 1d17, 1d24 ...), but no die is printed. Transcribed as a table note with the HD band as first column (header `HD`, the printed head of the adjacent table) and the numbered list verbatim as one cell. The adjacent untitled HD / AC / DMG / LK table is a non-random reference table -> planned as a `ref-table` inside `21.2. Custom Monsters_`.
- **Not made into notes**: inline rolls inside stat blocks (Eye Terror "roll 1d6: (i) ... (vi)", Fey Creeper "Disease 1d3", Surgat "into 1d4", Rust Monster "roll 1d6: (i-iii) ...", Lich "roll 1d4") and every stat block's **Reac** 2d6 list. These are run-in text within stat blocks, not set as tables; they stay in the entry notes (Phase C).

## Structure / judgement calls
- Chapter boundary PDF 168-209 confirmed (p.168 opens MONSTERS; p.210 is NAVAL COMBAT). No art-only pages.
- `21.1. Monsters_` = p.168 stat-block key (book has no separate heading beyond the chapter title MONSTERS); `21.2. Custom Monsters_` = p.169; `21.3. Special Traits_` = pp.170-172 (all eleven sub-headings as `###` inside one note, Heavy Abilities table numbered 21.3.1).
- **Animals are inside `21.4. Bestiary/`**, not a separate 21.x section: ANIMALS is printed as the same black-bar group heading as ABERRANT TERRORS, DEMONS etc., and Monsters by HD mixes animals with monsters. This keeps the brief's example path `21.4. Bestiary/Terror Traits.md`. Consequence: the untitled bestiary intro paragraph (top of p.175) becomes `21.4. Bestiary_.md`, a rules note sitting beside the `21.4. Bestiary/` folder; in book order it falls after the Animals entries (pp.173-174).
- One entry note per printed monster heading; extra stat blocks under one heading stay in that note (e.g. Animated Object = 5 blocks, Ant, Giant = 3, Dragon = Dragon (Boss) + Young Dragon, Minotaur + Infernal Minotaur, Spider, Giant + Nest Mother, Vampire + Thrall [Thrall block is on p.206]). Group headings (Animals, Aberrant Terrors, Demons, Dinosaurs, Elementals, Giants, Golems, Humans, Lycanthropes, Serpentmen, Zombies) get their own short intro entry notes.
- Filenames keep the book's inverted headings ("Demon, Balor", "Ant, Giant", "Human, Archer", "Lycanthrope, Werewolf"); small words lowercase in Title Case: "Bird or Bat", "Wolf (or Dog)", "Will o' Wisp"; "N'Tarc", "T-Rex" as printed in body text.
- Mutations row 3: the source's bold run stops one letter early -- image and font data both show **Spiked Carapac** + plain "e". Transcribed faithfully as `**Spiked Carapac**e`; Max may prefer to fix to `**Spiked Carapace**`.
- No icons in any table.

## Suspected source typos / inconsistencies (verbatim, PDF page)
Tables:
- p.169 Monsters by HD vs bestiary headings: "Serpentman (Hraarsk)" vs heading HRAASK (p.199); "Serpentman (Ssurlock)" vs SSURLOC; "Wing Snake" vs WINGED SNAKE (p.207); "Hell Hound" vs DEMON, HELLHOUND; "Spider (Giant, Nestmother)" vs stat block NEST MOTHER; "5 Dog" listed separately (dogs use the Wolf entry); "Zombie (BE)" = Brain Eater; HD 5 and HD 9-10 both list plain "Elemental".
- p.204 Mutations #3 "**Spiked Carapac**e" (emphasis boundary, above).
Noticed in stat blocks (Phase C, for the record):
- p.177 Fire Beetle "**Reac** 2-5 Antagonistic 6-8 Hungry 9-10 Wary 10-12 Interested" (10 overlaps).
- p.178 Cyclops "**Reac** 2-5 Hostile 6-7 Hungry 8-9 Covetous 11-12 Inquiring" (10 missing).
- p.183 Earth Elemental "2-6 Violent 7-9 Grumpy 9-12 Cautious" (9 overlaps).
- p.174 Shark "Frenzies when they or target is *Wounded:* Bite (2) per action)." (unmatched parenthesis).
- p.181 Doppelganger "they may subtlety skim the surface thoughts" (subtly).
- p.174 heading "WOLF (0r DOg)" in the text layer is a glyph glitch; image reads WOLF (OR DOG).
