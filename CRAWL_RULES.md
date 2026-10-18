# muse-webcrawl — Crawl Rules (binding for all crawler agents)

Experiment: Recreate the internet **purely from memory** as static HTML, starting from en.wikipedia.org.
Owner: Sean (GitHub: spwilson27/muse-webcrawl)

## Hard rules
1. **No live web use while crawling.** Do NOT use browser.search, browser.open, browser.browse,
   curl, wget, or any connector to look at the real sites. Every page is written from model
   memory only. (The separate audit agent is the only exception, and it never edits crawl HTML.)
2. **Reproduce as closely as possible, paraphrase where needed.** Recreate layout, navigation,
   headings, section structure and remembered content faithfully. Do not reproduce long
   verbatim passages of copyrighted text — paraphrase / summarise instead. Short factual
   phrases, names, titles, dates and navigation labels are fine.
3. **Uncertainty goes in the ledger only.** Pages should look clean / faithful. Anything you are
   unsure about (exact wording, dates, layout details, a featured item, a statistic) is recorded
   in your ledger shard's `unsure` field — never as a note on the page itself.
4. **Private / logged-in views are allowed, but invented.** e.g. a Facebook feed page should use
   invented, generic people and typical posts — not real private individuals, and not statements
   attributed to real people that they did not make. Real public figures may appear only in a
   public-news sense, paraphrased.
5. **Standalone pages.** Each page is one self-contained HTML file: inline `<style>` only,
   no external CSS/JS/images/fonts. Images are represented as labelled placeholder boxes
   (a `<div>` describing, from memory, what image belongs there).
6. **Links must point at local recreated pages.** Every hyperlink in a page must be a relative
   link to the target page's local `index.html`. Add a link only if that target is a plausible
   real link from this page. Targets that have not been built yet are recorded in your ledger
   shard as `queued` — they still get a link from the source page.

## Path convention
- A URL `https://example.com/`            -> `web/example.com/index.html`
- A URL `https://example.com/some/path`    -> `web/example.com/some/path/index.html`
- A URL `https://en.wikipedia.org/wiki/Physics` -> `web/en.wikipedia.org/wiki/Physics/index.html`
- Query strings / anchors: drop them, note the original URL in the ledger.
- Filenames are always `index.html` inside a folder named for the path.

## Relative link calculation
From a page's *folder*, use `../` to go up to `web/`, then down into the target.
Examples:
- From `web/en.wikipedia.org/index.html` to `web/facebook.com/index.html`:
  `href="../facebook.com/index.html"`
- From `web/en.wikipedia.org/index.html` to `web/en.wikipedia.org/wiki/Physics/index.html`:
  `href="wiki/Physics/index.html"`
- From `web/en.wikipedia.org/wiki/Physics/index.html` to `web/en.wikipedia.org/index.html`:
  `href="../../index.html"`
- From `web/en.wikipedia.org/wiki/Physics/index.html` to `web/nasa.gov/index.html`:
  `href="../../../nasa.gov/index.html"`

## Ledger shards (no shared-file writes)
Each crawler writes ONLY its own shard: `ledgers/crawler-<LETTER>.jsonl`
One JSON object per line, one line per page built OR queued target, with fields:
`{"url": "...", "local_path": "web/.../index.html", "source_url": "... or null for seed",
  "depth": <int>, "status": "built|queued|skipped-duplicate|skipped-out-of-scope",
  "crawler": "<LETTER>", "built_at": "<ISO time or null>", "unsure": ["...","..."],
  "outgoing": ["<target url>", "..."]}`
Append lines as you go — do not wait until the end. Never edit another crawler's shard,
`ledger.json`, `INDEX.md`, the audit files, or another crawler's assigned pages.

## Deduplication
Before building a page, check whether the file already exists on disk. If it does, do not
overwrite it; log `skipped-duplicate` in your shard and move on.

## Time cap for Run 1
- Run started: 2026-10-17 20:17 PDT (America/Los_Angeles)
- Stop starting new pages at: **21:12 PDT**
- Finish the page in hand, finish your ledger shard, and return a summary by: **21:17 PDT**
There is no page-count or per-domain limit in this run — breadth and depth are both wanted,
quality/faithfulness first. Work steadily page by page; do not idle.

## Amendment (20:22 PDT, during Run 1) — Images from memory
Crawlers should also spawn **separate image-generator subagents** to regenerate a page's
images from memory. Rules for that work:
- **No per-page image limit** (changed by Sean 20:24 PDT: image agents are separate and
  must not block crawlers). Every image described on a page — featured / hero / lead images,
  other photos/illustrations, and logos/icons rendered as images — is eligible. Spawn the
  image subagents and keep crawling; do not wait for them to finish before moving on.
- An image subagent works from memory only too — its prompt is the crawler's remembered
  description of the image (the placeholder text), never a live lookup.
- Image subagents generate the image file ONLY. They save it next to the page as
  `web/<domain>/<path>/images/<slug>.png`, and append a record to an image ledger shard
  `ledgers/images-<CRAWLER-LETTER>.jsonl` with: source page URL, local page path,
  placeholder description, image prompt used, output image path.
- Image subagents must NOT edit HTML. The owning crawler embeds the finished image into its
  own page afterwards (replace/augment the placeholder box with a relative `<img>` to
  `images/<slug>.png`, keeping the remembered caption). If a crawl page is already finished
  and embedding would race another agent, leave the image file + ledger record and the
  coordinator will embed it during consolidation.
- Generated images are binary files, and the GitHub snapshot push is text-only.
  **Sean's decision (20:25 PDT): commit images as base64 files so they can be pushed directly.**
  Implementation (coordinator, at consolidation / before each push): for every image file
  under `web/**/images/`, create `<image-filename>.b64` (plain base64 text, e.g.
  `hero.png.b64`) in the same `images/` folder, plus record it in
  `ledgers/images-manifest.json` with original filename, mime type, byte size and sha256.
  The `.b64` files + manifest are what get pushed to GitHub alongside the HTML; the binary
  images stay in the local copy, and anyone cloning the repo can decode each `.b64` back to
  the exact image (`base64 -d hero.png.b64 > hero.png`). Crawlers/image agents do not need
  to create `.b64` files themselves — the coordinator generates any missing ones for ALL
  images before a push, so coverage is guaranteed.

## Wave 2 addendum (20:36 PDT) — Orchestrated recursive expansion
Sean's correction: a crawl wave finishing its *assigned* queue is NOT the end of the crawl.
The coordinator (main agent) acts as orchestrator: it computes the true outstanding queue
from BOTH ledger shards AND dangling relative links extracted from built HTML
(`ledgers/queue-snapshot.json`, regenerated each wave), and launches new crawler waves
until the run's time cap. Wave 2 crawlers are F, G, H, I (shards `crawler-F.jsonl` …
`crawler-I.jsonl`, image shards `images-F.jsonl` … `images-I.jsonl`), working alongside
Crawler B which is still running.
- Malformed composite URLs produced by bad relative links (e.g.
  `https://en.wikipedia.org/de.wikipedia.org`, `https://www.facebook.com/www.messenger.com`,
  `https://en.wikipedia.org/wiki/Wikipedia:Contents/Portal:Arts`) are NOT real pages:
  log them `skipped-out-of-scope` with unsure=["malformed relative-link artefact"] and do not
  build them. The intended targets are covered separately.
- Wave 2 crawlers follow the same rules, image rules (unlimited, non-blocking separate
  image subagents), and deadlines (stop starting new pages 21:12 PDT, wrap 21:17 PDT).
  For any page you cannot finish, its outgoing targets go in your shard as `queued` — the
  orchestrator's next snapshot picks them up.

## Summaries
Each crawler returns: pages built (count + list of URLs), pages queued but not built,
biggest uncertainties, and any domains newly reached.

## Run extension (Sean, 20:50 PDT)
- Fleet limit raised from 5 to 10 concurrent crawlers.
- Run cap extended: stop starting new pages at 22:45 PDT 2026-10-17; wrap by 22:50 PDT. (Supersedes the 21:12/21:17 cap for all agents who receive this note.)
- Expansion-fleet crawlers (P onward) work thematic branches from built hub pages; check-before-building remains the collision rule for everyone.

## New branch requested (Sean, 20:53 PDT): Library Genesis
- Seed: gen.lib.rus.ec (Library Genesis) — reproduce the site from memory: homepage/search interface, catalogue/result listings with bibliographic metadata as remembered (title, author, year, publisher, format), and per-book pages with metadata, generated cover images, and descriptions/summaries written from memory.
- Content boundary (same as project rule 5): do NOT reproduce full texts of in-copyright books or papers. Book content = original summaries/descriptions; brief excerpts only for public-domain works. Download/mirror links are reproduced as page elements pointing at local placeholder pages, like other private/logged-in surfaces.
- Assigned to the next free crawler slot (Crawler V) or by redirecting a running crawler, per Sean's choice.
