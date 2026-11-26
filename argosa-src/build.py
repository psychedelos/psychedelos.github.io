#!/usr/bin/env python3
"""Rebuild Argosa Oracles from this folder.

    python3 argosa-src/build.py

1. the roll-table notes in ../Tales of Argosa MD (listed in table_pages.json) -> build/tables.json
2. templates/page.html + templates/tables_part.html + cards/*.webp + tables.json -> build/Argosa_Oracles.html
   (the self-contained page, as published to the Claude artifact)
3. the same page plus the home-screen web-app tags -> ../argosa/index.html (the GitHub Pages copy)
"""
import base64, glob, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, 'build')
os.makedirs(BUILD, exist_ok=True)

# 1. table data
VAULT = os.path.join(HERE, '..', 'Tales of Argosa MD')   # the vault is the source of the table data
subprocess.run([sys.executable, os.path.join(HERE, 'tools', 'build_tables.py'), VAULT,
                os.path.join(HERE, 'table_pages.json'), os.path.join(BUILD, 'tables.json')], check=True)

# 2. the page
page = open(os.path.join(HERE, 'templates', 'page.html'), encoding='utf-8').read()
part = open(os.path.join(HERE, 'templates', 'tables_part.html'), encoding='utf-8').read()
tables = open(os.path.join(BUILD, 'tables.json'), encoding='utf-8').read()
cards = [{'name': os.path.basename(f)[3:-5], 'src': 'data:image/webp;base64,' + base64.b64encode(open(f, 'rb').read()).decode()}
         for f in sorted(glob.glob(os.path.join(HERE, 'cards', '*.webp')))]
assert page.count('<!--TABLES_PANEL-->') == 1 and part.count('/*TABLES_JSON*/[]') == 1
out = page.replace('<!--TABLES_PANEL-->', part.replace('/*TABLES_JSON*/[]', tables.replace('</', '<\\/'))).replace('/*CARDS_JSON*/[]', json.dumps(cards))
art = os.path.join(BUILD, 'Argosa_Oracles.html')
open(art, 'w', encoding='utf-8').write(out)

# 3. GitHub Pages copy
head = '''<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Argosa">
<meta name="theme-color" content="#141110">
<title>Argosa Oracles</title>'''
assert out.count('<title>Argosa Oracles</title>') == 1 and out.count('</body>') == 1
site = out.replace('<title>Argosa Oracles</title>', head).replace('</body>', '''<script>
try { if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost')) navigator.serviceWorker.register('sw.js'); } catch (e) {}
</script>
</body>''')
open(os.path.join(HERE, '..', 'argosa', 'index.html'), 'w', encoding='utf-8').write(site)
print('built', art, 'and argosa/index.html', '(%.1f MB)' % (len(site) / 1e6))
print('Remember: bump CACHE in argosa/sw.js when the page changes.')
