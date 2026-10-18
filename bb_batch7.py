#!/usr/bin/env python3
import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl")
from bb_engine import build, finish

PAGES = [
{
"slug": "History_of_the_Internet", "title": "History of the Internet", "depth": 2,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "A timeline graphic from the ARPANET's four nodes in 1969 to the global network of today",
"body": [
"The <b>history of the Internet</b> begins with research into [[Packet_switching|packet switching]] in the 1960s and the development of the [[ARPANET]], the first wide-area packet-switched network, which connected its first four nodes — UCLA, SRI, UC Santa Barbara and the University of Utah — in late 1969.",
"Through the 1970s, networks proliferated (CYCLADES in France, the UK's NPL network, ALOHAnet in Hawaii) but could not talk to each other. [[Vint_Cerf]] and [[Bob_Kahn|Robert Kahn]] solved the interconnection problem with the [[Internet_protocol_suite|TCP/IP]] architecture, published in 1974; on 1 January 1983 the ARPANET switched to TCP/IP, the date often taken as the Internet's operational birthday. The NSFNET (1985) linked American universities, and networks in Europe, Asia and beyond joined, while [[Usenet]] and [[Email|email]] built the first mass user communities.",
"In 1989–1991 [[Tim_Berners-Lee]] at CERN invented the [[World_Wide_Web]], and the graphical [[Mosaic_(web_browser)|Mosaic]] browser (1993) made it vivid to non-specialists. The US government lifted commercial restrictions and retired NSFNET in 1995, the year of [[Netscape_Communications|Netscape's]] IPO, igniting the dot-com boom — and its 2000 crash. Broadband, [[Wi-Fi]] and then the smartphone (2007) made the Internet continuous and personal; social media and cloud computing reorganised it around platforms in the 2000s and 2010s; and the network that began as a resilient military research project became the general-purpose infrastructure of human communication, commerce and culture — used by more than five billion people.",
],
"see_also": ["Internet", "ARPANET", "World_Wide_Web", "Packet_switching", "Internet_protocol_suite"],
"unsure": ["User total (5+ billion) is per ITU-style estimates"],
},
{
"slug": "Computer_virus", "title": "Computer virus", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Malware",
"imgbox": "Stylised graphic of a magnifying glass over code with a warning symbol, representing virus detection",
"body": [
"A <b>computer virus</b> is a type of [[Malware|malware]] that, when executed, replicates itself by modifying other computer programs and inserting its own code into them. If this replication succeeds, the affected areas are then said to be 'infected' with a computer virus, a metaphor derived from biological viruses.",
"The concept was theorised by John von Neumann in 1949 (self-reproducing automata) and demonstrated playfully by Creeper on the [[ARPANET]] in 1971. The first viruses for personal computers appeared in the early 1980s — Elk Cloner (1982) spread between Apple II floppy disks — and Brain (1986), written by two brothers in Lahore, Pakistan, became the first widespread IBM PC virus. Viruses spread with their host files, later via documents with macros in the 1990s and email attachments, often carrying 'payloads' from pranks to data destruction.",
"As self-spreading [[Computer_worm|worms]] and stealthier trojans took over the headlines, the pure virus became a smaller share of malware, but the word stuck as the generic term — hence 'antivirus' software, an industry founded in the late 1980s that grew into modern endpoint security.",
],
"see_also": ["Computer_worm", "Malware", "Phishing", "Spam_(electronic)"],
"unsure": ["Elk Cloner date and authorship (Rich Skrenta, 1982) recalled from standard accounts"],
},
{
"slug": "Computer_worm", "title": "Computer worm", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Malware",
"imgbox": "World map graphic showing the rapid global spread of a worm outbreak over 24 hours",
"body": [
"A <b>computer worm</b> is a standalone [[Malware|malware]] program that replicates itself in order to spread to other computers, using a computer network — unlike a [[Computer_virus|virus]], it needs no host program and no human action to propagate. The term comes from John Brunner's 1975 novel <i>The Shockwave Rider</i>, and the first famous example was built by researchers at Xerox PARC in 1978–1982 as a benign experiment in distributed computing.",
"The Morris worm (2 November 1988) changed everything: released by Cornell graduate student Robert Tappan Morris, it exploited Unix vulnerabilities and spread far beyond its author's intent, crashing thousands of machines — a substantial fraction of the early [[Internet]] — and prompting the first felony conviction under the US Computer Fraud and Abuse Act and the creation of the CERT Coordination Center.",
"Email and network worms became the plague of the 2000s: Code Red and Nimda (2001), Slammer (2003, which doubled its population every 8.5 seconds and infected most of its victims within ten minutes), Blaster (2003) and Conficker (2008, millions of machines). Faster patching, firewalls and automatic updates reduced classic worm outbreaks, but the technique survives inside modern ransomware and botnets, whose self-propagation is pure worm logic.",
],
"see_also": ["Computer_virus", "Malware", "Internet", "Firewall_(computing)"],
"unsure": ["Slammer growth statistics are the famous figures from the CAIDA analysis"],
},
{
"slug": "Instant_messaging", "title": "Instant messaging", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_Relay_Chat",
"imgbox": "Screenshot-style image of a phone messaging app with a conversation of short bubbles",
"body": [
"<b>Instant messaging</b> (<b>IM</b>) is a type of online chat allowing immediate transmission of messages over the [[Internet]] or another computer network. Messages are typically transmitted between two or more parties in real time, and modern IM adds voice and video calls, file sharing, reactions and group chats of thousands.",
"IM's ancestors are the talk programs of 1970s timesharing systems and [[Internet_Relay_Chat]] (1988). The mass-market era began with ICQ (1996, from Israeli company Mirabilis — 'I seek you'), which gave users UIN numbers and a flower icon, and AOL Instant Messenger (1997), whose buddy list, away messages and door-slam sounds defined a generation of American adolescence. Microsoft's MSN/Windows Live Messenger and Yahoo! Messenger fought the 'messenger wars', refusing to interoperate.",
"The centre of gravity then moved to phones: WhatsApp (2009) used the phone number as identity and end-to-end encryption as a feature, passing two billion users; WeChat in China fused messaging with payments and mini-apps into a 'super-app'; and iMessage, Telegram, Signal and Discord each carved out territory. IM displaced SMS, and in much of the world it simply <i>is</i> the Internet's front door — the endpoint of the line that began with two mainframes exchanging 'LO' in 1969.",
],
"see_also": ["Internet_Relay_Chat", "Email", "Usenet", "Social_media"],
"unsure": ["WhatsApp user count (2+ billion) is the long-standing reported figure"],
},
{
"slug": "Optical_fiber", "title": "Optical fiber", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet_backbone",
"imgbox": "Photograph of a bundle of optical fibres glowing blue at their tips",
"body": [
"An <b>optical fiber</b> is a flexible glass or plastic strand constructed to guide light along its length by total internal reflection. Bundled into cables, optical fibres are the physical medium of the modern [[Internet]]: nearly all long-distance traffic — and increasingly the 'last mile' to homes — travels as pulses of light in glass.",
"The physics was demonstrated in the 19th century (light guided by water jets), but practical fibre communications required two breakthroughs: Charles Kao's 1966 insight that sufficiently pure glass would make fibre viable (recognised by a 2009 Nobel Prize), and Corning's low-loss fibre of 1970. A modern fibre is about 125 micrometres across including coating, with a core of ~9 micrometres for long-haul single-mode transmission; erbium-doped amplifiers boost the signal every 80 km or so without converting it to electricity.",
"Wavelength-division multiplexing — many colours of light, each an independent channel — multiplies capacity so that a single fibre pair can carry tens of terabits per second, and a [[Submarine_communications_cable|submarine cable]] contains several pairs. The economics are transformative: once the glass is in the ground or on the seabed, capacity upgrades come from the electronics at the ends, which is why the world's bandwidth keeps compounding.",
],
"see_also": ["Submarine_communications_cable", "Internet_backbone", "Broadband", "Ethernet"],
"unsure": ["Capacity figures per fibre pair are order-of-magnitude current values"],
},
{
"slug": "Streaming_media", "title": "Streaming media", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Screenshot-style image of a video streaming interface with a grid of programme thumbnails",
"body": [
"<b>Streaming media</b> is a form of multimedia delivered continuously and presented to a user while being delivered by a provider, rather than downloaded in full first. Its growth, once [[Broadband|broadband]] spread, moved music, film and television from physical media and scheduled broadcasts to on-demand services over the [[Internet]].",
"Streaming began in the 1990s with RealNetworks' RealAudio (1995), which squeezed intelligible audio through dial-up [[Modem|modems]], and the first live events — concerts and a baseball game — streamed to tiny, buffering audiences. Progressive download and then adaptive bitrate streaming (Apple's HLS, MPEG-DASH) solved the quality problem by switching resolution in step with the connection; YouTube (2005) made web video universal in Flash form, and Netflix's shift from DVDs to streaming in 2007 opened the 'streaming wars' that restructured Hollywood. Live streaming and [[Internet_Relay_Chat|chat]] culture (Twitch), music services (Spotify) and podcasting are branches of the same river.",
"Technically, streaming runs over [[HTTP]] through [[Content_delivery_network|CDNs]] using [[User_Datagram_Protocol|UDP]]- or TCP-based protocols tuned for timeliness; economically, it replaced ownership with subscription; culturally, it replaced the shared schedule with the personal queue — the defining media shift of the early 21st century.",
],
"see_also": ["Content_delivery_network", "Broadband", "Podcast", "User_Datagram_Protocol"],
"unsure": [],
},
{
"slug": "Bulletin_board_system", "title": "Bulletin board system", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Screenshot-style image of ANSI art and a text menu on a 1980s BBS welcome screen",
"body": [
"A <b>bulletin board system</b> (<b>BBS</b>) is a computer server running software that allows users to connect with a terminal program, log in, and perform functions such as uploading and downloading software and data, reading news and bulletins, and exchanging messages with other users through public message boards and sometimes direct chatting.",
"The first BBS, CBBS, was created in Chicago in February 1978 by Ward Christensen and Randy Suess during a blizzard, letting hobbyists dial in by [[Modem|modem]] to a single phone line — one user at a time. Through the 1980s BBSes multiplied into the tens of thousands: community noticeboards, shareware libraries (the origin of the shareware industry), multiplayer door games, elaborate ANSI art, and networks such as FidoNet (1984) that relayed mail and discussion between boards worldwide, forming a grassroots global network parallel to the academic [[Internet]].",
"Commercial online services (CompuServe, AOL) and then the [[World_Wide_Web]] absorbed the BBS's functions and users in the mid-1990s; most boards closed, though a nostalgic scene keeps hundreds running, now reached by telnet and web instead of dial-up. The BBS era invented online community conventions — handles, sysops, flame wars, files areas — that the Internet inherited wholesale.",
],
"see_also": ["Usenet", "Internet_Relay_Chat", "Modem", "Internet_forum"],
"unsure": ["CBBS date (16 February 1978) is the standard account"],
},
{
"slug": "Telnet", "title": "Telnet", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet_protocol_suite",
"imgbox": "Screenshot-style image of a terminal window showing a Telnet session login to a remote Unix system",
"infobox": [("Port", "TCP 23"), ("First RFC", "RFC 97 (1971); standard RFC 854 (1983)"), ("Purpose", "Remote terminal access (text-based)")],
"body": [
"<b>Telnet</b> is a client/server application protocol that provides access to virtual terminals of remote systems on local area networks or the [[Internet]]. It was one of the first protocols of the [[ARPANET]], developed from 1969 and standardised as RFC 854 in 1983, and for two decades it was <i>the</i> way to use a remote computer: a user at one machine logged into another across the network and worked in its command line as if sitting at its terminal.",
"Telnet's fatal flaw is that everything — including passwords — is transmitted in plaintext. On the trusting research network that was acceptable; on the commercial Internet it became untenable, and from the mid-1990s Telnet was displaced for remote administration by [[Secure_Shell|SSH]], which encrypts the session. Telnet survives in niches: configuring legacy network equipment, testing whether a [[TCP]] port answers (the classic 'telnet host 25' mail-server check), and charming anachronisms such as [[Bulletin_board_system|BBSes]] and ASCII-art Star Wars screenings served over port 23.",
],
"see_also": ["Secure_Shell", "File_Transfer_Protocol", "Internet_protocol_suite", "Bulletin_board_system"],
"unsure": [],
},
{
"slug": "Secure_Shell", "title": "Secure Shell", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Telnet",
"imgbox": "Screenshot-style image of an SSH terminal session showing a key fingerprint prompt",
"infobox": [("Abbreviation", "SSH"), ("Port", "TCP 22"), ("Created", "1995 by Tatu Ylönen"), ("Standard", "RFC 4251–4254 (2006)")],
"body": [
"The <b>Secure Shell Protocol</b> (<b>SSH</b>) is a cryptographic network protocol for operating network services securely over an unsecured network. Its most notable applications are remote login and command-line execution — the secure replacement for [[Telnet]] — and it is the standard tool by which administrators and developers run the [[Internet]]'s servers.",
"SSH was designed in 1995 by Tatu Ylönen, a researcher at Helsinki University of Technology, after a password-sniffing attack on the university network showed how exposed Telnet and the Unix r-commands were. SSH encrypts the whole session, authenticates the server by its host key (the 'authenticity of host can't be established' prompt every user has accepted), and supports password or — preferably — public-key authentication for users. Its port-forwarding and file-transfer companions (SCP and SFTP) make it a general secure tunnel.",
"Ylönen's company SSH Communications Security commercialised the protocol while the free OpenSSH implementation, created by the OpenBSD project in 1999, became the near-universal standard, shipping with every Unix-like system and eventually Windows. Modern infrastructure is inconceivable without it: cloud servers are born with SSH as their only door.",
],
"see_also": ["Telnet", "File_Transfer_Protocol", "Encryption", "Internet_protocol_suite"],
"unsure": [],
},
{
"slug": "Voice_over_IP", "title": "Voice over IP", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Diagram of a phone call converted to IP packets and routed across the Internet to another phone",
"body": [
"<b>Voice over Internet Protocol</b> (<b>VoIP</b>), also called IP telephony, is a method and group of technologies for voice calls using an [[Internet_Protocol]] network such as the [[Internet]], rather than the traditional public switched telephone network's dedicated circuits. Voice is digitised, compressed, chopped into packets — typically carried by [[User_Datagram_Protocol|UDP]] with the RTP protocol — and reassembled at the far end quickly enough to sustain conversation.",
"The first experiments date to the ARPANET era (1973), but consumer VoIP began with VocalTec's Internet Phone (1995) and flowered with Skype (2003), whose peer-to-peer design and free computer-to-computer calls, then cheap calls to real phones, devastated international calling prices. SIP became the standard signalling protocol for business phone systems, which migrated wholesale from PBX hardware to VoIP; mobile operators themselves now carry voice as data (VoLTE), and voice is simply one media type inside messaging and meeting apps — WhatsApp calls, Zoom, Teams.",
"The shift completed telephony's absorption into the Internet: the phone call, the original killer application of electrical networking, became a feature of software, priced at zero marginal cost and bundled with everything else.",
],
"see_also": ["User_Datagram_Protocol", "Instant_messaging", "Packet_switching", "Internet"],
"unsure": [],
},
{
"slug": "HTTP_cookie", "title": "HTTP cookie", "depth": 4,
"source": "https://en.wikipedia.org/wiki/HTTP",
"imgbox": "Screenshot-style image of a browser cookie consent banner with Accept and Reject buttons",
"body": [
"An <b>HTTP cookie</b> (also called a web cookie, Internet cookie or browser cookie) is a small block of data created by a [[Web_server|web server]] while a user is browsing a [[Website|website]] and placed on the user's computer or other device by the user's [[Web_browser|web browser]]. Cookies are designed to be a reliable mechanism for websites to remember stateful information — because [[HTTP]] itself is stateless, forgetting everything between requests.",
"Cookies were invented in 1994 by Lou Montulli at [[Netscape_Communications]] for an online shopping cart, and shipped in [[Netscape_Navigator]]; the name derives from 'magic cookies', a term already used by programmers for exchanged data tokens (and ultimately from fortune cookies). A server sets a cookie with a Set-Cookie header; the browser returns it on later requests to matching domains, enabling logins, carts, preferences and analytics.",
"The controversial form is the <b>third-party cookie</b>, set by a domain other than the one being visited — the mechanism that let advertising networks follow users across sites and build profiles. Privacy law (the EU ePrivacy Directive and GDPR, hence the ubiquitous consent banners) and browser policy pushed back: [[Safari_(web_browser)|Safari]] and [[Firefox]] block third-party cookies by default, and [[Google_Chrome]] spent years announcing, delaying and ultimately revising their removal — one of the defining privacy struggles of the web's third decade.",
],
"see_also": ["HTTP", "HTTPS", "Netscape_Navigator", "Web_browser", "Phishing"],
"unsure": ["Chrome's third-party cookie plans changed repeatedly; final status described in general terms deliberately"],
},
{
"slug": "WebAssembly", "title": "WebAssembly", "depth": 4,
"source": "https://en.wikipedia.org/wiki/JavaScript",
"imgbox": "The WebAssembly logo: the letters WASM in white on a purple square with a cut corner",
"body": [
"<b>WebAssembly</b> (<b>Wasm</b>) is a binary instruction format for a stack-based virtual machine, designed as a portable compilation target for programming languages. It enables deployment of client and server applications on the web at near-native speed — the fourth native language of the [[Web_browser|browser]], alongside [[HTML]], [[CSS]] and [[JavaScript]].",
"WebAssembly grew out of Mozilla's asm.js experiments (2013), which showed JavaScript engines could run compiled C code surprisingly fast. Announced in 2015 as a joint project of all major browser vendors and standardised by the [[World_Wide_Web_Consortium]] (first MVP in browsers in 2017, a W3C Recommendation in 2019), it lets developers compile C, C++, Rust, Go and other languages to a compact binary that browsers execute in the same sandbox as JavaScript.",
"Its showcase uses are heavy computation in the browser — photo and video editors, CAD, games (Unity and Unreal engines), Google Earth — and, increasingly, outside it: server-side and edge computing platforms adopted Wasm as a fast, safe, portable runtime, fulfilling part of the old 'write once, run anywhere' dream that Java applets and Flash once chased on the same turf.",
],
"see_also": ["JavaScript", "HTML", "HTML5", "Web_browser"],
"unsure": [],
},
{
"slug": "HTML5", "title": "HTML5", "depth": 4,
"source": "https://en.wikipedia.org/wiki/HTML",
"imgbox": "The HTML5 logo: an orange shield with a white number 5",
"body": [
"<b>HTML5</b> is a markup language used for structuring and presenting hypertext documents on the [[World_Wide_Web]]. It was the fifth and final major HTML version that is now a retired [[World_Wide_Web_Consortium|W3C]] recommendation; the current specification, maintained by the WHATWG as a 'living standard', is simply called [[HTML]].",
"HTML5's development was a standards drama: dissatisfied with the W3C's XHTML direction, browser makers (Apple, Mozilla, Opera) founded the WHATWG in 2004 and developed HTML5 as an evolution of what browsers actually did, standardising error handling so all browsers parse broken pages the same way. The W3C adopted the work in 2007 and published HTML5 as a Recommendation in 2014, later ceding authority back to the WHATWG (2019).",
"The substance was the web becoming an application platform: native &lt;video&gt; and &lt;audio&gt; (freeing the web from Flash), the &lt;canvas&gt; drawing surface, semantic elements (&lt;article&gt;, &lt;nav&gt;, &lt;header&gt;), offline storage, drag-and-drop, geolocation and the APIs that together let [[JavaScript]] applications rival desktop software — the foundation on which the modern, app-like web is built.",
],
"see_also": ["HTML", "CSS", "JavaScript", "WebAssembly", "World_Wide_Web"],
"unsure": [],
},
{
"slug": "Request_for_Comments", "title": "Request for Comments", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force",
"imgbox": "Screenshot-style image of the plain-text first page of RFC 1 with its 1969 heading",
"body": [
"A <b>Request for Comments</b> (<b>RFC</b>) is a publication in a series, numbered and edited by the RFC Editor, that documents technical and organisational notes about the [[Internet]] — protocols, procedures, best practices and research — most produced through the [[Internet_Engineering_Task_Force]] (IETF). The RFC series is the canonical record of how the Internet's standards were made.",
"The series began on 7 April 1969 with RFC 1, 'Host Software', written by Steve Crocker, a UCLA graduate student working on the [[ARPANET]]. Crocker chose the humble title deliberately: the notes were meant as informal working documents inviting discussion, not pronouncements — a tone that shaped Internet engineering culture permanently. Jon Postel served as RFC Editor for three decades, personally guarding the series' consistency.",
"Famous RFCs include RFC 791 ([[IPv4]]), RFC 821 (original [[SMTP]]), RFC 2616 and successors ([[HTTP]]) and RFC 1149, a humorous specification for IP over avian carriers (pigeons) — one of a tradition of April Fools' Day RFCs. There are now more than 9,000 RFCs; not all are standards (many are informational or historical), but to cite an RFC number is to cite the Internet's primary literature.",
],
"see_also": ["Internet_Engineering_Task_Force", "Internet_protocol_suite", "ARPANET", "Internet_Society"],
"unsure": ["Total RFC count passed 9,000 in the 2020s and grows monthly"],
},
{
"slug": "Data_center", "title": "Data center", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Photograph of a long aisle of server racks in a hyperscale data centre with blue lighting",
"body": [
"A <b>data center</b> (American English) or <b>data centre</b> is a building, a dedicated space within a building, or a group of buildings used to house computer systems and associated components, such as telecommunications and storage systems. Data centres are the factories of the [[Internet]]: the physical plants where cloud computing, [[Website|websites]] and AI models actually run.",
"Their design revolves around power and cooling: uninterruptible power supplies and diesel generators against outages, chillers and increasingly liquid cooling against the heat of computation, biometric security, fire suppression and redundant network connections — including to [[Internet_exchange_point|Internet exchanges]], which is why data centres cluster in a few 'carrier hotel' districts and fibre crossroads. Ratings (the Uptime Institute's Tiers I–IV) grade their redundancy.",
"From the 2010s, 'hyperscale' campuses built by Amazon, Microsoft, Google and Meta grew to the size of industrial estates, consuming power on the scale of cities and driving debates about energy, water and land use; the AI boom of the 2020s intensified both the build-out and the scrutiny. Meanwhile the colocation business lets thousands of smaller firms rent cages in the same buildings — the unglamorous real estate on which the cloud floats.",
],
"see_also": ["Cloud_computing", "Internet_backbone", "Internet_exchange_point", "Web_server"],
"unsure": [],
},
{
"slug": "Podcast", "title": "Podcast", "depth": 4,
"source": "https://en.wikipedia.org/wiki/RSS",
"imgbox": "Photograph of a podcaster speaking into a studio microphone with pop filter",
"body": [
"A <b>podcast</b> is a programme made available in digital format for download over the [[Internet]], typically a series of audio episodes to which users can subscribe. The medium is built on [[RSS]]: a podcast is fundamentally an RSS feed whose entries carry audio file enclosures, so any podcast app can fetch new episodes automatically — an open distribution system no single company owns.",
"The technology assembled in 2003–2004: RSS enclosures (Dave Winer), the first podcatcher software, and Adam Curry's promotion of the format; journalist Ben Hammersley coined 'podcasting' in a 2004 Guardian article, blending 'iPod' and 'broadcasting'. Apple's addition of podcasts to iTunes in 2005 brought the medium to the mainstream. It grew slowly as a niche of talk and comedy, then boomed in the 2010s — <i>Serial</i> (2014) proved the narrative form, smartphones and cars made listening effortless, and Spotify's entry (with nine-figure exclusive deals, most famously for Joe Rogan's show) pulled the open ecosystem toward platform exclusivity.",
"Podcasting's open RSS roots remain its defining tension: a medium born decentralised, now contested between the open feed and the walled garden — a small-scale replay of the [[World_Wide_Web|web's]] own history.",
],
"see_also": ["RSS", "Streaming_media", "Blog", "Internet"],
"unsure": ["Coinage attribution (Hammersley, 2004) is the standard account"],
},
]

for p in PAGES:
    build(p)
finish()
