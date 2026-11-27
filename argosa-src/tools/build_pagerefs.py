#!/usr/bin/env python3
"""Printed page numbers for names used by the character builder (abilities, spells, class features, tables).

pagemap.json (printed page -> vault notes and headings on it, from the vault's linking pass) and
table_pages.json (roll table note -> PDF pages) -> OUT: {lowercase name: first printed page}.
usage: build_pagerefs.py PAGEMAP TABLE_PAGES OUT
"""
import json, re, sys

pm, tp, out = sys.argv[1:4]
ref = {}
def put(name, page):
    k = re.sub(r'\s+', ' ', name).strip().lower()
    if k and (k not in ref or page < ref[k]): ref[k] = page
base = lambda note: re.sub(r'^[\d.]+\s*', '', note.split('/')[-1]).rstrip('_').strip()
for page, items in json.load(open(pm))['toa'].items():
    for it in items:
        put(base(it['note']), int(page))
        for h in it.get('headings', []):
            put(h if isinstance(h, str) else h.get('text', ''), int(page))
for note, v in json.load(open(tp)).items():
    m = re.match(r'toa (\d+)', v['pages'])
    if m: put(base(note[:-3]), int(m.group(1)) - 2)   # PDF page -> printed page
json.dump(ref, open(out, 'w'), separators=(',', ':'))
print('page refs:', len(ref), '->', out)
