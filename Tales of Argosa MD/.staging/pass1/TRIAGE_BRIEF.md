# Fidelity triage brief -- Tales of Argosa MD (prose notes, round 1)

## Context and authorization
Max owns this PDF (legitimately purchased; its text is also CC BY-SA 4.0) and the vault is his personal GM reference over it. He wants the highest fidelity. You review an automated check's findings on the prose/entry notes and propose exact, minimal patches. You do NOT edit the notes -- you write a patch file; the orchestrator applies it.

## Inputs (ROOT = /home/claude/toa)
- Flags: `ROOT/tri/<GROUP>.json` -- `{note path: {"pages": "toa lo-hi", "issues": [...]}}` (issue types: words replace/insert(source-only)/delete(note-only), emphasis, not-in-text-layer, no-source-match).
- Notes (read-only): `ROOT/merged/Tales of Argosa MD/<note path>`.
- Source text with the PDF's own emphasis, one file per PDF page: `ROOT/fm/toa/pNNN.md`; page images `ROOT/pages/toa/pNNN.png` (NNN = PDF page = printed page + 2).
- The vault conventions: `ROOT/BRIEF_C.md` (read "Note format").

## Known noise (leave, one-line reason)
- Section titles carried only by the filename (`delete` of the note's own heading words is impossible -- the opposite: `insert` of a heading the note omits because the filename carries it).
- Page numbers / running heads (`insert` of a lone number), embed lines `![[...]]`, callout markers (`[!note]`, `[!example]`), icon words in square brackets, reference tables whose cells the checker reads out of order, sidebar/column order differences.
- Words that sit in a Phase A roll-table note (the rules note embeds that table instead of copying it).

## Decide each issue
Patch when the note departs from the printed source and no convention explains it: missing/extra/wrong bold or italic; a mistyped, dropped, added or substituted word; a paragraph that belongs elsewhere. Treat every word substitution as suspicious until the page explains it. When the text layer and the image could disagree, open the image (crop/zoom with PIL into `ROOT/scratch/<GROUP>/`). Source typos stay verbatim.

## Patch rules (strict)
`old` occurs exactly once in the note (short, one line, enough context to be unique); change only the wrong words/markers; never touch filenames or embeds; no reflowing. Patches to the same file apply in list order.

## Output -- `ROOT/patches/<GROUP>.json`
{"patches": [{"file", "old", "new", "why": "pNNN: reason"}], "no_change": [{"file", "issue", "reason"}], "source_typos": [{"file","quote","page"}], "notes": "..."}
Reply with counts and 3-5 lines of patterns. Don't paste the patches.
