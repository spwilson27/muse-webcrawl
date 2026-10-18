#!/usr/bin/env python3
import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl")
from bb_engine import build, finish

PAGES = [
{
"slug": "HTTPS", "title": "HTTPS", "depth": 3,
"source": "https://en.wikipedia.org/wiki/HTTP",
"imgbox": "Browser address bar showing a padlock icon and an https:// address",
"infobox": [("Full name", "Hypertext Transfer Protocol Secure"), ("Port", "443"), ("Encryption", "TLS"), ("Introduced", "1994 (Netscape)")],
"body": [
"<b>Hypertext Transfer Protocol Secure</b> (<b>HTTPS</b>) is an extension of the [[HTTP|Hypertext Transfer Protocol]] in which the communication is encrypted using Transport Layer Security (TLS), the successor of the Secure Sockets Layer (SSL) protocol. It is used to protect the privacy and integrity of exchanged data between a user's [[Web_browser|browser]] and a [[Website|website]] — against eavesdroppers, tampering and impersonation on networks such as public [[Wi-Fi]].",
"When a browser connects to an HTTPS site, the server presents a digital certificate, issued by a trusted certificate authority, attesting that it controls the domain; the two sides then negotiate encryption keys (today, usually TLS 1.2 or 1.3) and the HTTP conversation proceeds inside the encrypted tunnel, conventionally on port 443. The padlock icon in the address bar signals the result.",
"HTTPS was created by Netscape in 1994 for its Navigator browser and was long reserved for logins and payments, because certificates cost money and encryption cost processor time. That changed with free, automated certificate authorities — notably Let's Encrypt (2015) — and with browsers marking plain-HTTP pages 'not secure'; by the early 2020s the overwhelming majority of web traffic was encrypted, and HTTPS became a precondition for modern browser features and good search ranking.",
],
"see_also": ["HTTP", "World_Wide_Web", "Web_browser", "Uniform_Resource_Locator"],
"unsure": ["Exact percentage of page loads using HTTPS varies by browser telemetry"],
},
{
"slug": "Hypertext", "title": "Hypertext", "depth": 3,
"source": "https://en.wikipedia.org/wiki/World_Wide_Web",
"imgbox": "Diagram of hypertext documents connected by highlighted links in a web-like graph",
"body": [
"<b>Hypertext</b> is text displayed on a computer display or other electronic device with references (hyperlinks) to other text that the reader can immediately access. Hypertext documents are interconnected in a structure that need not be linear like a book: readers choose their own paths through a network of information.",
"The idea has a long intellectual lineage, from Vannevar Bush's hypothetical Memex machine (1945) — a desk of linked microfilm — to [[Ted_Nelson]], who coined the words 'hypertext' and 'hypermedia' in the 1960s and pursued the vision for decades in his Project Xanadu, with its ambitions of two-way links, transclusion and micropayments for quoted content. Douglas Engelbart's NLS system demonstrated working hypertext in the famous 1968 'Mother of All Demos', and Apple's HyperCard (1987) brought a popular form of it to personal computers.",
"Hypertext became a planetary medium when [[Tim_Berners-Lee]] implemented a simple, one-way, decentralised version of it at CERN in 1989–1991: the [[World_Wide_Web]], with its documents in [[HTML]], addresses in [[Uniform_Resource_Locator|URLs]] and transport in [[HTTP]]. Nelson's richer design was never finished; Berners-Lee's simpler one conquered the world — a recurring lesson in the history of technology.",
],
"see_also": ["World_Wide_Web", "HTML", "Ted_Nelson", "Tim_Berners-Lee", "Uniform_Resource_Locator"],
"unsure": ["Nelson coined 'hypertext' around 1963-1965; sources differ on the exact year of first use"],
},
{
"slug": "Uniform_Resource_Locator", "title": "Uniform Resource Locator", "depth": 3,
"source": "https://en.wikipedia.org/wiki/World_Wide_Web",
"imgbox": "Diagram of a URL broken into parts: scheme, host, port, path, query and fragment",
"infobox": [("Abbreviation", "URL"), ("Standard", "RFC 3986 (URI); WHATWG URL Standard")],
"body": [
"A <b>Uniform Resource Locator</b> (<b>URL</b>), colloquially known as a <b>web address</b>, is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it. A URL is a specific type of Uniform Resource Identifier (URI), and is the fundamental addressing system of the [[World_Wide_Web]].",
"A URL such as <i>https://www.example.com:443/path/page?query=1#section</i> consists of a <b>scheme</b> (https), a <b>host</b> (a [[Domain_name|domain name]] or [[IP_address|IP address]]), an optional <b>port</b>, a <b>path</b>, an optional <b>query string</b> and an optional <b>fragment</b> identifying a part of the resource. The browser resolves the host through the [[Domain_Name_System|DNS]], connects — for [[HTTPS]], negotiating encryption — and requests the path with [[HTTP]].",
"URLs were defined by [[Tim_Berners-Lee]] and standardised in the 1990s (RFC 1738, later subsumed into the URI standard RFC 3986; browsers today follow the WHATWG URL Standard). Berners-Lee later apologised for the double slash after the scheme, calling it a pointless wart. URLs appear everywhere from advertisements to QR codes, and their design — readable, hierarchical, hackable — shaped how the web grew.",
],
"see_also": ["World_Wide_Web", "Domain_name", "HTTP", "Hypertext", "Web_page"],
"unsure": [],
},
{
"slug": "Web_page", "title": "Web page", "depth": 3,
"source": "https://en.wikipedia.org/wiki/World_Wide_Web",
"imgbox": "Screenshot-style image of a typical web page with header, navigation, article text and sidebar",
"body": [
"A <b>web page</b> (or <b>webpage</b>) is a document on the [[World_Wide_Web]] that is identified by a unique [[Uniform_Resource_Locator|uniform resource locator]] (URL). Web pages are accessed with a [[Web_browser|web browser]] and can include text, images, video and interactive elements; together, the pages under one domain form a [[Website|website]].",
"A page is usually written in [[HTML]], which describes its structure, styled with [[CSS]], and made interactive with [[JavaScript]]. When a browser visits a URL it requests the page over [[HTTP]] (today usually [[HTTPS]]), receives the HTML, then fetches the images, stylesheets and scripts the page references, and renders the result. Pages may be <b>static</b> — the same file served to everyone — or <b>dynamic</b>, generated on the fly by a [[Web_server|web server]] from databases and templates, or assembled in the browser by client-side code (a 'web application').",
"The very first web page, created by [[Tim_Berners-Lee]] at CERN in 1991, explained what the World Wide Web was and how to use it; a copy is preserved at its original address at info.cern.ch. From that single document the web grew to billions of pages within a generation.",
],
"see_also": ["Website", "HTML", "Web_browser", "World_Wide_Web", "Uniform_Resource_Locator"],
"unsure": [],
},
{
"slug": "Website", "title": "Website", "depth": 3,
"source": "https://en.wikipedia.org/wiki/World_Wide_Web",
"imgbox": "Collage-style image of several well-known website homepages as browser windows",
"body": [
"A <b>website</b> is a collection of [[Web_page|web pages]] and related content that is identified by a common [[Domain_name|domain name]] and published on at least one [[Web_server|web server]], accessible via the [[World_Wide_Web]]. Examples of notable websites are Wikipedia, Google, Amazon and YouTube.",
"A website is typically dedicated to a particular topic or purpose, such as news, education, commerce, entertainment or social networking; hyperlinking between its pages guides the visitor's navigation, usually starting from a home page. Websites can be the work of an individual, a business or an organisation, and are hosted on servers ranging from a single home computer — the first sites of the early 1990s — to vast cloud platforms serving billions of requests.",
"The first website, built by [[Tim_Berners-Lee]] at CERN, went live in 1991 to explain the web project itself. By the mid-1990s the web had commercialised explosively (the 'dot-com boom'), and websites became the default public face of organisations. Today there are on the order of two billion websites, though only a fraction are actively maintained; the rest are parked, abandoned or forgotten corners of the largest information system ever built.",
],
"see_also": ["Web_page", "World_Wide_Web", "Domain_name", "Web_server"],
"unsure": ["Total website counts (~2 billion) are estimates from survey scans"],
},
{
"slug": "Web_2.0", "title": "Web 2.0", "depth": 3,
"source": "https://en.wikipedia.org/wiki/World_Wide_Web",
"imgbox": "Word-cloud graphic of Web 2.0 buzzwords: blog, wiki, social, sharing, RSS, AJAX, tagging",
"body": [
"<b>Web 2.0</b> refers to websites that emphasise user-generated content, ease of use, participatory culture and interoperability, in contrast to the earlier generation of static [[Web_page|web pages]]. The term was popularised by Tim O'Reilly and the 2004 Web 2.0 Conference, held as the industry recovered from the dot-com crash.",
"The archetypal Web 2.0 sites were [[Blog|blogs]], [[Wiki|wikis]] such as Wikipedia itself, social networks, video- and photo-sharing services (YouTube, Flickr), and web applications like Gmail whose in-browser interactivity — powered by AJAX techniques (asynchronous [[JavaScript]] and XML) — rivalled desktop software. Under the hood, the shift combined technical ingredients (broadband, [[RSS]] feeds, APIs and mashups) with an economic one: platforms hosting other people's content and profiting from network effects.",
"Critics called Web 2.0 a marketing term for things the web had always allowed, or a glossy label on the centralisation of the web into a few giant platforms — a critique that later fuelled talk of a decentralised 'Web3'. Either way, the label marks the era, roughly 2004 to the early 2010s, when the web turned from a library into a conversation.",
],
"see_also": ["Blog", "Wiki", "RSS", "World_Wide_Web", "Social_media"],
"unsure": ["Period boundaries of 'Web 2.0 era' are fuzzy by nature"],
},
{
"slug": "Blog", "title": "Blog", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_2.0",
"imgbox": "Screenshot-style image of a personal blog homepage with dated posts in reverse chronological order",
"body": [
"A <b>blog</b> (a truncation of 'weblog') is a discussion or informational [[Website|website]] published on the [[World_Wide_Web]] consisting of discrete, often informal diary-style text entries called posts. Posts are typically displayed in reverse chronological order, so the most recent post appears first.",
"Early blogs of the mid-1990s were hand-coded pages of commentary and links — the word 'weblog' was coined by Jorn Barger in 1997, and 'blog' by Peter Merholz in 1999. Tools such as Blogger (1999) and [[WordPress]] (2003) removed the technical barrier, and blogs exploded into the millions: personal journals, political commentary that challenged established media, corporate and marketing blogs, and specialist publications that became businesses in their own right.",
"Blogging culture developed its own machinery — permalinks, comments, blogrolls, trackbacks and [[RSS]] feeds for following many sites at once — and much of it was later absorbed into social media, microblogging (Twitter/X) and newsletter platforms. The independent blog nevertheless persists as one of the web's native literary forms.",
],
"see_also": ["WordPress", "RSS", "Web_2.0", "Wiki"],
"unsure": ["Coinage attributions (Barger 1997, Merholz 1999) are the standard account"],
},
{
"slug": "Wiki", "title": "Wiki", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_2.0",
"imgbox": "Screenshot-style image of a wiki article page with an Edit tab at the top",
"body": [
"A <b>wiki</b> is a form of online hypertext publication that is collaboratively edited and managed by its own audience directly through a [[Web_browser|web browser]]. A typical wiki contains multiple [[Web_page|pages]] meant for the general public, and allows any visitor to add and change content, usually without programming knowledge.",
"The first wiki, WikiWikiWeb, was created by Ward Cunningham in 1995 to let programmers share patterns and ideas; he named it after the Hawaiian word <i>wiki</i>, meaning 'quick', which he had encountered on the Wiki Wiki shuttle bus at Honolulu airport. Wiki software tracks every revision, making collaboration self-correcting: bad edits can be reverted as easily as they were made.",
"The most famous wiki is Wikipedia (2001), the free encyclopedia whose open editing produced one of the largest reference works in history — and the site this page imitates. Wikis also thrive inside companies as knowledge bases, in fan communities documenting fictional universes in extraordinary depth, and as documentation for software projects. The wiki idea — that a page and its edit button are the same thing — was one of the conceptual foundations of [[Web_2.0]].",
],
"see_also": ["Blog", "Web_2.0", "World_Wide_Web", "Hypertext"],
"unsure": [],
},
{
"slug": "RSS", "title": "RSS", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Web_2.0",
"imgbox": "The orange RSS feed icon: a dot with two curved waves in the corner of a rounded square",
"body": [
"<b>RSS</b> (standing for RDF Site Summary, Rich Site Summary, or in its most common version Really Simple Syndication) is a web feed format used to publish frequently updated information — [[Blog|blog]] entries, news headlines, audio and video — in a standardised, machine-readable form. A feed reader (or 'aggregator') checks subscribed feeds automatically and presents new items from many sites in one place.",
"RSS grew from Netscape's 1999 portal technology and was developed by several hands, including Ramanathan Guha and Dave Winer, whose RSS 2.0 became the dominant flavour; a rival effort produced the IETF-style Atom format (2005). During the 2000s, feed readers such as Bloglines and Google Reader were many users' front door to the web, and the orange RSS icon was ubiquitous.",
"RSS declined as algorithmic social feeds took over and Google Reader was shut down in 2013 — a decision still lamented by its users. The format nevertheless remains infrastructure: nearly every podcast is distributed by RSS, news sites still publish feeds, and a quiet revival of readers, interoperability and the independent web keeps the protocol in daily use.",
],
"see_also": ["Blog", "Web_2.0", "Netscape"],
"unsure": ["Expansion of the RSS abbreviation differs by version and source"],
},
{
"slug": "Internet_Engineering_Task_Force", "title": "Internet Engineering Task Force", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_protocol_suite",
"imgbox": "Photograph of a large IETF plenary meeting room with hundreds of engineers",
"infobox": [("Abbreviation", "IETF"), ("Founded", "1986"), ("Type", "Standards organisation (open, volunteer)"), ("Motto", "'Rough consensus and running code'")],
"body": [
"The <b>Internet Engineering Task Force</b> (<b>IETF</b>) is an open standards organisation that develops and promotes voluntary Internet standards, in particular the standards that comprise the [[Internet_protocol_suite|Internet protocol suite]] (TCP/IP). It is organised into working groups by topic area — routing, transport, security, applications and others — and has no formal membership: participants are individual volunteers from industry, academia and elsewhere.",
"The IETF's standards are published as RFCs (Requests for Comments), a series begun in 1969 by Steve Crocker for the [[ARPANET]]. Its working method was captured by David Clark's famous 1992 remark: 'We reject: kings, presidents and voting. We believe in: rough consensus and running code.' Decisions are famously confirmed by humming in plenary rooms, and meetings rotate worldwide three times a year.",
"Under the umbrella of the [[Internet_Society]] for legal and organisational support, the IETF has standardised everything from [[IPv6]] and [[HTTPS|TLS]] to [[SMTP|email]] extensions and QUIC. Its open process — anyone may join a mailing list, and all documents are free — contrasts deliberately with the paywalled, nation-state voting of older telecommunications standards bodies, and is a large part of why Internet standards spread as fast as they did.",
],
"see_also": ["Internet_protocol_suite", "Internet_Society", "World_Wide_Web_Consortium", "ICANN", "IPv6"],
"unsure": [],
},
{
"slug": "Internet_Society", "title": "Internet Society", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Photograph of an Internet Society community networking workshop in a developing region",
"infobox": [("Abbreviation", "ISOC"), ("Founded", "1992"), ("Founders", "[[Vint_Cerf]], [[Bob_Kahn|Robert Kahn]], Lyman Chapin"), ("Type", "Non-profit advocacy and standards support")],
"body": [
"The <b>Internet Society</b> (<b>ISOC</b>) is an American nonprofit advocacy organisation founded in 1992 with the stated mission 'to promote the open development, evolution, and use of the [[Internet]] for the benefit of all people throughout the world.'",
"It was co-founded by Internet pioneers [[Vint_Cerf]] and [[Bob_Kahn]] to provide an institutional and financial home for the [[Internet_Engineering_Task_Force]] (IETF), whose standards work it still supports. The Society also works on Internet access and policy: community networks in underserved areas, encryption advocacy, and the annual Global Internet Report. Its chapters in more than a hundred countries bring local engineers and users into global governance discussions.",
"ISOC is also the parent of Public Interest Registry, which operates the .org [[Top-level_domain|top-level domain]] — a relationship that drew scrutiny in 2019–2020 when the registry was nearly sold to a private equity firm, a transaction ultimately blocked after [[ICANN]] withheld consent.",
],
"see_also": ["Internet_Engineering_Task_Force", "ICANN", "Vint_Cerf", "Bob_Kahn", "Internet"],
"unsure": ["Chapter counts and registry details change over time"],
},
{
"slug": "Bob_Kahn", "title": "Bob Kahn", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_protocol_suite",
"imgbox": "Portrait photograph of Robert Kahn, an older man in a suit, at an awards ceremony",
"infobox": [("Born", "Robert Elliot Kahn, 23 December 1938, New York City"), ("Known for", "Co-inventing [[Transmission_Control_Protocol|TCP]] and [[Internet_Protocol|IP]]"), ("Awards", "Turing Award (2004), Presidential Medal of Freedom (2005)")],
"body": [
"<b>Robert Elliot Kahn</b> (born 1938), known as <b>Bob Kahn</b>, is an American electrical engineer who, along with [[Vint_Cerf]], first formulated the Transmission Control Protocol and Internet Protocol ([[Transmission_Control_Protocol|TCP]]/[[Internet_Protocol|IP]]), the fundamental communication technologies at the heart of the [[Internet]].",
"Kahn worked on the [[ARPANET]] at Bolt Beranek and Newman, where he was responsible for the system design of its Interface Message Processors, and demonstrated the network publicly at the 1972 International Conference on Computer Communication. Moving to DARPA's Information Processing Techniques Office, he conceived the problem of interconnecting dissimilar packet networks ('internetworking'), and with Cerf produced the 1974 paper 'A Protocol for Packet Network Intercommunication' that defined the architecture. At DARPA he also initiated the Strategic Computing Program, then one of the largest computer research programmes ever funded by the US government.",
"In 1986 Kahn founded the Corporation for National Research Initiatives (CNRI), which he has led since, working on digital information infrastructure and the 'knowbot' and digital-object concepts. With Cerf he shared the Turing Award (2004), the US National Medal of Technology, and the Presidential Medal of Freedom (2005), and is routinely described as one of the 'fathers of the Internet'.",
],
"see_also": ["Vint_Cerf", "Internet_protocol_suite", "Internet_Society", "ARPANET"],
"unsure": ["Birth date (23 December 1938) recalled with high but not absolute confidence"],
},
{
"slug": "Ted_Nelson", "title": "Ted Nelson", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Hypertext",
"imgbox": "Portrait photograph of Ted Nelson in the 1970s with long hair, beside a copy of Computer Lib/Dream Machines",
"infobox": [("Born", "Theodor Holm Nelson, 17 June 1937, New York City"), ("Known for", "Coining '[[Hypertext|hypertext]]' and 'hypermedia'; Project Xanadu"), ("Notable work", "Computer Lib/Dream Machines (1974)")],
"body": [
"<b>Theodor Holm Nelson</b> (born 1937) is an American pioneer of information technology, philosopher and sociologist. He coined the terms <i>[[Hypertext|hypertext]]</i> and <i>hypermedia</i> in the 1960s, and founded Project Xanadu in 1960 — the first hypertext project, whose ambitions long predated, and in some respects still exceed, the [[World_Wide_Web]] that eventually succeeded.",
"Nelson's Xanadu design insisted on features the web omitted: links that never break and point both ways, transclusion (quotation by live reference, with provenance), version management, and built-in micropayments so authors would be compensated when their work was quoted. His self-published 1974 book <i>Computer Lib/Dream Machines</i> — two books back to back — evangelised personal computing with the rallying cry 'You can and must understand computers NOW'.",
"Xanadu itself became legendary for delay: development began in 1960, passed through many teams and a period under Autodesk's funding, and a version of the code was released only in 2014, decades after the simpler, 'worse is better' web of [[Tim_Berners-Lee]] had won. Nelson has remained a sharp critic of the web's one-way, breakable links and of computing conventions — files, hierarchies, the desktop metaphor — that he regards as historical accidents frozen in place.",
],
"see_also": ["Hypertext", "World_Wide_Web", "Tim_Berners-Lee"],
"unsure": ["Exact year 'hypertext' coined is variously given as 1963 or 1965"],
},
{
"slug": "Gopher_(protocol)", "title": "Gopher (protocol)", "depth": 4,
"source": "https://en.wikipedia.org/wiki/World_Wide_Web",
"imgbox": "Screenshot-style image of a text-based Gopher menu of numbered items",
"body": [
"The <b>Gopher protocol</b> is a communication protocol designed for distributing, searching and retrieving documents in [[Internet_Protocol|Internet Protocol]] networks. Released in 1991 by a team at the University of Minnesota — home of the Golden Gophers, hence the name, with its pun on 'go for' — Gopher presented the Internet as a hierarchy of menus from which documents, and other menus, could be fetched.",
"For a brief period Gopher was the Internet's most promising information system: thousands of 'gopherspace' servers, searchable with tools such as Veronica, which indexed menu titles across the world. In 1993, however, the University of Minnesota announced it would charge licensing fees for its server implementation, while at almost the same moment CERN placed the [[World_Wide_Web]] in the public domain for free. The web also offered pictures, formatting and free-form links instead of rigid menus. Gopher use collapsed within a few years.",
"Gopher survives as a curiosity maintained by hobbyists, and its design — simple, fast, text-first — periodically inspires minimalist revivals such as the Gemini protocol. Its rise and fall is a standard case study in how licensing and timing, not technical merit alone, decide standards contests.",
],
"see_also": ["World_Wide_Web", "Archie_(search_engine)", "File_Transfer_Protocol", "Hypertext"],
"unsure": ["Veronica's coverage figure (~99% of gopherspace) is the commonly cited claim"],
},
{
"slug": "Usenet", "title": "Usenet", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Screenshot-style image of a Usenet newsreader showing a threaded discussion in a newsgroup",
"body": [
"<b>Usenet</b> is a worldwide distributed discussion system available on computers. It was developed in 1979–1980 by Tom Truscott and Jim Ellis at Duke and the University of North Carolina, linking their machines over dial-up telephone lines with the UUCP protocol, years before either university had an [[Internet]] connection.",
"Usenet consists of <b>newsgroups</b> — hierarchically named discussion forums (comp.*, rec.*, sci.*, talk.*, the anarchic alt.* hierarchy) — whose articles are flooded from server to server around the world, so no single machine hosts the conversation. It developed a rich culture and vocabulary: FAQs, lurking, flaming, trolling, Godwin's law, and the annual September influx of new students — which became permanent ('Eternal September') when AOL opened Usenet access to its subscribers in 1993.",
"Usenet was where Linus Torvalds announced Linux, where Tim Berners-Lee announced the [[World_Wide_Web]], and where spam was effectively born (the 1994 'Green Card Lottery' posting). Web forums, then social media, drew away most discussion, and ISPs dropped their servers in the 2000s; Usenet persists mainly through paid providers and is widely used for binary file distribution, much of it unauthorised — a shadow of the text discussion network that defined early online community.",
],
"see_also": ["Internet_Relay_Chat", "Email", "Internet", "Spam_(electronic)"],
"unsure": ["Usenet creation year is given as 1979 or 1980 depending on whether one dates conception or first traffic"],
},
{
"slug": "Internet_Relay_Chat", "title": "Internet Relay Chat", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Screenshot-style image of a classic IRC client with a channel conversation and a nick list on the right",
"body": [
"<b>Internet Relay Chat</b> (<b>IRC</b>) is a text-based chat system for instant messaging, designed for group communication in discussion forums called <i>channels</i>, but also allowing one-on-one private messages. Created by Jarkko Oikarinen at the University of Oulu, Finland, in August 1988, it predates and influenced every chat system that followed.",
"IRC networks consist of servers linked together; users connect with a client (historically mIRC on Windows), choose a nickname, and join channels whose names begin with #. Operators moderate channels; automated 'bots' run services and games; and the protocol's simplicity made it a hacker and open-source institution — the coordination medium of countless software projects and, famously, of breaking-news crowds during the 1991 Gulf War and Soviet coup attempt, when IRC relayed live reports past media blackouts.",
"Though dwarfed by proprietary successors (Slack, Discord and their kin borrowed its channels, threads and culture wholesale), IRC remains in use, sustained by networks such as Libera Chat, which became the largest network in 2021 after the Freenode upheavals.",
],
"see_also": ["Usenet", "Internet", "Instant_messaging"],
"unsure": ["Network rankings changed after the 2021 Freenode/Libera split"],
},
{
"slug": "Submarine_communications_cable", "title": "Submarine communications cable", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet_backbone",
"imgbox": "Photograph of a cable-laying ship's stern wheel deploying a thick armoured cable into the sea",
"body": [
"A <b>submarine communications cable</b> is a cable laid on the sea bed between land-based stations to carry telecommunication signals across stretches of ocean and sea. The first submarine cables, laid in the 1850s, carried telegraphy traffic; the first transatlantic telephone cable followed in 1956 (TAT-1), and modern cables carry data on optical fibres.",
"A modern submarine cable is a bundle of fibre pairs — each pair carrying many terabits per second through wavelength multiplexing — wrapped in steel armouring and powered along its length to feed optical repeaters every 80 km or so. Specialised ships unspool the cable along surveyed routes, burying it in shallow water against trawlers and anchors, which remain the commonest cause of faults; sharks, earthquakes and anchors occasionally sever links and reroute continents' traffic.",
"Well over 400 active cable systems, totalling more than a million kilometres, carry an estimated 95–99% of intercontinental Internet traffic — nearly everything, despite the popular image of a satellite Internet. New systems are increasingly built by the content giants (Google, Meta, Microsoft, Amazon) rather than telecom consortia, and their landing points and routes are matters of geopolitical strategy.",
],
"see_also": ["Internet_backbone", "Internet", "Optical_fiber"],
"unsure": ["Counts of active systems and the traffic share are commonly cited ranges"],
},
{
"slug": "Archie_(search_engine)", "title": "Archie (search engine)", "depth": 4,
"source": "https://en.wikipedia.org/wiki/File_Transfer_Protocol",
"imgbox": "Screenshot-style image of a telnet session querying an Archie server for a filename",
"body": [
"<b>Archie</b> is a tool for indexing [[File_Transfer_Protocol|FTP]] archives, allowing users to find specific files. It is considered the first Internet search engine — the first tool that let people search the contents of the network rather than merely browse it.",
"Archie was created in 1990 by Alan Emtage, a student at McGill University in Montreal, with Bill Heelan and J. Peter Deutsch. Archie servers periodically contacted known anonymous FTP sites, downloaded their directory listings, and built a searchable database of filenames; users queried it by telnet, email or early clients. The name derives from 'archive' (minus the v), and inspired the era's naming style — the [[Gopher_(protocol)|Gopher]] search tools Veronica and Jughead followed the comic-book joke.",
"Archie indexed only filenames, not contents, and the rise of the [[World_Wide_Web]] brought web search engines that indexed the text of pages themselves. Archie servers dwindled through the late 1990s, though at least one, in Poland, kept the service alive for decades as a working museum of the early Internet.",
],
"see_also": ["File_Transfer_Protocol", "Gopher_(protocol)", "Search_engine", "Internet_Archive"],
"unsure": ["The survival status of the Polish Archie server is as reported in recent years"],
},
]

for p in PAGES:
    build(p)
finish()
