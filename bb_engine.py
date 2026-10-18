#!/usr/bin/env python3
"""Crawler BB build engine — muse-webcrawl Run 2, Technology & Internet branch."""
import json, os, re, sys, datetime

ROOT = "/home/hatch/workspace/muse-webcrawl"
WIKI = os.path.join(ROOT, "web", "en.wikipedia.org", "wiki")
SHARD = os.path.join(ROOT, "ledgers", "crawler-BB.jsonl")

STYLE = """body{font-family:sans-serif;margin:0;color:#202122;background:#f8f9fa;font-size:14px;line-height:1.6}a{color:#0645ad;text-decoration:none}a:hover{text-decoration:underline}.top{background:#fff;border-bottom:1px solid #a7d7f9;padding:8px 16px;font-family:Georgia,serif;font-size:22px}.layout{display:flex}.side{width:170px;padding:14px 10px;font-size:13px;flex:none}.side ul{list-style:none;padding-left:8px}.side li{margin:4px 0}.side h3{font-size:12px;color:#54595d;border-bottom:1px solid #c8ccd1;font-weight:normal}.main{background:#fff;padding:18px 28px;flex:1;border-left:1px solid #a7d7f9}h1{font-family:Georgia,serif;font-weight:normal;font-size:28px;border-bottom:1px solid #a2a9b1;margin:0 0 6px}h2{font-family:Georgia,serif;font-weight:normal;font-size:20px;border-bottom:1px solid #a2a9b1;margin-top:22px}.hat{font-size:13px;font-style:italic;margin:6px 0}.imgbox{border:1px solid #c8ccd1;background:#f8f9fa;color:#54595d;padding:20px 10px;text-align:center;font-size:12px;margin:8px 0;max-width:320px;float:right;margin-left:16px}.imgbox img{max-width:100%}.foot{border-top:1px solid #a2a9b1;margin-top:30px;padding-top:8px;font-size:12px;color:#54595d;clear:both}table.infobox{border:1px solid #a2a9b1;background:#f8f9fa;float:right;margin:0 0 12px 16px;font-size:12px;border-collapse:collapse;max-width:300px}table.infobox th,table.infobox td{border:1px solid #a2a9b1;padding:4px 8px;text-align:left}table.infobox th{background:#eef3f8}"""

SIDE = """<nav class="side"><h3>Navigation</h3><ul>
<li><a href="../../index.html">Main page</a></li><li><a href="../Wikipedia:Contents/index.html">Contents</a></li>
<li><a href="../Portal:Current_events/index.html">Current events</a></li><li><a href="../Special:Random/index.html">Random article</a></li>
<li><a href="../Wikipedia:About/index.html">About Wikipedia</a></li><li><a href="../Wikipedia:Contact_us/index.html">Contact us</a></li>
<li><a href="../Help:Contents/index.html">Help</a></li></ul><h3>Portals</h3><ul>
<li><a href="../Portal:History/index.html">History</a></li><li><a href="../Portal:Science/index.html">Science</a></li>
<li><a href="../Portal:Mathematics/index.html">Mathematics</a></li><li><a href="../Portal:Technology/index.html">Technology</a></li></ul></nav>"""

def linkify(text, outgoing):
    """Convert [[Slug]] / [[Slug|label]] to relative links; record outgoing slugs."""
    def rep(m):
        slug = m.group(1)
        label = m.group(2) if m.group(2) else slug.replace("_", " ")
        outgoing.append(slug)
        return '<a href="../%s/index.html">%s</a>' % (slug, label)
    return re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", rep, text)

def render(page, outgoing):
    title = page["title"]
    parts = []
    parts.append('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>%s - Wikipedia</title><style>%s</style></head><body>' % (title, STYLE))
    parts.append('<div class="top">WIKIPEDIA <span style="font-size:12px;font-family:sans-serif;color:#54595d">The Free Encyclopedia</span></div><div class="layout">')
    parts.append(SIDE)
    parts.append('<main class="main"><h1>%s</h1><div class="hat">From Wikipedia, the free encyclopedia</div>' % title)
    if page.get("infobox"):
        rows = "".join('<tr><th>%s</th><td>%s</td></tr>' % (k, linkify(v, outgoing)) for k, v in page["infobox"])
        parts.append('<table class="infobox"><tr><th colspan="2" style="text-align:center;background:#d6e6f2">%s</th></tr>%s</table>' % (title, rows))
    if page.get("imgbox"):
        parts.append('<div class="imgbox">[Image: %s]</div>' % page["imgbox"])
    for block in page["body"]:
        if isinstance(block, tuple) and block[0] == "h2":
            parts.append('<h2>%s</h2>' % block[1])
        else:
            parts.append('<p>%s</p>' % linkify(block, outgoing))
    if page.get("see_also"):
        items = "".join('<li><a href="../%s/index.html">%s</a></li>' % (s, s.replace("_", " ")) for s in page["see_also"])
        for s in page["see_also"]:
            outgoing.append(s)
        parts.append('<h2>See also</h2><ul>%s</ul>' % items)
    parts.append('<div class="foot">This article is part of Wikipedia, the free encyclopedia. Text is available under the Creative Commons Attribution-ShareAlike Licence.</div></main></div></body></html>')
    return "".join(parts)

def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds")

def append_shard(rec):
    with open(SHARD, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

built_slugs = []
linked_slugs = set()

def build(page):
    slug = page["slug"]
    folder = os.path.join(WIKI, slug)
    path = os.path.join(folder, "index.html")
    url = "https://en.wikipedia.org/wiki/" + slug
    if os.path.exists(path):
        append_shard({"url": url, "local_path": "web/en.wikipedia.org/wiki/%s/index.html" % slug,
                      "source_url": page.get("source"), "depth": page.get("depth", 3),
                      "status": "skipped-duplicate", "crawler": "BB", "built_at": None,
                      "unsure": [], "outgoing": []})
        print("SKIP-DUP", slug)
        return False
    outgoing = []
    html = render(page, outgoing)
    os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    out_urls = []
    for s in outgoing:
        linked_slugs.add(s)
        u = "https://en.wikipedia.org/wiki/" + s
        if u not in out_urls:
            out_urls.append(u)
    append_shard({"url": url, "local_path": "web/en.wikipedia.org/wiki/%s/index.html" % slug,
                  "source_url": page.get("source"), "depth": page.get("depth", 3),
                  "status": "built", "crawler": "BB", "built_at": now_iso(),
                  "unsure": page.get("unsure", []), "outgoing": out_urls})
    built_slugs.append(slug)
    print("BUILT", slug)
    return True

def finish(extra_queued=None):
    """Write queued lines for linked targets not on disk and not built by BB."""
    queued = []
    for s in sorted(linked_slugs):
        if s in built_slugs:
            continue
        if not os.path.exists(os.path.join(WIKI, s, "index.html")):
            queued.append(s)
    if extra_queued:
        for s in extra_queued:
            if s not in queued and s not in built_slugs and not os.path.exists(os.path.join(WIKI, s, "index.html")):
                queued.append(s)
    for s in queued:
        append_shard({"url": "https://en.wikipedia.org/wiki/" + s,
                      "local_path": "web/en.wikipedia.org/wiki/%s/index.html" % s,
                      "source_url": None, "depth": 4, "status": "queued", "crawler": "BB",
                      "built_at": None, "unsure": [], "outgoing": []})
    print("QUEUED", len(queued), queued)
    print("BUILT TOTAL THIS RUN:", len(built_slugs))
