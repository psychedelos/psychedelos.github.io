#!/usr/bin/env python3
"""Pregen list for the app: argosa-src/pregens/pregens.json + the files in argosa/pregens/ -> OUT json.

PDF pregens: every filled form field is read (Text1 name, Text2-5 description, Text6 class, ...).
Image pregens: the details typed into the manifest.
usage: build_pregens.py MANIFEST PREGEN_DIR OUT
"""
import json, os, re, sys
import pypdf

man, folder, out = sys.argv[1:4]
res = []
for p in json.load(open(man, encoding='utf-8'))['pregens']:
    path = os.path.join(folder, p['file'])
    if p['file'].endswith('.pdf'):
        f = {k: re.sub(r'\s+', ' ', str(v.get('/V'))).strip() for k, v in (pypdf.PdfReader(path).get_fields() or {}).items()
             if v.get('/V') not in (None, '') and str(v.get('/V')).strip()}
        e = {'file': p['file'], 'kind': 'pdf', 'name': f.get('Text1', ''), 'cls': f.get('Text6', ''), 'race': f.get('Text7', ''),
             'level': int(f.get('Text13', '1') or 1), 'bg': f.get('Text8', ''), 'sex': f.get('Text11', ''), 'age': f.get('Text12', ''),
             'bond': ' '.join(x for x in (f.get('Text9', ''), f.get('Text10', '')) if x), 'f': f}
    else:
        e = dict(p, kind='image')
    e['size'] = os.path.getsize(path)
    if p.get('white'):
        e['white'] = p['white']; e['wsize'] = os.path.getsize(os.path.join(folder, p['white']))
    res.append(e)
res.sort(key=lambda e: (e['name'], e['level']))
json.dump(res, open(out, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('pregens:', len(res), '->', out)
