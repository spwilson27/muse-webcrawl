#!/usr/bin/env python3
import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl")
from bb_engine import build, finish

PAGES = [
{
"slug": "Google_Chrome", "title": "Google Chrome", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_browser",
"imgbox": "The Google Chrome logo: a circle in blue surrounded by red, yellow and green segments",
"infobox": [("Released", "2 September 2008"), ("Developer", "Google"), ("Engine", "Blink, V8 JavaScript engine"), ("Written in", "C++ and others")],
"body": [
"<b>Google Chrome</b> is a [[Web_browser|web browser]] developed by Google. It was first released in 2008 for Microsoft Windows, built with free software components from Apple WebKit and Mozilla [[Firefox]]. It was later ported to Linux, macOS, iOS, and Android, where it is the default browser on many devices.",
"Chrome was released as a surprise: Google had publicly opposed building a browser, and its announcement came via a comic book drawn by Scott McCloud, mailed to journalists. Its technical pitch was speed and stability — a multiprocess architecture isolating each tab, the fast V8 [[JavaScript]] engine, a minimalist interface with a combined address-and-search 'Omnibox', and silent automatic updates. It overtook [[Internet_Explorer]] as the world's most-used browser around 2012 and has held a majority share of global browsing since.",
"Chrome's dominance — roughly two-thirds of the browser market in the 2020s — makes its engine (Blink, forked from WebKit in 2013) close to a web standard in itself, and most rival browsers ([[Microsoft_Edge]], [[Opera_(web_browser)|Opera]], Brave) are now built on its open-source [[Chromium_(web_browser)|Chromium]] base. Critics argue this concentrates power over web standards in Google, whose advertising business also drew scrutiny over Chrome's long-delayed plan to phase out third-party cookies.",
],
"see_also": ["Firefox", "Microsoft_Edge", "Web_browser", "Google_Search", "Safari_(web_browser)"],
"unsure": ["Market share figures vary by measurement service (StatCounter vs others)"],
},
{
"slug": "Firefox", "title": "Firefox", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_browser",
"imgbox": "The Firefox logo: an orange fox encircling a blue globe",
"infobox": [("Released", "9 November 2004 (version 1.0)"), ("Developer", "Mozilla Foundation / Mozilla Corporation"), ("Engine", "Gecko, Quantum"), ("Predecessor", "[[Netscape_Navigator|Netscape]] (via Mozilla Suite)")],
"body": [
"<b>Mozilla Firefox</b>, or simply <b>Firefox</b>, is a free and open-source [[Web_browser|web browser]] developed by the Mozilla Foundation and its subsidiary, the Mozilla Corporation. It is available for Windows, macOS, Linux and mobile platforms, and uses the Gecko rendering engine to display web pages.",
"Firefox descends from [[Netscape_Navigator|Netscape]], whose code Mozilla open-sourced in 1998. Written by Dave Hyatt and Blake Ross as a lightweight experimental branch (first named Phoenix, then Firebird, then Firefox to avoid trademark clashes), it reached version 1.0 in November 2004 and — faster, tabbed and more secure than the then-dominant [[Internet_Explorer]] — won tens of millions of users, breaking the Microsoft monopoly and reigniting the browser wars.",
"Its share peaked around 2009–2010 at roughly a third of the market before [[Google_Chrome]] overtook it. Firefox remains the only major browser with an independent engine (Gecko/Quantum, with large parts rewritten in Rust after the 2017 'Quantum' release), a fact its supporters cite as essential to keeping the web an open, multi-implementation platform rather than a monoculture. Mozilla funds development largely through search-placement deals, principally with Google — its chief competitor.",
],
"see_also": ["Google_Chrome", "Netscape_Navigator", "Web_browser", "Mozilla", "Internet_Explorer"],
"unsure": ["Whether 'Mozilla' exists as a page in this crawl; share peak figures are approximate"],
},
{
"slug": "Safari_(web_browser)", "title": "Safari (web browser)", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_browser",
"imgbox": "The Safari logo: a silver compass with a red and white needle",
"infobox": [("Released", "7 January 2003"), ("Developer", "Apple Inc."), ("Engine", "WebKit"), ("Platforms", "macOS, iOS, iPadOS")],
"body": [
"<b>Safari</b> is a graphical [[Web_browser|web browser]] developed by Apple. It is built into Apple's operating systems since Mac OS X Panther (2003) and is the default browser on Macs, iPhones and iPads — which makes it, thanks to the iPhone, the second most-used browser family in the world.",
"Safari's rendering engine, WebKit, was forked by Apple from the open-source KHTML engine of the KDE project; WebKit later became the ancestor of [[Google_Chrome|Chrome's]] original engine, and even after Google forked it into Blink, WebKit remained the required engine for every browser on iOS. Steve Jobs announced Safari at Macworld 2003 as Apple's answer to the ageing [[Internet_Explorer]] for Mac, touting its speed; a Windows version appeared in 2007 and was discontinued in 2012.",
"Privacy has been Safari's signature battleground: its Intelligent Tracking Prevention (from 2017) blocks cross-site tracking cookies by default, forcing the advertising industry to adapt, and its privacy reports show users what was blocked. Web developers periodically debate Apple's pace on new web features, making Safari the target of an 'is Safari the new IE?' argument that resurfaces every few years.",
],
"see_also": ["Google_Chrome", "Firefox", "Web_browser", "Internet_Explorer"],
"unsure": [],
},
{
"slug": "Microsoft_Edge", "title": "Microsoft Edge", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_browser",
"imgbox": "The Microsoft Edge logo: a stylised blue-green wave forming the letter e",
"infobox": [("Released", "29 July 2015 (with Windows 10)"), ("Developer", "Microsoft"), ("Engine", "EdgeHTML (2015–2019); Blink ([[Chromium_(web_browser)|Chromium]]) since 2020")],
"body": [
"<b>Microsoft Edge</b> is a proprietary cross-platform [[Web_browser|web browser]] developed by Microsoft. Released in 2015 as the successor to [[Internet_Explorer]], it is the default browser on Windows 10 and 11, and is also available on macOS, Linux and mobile platforms.",
"The original Edge, codenamed Spartan, was a clean break: a new engine (EdgeHTML), a stripped-down interface, and features such as reading mode, annotation and Cortana integration. It failed to win back users from [[Google_Chrome]] or to keep developers testing for it, so in December 2018 Microsoft made the once-unthinkable announcement that Edge would be rebuilt on the open-source [[Chromium_(web_browser)|Chromium]] project — the basis of Chrome itself. The Chromium-based Edge launched in January 2020 to generally positive reviews, and has since been augmented with vertical tabs, built-in shopping tools, and aggressive integration of Microsoft's Copilot AI assistant.",
"Edge's share sits in the single digits globally despite being preinstalled on every Windows PC — a position its critics call default-by-inertia and its prompts to switch have drawn regulatory attention in the EU. Its rise nonetheless completed the web's shift to a Chromium near-monoculture, with [[Firefox]] and [[Safari_(web_browser)|Safari]] the holdouts.",
],
"see_also": ["Internet_Explorer", "Google_Chrome", "Web_browser", "Chromium_(web_browser)"],
"unsure": ["Exact global share figures vary by source and year"],
},
{
"slug": "Internet_Explorer", "title": "Internet Explorer", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_browser",
"imgbox": "The Internet Explorer logo: a blue lowercase e with a gold ring orbiting it",
"infobox": [("Released", "16 August 1995"), ("Developer", "Microsoft"), ("Discontinued", "15 June 2022 (most Windows versions)"), ("Successor", "[[Microsoft_Edge]]")],
"body": [
"<b>Internet Explorer</b> (formerly Microsoft Internet Explorer, commonly abbreviated <b>IE</b>) is a discontinued series of graphical [[Web_browser|web browsers]] developed by Microsoft, part of the Windows operating system line from 1995 to 2022.",
"IE began as licensed code from Spyglass's [[Mosaic_(web_browser)|Mosaic]], and Microsoft pursued [[Netscape_Navigator|Netscape]] with relentless iteration and a decisive weapon: it was bundled free with Windows. Versions 4 and 5 won the first browser war, and at its 2002–2003 peak IE held about 95% of the browser market. That dominance — and the bundling that achieved it — was central to the United States v. Microsoft antitrust case.",
"Victory bred stagnation: after IE6 (2001) development nearly stopped for five years, security holes multiplied, and web developers despaired of its non-standard rendering, which 'quirks mode' preserved for a generation of sites. [[Firefox]] (2004) and then [[Google_Chrome]] (2008) dismantled its share; Microsoft retired the brand in favour of [[Microsoft_Edge]], and on 15 June 2022 Internet Explorer was disabled on mainstream Windows, ending a 27-year run — mourned ironically by the developers who had cursed it, many in South Korea and in corporate intranets where it lingered longest.",
],
"see_also": ["Microsoft_Edge", "Netscape_Navigator", "Firefox", "Google_Chrome", "Mosaic_(web_browser)"],
"unsure": ["Peak share (~95%) is the commonly cited figure"],
},
{
"slug": "Netscape_Navigator", "title": "Netscape Navigator", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_browser",
"imgbox": "The Netscape Navigator logo: a capital N on a teal hill under a starry sky",
"infobox": [("Released", "15 December 1994"), ("Developer", "[[Netscape_Communications|Netscape Communications]]"), ("Final release", "Version 9 (2007–2008)"), ("Successor", "[[Firefox]] (via Mozilla)")],
"body": [
"<b>Netscape Navigator</b> was a proprietary [[Web_browser|web browser]] that was the dominant browser in the mid-1990s and the flagship product of [[Netscape_Communications]]. It was based on the code of [[Mosaic_(web_browser)|Mosaic]], which several of its authors had created at the University of Illinois.",
"Navigator 1.0 shipped in December 1994 with innovations — on-the-fly page display as images loaded, then cookies, [[JavaScript]] (created by Brendan Eich in ten days in 1995), and eventually the browser as a platform for applications — that essentially defined the web experience. Netscape's August 1995 IPO, in which the stock doubled on its first day, is generally taken as the starting gun of the dot-com boom.",
"The 'browser wars' followed: Microsoft's [[Internet_Explorer]], bundled with Windows, eroded Netscape's share from around 90% to almost nothing by 2001. Netscape's lasting legacies were the release of its code as open source (Mozilla, ancestor of [[Firefox]]), JavaScript, the SSL protocol behind [[HTTPS]], and the proof that the web browser was the most important software in the world. AOL acquired Netscape in 1999; the Navigator brand was finally discontinued in 2008.",
],
"see_also": ["Netscape_Communications", "Internet_Explorer", "Firefox", "Marc_Andreessen", "Mosaic_(web_browser)"],
"unsure": ["'90% share' peak is the standard retelling; exact figures are estimates"],
},
{
"slug": "Netscape_Communications", "title": "Netscape Communications", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Netscape_Navigator",
"imgbox": "Photograph of the Netscape headquarters campus sign in Mountain View, California, in the 1990s",
"infobox": [("Founded", "4 April 1994, Mountain View, California"), ("Founders", "[[Marc_Andreessen]], Jim Clark"), ("IPO", "9 August 1995"), ("Fate", "Acquired by AOL (announced 1998, closed 1999); brand retired 2008")],
"body": [
"<b>Netscape Communications Corporation</b> was an American independent computer services company whose [[Netscape_Navigator|Navigator]] [[Web_browser|browser]] ignited the commercial [[World_Wide_Web]]. It was founded in April 1994 as Mosaic Communications Corporation by Silicon Graphics founder Jim Clark and [[Marc_Andreessen]], co-author of the [[Mosaic_(web_browser)|Mosaic]] browser, who recruited much of the original Mosaic team from the University of Illinois.",
"The company's August 1995 initial public offering is one of the famous events of business history: a 16-month-old company with no profits saw its shares jump from $28 to $75 on the first day, giving it a market value near $3 billion, and popular accounts date the dot-com era from that morning. Netscape raced Microsoft through the browser wars, contributed foundational web technologies — [[JavaScript]], cookies, SSL — and, losing the distribution war to the Windows bundle, open-sourced its browser code in 1998 as the Mozilla project.",
"AOL acquired Netscape in a stock deal valued at about $4.2 billion (announced November 1998). The company faded as a force, but its legacy — [[Firefox]], the open web's standardisation culture, and a generation of founders and engineers — radiates through Silicon Valley to this day.",
],
"see_also": ["Netscape_Navigator", "Marc_Andreessen", "Firefox", "Internet_Explorer"],
"unsure": ["Acquisition value is variously reported (~$4.2B in stock at announcement; higher by closing)"],
},
{
"slug": "Marc_Andreessen", "title": "Marc Andreessen", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Netscape_Communications",
"imgbox": "Portrait photograph of Marc Andreessen, a tall bald man in a dark shirt, speaking at a technology conference",
"infobox": [("Born", "9 July 1971, Cedar Falls, Iowa, US"), ("Known for", "Co-creating [[Mosaic_(web_browser)|Mosaic]]; co-founding [[Netscape_Communications|Netscape]] and Andreessen Horowitz")],
"body": [
"<b>Marc Lowell Andreessen</b> (born 1971) is an American businessman and software engineer. In 1993, as an undergraduate staff member at the National Center for Supercomputing Applications (NCSA) at the University of Illinois, he co-authored [[Mosaic_(web_browser)|Mosaic]] — with Eric Bina, the first widely used graphical [[Web_browser|web browser]] — the program that introduced images inline in web pages and brought the [[World_Wide_Web]] to the general public.",
"After graduating he moved to California and co-founded [[Netscape_Communications]] with Jim Clark, leading the development of [[Netscape_Navigator]]. Netscape's 1995 IPO made him, at 24, the public face of the Internet generation (a barefoot appearance on the cover of Time followed). After AOL acquired Netscape, he served as its chief technology officer, then co-founded Loudcloud/Opsware (sold to HP for about $1.6 billion in 2007), co-created the Ning platform, and in 2009 co-founded the venture capital firm Andreessen Horowitz (a16z) with Ben Horowitz, which became one of Silicon Valley's most influential firms.",
"Andreessen is also known as an essayist: his 2011 'Software Is Eating the World' is among the most quoted technology essays, and his 2023 'Techno-Optimist Manifesto' argued for unapologetic technological acceleration — positions that keep him a central, and contested, figure in debates about the industry's direction.",
],
"see_also": ["Netscape_Communications", "Netscape_Navigator", "Mosaic_(web_browser)", "Firefox"],
"unsure": ["Cover details and sale prices recalled from standard accounts"],
},
{
"slug": "Opera_(web_browser)", "title": "Opera (web browser)", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_browser",
"imgbox": "The Opera logo: a red letter O with a cut-out on its right side",
"infobox": [("Released", "10 April 1995"), ("Developer", "Opera Software (Norway)"), ("Engine", "Presto (until 2013); Blink ([[Chromium_(web_browser)|Chromium]]) since")],
"body": [
"<b>Opera</b> is a multi-platform [[Web_browser|web browser]] developed by Opera Software, a Norwegian company founded by Jon Stephenson von Tetzchner and Geir Ivarsøy out of a research project at Telenor. First released publicly in 1996 (developed from 1994), Opera is one of the oldest browsers still in production.",
"Opera pioneered features that later became universal: tabbed browsing (2000), a built-in pop-up blocker, page zoom, mouse gestures, a download manager, and 'speed dial' start pages. Its small size made it a favourite on early mobile phones (Opera Mini, 2005, compressed pages through proxy servers to slash data costs — transformative in Africa and Asia where bandwidth was dear) and on games consoles and embedded devices.",
"In 2013 Opera abandoned its own Presto engine for [[Google_Chrome|Chromium's]] Blink, shedding some distinctiveness for compatibility; a Chinese consortium acquired the browser business in 2016. Opera has since repositioned around built-in services — a free VPN, ad blocking, crypto wallet, and the AI-focused Opera One redesign — holding a small but durable global share, with particular strength in Africa and Asia.",
],
"see_also": ["Google_Chrome", "Firefox", "Web_browser", "Chromium_(web_browser)"],
"unsure": ["Opera Mini user figures and regional shares are approximate"],
},
{
"slug": "Internet_Archive", "title": "Internet Archive", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Photograph of the Internet Archive's headquarters, a former church with white columns in San Francisco",
"infobox": [("Founded", "May 1996"), ("Founder", "Brewster Kahle"), ("Headquarters", "San Francisco, California"), ("Collections", "Web pages, books, audio, video, software")],
"body": [
"The <b>Internet Archive</b> is an American nonprofit digital library with the mission of 'universal access to all knowledge'. Founded in 1996 by Brewster Kahle, it provides free public access to collections of digitised materials, including websites, software applications, music, audiovisual recordings and millions of books.",
"Its best-known service is the [[Wayback_Machine]], an archive of the [[World_Wide_Web]] holding hundreds of billions of captured web pages. Beyond the web, the Archive scans and lends books (its Open Library project), preserves early software and games playable in the browser, and hosts vast collections of live music, public-domain film and television news recordings — used by researchers to study everything from propaganda to broadcast history.",
"The Archive's 'controlled digital lending' of scanned books brought it into conflict with publishers: in the 2020 Hachette v. Internet Archive case, US courts ruled against its lending of scanned print books, a major legal setback. The Archive remains, nonetheless, the closest thing the Internet has to a memory: a recognition that on a network where the average [[Web_page|page]] vanishes or changes within months, preservation does not happen by itself.",
],
"see_also": ["Wayback_Machine", "World_Wide_Web", "Search_engine", "Archie_(search_engine)"],
"unsure": ["Holdings counts (hundreds of billions of pages) grow constantly; the Hachette ruling (2023 district court, affirmed 2024) is recalled in outline"],
},
{
"slug": "Wayback_Machine", "title": "Wayback Machine", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet_Archive",
"imgbox": "Screenshot-style image of the Wayback Machine calendar interface showing capture dates for a website",
"infobox": [("Launched", "2001 (public access)"), ("Operator", "[[Internet_Archive]]"), ("Purpose", "Preserving snapshots of websites")],
"body": [
"The <b>Wayback Machine</b> is a digital archive of the [[World_Wide_Web]] built by the [[Internet_Archive]]. Launched publicly in 2001 (its crawls reach back to 1996), it allows users to go 'back in time' to see how websites looked in the past.",
"Anyone can enter a [[Uniform_Resource_Locator|URL]] and browse a calendar of captures: snapshots of pages — HTML, images and stylesheets — recorded by the Archive's crawlers or submitted by users through 'Save Page Now'. The archive holds hundreds of billions of pages, and researchers use it to recover deleted pages, verify what a site said on a given date, and study the web's own history; lawyers use it as evidence, and journalists to hold officials to their earlier statements.",
"The Wayback Machine honours some exclusions (historically robots.txt, and removal requests), and its completeness is patchy — deep pages, paywalled content and interactive applications survive poorly. But as link rot steadily erases the early web, the Wayback Machine has become the default time machine of the Internet age, and a working argument that someone must deliberately keep the copies.",
],
"see_also": ["Internet_Archive", "World_Wide_Web", "Uniform_Resource_Locator"],
"unsure": ["Snapshot counts change daily"],
},
{
"slug": "DuckDuckGo", "title": "DuckDuckGo", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Search_engine",
"imgbox": "The DuckDuckGo logo: a white duck's head with a red bow tie in a red circle",
"infobox": [("Founded", "2008"), ("Founder", "Gabriel Weinberg"), ("Type", "Search engine and browser; privacy-focused"), ("Mascot", "Dax the duck")],
"body": [
"<b>DuckDuckGo</b> is an American software company whose eponymous search engine is notable for not tracking its users. While other search engines log queries, build profiles and personalise results, DuckDuckGo does not store IP addresses or user information, does not create search profiles, and shows the same results to everyone — a stance summed up in its slogan and its duck mascot.",
"Founded by Gabriel Weinberg in 2008 and named (loosely) after the children's game 'duck, duck, goose', it grew slowly until the 2013 Snowden revelations made search privacy a mainstream concern, after which its traffic multiplied. Results draw on its own crawler and hundreds of sources including Microsoft's [[Bing_(search_engine)|Bing]] index under licence, supplemented by instant answers and '!bang' shortcuts that redirect a query to another site's own search.",
"DuckDuckGo has extended into browser apps and extensions that block trackers, and a desktop browser; its share of searches remains a few percent at most against [[Google_Search|Google]], but it is the most prominent proof that a search engine can run as a business on contextual advertising alone, without surveillance of its users.",
],
"see_also": ["Search_engine", "Google_Search", "Bing_(search_engine)", "Web_browser"],
"unsure": ["Share figures are a low single-digit percentage depending on market"],
},
{
"slug": "Bing_(search_engine)", "title": "Bing (search engine)", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Search_engine",
"imgbox": "Screenshot-style image of the Bing homepage with a scenic daily background photograph and search box",
"infobox": [("Launched", "3 June 2009"), ("Owner", "Microsoft"), ("Predecessors", "MSN Search, Windows Live Search, Live Search")],
"body": [
"<b>Microsoft Bing</b>, commonly referred to as <b>Bing</b>, is a web search engine owned and operated by Microsoft. It was unveiled by CEO Steve Ballmer in 2009 as the successor to Microsoft's earlier search services, and is the second largest search engine in most Western markets — though a distant second to [[Google_Search|Google]].",
"Bing distinguished itself with a photographic homepage (a daily image with embedded trivia), decision-oriented features for travel and shopping, and integration across Microsoft's products: it is the default search in [[Microsoft_Edge]] and Windows, powers voice assistants, and under licence supplies results to [[DuckDuckGo]], Yahoo! and others. A 2009 deal made Bing the search backend for Yahoo! Search as well, consolidating the non-Google market around Microsoft's index.",
"In February 2023 Bing became the public face of Microsoft's AI push when it relaunched with a built-in chat assistant ('the new Bing') based on OpenAI's large language models, briefly making Bing a contender in the AI race before the technology was folded into the broader Copilot brand. Despite decades of investment, its share of global searches remains in the low single digits — the measure of [[Google_Search|Google's]] entrenchment.",
],
"see_also": ["Google_Search", "DuckDuckGo", "Search_engine", "Microsoft_Edge"],
"unsure": ["Market share phrasing kept deliberately general"],
},
{
"slug": "AltaVista", "title": "AltaVista", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Search_engine",
"imgbox": "The AltaVista logo from the late 1990s: the word AltaVista with a mountain peak over the V",
"body": [
"<b>AltaVista</b> was a web search engine established in 1995 by researchers at Digital Equipment Corporation (DEC). It was one of the most popular search engines of the early web, and for a time the most capable: at launch it indexed some 16 million pages — far more than rivals — and answered queries in fractions of a second from DEC's powerful Alpha servers.",
"AltaVista pioneered features users still expect: full-text indexing of the whole web, a simple uncluttered search page (a lesson [[Google_Search|Google]] would perfect), advanced query operators, and the Babel Fish machine-translation service (1997), the first of its kind. Its name, Spanish for 'high view', came from its Palo Alto surroundings.",
"The service declined through a chain of ownership — DEC to Compaq (1998), sale to CMGI (1999), a portal-era cluttering of its homepage, then Overture and Yahoo! (2003) — while Google's cleaner results and PageRank left it behind. Yahoo! finally shut AltaVista down on 8 July 2013, redirecting it to Yahoo! Search; it is remembered as the search engine that proved the web could be indexed at scale, a decade-defining product undone by corporate drift.",
],
"see_also": ["Search_engine", "Google_Search", "Lycos", "Bing_(search_engine)"],
"unsure": ["Launch index size (16 million pages) is the commonly cited figure"],
},
{
"slug": "Lycos", "title": "Lycos", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Search_engine",
"imgbox": "The Lycos logo with its black Labrador mascot and the slogan 'Go get it'",
"body": [
"<b>Lycos</b> is a web search engine and web portal established in 1994. Developed at Carnegie Mellon University by Michael L. Mauldin, it began as a university research project to measure and index the size of the young [[World_Wide_Web]] — its name derives from <i>Lycosidae</i>, the wolf spider family, a spider being the natural mascot for software that crawls the web.",
"Spun out as a company in 1995, Lycos was among the first search engines to turn a profit and one of the most visited sites of the early web, expanding into a portal of email (Lycos Mail), web hosting (Tripod, Angelfire) and community services. At the peak of the dot-com bubble in 2000 it was acquired by Spain's Terra Networks in a stock deal valued around $12.5 billion — then one of the largest Internet acquisitions ever — before the crash destroyed most of that value.",
"The Lycos brand and assets passed through Daum (2004) and Ybrant Digital (2010), shrinking to a small search and advertising business. Lycos's historical importance is as an elder of web search: it demonstrated, years before [[Google_Search|Google]], that indexing the web could be a business — though not yet which kind of business would win.",
],
"see_also": ["Search_engine", "AltaVista", "Google_Search", "World_Wide_Web"],
"unsure": ["Terra acquisition value is as reported at announcement (~$12.5B in stock)"],
},
]

for p in PAGES:
    build(p)
finish()
