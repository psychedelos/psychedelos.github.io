# Transcription Progress -- Tales of Argosa MD

Working log so any session can resume. Read this first. Update after every finished batch.

## Decisions (confirmed by Max, 2026-11-25)
- Order: (1) transcribe every roll table into the note where it lives in the full-book vault, (2) build the Argosa Oracles roll-table tool from the vault's tables, (3) transcribe the rest of the book into the vault.
- Vault lives in the cloud workspace ("keep it in the workspace so it's at hand"); deliver at the end: updated Argosa Oracles artifact, its HTML file, and a zip of the completed vault. No interim deliveries.
- Vault name "Tales of Argosa MD"; plain keyboard punctuation everywhere (standing rule).

## Conventions
- Knave-style numbered layout (osr_table_book_conventions.md): chapter folders `X. Name/`, rules notes `X.N. Name_.md`, roll tables `X.N.M. Name.md`, per-entry collections in `X.N. Name/` subfolders (one note per entry).
- Every roll table is its own note; non-roll reference tables stay inside their rules note.
- Table notes: table only (+ text inside the table frame), die header from the page, other header cells only printed words; model = `.staging/brief/samples/13.2.1. Blade Trauma.md`.
- Pass 1 verbatim, emphasis from font data, page references kept; linking pass afterwards.

## Technical notes
- Source: Tales_of_Argosa_5_4_25_reduced.pdf, 265 pages. PDF page = printed page + 2.
- Font pages: `font_markdown.py toa.pdf fm/toa --first-page 1 --x-tolerance 2 --tight-split 1.2` (justified text has no space glyphs; default tolerance glues words). Fonts: CalistoMT body, CalisMTBol bold, CalistoMT-Italic/-BoldItalic, Estus display headings (always display size), SimSun bullets.
- Page images: split into 33-page chunks named toa_FFF-LLL.pdf, `render_pages.sh` each (200 DPI).
- Reading order in pNNN.md does not always follow printed columns: place table rows by the image.

## Folder map
- See `.staging/brief/BRIEF.md` (chapter list with PDF ranges) and the per-batch `_plan.md` files in `.staging/plans/`.

## Status
- [x] Phase A: roll tables (batches A1-A10, see .staging/brief/batches.tsv) -- 133 table notes
- [x] Phase A verification (fidelity_check, table_check, image pass on every table page: 12 groups, ~2,200 rows, 0 corrections)
- [x] Phase B: roll-table tool in Argosa Oracles (tool/build_tables.py + tables_part.html; rebuild at the end)
- [x] Phase C: rest of the book (batches C1-C14, 429 notes; plan rows 100% covered)
- [x] Verification: fidelity check (prose flags triaged, 1 patch), completeness check (no gaps), structure check; logs compiled (_verification_log.md, _suggested_edits.md); snapshot .snapshots/pass1
- [x] Linking pass: 7 groups, 1,804 links in 378 notes, link_verify 0 errors, 0 unresolved; snapshot .snapshots/pass2
- [x] Roller rebuilt from the linked vault (133 tables) and delivered: Argosa Oracles artifact + HTML + vault zip

## Batches
- Plan: `.staging/brief/batches.tsv` (+ BRIEF.md, samples). Applied: C1-C14, links L1-L7; A1, A2, A3, A4, A5a, A5b, A6, A7, A8, A9, A10 (Phase C plan: .staging/brief/batches_c.tsv)

## Log
- 2026-11-25: inventory done, font pages + images built, brief + batch plan written; dispatching Phase A batches A1-A10.
- 2026-11-25: Phase A landed (133 tables) and passed the table image check; roller tab built; dispatching Phase C batches C1-C14.
- 2026-11-25: Phase C landed (C1-C14), verified, logs compiled, pass1 snapshot; linking pass applied (pass2 snapshot); roller rebuilt; delivered.
