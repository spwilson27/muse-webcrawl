#!/usr/bin/env python3
import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl")
from bb_engine import build, finish

PAGES = [
{
"slug": "Chromium_(web_browser)", "title": "Chromium (web browser)", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Google_Chrome",
"imgbox": "The Chromium logo: a blue-grey circle surrounded by three muted blue segments",
"body": [
"<b>Chromium</b> is a free and open-source [[Web_browser|web browser]] project, primarily developed and maintained by Google. It is the codebase from which [[Google_Chrome]] is built, differing mainly in branding and in some proprietary additions (licensed media codecs, crash reporting and Google integration).",
"Released alongside Chrome in 2008, Chromium's code — including the Blink rendering engine (forked from WebKit in 2013) and the V8 [[JavaScript]] engine — became the foundation of the modern browser ecosystem. [[Microsoft_Edge]], [[Opera_(web_browser)|Opera]], Brave, Vivaldi and many other browsers are Chromium-based, so a large majority of all web browsing runs on this single open-source codebase.",
"That success is double-edged: Chromium's openness lets anyone build a competitive browser, yet Google's stewardship of the project gives it outsized influence over web standards — a tension at the heart of debates about the web's future governance.",
],
"see_also": ["Google_Chrome", "Microsoft_Edge", "Opera_(web_browser)", "Web_browser"],
"unsure": [],
},
{
"slug": "WordPress", "title": "WordPress", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Blog",
"imgbox": "The WordPress logo: a white capital W in a circle on a blue-grey disc",
"infobox": [("Released", "27 May 2003"), ("Developers", "Matt Mullenweg, Mike Little; WordPress Foundation"), ("Written in", "[[PHP]]"), ("Type", "Content management system / blogging platform")],
"body": [
"<b>WordPress</b> is a free and open-source content management system (CMS) written in [[PHP]] and paired with a MySQL or MariaDB database. Features include a plugin architecture and a template system, referred to within WordPress as 'Themes'. It is the most-used CMS in the world, powering — by most surveys — more than 40% of all [[Website|websites]].",
"WordPress began in 2003 when Matt Mullenweg and Mike Little forked the stalled b2/cafelog blogging software. It grew from a personal [[Blog|blogging]] tool into a general platform through its plugin ecosystem (tens of thousands of plugins, from the WooCommerce shop system to security and SEO suites), its themes market, and the hosted service WordPress.com run by Mullenweg's company Automattic, alongside the self-hosted software from WordPress.org.",
"Its dominance makes it a bellwether and a target: a large share of web compromises involve outdated WordPress sites, and its decisions (such as the 2018 Gutenberg block editor) shape web publishing generally. A public dispute in 2024 between Automattic and the hosting company WP Engine over trademarks and contributions drew unusual attention to the governance of a project on which so much of the web depends.",
],
"see_also": ["PHP", "Blog", "Apache_HTTP_Server", "Website"],
"unsure": ["Share of websites (~43%) is per W3Techs-style surveys and fluctuates"],
},
{
"slug": "Apache_HTTP_Server", "title": "Apache HTTP Server", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_server",
"imgbox": "The Apache feather logo in red and purple gradient colours",
"infobox": [("Released", "1995"), ("Developer", "Apache Software Foundation"), ("Type", "[[Web_server|Web server]]"), ("Licence", "Apache License 2.0")],
"body": [
"The <b>Apache HTTP Server</b> is a free and open-source cross-platform [[Web_server|web server]] software, released under the terms of Apache License 2.0. Apache is developed and maintained by an open community of developers under the auspices of the Apache Software Foundation.",
"Apache began in 1995 as a set of patches to the NCSA HTTPd server — hence the punning name 'a patchy server' — and quickly became the web's dominant server software, powering the majority of websites from 1996 for well over a decade. Its modular architecture let administrators load exactly the features they needed (including the mod_php module that made the 'LAMP' stack — Linux, Apache, MySQL, [[PHP]] — the default platform of the early dynamic web), and its .htaccess configuration files gave shared-hosting customers local control.",
"From the 2010s, [[Nginx]] took much of Apache's share with a leaner event-driven design, and cloud platforms abstracted the server away entirely; Apache nevertheless still serves a large minority of websites and remains a fixture of enterprise and hosting environments. The Apache Software Foundation grew around it into an umbrella for hundreds of major open-source projects.",
],
"see_also": ["Nginx", "Web_server", "PHP", "WordPress", "HTTP"],
"unsure": ["Current market share figures vary by survey methodology"],
},
{
"slug": "Nginx", "title": "Nginx", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_server",
"imgbox": "The Nginx wordmark in green capital letters",
"infobox": [("Released", "4 October 2004"), ("Author", "Igor Sysoev"), ("Type", "[[Web_server|Web server]], reverse proxy, load balancer")],
"body": [
"<b>Nginx</b> (pronounced 'engine x') is a [[Web_server|web server]] that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. The software was created by Russian developer Igor Sysoev and publicly released in 2004.",
"Sysoev designed Nginx to solve the C10K problem — serving ten thousand simultaneous connections — which the process-per-connection model of the [[Apache_HTTP_Server]] handled poorly. Nginx's event-driven, asynchronous architecture uses a small, fixed number of worker processes and handles each connection cheaply, giving it a reputation for speed and low memory use under heavy load. It became the server of choice for many of the world's busiest sites and, by common surveys, overtook Apache in the 2020s as the most widely used web server.",
"Beyond serving static files, Nginx is typically deployed in front of application servers as a reverse proxy and load balancer, terminating [[HTTPS|TLS]] and distributing requests — a role that made it core infrastructure of the cloud era. The company behind it, NGINX Inc., was acquired by F5 Networks in 2019 for a reported $670 million.",
],
"see_also": ["Apache_HTTP_Server", "Web_server", "HTTP", "Proxy_server", "Content_delivery_network"],
"unsure": ["Acquisition price as reported in 2019"],
},
{
"slug": "PHP", "title": "PHP", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_server",
"imgbox": "The PHP logo: the letters php in white inside a blue-violet oval",
"infobox": [("Designed by", "Rasmus Lerdorf (1995)"), ("Paradigm", "Multi-paradigm, scripting"), ("Typing", "Dynamic, weak"), ("Used by", "[[WordPress]], Facebook (originally), Wikipedia")],
"body": [
"<b>PHP</b> is a general-purpose scripting language geared toward web development. It was originally created by Danish-Canadian programmer Rasmus Lerdorf in 1993 and released in 1995 as 'Personal Home Page' tools; the reference implementation is now produced by The PHP Group, and the name is a recursive backronym: 'PHP: Hypertext Preprocessor'.",
"PHP code is executed on the server by an interpreter, typically embedded in the [[Apache_HTTP_Server]] or fronted by [[Nginx]], and generates [[HTML]] (or other output) sent to the client's browser. Its low barrier to entry — a beginner can mix code into a page in minutes and simply upload it to shared hosting — made it the engine of the dynamic web: [[WordPress]], Drupal and Joomla run on it, as did early Facebook and Wikipedia (MediaWiki). Surveys consistently find PHP on the server side of roughly three-quarters of websites whose technology is known.",
"Long criticised for inconsistencies and security pitfalls, the language modernised substantially with PHP 7 (2015, much faster) and PHP 8 (2020, just-in-time compilation and a tidier type system). Whatever fashion says, the sheer mass of running PHP — most of the web's content management — guarantees its long future.",
],
"see_also": ["WordPress", "Apache_HTTP_Server", "JavaScript", "Web_server", "HTML"],
"unsure": ["Usage share (~76%) per W3Techs-style surveys"],
},
{
"slug": "Spam_(electronic)", "title": "Spam (electronic)", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Email",
"imgbox": "Screenshot-style image of an email inbox full of junk messages with implausible subject lines",
"body": [
"<b>Spam</b> is unsolicited, unwanted digital communication sent in bulk, most famously by [[Email|email]] but also by text message, social media and comments. The name is borrowed from the Monty Python sketch in which the canned meat Spam drowns out every other menu item — as junk drowns out wanted messages.",
"The first notorious email spam was sent in 1978 by Gary Thuerk, an ARPANET marketer who advertised DEC computers to hundreds of users and drew sharp complaints. Commercial spam exploded in 1994 with the 'Green Card Lottery' posting to [[Usenet]], whose authors cheerfully published a book on advertising to millions for pennies. As email became universal, spam became industrial: botnets of hijacked PCs sent billions of messages advertising pharmaceuticals, frauds and malware, at times constituting the overwhelming majority of all email traffic.",
"Defences co-evolved: statistical (Bayesian) filters, sender-authentication standards (SPF, DKIM, DMARC) bolted onto [[SMTP]], and machine-learning classifiers in the large mailbox providers, which together drove visible spam to a trickle for most users even as total volumes stayed immense. Legislation such as the US CAN-SPAM Act (2003) and the EU's GDPR regulates the practice without eliminating it — an arms race that became the template for every later fight over abuse of open networks.",
],
"see_also": ["Email", "Phishing", "Malware", "SMTP", "Usenet"],
"unsure": ["Historical peak share of email traffic (often cited ~80-90% in late 2000s)"],
},
{
"slug": "Phishing", "title": "Phishing", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Spam_(electronic)",
"imgbox": "Screenshot-style image of a fake bank login page with subtle spelling errors in the address bar",
"body": [
"<b>Phishing</b> is a form of social engineering and a scam in which attackers deceive people into revealing sensitive information (passwords, card numbers) or installing malware, usually by impersonating a trustworthy organisation in an [[Email|email]], message or fake [[Website|website]]. The word is a hacker respelling of 'fishing' — dangling bait for victims.",
"The practice dates to the mid-1990s, when AOL users were tricked into revealing passwords by fake staff messages; it industrialised in the 2000s with pixel-perfect clones of bank and PayPal login pages hosted on look-alike domains. Variants include <b>spear phishing</b> (researched, personalised attacks on individuals), <b>whaling</b> (executives), business email compromise (fake invoices and payment instructions, among the costliest cybercrimes by reported losses), smishing (SMS) and vishing (voice calls).",
"Phishing is the entry point in most major data breaches, because it attacks people rather than software. Defences combine technical filters, the [[HTTPS]] indicators and warnings in browsers, multi-factor authentication — especially phishing-resistant passkeys and hardware keys — and user training, though the fundamental asymmetry (the attacker needs one click; the defender needs every user to refuse every lure) keeps it endemic.",
],
"see_also": ["Spam_(electronic)", "Malware", "HTTPS", "Email", "Firewall_(computing)"],
"unsure": ["Breach-attribution statistics (commonly '~90% involve phishing/social engineering') vary by report"],
},
{
"slug": "Malware", "title": "Malware", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Stylised graphic of a glowing skull and warning symbols over circuit-board patterns, evoking malicious software",
"body": [
"<b>Malware</b> (a portmanteau of <i>malicious software</i>) is any software intentionally designed to cause disruption to a computer, server, client or network, to leak private information, gain unauthorised access, or deprive users of access to their data. The category includes [[Computer_virus|viruses]], [[Computer_worm|worms]], trojan horses, ransomware, spyware and rootkits.",
"Malware is nearly as old as networking: the Creeper program wandered the [[ARPANET]] in 1971 as an experiment, and the Morris worm of 1988 — released by a graduate student to measure the Internet — accidentally crippled roughly a tenth of it, leading to the first US conviction under the Computer Fraud and Abuse Act and the creation of the first CERT. Email viruses of the 1990s (Melissa, ILOVEYOU) and self-spreading worms of the 2000s (Code Red, Slammer, Conficker) gave way to a criminal economy: botnets rented for [[Spam_(electronic)|spam]] and denial-of-service attacks, banking trojans, and ransomware that encrypts a victim's files for payment — attacks that have shut down hospitals, pipelines and city governments.",
"Defence is an industry: antivirus software evolved into endpoint detection platforms, operating systems hardened, and the cat-and-mouse economics — malware authors, security researchers, and intelligence agencies (whose own exploits, such as Stuxnet, blurred every line) — makes malware a permanent feature of the networked world rather than a solved problem.",
],
"see_also": ["Computer_virus", "Computer_worm", "Phishing", "Spam_(electronic)", "Firewall_(computing)"],
"unsure": ["Morris worm impact often stated as ~10% of the then-Internet (~6,000 machines)"],
},
{
"slug": "Firewall_(computing)", "title": "Firewall (computing)", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Computer_network",
"imgbox": "Diagram of a firewall as a brick wall gateway between a trusted internal network and the untrusted Internet",
"body": [
"In computing, a <b>firewall</b> is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network, such as the [[Internet]]. The term was borrowed from the fireproof walls that stop a building fire spreading.",
"Firewalls evolved in generations: packet filters inspecting addresses and ports (late 1980s), stateful firewalls tracking connections, application-layer proxies, and modern 'next-generation' firewalls and web application firewalls that parse the traffic itself. Most home [[Router_(computing)|routers]] include a firewall — network address translation gives incidental protection — and every major operating system ships a host firewall. At national scale, the same word describes China's 'Great Firewall', the censorship and surveillance apparatus filtering a country's connection to the global Internet, a reminder that the technology is a checkpoint that can serve security or control.",
"Firewalls remain a first line of defence, though the industry's centre of gravity has shifted toward identity and 'zero trust' models that assume the perimeter has already failed — phones, laptops and cloud services having dissolved the tidy inside/outside world the firewall was built for.",
],
"see_also": ["Virtual_private_network", "Proxy_server", "Malware", "Router_(computing)", "Phishing"],
"unsure": [],
},
{
"slug": "Virtual_private_network", "title": "Virtual private network", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Diagram of an encrypted VPN tunnel between a laptop and a remote network across the public Internet",
"body": [
"A <b>virtual private network</b> (<b>VPN</b>) extends a private network across a public network, enabling users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network. Traffic travels inside an encrypted tunnel, protected from observers on the intervening networks.",
"VPNs began as enterprise technology: in the 1990s, protocols such as PPTP, L2TP/IPsec and later OpenVPN let employees reach the office network securely from home or the road, replacing expensive leased lines. A second, consumer market then grew around privacy and geography: commercial VPN services route a subscriber's traffic through their servers, hiding it from the local network operator and [[Internet_service_provider]], and making it appear to originate in another country — useful against surveillance, public [[Wi-Fi]] snoops, and region-locked streaming alike, at the cost of trusting the VPN provider instead.",
"Modern protocols such as WireGuard (merged into the Linux kernel in 2020) made VPNs faster and simpler to audit. Meanwhile employers have begun replacing blanket VPN access with 'zero trust' per-application controls, even as consumer VPN advertising — sometimes with exaggerated claims — made the term a household word.",
],
"see_also": ["Proxy_server", "Firewall_(computing)", "Internet_service_provider", "HTTPS"],
"unsure": [],
},
{
"slug": "Proxy_server", "title": "Proxy server", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Web_server",
"imgbox": "Diagram of a client sending a web request through a proxy server, which forwards it to the origin server",
"body": [
"In computer networking, a <b>proxy server</b> is a server application that acts as an intermediary between a client requesting a resource and the server providing that resource, relaying requests and responses between them. The word 'proxy' means one who acts on another's behalf — exactly the function here.",
"Forward proxies sit in front of clients: in the 1990s, caching proxies (such as Squid) at [[Internet_service_provider|ISPs]] and companies stored copies of popular [[Web_page|web pages]] to save scarce bandwidth and speed up browsing; today forward proxies and [[Virtual_private_network|VPNs]] are used for privacy, filtering and bypassing geographic restrictions. Reverse proxies sit in front of servers, presenting one public face for many backends: they terminate [[HTTPS]], balance load (the classic role of [[Nginx]] and HAProxy), cache content and shield origin servers — the operating principle of [[Content_delivery_network|content delivery networks]].",
"Because all traffic passes through them, proxies are also control points: employers use them to filter categories of sites, and censors and their opponents fight over them, which makes the humble proxy a quiet fixture of Internet geopolitics as well as engineering.",
],
"see_also": ["Virtual_private_network", "Nginx", "Content_delivery_network", "Firewall_(computing)", "Web_server"],
"unsure": [],
},
{
"slug": "Content_delivery_network", "title": "Content delivery network", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "World map diagram of a CDN: many edge server locations near clusters of users, fed by one origin",
"body": [
"A <b>content delivery network</b> (<b>CDN</b>) is a network of geographically distributed [[Proxy_server|proxy servers]] and their data centres whose goal is to provide high availability and performance by distributing the service spatially relative to end users. When you load a popular [[Website|website]] or stream a video, the bytes most likely come not from the publisher's own computers but from a CDN cache in your own city.",
"CDNs arose in the late 1990s as the web outgrew single-server sites: Akamai, founded in 1998 by MIT's Tom Leighton and Danny Lewin from work on consistent hashing, built the first large network and still serves a significant share of web traffic. A CDN caches static content at the 'edge', routes each user to a nearby healthy node (often using [[Domain_Name_System|DNS]] and anycast), absorbs traffic spikes and denial-of-service attacks, and increasingly runs customers' code (edge computing) and security filtering at those same points.",
"Competitors such as Cloudflare, Fastly and the hyperscalers' own networks (Amazon CloudFront, Google Cloud CDN) made CDN delivery the default architecture of the popular web — with a side effect that an outage at one CDN can take down a visible slice of the Internet at once, as several memorable Fastly and Cloudflare incidents demonstrated.",
],
"see_also": ["Proxy_server", "Nginx", "Internet_backbone", "Domain_Name_System", "Web_server"],
"unsure": ["Market shares and traffic proportions are estimates"],
},
{
"slug": "Internet_of_things", "title": "Internet of things", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Photograph of smart home devices — a voice assistant speaker, thermostat and smart light bulbs — connected by glowing lines",
"body": [
"The <b>Internet of things</b> (<b>IoT</b>) describes devices with sensors, processing ability, software and other technologies that connect and exchange data with other devices and systems over the [[Internet]] or other communications networks. The 'things' range from smart thermostats, light bulbs and doorbells to industrial machinery, medical devices, vehicles and city infrastructure.",
"The phrase was coined by Kevin Ashton in 1999 in the context of RFID-tagged supply chains; the preconditions — cheap sensors, ubiquitous [[Wi-Fi]] and cellular data, [[IPv6]] addresses enough for everything, and cloud platforms to hold the data — assembled over the following two decades. Consumer IoT boomed with the smart home (Nest thermostats, voice assistants, connected appliances); industrial IoT quietly instrumented factories, farms and logistics; and estimates of connected devices run into the tens of billions.",
"IoT also imported the Internet's security problems into the physical world: devices shipped with default passwords and unpatchable software have been conscripted into botnets (the Mirai botnet of 2016 knocked major sites offline using cameras and DVRs), and regulators have responded with labelling and baseline-security laws. The field thus replays the whole history of the Internet — exuberant connection first, security and standards after — compressed into a decade.",
],
"see_also": ["Internet", "Malware", "IPv6", "Cloud_computing"],
"unsure": ["Device counts ('tens of billions') are industry estimates that vary widely"],
},
{
"slug": "Net_neutrality", "title": "Net neutrality", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_service_provider",
"imgbox": "Graphic of data packets of different services being treated unequally at a toll-booth-like gateway",
"body": [
"<b>Net neutrality</b> is the principle that [[Internet_service_provider|Internet service providers]] must treat all Internet communications equally, offering users and online content providers consistent transfer rates regardless of content, website, platform, application, type of equipment, source address, destination address, or method of communication. Its supporters say it preserves the Internet's level playing field; its opponents say it restricts legitimate network management and investment.",
"The concept was named and popularised by Columbia law professor Tim Wu in a 2003 paper, but the debate is older: it recapitulates the common-carrier obligations of telegraph and telephone networks. The flashpoints are practices such as blocking, throttling, and paid prioritisation ('fast lanes'), and zero-rating of favoured services. In the United States the rules have oscillated with administrations: the FCC imposed strong rules in 2015, repealed them in 2017, voted to restore them in 2024, and saw them struck down by a federal appeals court in early 2025. The European Union, by contrast, has had an Open Internet Regulation since 2015.",
"Beyond law, the debate persists because the architecture shifted: the largest content companies now interconnect directly and run their own [[Content_delivery_network|CDNs]], so 'equal treatment' means something more complicated than it did when the argument began.",
],
"see_also": ["Internet_service_provider", "Internet", "Content_delivery_network", "Broadband"],
"unsure": ["US regulatory timeline (2015 rules, 2017 repeal, 2024 restoration, 2025 court decision) recalled in outline; the January 2025 Sixth Circuit ruling is the latest step I am aware of"],
},
]

for p in PAGES:
    build(p)
finish()
