#!/usr/bin/env python3
"""Crawler AM page builder: generates Wikipedia-style pages + ledger lines."""
import json, os, sys, datetime

ROOT = "/home/hatch/workspace/muse-webcrawl"
WIKI = os.path.join(ROOT, "web/en.wikipedia.org/wiki")
SHARD = os.path.join(ROOT, "ledgers/crawler-AM.jsonl")
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

CSS = """body{font-family:sans-serif;margin:0;color:#202122;background:#f8f9fa;font-size:14px;line-height:1.6}
a{color:#0645ad;text-decoration:none}a:hover{text-decoration:underline}
.topbar{background:#fff;border-bottom:1px solid #a7d7f9;padding:8px 16px;display:flex;gap:16px;align-items:center}
.wordmark{font-family:Georgia,serif;font-size:24px;color:#000}.tagline{font-size:12px;color:#54595d}
.topbar input{padding:5px;width:240px;border:1px solid #a2a9b1}
.layout{display:flex}.sidebar{width:170px;padding:14px 10px;font-size:13px;flex:none}
.sidebar h3{font-size:12px;color:#54595d;border-bottom:1px solid #c8ccd1;font-weight:normal}
.sidebar ul{list-style:none;padding-left:8px}.sidebar li{margin:4px 0}
.globe{width:90px;height:90px;border:2px solid #54595d;border-radius:50%;text-align:center;line-height:90px;font-family:Georgia,serif;font-size:38px;color:#54595d;margin:4px auto;background:#fff}
.content{background:#fff;padding:18px 28px;flex:1;border-left:1px solid #a7d7f9;max-width:1050px}
h1{font-family:Georgia,serif;font-weight:normal;font-size:29px;border-bottom:1px solid #a2a9b1;margin:0 0 6px;padding-bottom:4px}
h2{font-family:Georgia,serif;font-weight:normal;font-size:22px;border-bottom:1px solid #a2a9b1;margin:24px 0 8px}
.toc{display:table;background:#f8f9fa;border:1px solid #a2a9b1;padding:8px 16px;font-size:13px;margin:14px 0}
.imgbox{border:1px solid #c8ccd1;background:#f8f9fa;color:#54595d;padding:20px 10px;text-align:center;font-size:12px;margin:8px 0}
.thumb{float:right;width:240px;margin:6px 0 12px 18px;border:1px solid #c8ccd1;background:#f8f9fa;padding:6px;font-size:12px}
.thumb img{max-width:100%;display:block}
table.info{border-collapse:collapse;background:#f8f9fa;border:1px solid #a2a9b1;float:right;margin:6px 0 12px 18px;font-size:13px;width:250px}
table.info th,table.info td{border:1px solid #a2a9b1;padding:4px 8px;text-align:left}
.footer{border-top:1px solid #a2a9b1;margin-top:34px;padding-top:10px;font-size:12px;color:#54595d;clear:both}"""

def L(target, text=None):
    """link to another wiki page"""
    return ('LINK', target, text or target.replace('_', ' '))

def render_body(blocks):
    """blocks: list of tuples ('p', [parts]) / ('h2', text) / ('thumb', slug, desc, caption)
       parts: strings or L() tuples"""
    out = []
    for b in blocks:
        if b[0] == 'h2':
            out.append(f"<h2>{b[1]}</h2>")
        elif b[0] == 'thumb':
            out.append(f'<div class="thumb"><div class="imgbox" data-img="{b[1]}">[Image: {b[2]}]</div>{b[3]}</div>')
        elif b[0] == 'p':
            s = ""
            for part in b[1]:
                if isinstance(part, tuple):
                    s += f'<a href="../{part[1]}/index.html">{part[2]}</a>'
                else:
                    s += part
            out.append(f"<p>{s}</p>")
        elif b[0] == 'raw':
            out.append(b[1])
    return "\n".join(out)

def page_html(title, blocks):
    body = render_body(blocks)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{title} - Wikipedia</title><style>{CSS}</style></head>
<body>
<div class="topbar"><div><div class="wordmark">WIKIPEDIA</div><div class="tagline">The Free Encyclopedia</div></div><div><input type="search" placeholder="Search Wikipedia"></div></div>
<div class="layout"><nav class="sidebar"><div class="globe">W</div><h3>Navigation</h3><ul>
<li><a href="../../index.html">Main page</a></li><li><a href="../Wikipedia:Contents/index.html">Contents</a></li>
<li><a href="../Portal:Current_events/index.html">Current events</a></li><li><a href="../Wikipedia:About/index.html">About Wikipedia</a></li>
<li><a href="../Help:Contents/index.html">Help</a></li></ul>
<h3>Spaceflight</h3><ul>
<li><a href="../Spaceflight/index.html">Spaceflight</a></li><li><a href="../Rocket/index.html">Rocket</a></li>
<li><a href="../NASA/index.html">NASA</a></li><li><a href="../International_Space_Station/index.html">ISS</a></li>
<li><a href="../Apollo_program/index.html">Apollo program</a></li></ul></nav>
<main class="content"><h1>{title}</h1>
<p>From Wikipedia, the free encyclopedia</p>
{body}
<div class="footer">This page was recreated from memory as part of the muse-webcrawl experiment. See also <a href="../Spaceflight/index.html">Spaceflight</a> and <a href="../Timeline_of_spaceflight/index.html">Timeline of spaceflight</a>.</div>
</main></div></body></html>"""

def outgoing_of(blocks):
    tgts = []
    for b in blocks:
        if b[0] == 'p':
            for part in b[1]:
                if isinstance(part, tuple):
                    tgts.append("https://en.wikipedia.org/wiki/" + part[1])
    base = ["https://en.wikipedia.org/wiki/Spaceflight",
            "https://en.wikipedia.org/wiki/Timeline_of_spaceflight"]
    return base + [t for t in tgts if t not in base]

def build(slug, title, blocks, unsure, depth=2):
    folder = os.path.join(WIKI, slug)
    path = os.path.join(folder, "index.html")
    url = "https://en.wikipedia.org/wiki/" + slug
    rel = f"web/en.wikipedia.org/wiki/{slug}/index.html"
    if os.path.exists(path):
        rec = {"url": url, "local_path": rel, "source_url": "https://en.wikipedia.org/wiki/Spaceflight",
               "depth": depth, "status": "skipped-duplicate", "crawler": "AM", "built_at": None,
               "unsure": [], "outgoing": []}
        with open(SHARD, "a") as f: f.write(json.dumps(rec) + "\n")
        print("SKIP-DUP", slug); return False
    os.makedirs(folder, exist_ok=True)
    with open(path, "w") as f: f.write(page_html(title, blocks))
    rec = {"url": url, "local_path": rel, "source_url": "https://en.wikipedia.org/wiki/Spaceflight",
           "depth": depth, "status": "built", "crawler": "AM", "built_at": NOW,
           "unsure": unsure, "outgoing": outgoing_of(blocks)}
    with open(SHARD, "a") as f: f.write(json.dumps(rec) + "\n")
    print("BUILT", slug); return True

def queue(slug, source_slug, unsure=None):
    url = "https://en.wikipedia.org/wiki/" + slug
    rel = f"web/en.wikipedia.org/wiki/{slug}/index.html"
    if os.path.exists(os.path.join(ROOT, rel)):
        return
    rec = {"url": url, "local_path": rel,
           "source_url": "https://en.wikipedia.org/wiki/" + source_slug,
           "depth": 3, "status": "queued", "crawler": "AM", "built_at": None,
           "unsure": unsure or [], "outgoing": []}
    with open(SHARD, "a") as f: f.write(json.dumps(rec) + "\n")
    print("QUEUED", slug)
