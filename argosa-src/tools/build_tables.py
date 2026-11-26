#!/usr/bin/env python3
"""Build tables.json for the Argosa Oracles roller from the vault's roll-table notes.

Usage: build_tables.py VAULT_ROOT FIDELITY_JSON OUT_JSON
Every non-underscore note that is a markdown table becomes one rollable table.
Cells are converted to HTML and decorated with:
  <span class="dx" data-e="2d6+1">2d6+1</span>         dice expression (tap to roll)
  <span class="pc" data-p="50">50%</span>              percentage chance
  <span class="tr" data-t="ID" data-r="13">...</span>  reference to another table (optional row)
  <span class="bo">Consult the Bones</span>            Bones oracle
  <span class="sg">Read the Signs</span>               Deck of Signs
  <span class="op" data-lo data-hi>...</span>          option inside a cell, picked by an in-cell roll
"""
import glob, html, json, os, re, sys

VAULT, FID, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
fid = json.load(open(FID))

# PDF pages for notes the checker could not place (from the image-check reports)
EXTRA_PAGES = {"16.6.1. Pet Qualities": [124], "17.4.2. Weather Shift": [138], "18.3.1. Personality": [159],
               "25.4.1. Dungeon Site": [220], "25.4.5. Main Opposition": [221], "27.10.2. Jewellery": [258],
               "27.10.3. Clothing": [258], "5.5.2. Spell Like Blessings": [27]}

ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii"]
RN = {r: i + 1 for i, r in enumerate(ROMAN)}


def split_row(line):
    s = line.strip()
    if s.startswith("|"): s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"): s = s[:-1]
    cells, cur, i = [], "", 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s) and s[i + 1] == "|":
            cur += "|"; i += 2; continue
        if s[i] == "|":
            cells.append(cur.strip()); cur = ""; i += 1; continue
        cur += s[i]; i += 1
    cells.append(cur.strip())
    return cells


def md_inline(t):
    """markdown inline -> html (bold/italic, escapes, <br>, <sup>)."""
    t = t.replace("\\*", "\x01").replace("\\[", "[").replace("\\]", "]").replace("\\_", "_")
    t = html.escape(t, quote=False)
    for tag in ("br", "sup", "/sup"):
        t = t.replace(f"&lt;{tag}&gt;", f"<{tag}>")
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    return t.replace("\x01", "*")


def parse_roll(s, die):
    s = re.sub(r"[*\s]", "", s)
    m = re.fullmatch(r"\(([ivx]+)\)", s)
    if m and m[1] in RN: return RN[m[1]], RN[m[1]]
    if s == "<1": return 0, 0
    if s == "00": return 100, 100
    m = re.fullmatch(r"(\d+)-(\d+)", s)
    if m:
        lo, hi = int(m[1]), int(m[2])
        if hi == 0 or (hi < lo and m[2] == "00"): hi = 100
        return lo, hi
    m = re.fullmatch(r"(\d+)\+", s)
    if m: return int(m[1]), 999
    m = re.fullmatch(r"(\d+)", s)
    if m:
        v = int(m[1])
        return (100, 100) if (v == 0 and die == "d100") else (v, v)
    return None


def die_of(h):
    h = h.strip().lower()
    if re.fullmatch(r"(1?d(3|4|6|8|10|12|20|66|100)|2d6)", h): return h.lstrip("1")
    if h == "d4/d12": return h
    return None


# ---------------------------------------------------------------- read notes
notes = []
for f in sorted(glob.glob(os.path.join(VAULT, "**", "*.md"), recursive=True)):
    rel = os.path.relpath(f, VAULT)
    base = os.path.basename(f)[:-3]
    if base.endswith("_") or base.startswith("_") or rel.startswith("."): continue
    if rel not in fid: continue          # only the roll-table notes (the Phase A set the checker covered)
    lines = open(f, encoding="utf-8").read().splitlines()
    tl = [l for l in lines if l.startswith("|")]
    if len(tl) < 3: continue
    notes.append((rel, base, lines))

tables = []
for rel, base, lines in notes:
    parts = rel.split(os.sep)
    chapter = parts[0]
    m = re.match(r"^(\d+(?:\.\d+)*)\.\s+(.*)$", base)
    num, title = (m[1], m[2]) if m else ("", base)
    if not num and len(parts) > 2:              # entry-folder tables, e.g. "21.4. Bestiary/Terror Traits"
        num = re.match(r"^(\d+(?:\.\d+)*)\.", parts[1])[1] + ".x"
    tl_idx = [i for i, l in enumerate(lines) if l.startswith("|")]
    header = split_row(lines[tl_idx[0]])
    rows_md = [split_row(lines[i]) for i in tl_idx[2:]]
    after = [l for l in lines[tl_idx[-1] + 1:] if l.strip()]
    before = [l for l in lines[:tl_idx[0]] if l.strip()]
    die = die_of(header[0])
    rows = []
    ok = 0
    for r in rows_md:
        rr = parse_roll(r[0], die) if r and die else None
        if rr: ok += 1
        rows.append({"k": r[0], "lo": rr[0] if rr else None, "hi": rr[1] if rr else None, "c": r[1:]})
    lookup = not die or ok < len(rows) * 0.8
    fp = fid.get(rel, {}).get("pages", "")
    mm = re.match(r"toa (\d+)-(\d+)", fp or "")
    pdfp = list(range(int(mm[1]), int(mm[2]) + 1)) if mm else EXTRA_PAGES.get(base, [])
    tables.append({"id": re.sub(r"[^a-z0-9]+", "-", (num + " " + title).lower()).strip("-"),
                   "num": num, "title": title, "chapter": re.sub(r"^\d+\.\s*", "", chapter),
                   "chapterNum": int(chapter.split(".")[0]), "path": rel[:-3],
                   "die": die, "lookup": lookup, "header": header, "rows": rows,
                   "pre": before, "post": after, "pages": [p - 2 for p in pdfp]})

# ---------------------------------------------------------------- references
by_title = {}
for t in tables:
    by_title.setdefault(t["title"].lower(), t["id"])
ALIASES = {  # phrase (lowercase) -> table id prefix match on title
    "ddm": "Dark and Dangerous Magic", "dark & dangerous magic": "Dark and Dangerous Magic",
    "divine rebuke": "Divine Rebuke", "spell list": "Spell List", "valuables a": "Valuables A",
    "valuables b": "Valuables B", "carry loot a": "Carry Loot A", "carry loot b": "Carry Loot B",
    "trinkets & curios": "Trinkets & Curios", "minor magical item": "Minor Magical Items",
    "minor magic item": "Minor Magical Items", "minor charm": "Minor Charms", "minor charms": "Minor Charms",
    "major magic item": "Major Magical Items", "major magical item": "Major Magical Items",
    "potions": "Potions", "potion": "Potions", "old magic grimoire": "Old Magic Grimoires",
    "injuries & setbacks": "Injuries & Setbacks", "blade trauma": "Blade Trauma", "blast trauma": "Blast Trauma",
    "blunt trauma": "Blunt Trauma", "missile trauma": "Missile Trauma", "toxin trauma": "Toxin Trauma",
    "reaction": "Reaction", "activity": "Activity", "weather": "Weather Shift", "random encounter": "__ENC",
    "dungeon event": "Dungeon Event", "madness": "Madness", "mutations": "Mutations", "mutations table": "Mutations",
    "random disease": "Diseases", "disease": "Diseases", "parasite": "Parasites", "carousing": "Carousing",
    "monsters by hd": "Monsters by HD", "monster by hd": "Monsters by HD", "common gear": "Common Gear",
    "pilfer pouch": "Pilfer Pouch - d100 Table", "theme items": "Theme Items", "complication": "Complications",
    "random trap": "Danger Level", "rites of atonement": "Rites of Atonement", "hireling": "Names",
    "trap": "Danger Level", "heavy abilities": "Heavy Abilities", "chase events": "Chase Events",
}
title_to_id = {t["title"]: t["id"] for t in tables}
# phrases matched case-insensitively at word boundaries; generic ones only when italic or followed by "table"
STRICT = {"reaction", "activity", "weather", "madness", "disease", "parasite", "potion", "potions",
          "complication", "trap", "hireling", "random trap", "dungeon event", "carousing", "random encounter"}
phr = {}
for t in tables:
    tt = t["title"].lower()
    if len(tt) >= 6 and tt not in ("magic", "poison", "monster", "size", "doors", "reward", "names", "traits",
                                  "gas", "pit", "snare", "alarm", "acid", "needle", "lockdown", "drowning",
                                  "relocation", "clothing", "jewellery", "miscellaneous", "personality",
                                  "conjuring", "enchantment", "exploring", "artillery", "boarding",
                                  "payback", "catchphrase", "objective", "complications", "deadfall"):
        phr[tt] = t["id"]
for a, tit in ALIASES.items():
    if tit in title_to_id: phr[a] = title_to_id[tit]
    elif tit == "__ENC": phr[a] = "__ENC"
PHRASES = sorted(phr, key=len, reverse=True)
PAGE_TABLES = {}
for t in tables:
    for p in t["pages"]:
        PAGE_TABLES.setdefault(p, []).append(t["id"])

DICE = re.compile(r"(?<![\w.])(?:(\d+)\s*x\s*)?(\d*)d(\d+)(?:\s*([+\-])\s*(\d+))?(?:\s*x\s*(\d+))?(?![\w])")


def decorate_text(txt, self_id, ctx):
    """decorate a text node (no tags)."""
    out, i = [], 0
    events = []
    for m in DICE.finditer(txt):
        mult, n, s, op, k, mult2 = m.groups()
        if s not in ("2", "3", "4", "6", "8", "10", "12", "20", "100"): continue
        e = f"{n or 1}d{s}" + (f"{op}{k}" if op else "")
        if mult: e = f"{mult}x" + e
        if mult2: e = e + f"x{mult2}"
        events.append((m.start(), m.end(), f'<span class="dx" data-e="{e}">{m.group(0)}</span>'))
    for m in re.finditer(r"(?<![\w.])(\d{1,2})%", txt):
        events.append((m.start(), m.end(), f'<span class="pc" data-p="{m[1]}">{m.group(0)}</span>'))
    for m in re.finditer(r"Consult(?:ing)? the Bones", txt, re.I):
        events.append((m.start(), m.end(), f'<span class="bo">{m.group(0)}</span>'))
    for m in re.finditer(r"Read(?:ing)? the Signs", txt, re.I):
        events.append((m.start(), m.end(), f'<span class="sg">{m.group(0)}</span>'))
    low = txt.lower()
    for ph in PHRASES:
        for m in re.finditer(r"(?<![\w])" + re.escape(html.escape(ph, quote=False)) + r"(?:s)?(?![\w])", low):
            tid = phr[ph]
            if tid == self_id: continue
            if ph in STRICT:
                tail = low[m.end():m.end() + 7]
                if not (ctx.get("italic") or tail.startswith(" table") or tail.startswith(" check")
                        or ph == "random encounter" or (ph in ("weather",) and txt[m.start()] == "W")):
                    continue
            row = None
            pre = txt[max(0, m.start() - 6):m.start()]
            rm = re.search(r"#(\d+)\s*$", pre)
            if rm: row = rm[1]
            events.append((m.start(), m.end(), f'<span class="tr" data-t="{tid}"' + (f' data-r="{row}"' if row else "") + f'>{txt[m.start():m.end()]}</span>'))
    pass  # page references are linked only where the vault links them
    events.sort(key=lambda e: (e[0], -(e[1] - e[0])))
    pos = 0
    for s, e, rep in events:
        if s < pos: continue
        out.append(txt[pos:s]); out.append(rep); pos = e
    out.append(txt[pos:])
    return "".join(out)


def decorate(h, self_id):
    parts = re.split(r"(<[^>]+>|\x05[^\x07]*\x07)", h)
    depth_i = 0
    res = []
    for p in parts:
        if p.startswith("\x05"):
            res.append(p); continue
        if p.startswith("<"):
            if p in ("<i>",): depth_i += 1
            if p in ("</i>",): depth_i -= 1
            res.append(p)
        else:
            res.append(decorate_text(p, self_id, {"italic": depth_i > 0}))
    return "".join(res)


def wrap_options(md, kind):
    """mark sub-options inside a cell so an in-cell roll can highlight one."""
    if kind == "roman":
        pat = re.compile(r"\(([ivx]+)(?:\s*-\s*([ivx]+))?\)")
        ms = [m for m in pat.finditer(md) if m[1] in RN and (not m[2] or m[2] in RN)]
        if len(ms) < 2: return md
    elif kind == "range":
        pat = re.compile(r"\*\*(\d+)(?:-(\d+))?\*\*")
        ms = list(pat.finditer(md))
        if len(ms) < 2: return md
    elif kind == "list":
        pat = re.compile(r"(?:(?<=^)|(?<=, ))(\d+) (?=[A-Z])")
        ms = list(pat.finditer(md))
        if len(ms) < 2: return md
    out, pos = [], 0
    for j, m in enumerate(ms):
        lo = RN[m[1]] if kind == "roman" else int(m[1])
        g2 = m.group(2) if (m.re.groups >= 2) else None
        hi = (RN[g2] if kind == "roman" else int(g2)) if g2 else lo
        end = ms[j + 1].start() if j + 1 < len(ms) else len(md)
        out.append(md[pos:m.start()])
        out.append(f"\x02{lo},{hi}\x03" + md[m.start():end] + "\x04")
        pos = end
    out.append(md[pos:])
    return "".join(out)


BASE_TO_ID = {}
LINKRE = re.compile(r"\[\[([^\]|\\#]+)(?:#[^\]|\\]*)?(?:\\?\|([^\]]+))?\]\]")


def unlink(md):
    """[[target|alias]] -> alias; a link to a roll-table note becomes a roller reference."""
    def rep(m):
        tgt, alias = m[1].strip(), (m[2] or m[1]).strip()
        tid = BASE_TO_ID.get(tgt)
        if not tid:
            m2 = re.match(r"^(\d+(?:\.\d+)*)\.\s.*_$", tgt)
            if m2 and any(t["num"].startswith(m2[1] + ".") for t in tables):
                tid = "__SEC:" + m2[1]
        return f"\x05{tid}\x06{alias}\x07" if tid else alias
    return LINKRE.sub(rep, md)


def cell_html(md, self_id, kind=None):
    md = unlink(md)
    md2 = wrap_options(md, kind) if kind else wrap_options(md, "roman")
    h = decorate(md_inline(md2), self_id)
    h = re.sub(r"\x02(\d+),(\d+)\x03", r'<span class="op" data-lo="\1" data-hi="\2">', h)
    h = re.sub(r"\x05([^\x06]+)\x06(.*?)\x07", lambda m: m[2] if m[1] == self_id else f'<span class="tr" data-t="{m[1]}">{m[2]}</span>', h)
    h = re.sub(r'#(\d+)(\s*(?:<[ib]>)*)<span class="tr" data-t="([^"]+)">', r'#\1\2<span class="tr" data-t="\3" data-r="\1">', h)
    return h.replace("\x04", "</span>")


for t in tables:
    BASE_TO_ID[os.path.basename(t["path"])] = t["id"]
for t in tables:
    kind = "range" if t["title"] == "Theme Items" else "list" if t["title"] == "Monsters by HD" else None
    t["header"] = [md_inline(h) for h in t["header"]]
    for r in t["rows"]:
        r["k"] = md_inline(r["k"])
        r["c"] = [cell_html(c, t["id"], kind) for c in r["c"]]
    t["post"] = [cell_html(p, t["id"]) for p in t["post"]]
    t["pre"] = [cell_html(p, t["id"]) for p in t["pre"]]

tables.sort(key=lambda t: [int(x) if x.isdigit() else 999 for x in re.split(r"\.", t["num"] or "0") if x] + [t["title"]])
json.dump(tables, open(OUT, "w"), ensure_ascii=False, separators=(",", ":"))
print(len(tables), "tables;", sum(len(t["rows"]) for t in tables), "rows;",
      sum(1 for t in tables if t["lookup"]), "lookup;", os.path.getsize(OUT) // 1024, "KB")
for t in tables:
    if t["lookup"]: print("  lookup:", t["path"])
