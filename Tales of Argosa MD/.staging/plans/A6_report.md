# A6 report -- 18. Hirelings, 19. Madness, 20. Mass Battle (PDF 158-167)

## Table notes written (10)
| note | PDF pages | die header | inferred? |
| --- | --- | --- | --- |
| 18. Hirelings/18.1.1. Names.md | 158 | d100 | inferred (no roll printed; 1-2 ... 99-00, 50 rows) |
| 18. Hirelings/18.3.1. Personality.md | 159 | d100 | inferred (1-3 ... 99-00, 42 rows) |
| 18. Hirelings/18.4.1. Traits.md | 159 | d100 | inferred (1-2 ... 99-00, 50 rows) |
| 18. Hirelings/18.5.1. Hireling Gear.md | 160 | d4/d12 | printed in prose: non-combatants "Roll 1d4", mercenaries "Roll 1d12" (one shared table) |
| 18. Hirelings/18.5.2. Catchphrase.md | 160-161 | d100 | printed ("Roll d100 for a catchphrase") |
| 18. Hirelings/18.6.1. Hireling Advancement.md | 161 | 2d6 | printed ("roll 2d6") |
| 18. Hirelings/18.7.1. Payback.md | 161-162 | 2d6 | printed ("2d6 roll on the Payback table") |
| 19. Madness/19.1.1. Madness.md | 163 | d20 | inferred (1-20; no roll printed) |
| 20. Mass Battle/20.1.1. Field Events.md | 164-166 | d20 | printed ("Roll 1d20 on the chart", procedure step 2) |
| 20. Mass Battle/20.2.1. Sudden Twist.md | 166-167 | d20 | printed ("Roll 1d20 and see below") |

Self-check: every note covers its die with no gaps or duplicates (d100 tables 1-100 with 00 = 100; 2d6 tables 2-12; d20 tables 1-20; Hireling Gear 1-12). Every cell was checked against the page images and machine-checked against pNNN.md (emphasis included, `check.py` in scratch: 0 mismatches). No typographic punctuation in output.

## Judgement calls
- Multi-column tables (Names: 5 column pairs; Personality and Traits: 2 column pairs) are each one 2-column table in roll order.
- Hireling Gear rows 1-4 print two lines, a **Non-Combatant** line and a **Mercenary** line; joined with `<br>` (as separate entries) rather than a single space. Header `d4/d12` because the one table serves both dice (non-combatants use rows 1-4 only).
- Continued tables joined across columns/pages: Catchphrase (p160 -> p161), Payback (p161 -> p162 left column), Field Events (p164 -> p165 -> p166), Sudden Twist (p166 -> p167). Table title bars "SUDDEN TWIST" (singular) and section sidebar "SUDDEN TWISTS" (plural) kept as printed: table note `Sudden Twist`, rules note `Sudden Twists_`.
- Section split: Roles / How Many? / Cost & Names kept as ### inside 18.1. Hirelings_; Backgrounds, Personalities, Traits, Gear, Hireling Advancement and Payback each get a rules note (each has its own table except Backgrounds). Madness is one rules note (Symptoms / Acute Episodes / Curing as ###). Mass Battle intro + Field Events procedure share 20.1. Mass Battle_; the two sidebars (Sudden Twists, Final Confrontation) are their own notes.
- Possibly rollable, NOT made into notes (inline prose lists, no frame): mercenary backgrounds "roll 1d8 (i) ex-city watch ... (viii) green recruit" (p159, stays in 18.2. Backgrounds_). Nested in-cell rolls (e.g. Madness 15 Hallucinations 1d8, Field Events 1/3/9/10/13/14/17, Sudden Twist 20) stay inside their cells.
- The batch note mentions a "final confrontation" table: the book has none -- FINAL CONFRONTATION (p167) is a one-paragraph sidebar; planned as rules note 20.3.
- Line-end hyphen "non-" + "combatant(s)" kept as the compound "non-combatant(s)" (Payback 12, Field Events 5).
- Asterisks escaped: Catchphrase 17-18 "bullsh\*t", 57-58 "sh\*t".

## Suspected source typos (kept verbatim)
- p159 Personality 1-3: "Loose Canon" (Cannon).
- p161 Hireling Advancement 11-12: "Transforms into a beautiful henchmen." (henchman); same singular "henchmen" in p164 Field Events 8 "a free random henchmen" and p166 Sudden Twist 4 "A hireling, henchmen, pet".
- p166 Sudden Twist 1: "a stray crossbow bolt or distant marksmen takes" (marksman).
- p167 Sudden Twist 13: "a nameless solider automatically intervenes" (soldier).
- p161 Catchphrase 69-70: "puss puddle plague" (pus? may be intentional).
- p164 Field Events 3: "(vi) Nets." capitalised mid-list.
- p161 Catchphrase 83-84: "Storm's brewin'" has no closing full stop (all other rows end in punctuation).

## Icons
None in these tables.

## Chapter boundaries
Confirmed against images: Hirelings 158-161 (Payback table runs onto p162 left column), Madness 162-163 (starts right column of p162), Mass Battle 164-167. No corrections.
