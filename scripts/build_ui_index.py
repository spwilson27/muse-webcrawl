#!/usr/bin/env python3
"""Build sitemap.json for the muse-webcrawl GitHub Pages UI.

Walks web/ (every recreated site lives at web/<domain>/<path>/index.html),
extracts each page's <title>, counts image files per domain, and writes
sitemap.json at the project root:

    {
      "generated_at": "<iso8601 utc>",
      "totals": {"pages": N, "domains": N, "images": N},
      "domains": {
        "<domain>": {
          "pages": [{"path": "web/<domain>/.../index.html", "title": "..."}],
          "images": <count>
        }
      }
    }

Paths are repo-root-relative so the landing page (index.html at the root)
can link straight to them. Stdlib only.

Usage:  python3 scripts/build_ui_index.py
Re-run whenever the crawl grows and before pushing.
"""

import html
import json
import os
import re
import sys
from datetime import datetime, timezone

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
READ_BYTES = 65536  # titles live in the head; no need to read whole files


def page_title(fs_path, fallback):
    try:
        with open(fs_path, "rb") as fh:
            head = fh.read(READ_BYTES).decode("utf-8", errors="replace")
    except OSError:
        return fallback
    m = TITLE_RE.search(head)
    if not m:
        return fallback
    title = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
    return title or fallback


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_dir = os.path.join(root, "web")
    if not os.path.isdir(web_dir):
        print(f"error: {web_dir} not found", file=sys.stderr)
        return 1

    domains = {}
    total_pages = 0
    total_images = 0

    for dirpath, dirnames, filenames in os.walk(web_dir):
        dirnames.sort()
        rel_dir = os.path.relpath(dirpath, root).replace(os.sep, "/")
        domain = rel_dir.split("/")[1] if "/" in rel_dir else rel_dir
        entry = domains.setdefault(domain, {"pages": [], "images": 0})
        for name in sorted(filenames):
            lower = name.lower()
            if lower == "index.html":
                rel_path = f"{rel_dir}/index.html"
                entry["pages"].append(
                    {"path": rel_path, "title": page_title(os.path.join(dirpath, name), rel_path)}
                )
                total_pages += 1
            elif os.path.splitext(lower)[1] in IMAGE_EXTS:
                entry["images"] += 1
                total_images += 1

    for entry in domains.values():
        entry["pages"].sort(key=lambda p: p["path"])

    sitemap = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "totals": {"pages": total_pages, "domains": len(domains), "images": total_images},
        "domains": dict(sorted(domains.items())),
    }

    out_path = os.path.join(root, "sitemap.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(sitemap, fh, ensure_ascii=False, indent=1)

    print(
        f"wrote {out_path}: {total_pages} pages, {len(domains)} domains, "
        f"{total_images} images"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
