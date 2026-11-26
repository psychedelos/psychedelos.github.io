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

## Vault

`Tales of Argosa MD/` -- full-book Obsidian vault (562 notes), with `_suggested_edits.md` (Max ticks those, never Claude), `_verification_log.md`, `_Transcription Progress.md`, snapshots in `.snapshots/`.

## Open items

- Max is giving character-generation questions and suggestions one at a time; the sheet export was the first. Ask for the next.
- Unanswered offer: a race menu (Random d12 by default, optional "Humans only").
- Not yet confirmed on device: safe-area padding on iPhone; the Save -> share sheet flow; the font fix above.
- Gear choices like "Longsword (1d8) or Spear (1d6+1)": the sheet gets the first option (weapon row and battle slot agree); the builder screen still shows the choice.
