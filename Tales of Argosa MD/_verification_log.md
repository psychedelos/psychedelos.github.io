# Verification Log -- Tales of Argosa MD

This log records what the transcription did, what conventions it applied, and how it was checked. Compiled 2026-11-25. Source-level errors are listed separately in `_suggested_edits.md`. None of them was fixed in the notes.

## Sources and method

- **Source:** *Tales of Argosa* (Tales_of_Argosa_5_4_25_reduced.pdf, 265 pages), owned by Max; the text is also CC BY-SA 4.0. **PDF page = printed page + 2.**
- **Pages covered:** PDF 6-263 (printed 4-261). Not transcribed: the cover, front matter, credits and contents (PDF 1-5) and the index (PDF 264-265). Fourteen full-page art pages have no text: PDF 12, 31, 53, 56, 70, 73, 78, 90, 92, 114, 129, 130, 219, 230.
- **Method: font-assisted.** Every page's text was extracted from the PDF's own font data, with **bold** / *italic* / ***both*** applied from the font names (CalistoMT body, CalisMTBol bold, CalistoMT-Italic / -BoldItalic, Estus display headings, SimSun bullets). The command was `font_markdown.py toa.pdf fm/toa --first-page 1 --x-tolerance 2 --tight-split 1.2`.
  - x-tolerance 2 plus tight-split extraction was needed because the justified text has no space glyphs; the default tolerance glues words together.
  - Each page was also rendered as an image at 200 DPI (1700x2200) and saved with pdftotext -layout.
  - Agents typed from the font text and placed everything by the page image. The text layer's reading order does not always follow the printed columns: table rows can interleave with the facing column, and sidebars can sit anywhere.
- **Phase A** (batches A1-A10, A5a, A5b) wrote the 133 roll tables as their own notes and a chapter plan for every page (`.staging/plans/A*.md`). The plans fixed all numbering before any prose was written.
- **Phase C** (batches C1-C14) wrote the other 429 notes from those plans. It embedded the Phase A tables rather than copying them.
- **Checks:** every page of every batch was opened as an image. Every note was machine-checked word by word and emphasis by emphasis against the font text. The chapter boundaries in the brief matched the page images, so no corrections were needed.
- **Linking:** a second pass (L1-L7) added wiki-links; see "Linking pass (2026-11-25)" below.
- **Evidence files** are in the vault's hidden `.staging/` folder:
  - `brief/`: the briefs and the approved sample
  - `plans/`: the chapter plans and Phase A reports
  - `pass1/`: the batch reports, `checks/`, `checks2/` and `patches/`
  - `pass2/`: the link brief, `reports/L1-L7` and `verify_all.md`
- **Snapshots:** `.snapshots/pass1` (verbatim transcription) and `.snapshots/pass2` (after linking; LATEST). Each holds a notes.tgz and a sha256 manifest.

## Vault structure

The vault holds 562 notes (plus `_Transcription Progress.md` and these two logs):

| kind | count | pattern |
| --- | --- | --- |
| rules / prose notes | 136 | `X.N. Name_.md` (the trailing `_` marks a rules note) |
| roll-table notes | 133 | 125 as `X.N.M. Name.md`, plus 8 in collection folders |
| per-entry notes | 293 | one note per entry in a collection subfolder |

- **28 chapter folders** in book order, `1. What Is Tales of Argosa/` ... `28. Variant Rules/`.
- **Knave-style numbering.** Every number segment ends with a period (`13.2.1. Blade Trauma.md`). Rules notes follow the book's black-bar and big headings; minor sub-headings stay inside their section note.
- **Roll tables as their own notes, embedded in the rules note.** All 133 table notes are embedded exactly once, at the place the table prints (an embed line holding the table's basename, e.g. 13.2.1. Blade Trauma). Non-random reference tables stay inside their rules note: 84 markdown tables in 76 notes, including the class Attack Bonus & Abilities tables, the weapon/armour/gear lists, the XP tables, Ships, Cost, the Rival Adventurers table and the 20 major-item power tables.
- **Collections:** each subfolder shares its section's number. Notes are named by the printed name in Title Case.

| folder | entries | notes |
| --- | --- | --- |
| `5. Classes/5.5. Example Gods/` | 6 | beside `5.5. Cultist_.md` |
| `7. Unique Features/7.2. Example Unique Features/` | 41 | |
| `15. Sorcery/15.9. Spells/` | 50 | beside `15.9. Spells_.md` |
| `21. Monsters/21.4. Bestiary/` | 164 | 153 monster entries + 11 group intros (Animals, Aberrant Terrors, Demons, Dinosaurs, Elementals, Giants, Golems, Humans, Lycanthropes, Serpentmen, Zombies); beside `21.4. Bestiary_.md` |
| `27. Treasure/27.6. Old Magic Grimoires/` | 12 | beside `27.6. Old Magic Grimoires_.md` |
| `27. Treasure/27.8. Major Magical Items/` | 20 | beside `27.8. Major Magical Items_.md` and `27.8.1. Major Magical Items.md` |

- **Tables that belong to one entry** live in that entry's collection folder, under their printed title bar:
  - `Pilfer Pouch - d100 Table`
  - `Conjuring` (Conjure Entity)
  - `Gabbling of the Jade Moon - Madness`
  - `Enchantment` (Witchblade)
  - `Terror Traits`, `Ooze Traits`, `Shrieker Traits`, `Mutations` (Urgot)
- **Filenames:** Title Case of the printed title, with the book's own words. Inverted bestiary headings are kept ("Ant, Giant", "Demon, Balor"). `/` and `:` become ` - `. Two clashing titles were suffixed: `Gabbling of the Jade Moon - Madness` (vs `19.1.1. Madness`) and `Pilfer Pouch - d100 Table` (vs the entry `Pilfer Pouch`). The printed spelling is kept even where it is a likely typo, e.g. `Sever Arcarnum`, `Injury Adaption`, `Monk Techniques (Cross Class)`, `Hraask`.

### Conventions applied

- **No H1 and no H2.** The filename carries the section title, which is never repeated in the note. Printed headings under a section are `###` (329 in total); minor headings under those are `####` (20). Display and small-caps headings are written in Title Case.
- **Callouts** (41 in total):
  - Designer's Thoughts boxes -> `> [!note] Designer's Thoughts` (10)
  - worked examples and examples of play printed in boxes -> `> [!example]`, untitled as printed (19)
  - the Artificer OPTIONAL box -> `> [!tip] Optional` (1)
  - other titled boxes -> `> [!note] <Title>`: Buildings, Delay & Ready Action, Readied Gear, Travel Procedure, Carry Loot A, Side Effects
  - untitled non-example boxes -> `> [!note]` (17.1 intro box, 16.2 Session Advances box, the Uncommon Gear and Rare Gear item lists in 9.4/9.5, the 27.4 Lair Treasure sidebar)
  - exception: the Sudden Twists and Final Confrontation boxes are whole notes (`20.2.`, `20.3.`), so they are written as plain paragraphs
- **Bullets and lists.** Diamond bullets become `- `. Numbered steps stay numbered. Roman and lettered sub-items keep their printed markers.
- **Class stat block** (Key Attribute, Hit Points, Weapons, Armour & Shields, Class Starting Gear, Skills): a bold label plus a hard line break, not headings. 129 hard-break lines across the vault, in class headers, spell headers and Travel Roles.
- **Spells and grimoire spells.** The note opens with `**Range:** ...` / `**Duration:** ...` joined by a hard break, then the description.
- **Monsters.** Description paragraphs come first, then each printed stat block as one paragraph with its bold/italic from the font data. Extra stat blocks under one heading stay in that note, e.g. Animated Object x5, Ant, Giant x3, Dragon + Young Dragon, Minotaur + Infernal Minotaur, Vampire + Thrall.
- **Roll-table notes** hold only the table plus any text printed inside its frame, modelled on the approved sample `13.2.1. Blade Trauma`:
  - The first column is the roll, and its header is the die from the page.
  - Other header cells hold only printed column titles. Where printed, those are kept: Activity STATUS / INTELLIGENT CREATURE / OTHER CREATURES; Objective TASK / THING; Triggers & Counters TRIGGER / COUNTER; Travel Events OVERLAND / UNDERGROUND / VOYAGE; the Lair Treasure columns.
  - Rows are in roll order, with ranges verbatim (`1-2`, `99-00`, `00`; Mutagen keeps `(i)`-`(viii)` under `d8`).
  - The lines of a multi-line cell are joined with single spaces. `<br>` is used only for separate printed paragraphs or lists.
  - Die numbers are plain, although the print sets them bold.
  - In-frame captions and footnotes are kept: the Fortune Die Examples caption, the two DDM footnotes.
- **Reference tables.** The header row is the printed column titles exactly, or empty cells where none are printed. A title bar becomes a `###`/`####` heading above the table.
- **Escapes.** Literal asterisks are written `\*` (the book's required-skill marker, e.g. `Int (Arcane Lore\*)`). Pipes in cells are `\|`. Angle-bracket asides in the How to Play example are `\<...>`.
- **Punctuation.** Only plain keyboard punctuation is used (straight quotes, `...`, `--`, `-`, `x`); a grep finds no typographic punctuation anywhere. The only non-ASCII characters are the printed letters in "Yûlnvorg" and "déjà vu".

### Die headers that are not printed for the table

- **Inferred from the entries alone** (no die printed anywhere):

| table note | header | basis |
| --- | --- | --- |
| `5. Classes/5.5.2. Spell Like Blessings.md` | d12 | rows 7-12 of the Blessings d12 |
| `9. Equipment/9.3.1. Common Gear.md` | d66 | 11-66 numbering |
| `9. Equipment/9.15.1. Masterforged Weapon.md` | d8 | entries 1-8 |
| `9. Equipment/9.15.2. Masterforged Armour.md` | d6 | entries 1-6 |
| `13. Injury & Death/13.2.2. Blast Trauma.md` | d12 | the prose says only "1d6 to 1d12 depending on the attack"; entries 1-12 |
| `15. Sorcery/15.8.1. Spell List.md` | d100 | ranges 1-2 ... 99-00, and Spellcraft (PDF 36) says "roll 1d100 & consult the Spell List" |
| `17. GM Tools/17.2.2. Parasites.md` | d3 | 3 entries |
| `17. GM Tools/17.4.1. Fortune Die Examples.md` | d8 | 8 entries |
| `18. Hirelings/18.1.1. Names.md`, `18.3.1. Personality.md`, `18.4.1. Traits.md` | d100 | ranges run to 99-00 |
| `19. Madness/19.1.1. Madness.md` | d20 | 20 entries |
| `21. Monsters/21.4. Bestiary/Mutations.md` | d20 | 20 entries; the Urgot prose says only "Roll on the Mutations Table" |
| `27. Treasure/27.2.1. Valuables A.md`, `27.2.2. Valuables B.md`, `27.3.1. Trinkets & Curios.md`, `27.5.1. Minor Magical Items.md` | d100 | ranges to 96-100 |
| `27. Treasure/27.8.1. Major Magical Items.md` | d20 | 20 entries |

- **Taken from prose outside the table frame:**
  - `17. GM Tools/17.5.1.`-`17.5.12.` Encounter Tables: d20, from PDF 141 "For most tables roll 1d20 during the day or 1d12+8 at night" and PDF 142 "twenty encounters". `17.5.2. City, Town, Village` is d100 (50 paired rows).
  - `11. Encounters/11.2.1. Activity.md`: d6, from "Activity Die".
  - `5. Classes/5.2.2. Mutagen.md`: d8, from Alchemy row 11 "Roll 1d8 for the Mutagen effect".
  - `27. Treasure/27.10.2. Jewellery.md` / `27.10.3. Clothing.md` (d8) and `27.10.4. Miscellaneous.md` (d20): from the Item Type cells.
  - `18. Hirelings/18.5.1. Hireling Gear.md`: `d4/d12`, from "Roll 1d4" for non-combatants and "Roll 1d12" for mercenaries.
  - The Dungeon Generator and Simple Traps tables: from their "roll ..." lead-ins (e.g. Mode of Attack d20, Magic d12, Poison d20, Danger Level / Bypasses / Triggers & Counters 2d6).
- **Not a die:**
  - `16. Downtime/16.9.1. Standard Research.md`: "Int check" (result bands of the Int check named in the prose; inferred and flagged).
  - `15. Sorcery/15.1.1. Spell Casting.md`, `15. Sorcery/15.9. Spells/Conjuring.md` and the 20 trap-mode tables (`26.4.5.`-`26.4.24.`): the header cells are empty, because the rows are check-result or danger bands and nothing is printed.
  - `21. Monsters/21.2.1. Monsters by HD.md` and `27. Treasure/27.4.1. Lair Treasure.md`: `HD`. Lair Treasure prints its own header row; Monsters by HD uses the printed column head of the adjacent Custom Monsters table.
  - `25. Solo Rules/25.4.11. Theme Items.md`: `| | d20 |` (theme names, then inline d20 sub-ranges).

## Verification and results

| check | scope | result |
| --- | --- | --- |
| Fidelity check (`.staging/pass1/checks2/fidelity_summary.md`) | all 562 notes, word by word and emphasis by emphasis against the per-page font text | flags: reordered 302, words 216, not-in-text-layer 172, moved 75, emphasis 10, no-source-match 9, table-emphasis 5; 136 notes had word/emphasis/number flags |
| Prose triage (R1, R2) | the 86 prose/entry notes with flags (R1: chapters 1-21 up to Beetle, Fire; R2: rest of the bestiary to 28) | 149 flags judged noise (embedded table rows, filename-carried titles, page numbers, column order, icon words, checker page ranges); **1 patch applied**: `5. Classes/5.2. Artificer_.md` `> 13. **Poison**` -> `> **13. Poison**` (the print bolds the whole label) |
| Completeness check (`.staging/pass1/checks2/coverage.txt`) | every page's word bigrams vs the notes | bigram coverage 0.83-0.98 on the 44 pages with "unexplained words"; every one explained (stat-block tokens split by bold markers, `<sup>` footnote markers, filename-carried headings, the fixed "mayonly"); nothing missing |
| Structure check (`.staging/pass1/checks2/structure.txt`) | all 562 notes | only NO-H1 (by design) and one SHORT note (`15.8. Spell List_`, embed-only stub) |
| Automated table check (`.staging/pass1/checks/table_check_summary.md`) | 133 table notes | flags as layout noise: cell-spans-rows 150, header-unlocated 114, text-between-rows 99, row-unlocated 47, cell-cut-short 46, cell-not-in-row 37, row-cells-apart 17, cell-misplaced 4, no-source-match 8, sign-not-printed 1 |
| Table image check (`.staging/pass1/patches/TABLES-T01..T12.json`) | every row of every roll table against the page image and the font text | **133 tables, 2,169 rows, 0 corrections** (2,285 row checks including 6 tables rechecked in T12) |
| Typography grep | all notes | no typographic punctuation |
| Embed check | all notes | 133 embeds, every table note embedded exactly once |

Table image check by group (rows checked; 0 patches in every group):

| group | tables | rows | contents |
| --- | --- | --- | --- |
| T01 | 10 | 153 | Backgrounds, Party Bonds, class lists (Alchemy & Mechanica ... Tricks & Techniques) |
| T02 | 13 | 207 | Pilfer Pouch, Common Gear, Masterforged, Reaction, Activity, Chase Events, Injuries & Setbacks, five Trauma tables |
| T03 | 4 | 139 | Spell Casting, Dark and Dangerous Magic, Divine Rebuke, Rites of Atonement |
| T04 | 8 | 121 | Spell List, Conjuring, Gabbling - Madness, Enchantment, Ritual Components, Downtime Period/Event, Complication |
| T05 | 8 | 124 | Carousing, Pet Qualities, Monstrous Instincts, Standard Research, Diseases, Parasites, Fancy Meeting You Here, Dungeon Event |
| T06 | 9 | 179 | Fortune Die Examples, Weather Shift, Exploring, Travel Events, Back to Base, Aerial, City/Town/Village, Deserts, Jungles |
| T07 | 9 | 210 | Forests ... Underground, Names |
| T08 | 11 | 271 | Personality, Traits, Hireling Gear, Catchphrase, Hireling Advancement, Payback, Madness, Field Events, Sudden Twist, Monsters by HD, Heavy Abilities |
| T09 | 16 | 180 | Terror/Ooze/Shrieker Traits, Mutations, Artillery, Boarding, Crew vs Crew, Dungeon Generator 25.4.1-25.4.8, 25.4.10 |
| T10 | 31 | 244 | Room Theme, Theme Items, Complications, all 24 Simple Traps tables, Carry Loot A/B, Valuables A/B |
| T11 | 5 | 146 | Trinkets & Curios, Lair Treasure, Minor Magical Items, Potions, Old Magic Grimoires |
| T12 | 15 | 311 | Minor Charms, Major Magical Items, Item Generator 27.10.1-27.10.7, plus rechecks of 6 tables the checker could not locate |

## Format adaptations

- **Icons** carry meaning, so they are written in words in square brackets:
  - `11. Encounters/11.2.1. Activity.md`: `[dagger icon]`, `[group of people icon]`, `[drumstick icon]`, `[shovel icon]`, `[footprint icon]`, `[campfire icon]`
  - `23. Oracle Tools/23.2. Consult the Bones_.md`: `[Yes rune icon]` / `[No rune icon]` (the two dice's different rune shapes are written the same way), `[sun icon]` / `[skull icon]`
  - `25. Solo Rules/25.2. Lone Wolf_.md`: `[sun icon]` / `[skull icon]`
  - `23. Oracle Tools/23.3. Read the Signs_.md`: the labelled card diagram is one bracketed description line, including `[direction arrow icon]`
- **Merged split tables.** Tables printed in side-by-side halves, or continued in the next column or on the next page, are one table in roll order:
  - Backgrounds, Ritual Components (three column pairs), Names (five pairs), Personality, Traits
  - Downtime Period/Event, Pet Qualities, Weather Shift, Exploring, Fortune Die Examples, Old Magic Grimoires, Item Type, Jewellery, Clothing, Miscellaneous, Number of Powers, Major Magical Items
  - the Dungeon Generator and Simple Traps halves
  - the continued tables: Diseases, Injuries & Setbacks, Blade/Blunt/Missile Trauma, Catchphrase, Payback, Field Events, Sudden Twist, Boarding, Mutations
  - reference tables: ATT/GS/TF (10.3), the Rival Adventurers table (its repeated p.217 header dropped), and six major-item power tables
- **Joined emphasis spans.** Bold or italic runs that the text layer breaks at a line end were merged into one span where the image shows continuous emphasis, e.g. `*Gaze of Beguilement*`, `**Will (Divine Lore\*) check**`, `**Nat 19-20**`. Emphasis was never added or removed by category; trailing punctuation inside a span is kept as the font data gives it.
- **Title Case headings** from the book's all-caps and small-caps display headings. Text-layer casing glitches were ignored ("Deadly StrikeS", "SPEAKER OF tONGUES").
- **Numbered steps.** The print bolds the number together with its label (`**1. Surprise**`), but a Markdown list marker cannot be bold, so these are written `1. **Surprise** ...` (Character Creation, Exploits, Travel Procedure, Field Events, Naval Combat, Traps). One exception: the Artificer OPTIONAL entry is prose inside a callout, not a list, so it keeps `**13. Poison**` (the R1 patch).
- **Text-layer glitches** were written as the image shows: "roof's", "may only", "Thieves' Grace", "Ballard's Blade", "Thief! Thief!", `**N'TARC**`, "Medium, Wood", "a -1 XP". Sixth Sense was placed under its heading. Group headings missing from the text layer (Lycanthropes, Serpentmen) were placed from the image.
- **Hyphenation.** Line-end hyphens are re-joined ("repurposes"). Real compounds are kept ("non-magical", "to-ings and fro-ings", "ten-sided"), and split numeric ranges are re-joined (`11-12`, `(i-iii)`). Words the book splits at a line break with no hyphen are kept as two words ("pre occupation", "super natural").
- **Smaller adaptations:**
  - Double spaces in the source are collapsed to one.
  - The underlined "or" in Travel Events row 20 is plain, because Markdown has no underline.
  - The DDM footnote markers are written `<sup>1</sup>` / `<sup>2</sup>`.
  - Travel Events cells that span several columns are repeated in each column.
  - The Ships NAME cells are `**Skiff**<br>Rowboat`.
  - Hireling Gear rows 1-4 put the Non-Combatant and Mercenary lines on separate `<br>` lines.
  - Graxus' two-line phrases are joined.
- **Embeds** follow the printed reading order. For example, the DDM table closes 15.5, the Injuries & Setbacks table closes 13.1, and the 20 trap-mode tables follow `#### Cost` in 26.4.
- **Plan deviations** (numbering untouched):
  - 12.1 "Delay & Ready Action", 17.3 "Readied Gear" and 17.4 "Travel Procedure" are boxed in print, so they are callouts rather than `###` headings.
  - 9.9 "Second Rank Weapons" and 17.3 "Consult the Bones" are `####`.
  - The 27.5 first heading is not repeated.
  - The PDF 250 Designer's Thoughts box sits in 27.9, where it prints.
  - The 27.8.1 embed closes 27.8.
- **Left out:** running heads, page numbers, art, art credits and signatures, the Party Bonds art captions, the illegible pseudo-script on the clockwork-arm sketch (PDF 21), the p.221 card-fan art words, and a hidden "WEAPON" token on PDF 216.

## Linking pass (2026-11-25)

- **Result:** 1,804 wiki-links across 378 notes. 203 page references were consumed. `link_verify` (`.staging/pass2/verify_all.md`): 378 changed notes, 1,804 links, 203 consumed page refs, **0 errors**. None of the 133 embeds was touched. Pre-link copies are in `.staging/link_backup/` and `.snapshots/pass1`.
- **Per group, before harmonising:**

| group | chapters | notes changed | links | page refs consumed |
| --- | --- | --- | --- | --- |
| L1 | 1-8 | 51 | 149 | 29 |
| L2 | 9-14 | 32 | 117 | 18 |
| L3 | 15-16 | 47 | 276 | 20 |
| L4 | 17 | 22 | 352 | 39 |
| L5 | 18-20, 22-26 | 42 | 163 | 20 |
| L6 | 21 | 139 | 549 | 19 |
| L7 | 27-28 | 47 | 234 | 58 |
| total | | 380 | 1,840 | 203 |

- **Harmonising:** the orchestrator then unlinked 36 links, *Reroll(s)* (L2, L6, L7) and the special-metal words *cold iron* / *silvered* / *adamantine* (L7), so that every group follows one rule. That left 1,804 links in 378 notes. Two deliberate exceptions remain:
  - "see *Luck*" (`10. Doing Things/10.1. Doing Things_.md`) is an explicit "see X".
  - "adamantine shield" (`9. Equipment/9.15.2. Masterforged Armour.md`) consumes "(p.61)" and points to `9.11. Shields_`.

### Link rules applied

1. **Displayed text never changes.** Strip every link to its alias and the note reads as before. The only text removed is a consumed print page reference (`(p.66)`, `p.229`) plus, at most, a preposition that worked only with it ("see", "on").
2. **Only real references are linked:**
   - page references; "see X"; "the X table / chart"; "roll on X"
   - *italic* names that the book uses as cross-reference markers: spells, monsters, magic items, table names, conditions (-> `12.11. Conditions_#Heading`), *Consult the Bones* / *Read the Signs* (-> 23.2 / 23.3), *Boss* / *Heavy* (-> 21.3 headings)

   Bare rule words in running prose stay plain.
3. **Page references:**
   - A page ref next to a name: the name is linked and the page ref dropped ("the Activities table (p.66)" -> "Activities" linked to `11.2.1. Activity`).
   - A page ref that names nothing: the page text is kept as the alias ("use p.229" -> "p.229" linked to `27.1. Treasure_`).
   - Ambiguous pages, and misprinted pages, were left as printed.
4. **Link format:** basename targets with an alias; anchors only to real headings; no self-links (a few same-note heading anchors where useful); never inside headings or embed lines.
5. **Emphasis and tables:** the emphasis markers go outside the link; pipes are escaped in table rows.
6. **Per-entry notes** (spells, monsters, items, gods, unique features) link only italic names and page references.
7. **Ambiguous or missing targets** are left as printed. Plural, inverted and inflected names link with the printed word as the alias, e.g. Giant Eagles -> `Eagle, Giant`, Owlbears -> `Owlbear`, Hell Hound -> `Demon, Hellhound` (in Monsters by HD only).
8. **Never linked:** *Luck* (it marks the Luck stat and save hundreds of times), *Reroll(s)*, special-metal words (*cold iron*, *silvered*, *adamantine*, *mithral*), and attribute names.
9. **Bold names linked as exceptions:** the bold names in `15.8.1. Spell List` (all 50 spells), `15.10.1. Ritual Components` and every name in `21.2.1. Monsters by HD` (166 of 169 names). In these tables every entry names its note.

The unlinked references (ambiguous, misprinted, spelling mismatches) are listed under "Open questions" in `_suggested_edits.md`.
