# A3 report -- 15. Sorcery (PDF 93-114)

## Table notes written (9)
All paths under `Tales of Argosa MD/15. Sorcery/`. Every row was checked against the page image.

| note | PDF pages | die header | source of die |
| --- | --- | --- | --- |
| 15.1.1. Spell Casting.md | 93 | (empty) | check-result bands, no die; nothing printed, so header cells left empty |
| 15.5.1. Dark and Dangerous Magic.md | 94-97 | d100 | prose p.94 "roll **1d100** for an additional effect from the DDM table" |
| 15.6.1. Divine Rebuke.md | 98-100 | d100 | prose p.98 "**Roll 1d100** on the table below" |
| 15.7.1. Rites of Atonement.md | 100-101 | d20 | prose p.100 "**roll 1d20**" |
| 15.8.1. Spell List.md | 102-104 | d100 | inferred: not printed on the page; ranges 1-2 ... 99-00, and p.36 Spellcraft says "roll 1d100 & consult the Spell List" (also treasure pages) |
| 15.9. Spells/Conjuring.md | 106 | (empty) | check-result bands inside Conjure Entity; nothing printed |
| 15.9. Spells/Gabbling of the Jade Moon - Madness.md | 108 | d4 | prose in the Gabbling entry, p.107 "roll 1d4 for the effect" |
| 15.9. Spells/Enchantment.md | 112 | d6 | prose in Witchblade, p.112 "(roll 1d6)" |
| 15.10.1. Ritual Components.md | 113 | d66 | prose p.113 "**rolls d66**" |

Coverage self-check: every numeric table covers its die with no gap or duplicate, except the Spell List's printed `23-34` row (see typos). The typographic-punctuation grep found nothing.

## Was it a roll table? (judgement calls)
- **Spell Casting** (p.93) and **Conjuring** (p.106): result bands of the casting check, written as table notes because the brief says to include them. They have no die, so the header row is empty. The band labels (Great Success etc.) keep their bold.
- **DDM DIE** (p.94: Level 1-3 1d8 / Level 4-6 1d10 / Level 7-9 1d12 / Magic Item 1d20) tells you which die to roll, but nothing is rolled on it. I listed it as a ref-table inside `15.5. Dark & Dangerous Magic_`.
- Inline lists inside cells and entries ("Roll 1d6..." style: Diseased 1d4, Marked 1d10, Claimed 1d8, Infuse Animus 1d3, Conjure Entity's six-choice list) stay inline. None of them has its own frame.

## Other judgement calls
- **Footnotes:** the DDM table has two footnotes printed inside its frame. Footnote 1 ("Roll 1d12" monster) is under column 2 on p.94 and footnote 2 ("Roll 1d8" spell) is under column 1 on p.95. Both sit below the table as separate paragraphs. The markers are written `<sup>1</sup>` / `<sup>2</sup>`. The text layer has them as bold digits glued to the word (`monster**1**`); I dropped the bold on the superscript digit only.
- **Filename clash:** the MADNESS title bar on p.108 has the same title as the MADNESS table in chapter 19 (p.163, batch A6). So it is named `Gabbling of the Jade Moon - Madness.md`, after the spell it belongs to. Conjuring and Enchantment keep their printed titles. They sit in the Spells subfolder beside the spell entries, so they can look like spells in a file list.
- **DDM filename:** the title bar reads "DARK AND DANGEROUS MAGIC" but the section heading reads "DARK & DANGEROUS MAGIC". The table note follows the title bar and the rules note follows the heading.
- **Spell List layout:** 4 columns with no printed column titles. The bold spell name and the smaller classic-name line under it (e.g. "Invisibility") are joined with a space in one cell, because the print runs them inline for "Gabbling of the Jade **Moon** Confusion". The text layer splits "**Gabbling of the Jade** / **Moon**"; it is merged into one bold span.
- **Ritual Components:** the d66 table is printed in three side-by-side column pairs (11-26 / 31-46 / 51-66). It is one table in roll order. Bold follows the font data instance by instance: the trailing period is bold in most rows but plain in 33 "**Manticore**." and 35 "**Yegnu**.".
- **Page 93 split:** p.93 has four book headings (Spell Casting incl. ### Spell Limits, Spell Duration, Sensing Magic, Illusions), so it becomes four short rules notes, 15.1-15.4. The chapter intro paragraph goes in 15.1.
- **Spell List section:** it has no prose of its own. I planned a stub, `15.8. Spell List_`, so the table can be 15.8.1. The SPELLS heading (p.105) gets `15.9. Spells_.md` (intro paragraph) next to the `15.9. Spells/` folder.
- **Spell entry names** use the Spell List's Title Case (e.g. "Speaker of Tongues" for the heading "SPEAKER OF tONGUES"; the text-layer casing glitches are ignored). There are 50 entries, one per Spell List row.
- "super natural" (DDM 51-52) is printed as two words at a line break with no hyphen. Kept as two words.

## Suspected source typos / errors (kept verbatim)
- p.102 Spell List: `23-34` **Crush of the Warp** -- should be 23-24. It overlaps 25-34.
- p.94 DDM 8: "They recede in 1d6 weeks" -- missing the final period.
- p.96 DDM 61-62: "**Rift:**" has a colon; the other Rift rows don't.
- p.97 DDM 99: "(ii) *Breathless* (iii)" -- missing comma. Also "*Called From Below*" here vs row title "Called from Below" (27).
- p.99 Divine Rebuke 9-10: "You catch a glimpse your patron's true form" -- missing "of".
- p.99 Divine Rebuke 41-42: refers to "the *Consecrated Ground* Rite of Atonement", but the Rites of Atonement table has no rite by that name.
- p.100 Divine Rebuke 78-80: "(even chance. If magical the item is damaged instead, not usable until repaired)" -- the full stop inside the parenthesis is odd.
- p.103 / p.110: "Sever Arcarnum" (probably meant Arcanum). Kept in the Spell List and as the planned entry name.
- Phase C prose, noted for later: p.105 Beseech the Ancient Ones has "*Consult to Bones (likely)*" (should be "the"); p.106 Conjure Entity has a stray ". rules apply:" artifact (a period printed at the start of the line in the image too).
- DDM 29 is "Whisper of the Watchers" while the spell is "Whispers of the Watchers". Possibly intentional; flagged only.

## Icons
None in any table in this range.

## Chapter boundaries
Confirmed against the images: the SORCERY title is on PDF 93 (printed 91), and PDF 114 (printed 112) is a full-page art page with no text, listed as an `art` row in the plan. Downtime starts at PDF 115 as briefed. No corrections.
