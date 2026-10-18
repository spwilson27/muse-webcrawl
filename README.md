# muse-webcrawl

An experiment: **rebuilding the internet purely from Muse's memory.**

Starting from `en.wikipedia.org`, Muse recreates web pages as static HTML from memory alone
— no live lookups during the crawl — then "follows" the links on each recreated page and
recreates those pages too, expanding outward recursively, with up to 5 crawler agents in
parallel.

- Seed: `web/en.wikipedia.org/index.html`
- Every recreated site lives under `web/<domain>/<path>/index.html`
- `ledger.json` / `INDEX.md` — the master ledger of every link traversed (consolidated from
  the per-crawler shards in `ledgers/`)
- `audit/` — a separate audit ledger, written by a separate agent comparing the recreated
  pages against the real web. The auditor never edits the crawl HTML.
- Uncertainty about any page is recorded in the ledger only, never on the pages themselves.

Run 1: 2026-10-17 20:17–21:17 PDT, time-capped at 1 hour, no page or per-domain limit.
Repository: https://github.com/spwilson27/muse-webcrawl — checkpoint pushes about every
~1000 pages produced, and at the end of a run.

## Browsing via GitHub Pages

The whole recreation is static HTML, so it can be browsed as a website via GitHub Pages:

**https://spwilson27.github.io/muse-webcrawl/**

One-time setup (repo owner, on GitHub): **Settings → Pages → Build and deployment →
Deploy from a branch → Branch: `main`, folder: `/ (root)` → Save.** After the next push,
Pages serves the repo root: `index.html` is the browse UI, and every recreated page is
reachable under `web/<domain>/…` exactly as it sits in the repo.

The landing page (`index.html`) shows live totals and lets you search and browse every
domain and page; the index it reads is `sitemap.json`, generated from the crawl tree by:

```sh
python3 scripts/build_ui_index.py   # rewrites sitemap.json at the repo root
```

Re-run it whenever the crawl grows, before pushing, so the UI reflects the new pages.

### How images work (base64 + service worker)

GitHub pushes for this repo go through a **text-only channel**, so images are not stored
as binaries. Each generated image is encoded as a base64 **text** file sitting next to
where the image belongs:

```
web/en.wikipedia.org/wiki/X/images/foo.png.b64   ← text, pushed to GitHub
web/en.wikipedia.org/wiki/X/images/foo.png       ← what the pages reference
```

To make those pages render correctly in a browser, the landing page registers a service
worker (`sw.js`, repo-root scope) that intercepts every image request, fetches the
sibling `.b64` file instead, decodes it in-browser, caches the decoded bytes, and serves
them with the correct `Content-Type`. If a `.b64` file is missing, the worker serves a
transparent 1×1 placeholder rather than a broken-image icon. A small fallback helper
(`assets/museweb.js`, `MuseWeb.fixImages`) does the same decode-and-swap via blob URLs
in browsers where no service worker is active.

Practical notes:

- **Visit the landing page once per browsing session first** — that is what registers
  and activates the service worker; pages you open afterwards in the same session are
  covered automatically.
- If a page ever shows blank pictures, return to the landing page (worker may have been
  updated) and then **hard-refresh** the article page (Ctrl/Cmd+Shift+R).
- The worker only touches image requests on this site's own origin; navigation, HTML,
  JSON, JS and CSS are never intercepted.
