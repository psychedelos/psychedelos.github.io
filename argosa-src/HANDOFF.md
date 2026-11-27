# Argosa Oracles -- working notes (read this first when resuming)

Max's running notes for Claude. When a conversation resets, read this file, `README.md`, and the latest `git log`, then pick up from "Open items". Keep this file current: update it in the same commit as each change.

## What this is

- Site: https://psychedelos.github.io/argosa/ -- Max uses it as an iPhone home-screen web app ("Open as Web App" on). Repo: psychedelos/psychedelos.github.io (public, branch `main`). Git is the source of truth.
- Tabs: Dice (d2 d3 d4 d6 d8 d10 d12 d20 d100 d66), Bones (Consult the Bones), Signs (draw two Deck of Signs cards), Tables (all 133 roll tables + generators: character, dungeon, room, lair, item, hireling).
- Claude artifact copy: slug `5f5b61d6-a07e-4b47-8bcd-a152e525b8bb` (https://claude.ai/artifact/CmxPDiGfr7GVhmLgvfqBJz). Republish from `argosa-src/build/Argosa_Oracles.html` with `publish_files` (get the live version with `get_artifact` first). Sheet export does not work inside the artifact (no downloads, can't fetch the sheet files) -- that's expected.
- Max no longer wants the HTML file sent to him; updates go to GitHub + artifact.

## How to change things

1. Edit `argosa-src/templates/page.html` (Dice/Bones/Signs, shared shell) or `argosa-src/templates/tables_part.html` (Tables tab, generators, character builder, sheet export).
2. `python3 argosa-src/build.py` -- rebuilds `argosa/index.html` and `argosa-src/build/Argosa_Oracles.html`.
3. Bump `CACHE` in `argosa/sw.js` (and add any new offline files to `FILES`).
4. Test in headless Chromium: `python3 -m http.server 8766` at the repo root, open `http://localhost:8766/argosa/#tables`. For sheet export, override `navigator.canShare` to undefined and capture the blob from `URL.createObjectURL`, then render with `pdftoppm` and check fields with `pypdf`.
5. Commit as `Claude <noreply@anthropic.com>` and push with `git -c push.negotiate=true push origin main`. Then republish the artifact.

## Rules Max has set

- By the book. Character creation order: roll 3d6 x7, background bonus (cap 16), step 3 (raise one attribute to 15 / a second to 13, or swap) happens before choosing a class; class minimums (Artificer Int 15, Barbarian Con 13) are by the book; humans +1 to class key attribute.
- Race: rolled d12 by default; a "Humans only" toggle (remembered on the device) rolls a new human. By the book (Races, p.13) humans get +1 attribute and +1 Reroll only when other races are allowed, so humans-only characters don't get them.
- Age: humans can toggle Average (1d20+16) / Elderly (1d10+60) -- Max wants the word "Elderly", not "old". Both ages are rolled at creation. Elderly = -1 Str & Con, +1 Int & Will (max 16), +1 use of the 1st level class ability. Its own layer (`oldMod`), after the class steps, so class minimums, the 13/15 rule and swaps use the pre-age scores (`baseA`).
- Step 16 traits apply (Max, 2026-11-27), last of all: Half Dwarf -> Con 15, Half Skorn -> Str & Con 13 (raised to that, never lowered -- our reading), Lucky (like a Halfling) +1 Luck, Elderly (any race; locks the toggle on; non-humans keep their rolled age, book has no elderly age for them), 1d4+12 yrs old replaces the age and hides the Elderly toggle, Random Disease rolls on Diseases (p.130). 23-24 and 91-92 are rerolled. Injury traits: adaptation is assumed, no note needed.
- Class ability uses: one per level (+1 elderly), shown as e.g. "Spellcraft (1)" (CLASSES[x].uses).
- Weapon rows (builder and sheet): melee weapons say "Melee"; throwable melee weapons get a second "(throw)" row using Perc; HIT = class AB + Str (Monk: Dex if better) / Perc; DMG = weapon dice + that mod; CRIT = max damage + half level (round up); zero written as "-"; sheet Nat 19 column = dice + "*" when there's an alternative (pregen style). Initiative shows "base/with weapon" for +-2 Initiative weapons (eg 11/9).
- Race traits (Races, p.13) are listed in the builder and written under Skills & Abilities on the sheet (overflow goes to the notes); numeric ones are applied (halfling +1 Luck/AC, human perks, half-skorn +2 Death saves shown as "(+2)" in the builder and "11+2" in the sheet's narrow Death box).
- Halfling weapons (Max's calls, 2026-11-26): large weapons are replaced -- Great Axe -> Battle Axe (1d8), Longbow -> Shortbow (1d6), also Great Sword -> Longsword, Great Hammer -> Heavy Hammer, Polearm -> Spear. "+1 dmg two handed" weapons are mid-size: two hands for a halfling, no +1 (shown in gear and the weapon row). A halfling Fighter keeps Longsword/Spear and shield, but AC is shown without the shield, with a note that it counts only with a small one-handed weapon.
- Changing class keeps everything except what the class decides. Manual changes ("Your changes") are listed separately from "Automatic adjustments".
- Vault text: plain keyboard punctuation (' " ... -- - x).
- Do not commit the purchased Tales of Argosa PDF (art/layout all rights reserved). The free playtest PDF (v5) is not the same content as the final book; not added.
- Max's Mac TTRPG/Obsidian folders are read-only for Claude.

## Character sheet export

- Sheets: `argosa/sheets/classic.pdf`, `argosa/sheets/simple.pdf` -- Max's free official form-fillable sheets, slimmed from 29 MB by removing ~90 unused fonts from the form's resource list (page art untouched). The form's own fonts are kept: Segoe Print, Segoe Print Bold, Segoe Script Bold.
- Filling (`exportSheet` in tables_part.html): pdf-lib + fontkit (`argosa/lib/`). Each field is written in the font, size and colour its own appearance string (DA) names, using the font file taken from the sheet itself; text shrinks to fit (min 6) and notes wrap line to line at an even 8 pt. After drawing, the DA is put back to the sheet's own font so editing on the phone stays in the same font. Saved with `updateFieldAppearances: false`.
- Gotcha: the widget's DA overrides the field's DA when pdf-lib draws, so set the widget DA to the chosen size before `updateAppearances`.
- 2026-11-26: Max found the first version sloppy (mixed fonts) -- it had used Patrick Hand for filled values. Replaced by the sheet's own fonts; Patrick Hand removed.
- Field map: see `sheetData()` (Text1 name ... Text140-150 notes; battle/pack slots differ between Classic and Simple).

## Pregens

- Official pregens Max sent (2026-11-27, batch 1 of 2): 7 form-fillable PDFs (level 1) slimmed into `argosa/pregens/*.pdf` with `tools/slim_sheet.py` (30 MB -> ~4 MB, pixel-identical), and 5 sheet pictures (levels 2-3) as JPEGs. Listed in `argosa-src/pregens/pregens.json` (images need their details typed in); `tools/build_pregens.py` reads the PDF fields at build time; the Character screen has a "Pregens..." menu that shows one in place of the generator, with a link to its sheet.
- To add more: slim the PDF into `argosa/pregens/`, add an entry to the manifest, rebuild. Max is sending 12 more.
- What they taught us (see the 2026-11-27 conversation): the generator matches them on Init, HP, Luck, Rerolls, slots and to-hit; their known slips are noted there (Barbarian AC ignores Wild Born, Cultist Death ignores elderly Will, some level 1 damage/crit off by one).
- Max chose a public repo and asked for these to be committed; they're the publisher's free downloads like the sheets (art belongs to the publisher).

## Vault

`Tales of Argosa MD/` -- full-book Obsidian vault (562 notes), with `_suggested_edits.md` (Max ticks those, never Claude), `_verification_log.md`, `_Transcription Progress.md`, snapshots in `.snapshots/`.

## Open items

- Waiting on Max: name type (culture + female/male from the Names tags) -- proposal: name type on the line under the name, then Personality, Trait, Languages (the sheets have 4 lines there, Text2-5), and fill the Sex box from the tag. Also: should staff/spear (and 10 ft pole) count as 2 item slots like the pregens do (book: "Two handed items take two slots")?

- Max wants RAW (2026-11-26). Halfling spear/staff: read as "longswords or similar moderately sized" (same "+1 dmg two handed" line as the longsword), so two hands, no +1; a halfling Fighter's shield only counts with a small one-handed weapon. Rapier/flail (1d8, one-handed, no +1) might also be "moderately sized" given the rule's "if applicable", but the book doesn't say and no class or background starts with them -- left as normal.

- Max is giving character-generation questions and suggestions one at a time; the sheet export was the first. Ask for the next.
- Not yet confirmed on device: safe-area padding on iPhone; the Save -> share sheet flow; the font fix above.
- Gear choices like "Longsword (1d8) or Spear (1d6+1)": the sheet gets the first option (weapon row and battle slot agree); the builder screen still shows the choice.
