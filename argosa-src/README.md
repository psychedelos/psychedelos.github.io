# Argosa Oracles -- source

Source for the page at `/argosa/` (dice roller, Consult the Bones, Read the Signs, and every roll table from *Tales of Argosa* with generators and a character builder).

- `build.py` -- rebuilds everything: `python3 argosa-src/build.py`
- `templates/page.html` -- the page shell: Dice, Bones and Signs tabs
- `templates/tables_part.html` -- the Tables tab: roller, chained rolls, generators, character sheet
- `tools/build_tables.py` -- turns the roll-table notes into the page's table data
- `table_pages.json` -- the 133 roll-table notes in `../Tales of Argosa MD/` the roller uses, and the book pages each sits on
- `../Tales of Argosa MD/` -- the full Obsidian vault (the source of the table data; see its `_License.md`)
- `cards/` -- the 50 Deck of Signs card faces
- `build/` -- output (not committed)

Credits: *Tales of Argosa* text is licensed CC BY-SA 4.0 by its author (see the book's credits page). Deck of Signs card art by DTCards.
