#!/usr/bin/env python3
"""Shrink an official ToA form-fillable sheet (or pregen) without touching what's on the page.

The sheets ship ~90 fonts in the form's default resources (AcroForm /DR) that no field uses;
they are ~90% of the file. Drop every /DR font that no field's appearance string (DA) names,
keep everything else (page art, fields, values, appearances), and save; unreferenced objects
are dropped on save.

usage: slim_sheet.py IN.pdf OUT.pdf
"""
import re, sys
import pikepdf

src, dst = sys.argv[1], sys.argv[2]
pdf = pikepdf.open(src)
af = pdf.Root.AcroForm
used = set()
def da_font(o):
    da = o.get('/DA')
    if da is not None:
        m = re.match(r'\s*/(\S+)', str(da))
        if m: used.add('/' + m.group(1))
def walk(o):
    da_font(o)
    for k in o.get('/Kids', []):
        walk(k)
da_font(af)
for f in af.get('/Fields', []):
    walk(f)
for p in pdf.pages:
    for a in p.obj.get('/Annots', []):
        walk(a)
fonts = af.DR.Font
before = len(fonts.keys())
for k in list(fonts.keys()):
    if k not in used:
        del fonts[k]
pdf.save(dst, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
print(f'{src} -> {dst}: form fonts {before} -> {len(fonts.keys())} {sorted(used)}')
