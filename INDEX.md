# muse-webcrawl — Index

Rebuilding the web from memory, starting from Wikipedia. Every page under `web/`
was recreated from model memory as standalone HTML — no live fetching — with
generated images, a full traversal ledger, and an independent audit.

- **Seed:** https://en.wikipedia.org/
- **Run 1:** 2026-10-17 evening — 4,487 pages, 109 domains
- **Run 2:** 2026-10-17 22:14 → 2026-10-18 00:05 PDT — queue fully resolved
- **Totals after Run 2:** 9183 pages · 154 domains · 3323 image files
- **Master ledger:** `ledger.json` (merged from all `ledgers/crawler-*.jsonl` shards; per-image records in `ledgers/images-*.jsonl`, manifest in `ledgers/images-manifest.json`)
- **Machine-readable site index:** `sitemap.json` (drives the browsing UI in `index.html`)
- **Audit:** `audit/AUDIT_LEDGER.md` — 411 pages sampled: 301 close, 100 broadly-right, 10 divergent, 0 largely-invented
- **Next queue:** `ledgers/queue-snapshot-run3.json` (top dangling-link targets by inbound count + unbuilt leftovers)

## Pages by domain

| Domain | Pages | Images |
|---|---:|---:|
| en.wikipedia.org | 8102 | 2995 |
| gen.lib.rus.ec | 372 | 135 |
| sci-hub.se | 59 | 7 |
| www.nasa.gov | 19 | 5 |
| nasa.gov | 17 | 4 |
| science.nasa.gov | 13 | 11 |
| www.esa.int | 11 | 5 |
| www.nytimes.com | 11 | 1 |
| www.cnn.com | 10 | 1 |
| www.nature.com | 10 | 1 |
| www.tesla.com | 10 | 5 |
| en.wikivoyage.org | 9 | 5 |
| apnews.com | 8 | 1 |
| commons.wikimedia.org | 8 | 5 |
| www.aljazeera.com | 8 | 1 |
| www.apple.com | 8 | 3 |
| www.bbc.com | 8 | 3 |
| www.theguardian.com | 8 | 1 |
| www.amazon.com | 7 | 6 |
| www.foxnews.com | 7 | 2 |
| www.latimes.com | 7 | 3 |
| www.reuters.com | 7 | 1 |
| www.washingtonpost.com | 7 | 2 |
| www.wikidata.org | 7 | 1 |
| abcnews.go.com | 6 | 2 |
| elpais.com | 6 | 0 |
| github.com | 6 | 1 |
| meta.wikimedia.org | 6 | 0 |
| news.sky.com | 6 | 2 |
| nypost.com | 6 | 2 |
| time.com | 6 | 2 |
| timesofindia.indiatimes.com | 6 | 0 |
| www.cbsnews.com | 6 | 2 |
| www.chicagotribune.com | 6 | 2 |
| www.economist.com | 6 | 2 |
| www.euronews.com | 6 | 0 |
| www.france24.com | 6 | 0 |
| www.ft.com | 6 | 3 |
| www.huffpost.com | 6 | 0 |
| www.independent.co.uk | 6 | 2 |
| www.mirror.co.uk | 6 | 3 |
| www.nbcnews.com | 6 | 2 |
| www.newyorker.com | 6 | 2 |
| www.npr.org | 6 | 2 |
| www.scmp.com | 6 | 0 |
| www.smh.com.au | 6 | 0 |
| www.telegraph.co.uk | 6 | 2 |
| www.theglobeandmail.com | 6 | 0 |
| www.thehindu.com | 6 | 2 |
| www.thesun.co.uk | 6 | 2 |
| www.thetimes.co.uk | 6 | 4 |
| www.usatoday.com | 6 | 3 |
| www.wsj.com | 6 | 3 |
| en.wikisource.org | 5 | 0 |
| tass.com | 5 | 0 |
| www.afp.com | 5 | 0 |
| www.axios.com | 5 | 2 |
| www.bloomberg.com | 5 | 2 |
| www.dailymail.co.uk | 5 | 0 |
| www.dw.com | 5 | 0 |
| www.haaretz.com | 5 | 0 |
| www.lemonde.fr | 5 | 0 |
| www.mediawiki.org | 5 | 1 |
| www.msnbc.com | 5 | 0 |
| www.politico.com | 5 | 2 |
| www.propublica.org | 5 | 0 |
| www.spiegel.de | 5 | 0 |
| www.theatlantic.com | 5 | 2 |
| www.xinhuanet.com | 5 | 0 |
| aws.amazon.com | 4 | 1 |
| en.wikibooks.org | 4 | 0 |
| en.wiktionary.org | 4 | 1 |
| play.google.com | 4 | 0 |
| species.wikimedia.org | 4 | 2 |
| store.steampowered.com | 4 | 2 |
| www.costco.com | 4 | 0 |
| www.instagram.com | 4 | 3 |
| www.khanacademy.org | 4 | 0 |
| www.linkedin.com | 4 | 1 |
| www.nvidia.com | 4 | 2 |
| www.walmart.com | 4 | 1 |
| www.youtube.com | 4 | 6 |
| www3.nhk.or.jp | 4 | 0 |
| de.wikipedia.org | 3 | 1 |
| en.wikinews.org | 3 | 0 |
| en.wikiquote.org | 3 | 0 |
| es.wikipedia.org | 3 | 1 |
| fr.wikipedia.org | 3 | 1 |
| home.cern | 3 | 1 |
| ja.wikipedia.org | 3 | 1 |
| ru.wikipedia.org | 3 | 0 |
| www.adobe.com | 3 | 1 |
| www.bestbuy.com | 3 | 0 |
| www.delta.com | 3 | 0 |
| www.ebay.com | 3 | 0 |
| www.facebook.com | 3 | 4 |
| www.google.com | 3 | 2 |
| www.ibm.com | 3 | 1 |
| www.meta.com | 3 | 1 |
| www.microsoft.com | 3 | 1 |
| www.mozilla.org | 3 | 0 |
| www.oracle.com | 3 | 0 |
| www.samsung.com | 3 | 0 |
| www.snapchat.com | 3 | 1 |
| www.target.com | 3 | 0 |
| www.tiktok.com | 3 | 3 |
| www.whatsapp.com | 3 | 1 |
| x.com | 3 | 0 |
| zh.wikipedia.org | 3 | 0 |
| about.google | 2 | 0 |
| accounts.google.com | 2 | 0 |
| en.wikiversity.org | 2 | 0 |
| music.youtube.com | 2 | 4 |
| news.google.com | 2 | 0 |
| open.spotify.com | 2 | 4 |
| scholar.google.com | 2 | 0 |
| www.berkshirehathaway.com | 2 | 0 |
| www.disneyplus.com | 2 | 0 |
| www.harvard.edu | 2 | 2 |
| www.intel.com | 2 | 0 |
| www.messenger.com | 2 | 1 |
| www.mit.edu | 2 | 1 |
| www.netflix.com | 2 | 5 |
| www.reddit.com | 2 | 1 |
| www.stanford.edu | 2 | 0 |
| www.tsmc.com | 2 | 1 |
| about.meta.com | 1 | 3 |
| ar.wikipedia.org | 1 | 0 |
| docs.google.com | 1 | 0 |
| drive.google.com | 1 | 0 |
| ekantipur.com | 1 | 0 |
| it.wikipedia.org | 1 | 0 |
| mail.google.com | 1 | 0 |
| maps.google.com | 1 | 0 |
| nl.wikipedia.org | 1 | 0 |
| old.reddit.com | 1 | 0 |
| pl.wikipedia.org | 1 | 0 |
| pt.wikipedia.org | 1 | 0 |
| pubmed.ncbi.nlm.nih.gov | 1 | 0 |
| query.wikidata.org | 1 | 0 |
| wikimediafoundation.org | 1 | 0 |
| www.ams.org | 1 | 0 |
| www.apache.org | 1 | 0 |
| www.ligo.org | 1 | 1 |
| www.linuxfoundation.org | 1 | 0 |
| www.ncbi.nlm.nih.gov | 1 | 0 |
| www.nhm.ac.uk | 1 | 1 |
| www.nic.net.np | 1 | 0 |
| www.royalsociety.org | 1 | 0 |
| www.rsc.org | 1 | 0 |
| www.thewaltdisneycompany.com | 1 | 1 |
| www.threads.net | 1 | 0 |
| www.thunderbird.net | 1 | 0 |
| www.wikipedia.org | 1 | 1 |
| **Total** | **9183** | **3323** |
