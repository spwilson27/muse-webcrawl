#!/usr/bin/env python3
import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl")
from bb_engine import build, finish

PAGES = [
{
"slug": "Jon_Postel", "title": "Jon Postel", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Request_for_Comments",
"imgbox": "Portrait photograph of Jon Postel with his trademark beard and sandals, in the 1990s",
"infobox": [("Born", "Jonathan Bruce Postel, 6 August 1943, Altadena, California"), ("Died", "16 October 1998 (aged 55), Santa Monica, California"), ("Known for", "RFC Editor; IANA; [[SMTP]], [[Internet_Protocol|IP]] standards")],
"body": [
"<b>Jonathan Bruce Postel</b> (6 August 1943 – 16 October 1998) was an American computer scientist who made many significant contributions to the development of the [[Internet]], particularly with respect to standards. He is known principally as the editor of the [[Request_for_Comments]] (RFC) document series — a role he held for nearly three decades — and as the founder and steward of the Internet Assigned Numbers Authority (IANA).",
"At UCLA and then at USC's Information Sciences Institute, Postel was at the centre of the [[ARPANET]] community: he wrote or edited the specifications for [[Internet_Protocol|IP]], [[Transmission_Control_Protocol|TCP]]'s companions, and [[SMTP|mail]], and personally maintained the registries of protocol numbers, port numbers and address allocations on which the whole system depended. He is the author of the robustness principle that bears his name — 'Postel's law': <i>be conservative in what you do, be liberal in what you accept from others</i> — the design ethic of interoperable networking.",
"In January 1998 Postel briefly demonstrated how much authority rested in one trusted person by redirecting eight of the twelve root [[Name_server|name servers]] to IANA as a test — an act that alarmed the US government and hastened the creation of [[ICANN]], into which IANA was folded weeks before his death from complications of heart surgery in October 1998. [[Vint_Cerf]]'s memorial RFC 2468, 'I Remember IANA', remains the RFC series' most famous obituary.",
],
"see_also": ["Request_for_Comments", "ICANN", "Internet_Engineering_Task_Force", "Vint_Cerf", "Steve_Crocker"],
"unsure": ["Date and count of root servers in the 1998 episode are as commonly reported"],
},
{
"slug": "Steve_Crocker", "title": "Steve Crocker", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Request_for_Comments",
"imgbox": "Portrait photograph of Steve Crocker speaking at an Internet governance meeting in the 2010s",
"infobox": [("Born", "Stephen David Crocker, 15 October 1944, Pasadena, California"), ("Known for", "Writing RFC 1; ARPANET protocols; [[ICANN]] chair (2011–2017)")],
"body": [
"<b>Stephen David Crocker</b> (born 1944) is an American Internet pioneer. In 1969, as a graduate student at UCLA, he wrote the first [[Request_for_Comments]] — RFC 1, 'Host Software' — and convened the Network Working Group of graduate students who designed the [[ARPANET]]'s host protocols, inventing along the way the open, discussion-based standards culture that still governs Internet engineering.",
"Crocker was part of the UCLA team that connected the first ARPANET node and sent the network's first message (the famous crashed 'LO' of 'LOGIN', 29 October 1969). He later worked at DARPA, founded the Internet Society's predecessor activities, and pursued network security ventures. In a symmetry much remarked upon, the student who wrote RFC 1 returned as a governor of the mature Internet: he served on, then chaired, the board of [[ICANN]] from 2011 to 2017, overseeing the period that included the 2016 IANA stewardship transition ending US government oversight of the [[Domain_Name_System|DNS]] root — functions whose informal origins lay with his friend [[Jon_Postel]].",
],
"see_also": ["Request_for_Comments", "Jon_Postel", "ICANN", "ARPANET", "Internet_Engineering_Task_Force"],
"unsure": [],
},
{
"slug": "Paul_Mockapetris", "title": "Paul Mockapetris", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Domain_Name_System",
"imgbox": "Portrait photograph of Paul Mockapetris in the 2000s",
"infobox": [("Born", "Paul V. Mockapetris, 1948"), ("Known for", "Inventing the [[Domain_Name_System|Domain Name System]] (1983)")],
"body": [
"<b>Paul V. Mockapetris</b> (born 1948) is an American computer scientist and Internet pioneer, known as the inventor of the [[Domain_Name_System]] (DNS), the distributed naming system that translates human-readable [[Domain_name|domain names]] into [[IP_address|IP addresses]].",
"In 1983, at USC's Information Sciences Institute, Mockapetris was asked by [[Jon_Postel]] to reconcile competing proposals for replacing the ARPANET's single HOSTS.TXT file — a centrally maintained table that every site copied nightly and that could not scale with the growing network. His design, specified in RFCs 882 and 883 (1983) and refined in RFCs 1034 and 1035 (1987), was hierarchical and distributed: delegable zones, authoritative [[Name_server|name servers]], caching resolvers. Mockapetris also wrote the first implementation, JEEVES.",
"DNS became one of the Internet's load-bearing designs — arguably the largest distributed database in the world — and one of its most durable: the protocol of 1987, extended but never replaced, now answers trillions of queries a day. Mockapetris later worked in industry (including as chief scientist at Nominum) and received the IEEE Internet Award and induction into the Internet Hall of Fame.",
],
"see_also": ["Domain_Name_System", "Domain_name", "Jon_Postel", "Name_server", "ICANN"],
"unsure": ["Birth year (1948) recalled with moderate confidence"],
},
{
"slug": "Lawrence_Roberts", "title": "Lawrence Roberts", "depth": 4,
"source": "https://en.wikipedia.org/wiki/ARPANET",
"imgbox": "Photograph of Lawrence Roberts in the 1960s beside early networking equipment",
"infobox": [("Born", "Lawrence Gilman Roberts, 21 December 1937, Westport, Connecticut"), ("Died", "26 December 2018 (aged 81)"), ("Known for", "Program manager of the [[ARPANET]]; founder of Telenet")],
"body": [
"<b>Lawrence Gilman Roberts</b> (21 December 1937 – 26 December 2018) was an American engineer who was the program manager and principal architect of the [[ARPANET]], the precursor to the [[Internet]]. Recruited to ARPA in 1966 by Robert Taylor, Roberts designed the network's architecture — adopting [[Packet_switching|packet switching]] (building on the work of [[Paul_Baran]] and [[Donald_Davies]]) and the subnet of Interface Message Processors built by BBN — and managed its deployment to the first nodes in 1969.",
"Roberts had earlier connected computers across a continent in the 1965 Lincoln Laboratory experiment with Thomas Marill, one of the first demonstrations of computer networking. After ARPA he founded Telenet (1973), the first commercial packet-switching service, which brought networking to businesses and seeded the commercial data-network industry.",
"With [[Bob_Kahn]] and [[Vint_Cerf]] he is routinely counted among the founders of the Internet, receiving the Draper Prize and the Prince of Asturias Award; his role — the manager-architect who turned an idea into a funded, built system — is the organisational counterpart to the more famous protocol designers.",
],
"see_also": ["ARPANET", "Packet_switching", "Paul_Baran", "Donald_Davies", "Bob_Kahn"],
"unsure": [],
},
{
"slug": "Paul_Baran", "title": "Paul Baran", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Packet_switching",
"imgbox": "Portrait photograph of Paul Baran in the 1960s at RAND",
"infobox": [("Born", "29 April 1926, Grodno, Poland (now Belarus)"), ("Died", "26 March 2011 (aged 84), Palo Alto, California"), ("Known for", "Inventing distributed [[Packet_switching|packet switching]] (1960–1964)")],
"body": [
"<b>Paul Baran</b> (29 April 1926 – 26 March 2011) was a Polish-American engineer who was a pioneer in the development of computer networks. At the RAND Corporation in the early 1960s, working on Cold War communications survivability, he developed the concept of distributed, redundant packet networks — the intellectual foundation of [[Packet_switching]].",
"Baran's problem was stark: how could command-and-control communications survive a nuclear first strike? His answer, set out in the eleven-volume 1964 study <i>On Distributed Communications</i>, was a network with no centre: messages chopped into standardised 'message blocks', routed adaptively ('hot-potato routing') over many redundant links, reassembling at their destination. Each node was equal; the network could lose many and still deliver. AT&T, then America's telephone monopoly, famously dismissed the idea as unworkable.",
"When the [[ARPANET]] was designed, Baran's work — alongside [[Donald_Davies]]'s independent British invention of packets — informed its architecture; the Internet that resulted embodies Baran's principles at world scale. He later co-founded the Institute for the Future and several networking companies, and received the National Medal of Technology and Innovation in 2007.",
],
"see_also": ["Packet_switching", "Donald_Davies", "ARPANET", "Lawrence_Roberts"],
"unsure": [],
},
{
"slug": "Donald_Davies", "title": "Donald Davies", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Packet_switching",
"imgbox": "Photograph of Donald Davies at the National Physical Laboratory in the 1960s",
"infobox": [("Born", "Donald Watts Davies, 7 June 1924, Treorchy, Wales"), ("Died", "28 May 2000 (aged 75)"), ("Known for", "Co-inventing [[Packet_switching]]; coining the word 'packet'")],
"body": [
"<b>Donald Watts Davies</b> (7 June 1924 – 28 May 2000) was a Welsh computer scientist who, independently of [[Paul_Baran]] in the United States, invented [[Packet_switching]] — and gave it its name. His work at the UK's National Physical Laboratory (NPL) directly influenced the design of the [[ARPANET]].",
"Davies had worked on Alan Turing's ACE computer project at NPL. In 1965, frustrated by the inefficiency of circuit-switched lines for bursty computer traffic, he conceived a store-and-forward network in which messages were divided into small fixed-size units — for which, consulting a linguist colleague, he chose the word <b>packet</b>. The NPL Mark I network went live in the early 1970s as the first local packet-switched network, and Davies's 1967 Gatlinburg paper brought the idea to the American team building the ARPANET, whose leader [[Lawrence_Roberts]] adopted it.",
"Davies later turned to network security, leading work on encryption and banking security in the 1980s. Recognition came late — including posthumous induction into the Internet Hall of Fame — a modest fate for the man who named the atom of the Internet age.",
],
"see_also": ["Packet_switching", "Paul_Baran", "Lawrence_Roberts", "ARPANET", "Computer_network"],
"unsure": ["Exact first-operation date of NPL Mark I (1970/1971) varies by source"],
},
{
"slug": "Radia_Perlman", "title": "Radia Perlman", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Ethernet",
"imgbox": "Portrait photograph of Radia Perlman speaking at a technical conference",
"infobox": [("Born", "18 December 1951, Portsmouth, Virginia, US"), ("Known for", "Inventing the spanning-tree protocol (1985)"), ("Nickname", "'Mother of the Internet' (a title she dislikes)")],
"body": [
"<b>Radia Joy Perlman</b> (born 1951) is an American computer programmer and network engineer, known principally for her invention of the spanning-tree protocol (STP), which is fundamental to the operation of network bridges and [[Network_switch|switches]] — and thus of [[Ethernet]] [[Local_area_network|local area networks]] everywhere.",
"Working at Digital Equipment Corporation in 1985, Perlman solved the problem of loops in bridged networks — which otherwise produce broadcast storms — with an elegant distributed algorithm by which bridges elect a root and prune links into a loop-free tree, reconfiguring automatically when links fail. She documented it in a famous poem ('Algorhyme': <i>I think that I shall never see / a graph more lovely than a tree…</i>) in her paper. STP was standardised as IEEE 802.1D and remains embedded in every switched LAN, though faster successors (RSTP, TRILL — her own later design) have refined it.",
"Perlman's broader career spans routing protocol design (IS-IS, still used in large provider networks) and network security; her textbook <i>Interconnections</i> is a standard reference. She is often styled 'Mother of the Internet', a label she resists — noting the Internet had many parents and that her contribution, though essential, is the humble plumbing of the local network.",
],
"see_also": ["Ethernet", "Network_switch", "Local_area_network", "Routing"],
"unsure": ["Birth date recalled from standard biographies"],
},
{
"slug": "Digital_divide", "title": "Digital divide", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Broadband",
"imgbox": "Photograph contrasting a teenager with a laptop in a city with children sharing one phone in a rural village",
"body": [
"The <b>digital divide</b> is the unequal distribution of information and communication technologies — in access, quality, skills and outcomes — between different populations, whether between countries, between urban and rural areas of one country, or between demographic groups within a city. The term came into wide use in the mid-1990s, as the [[Internet]] commercialised and US policy reports (the NTIA's 'Falling Through the Net' series) documented who was being left offline.",
"The divide has several layers: the <i>access</i> divide (is there a connection and a device?), the <i>quality</i> divide (fibre [[Broadband|broadband]] versus a prepaid phone on a congested network), the <i>skills</i> divide (digital literacy), and the <i>outcome</i> divide (who converts access into education, income and civic power). Globally, roughly two-thirds of humanity is now online, with near-universal access in rich countries and far lower rates in the least developed ones; within countries, cost, age, disability and rurality are the usual fault lines.",
"Policy responses range from universal-service funds and community networks to satellite constellations serving remote regions and public access in libraries and schools. The COVID-19 pandemic, which moved work and schooling online overnight, recast the divide from an abstract concern into an emergency measured in children without connections — and 'broadband as utility' from a slogan into legislation in several countries.",
],
"see_also": ["Broadband", "Internet_service_provider", "Internet", "Net_neutrality"],
"unsure": ["Global online share (~two-thirds) per ITU estimates, which move yearly"],
},
{
"slug": "Internet_governance", "title": "Internet governance", "depth": 3,
"source": "https://en.wikipedia.org/wiki/ICANN",
"imgbox": "Photograph of a UN Internet Governance Forum plenary hall with rows of delegates and flags",
"body": [
"<b>Internet governance</b> is the development and application by governments, the private sector and civil society, in their respective roles, of shared principles, norms, rules, decision-making procedures, and programmes that shape the evolution and use of the [[Internet]]. That famously convoluted definition, from the UN's 2005 Tunis Agenda, reflects the field's central fact: no one is in charge of the Internet as a whole, yet it must somehow be governed.",
"In practice, governance is layered and fragmented. Technical coordination — names, numbers and protocol standards — is done by the multistakeholder bodies: [[ICANN]], the regional address registries and the [[Internet_Engineering_Task_Force]], their legitimacy resting on openness and on the 2016 transition that ended formal US stewardship of the DNS root. Policy issues — cybercrime, content, privacy, trade, human rights — spill into national law and international forums: the UN's Internet Governance Forum (a talk-shop without decision power), the ITU, trade negotiations and courts.",
"The standing argument is between the multistakeholder model, defended by most Western governments, engineers and much of civil society, and state-sovereignty models advanced by Russia, China and others, in which governments control their national Internet segments (the 'splinternet' fear). Every few years the argument re-ignites — over encryption, platform power, AI — because the Internet's governance is, in effect, the constitution-writing of a borderless polity that never quite agrees to have one.",
],
"see_also": ["ICANN", "Internet_Society", "Internet_Engineering_Task_Force", "Net_neutrality", "Internet"],
"unsure": [],
},
{
"slug": "WebCrawler", "title": "WebCrawler", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Search_engine",
"imgbox": "Screenshot-style image of the WebCrawler homepage from 1995 with its spider mascot on a web",
"body": [
"<b>WebCrawler</b> was a metasearch engine established in 1994, notable as the first web search engine to provide full-text search — indexing the actual words of [[Web_page|pages]] rather than only their titles. It was developed by Brian Pinkerton at the University of Washington and launched on 20 April 1994 with a database of pages from about 4,000 websites.",
"WebCrawler's spider icon and clean operation made it one of the essential early-web landmarks, at times so popular it had to ask users to come back at night. It was acquired by AOL in 1995 and sold to Excite in 1997, passing through the portal era as a brand; it survives as a metasearch front end aggregating results from [[Google_Search|Google]], [[Bing_(search_engine)|Bing]] and others.",
"Its historical place is as the proof of concept for modern web search: that a crawler, an index and a query box could tame the whole web — the template [[AltaVista]] scaled and Google perfected.",
],
"see_also": ["Search_engine", "AltaVista", "Lycos", "Google_Search"],
"unsure": ["Launch database size is the figure given in contemporary accounts"],
},
{
"slug": "Yahoo!_Search", "title": "Yahoo! Search", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Search_engine",
"imgbox": "Screenshot-style image of the Yahoo! Search results page with its purple branding",
"body": [
"<b>Yahoo! Search</b> is a search engine owned by Yahoo! Inc. For much of the web's history it was one of the top search properties — Yahoo! began in 1994 as a human-edited directory of websites ('Jerry and David's Guide to the World Wide Web', by Jerry Yang and David Filo) and only gradually became a search engine, at first licensing results from others ([[AltaVista]], Inktomi, then [[Google_Search|Google]] itself from 2000 to 2004).",
"Yahoo! built its own crawler-based engine in 2003–2004 (acquiring Inktomi and Overture, hence AltaVista and AlltheWeb) and was for several years the world's number-two search engine. But it never matched Google's results quality or advertising economics; in 2009 Yahoo! exited the technology race, signing a ten-year deal for Microsoft's [[Bing_(search_engine)|Bing]] to power its results — an admission that the search war was over, from the company that had once <i>been</i> the front door of the web.",
"Yahoo! Search persists as a Bing-powered service within the shrunken Yahoo! portal. Its arc — directory, portal, search also-ran — is the canonical story of the web's first era, when guiding humans to websites was the industry's centre and owning the guide seemed like owning the future.",
],
"see_also": ["Search_engine", "Bing_(search_engine)", "Google_Search", "AltaVista"],
"unsure": ["Timeline of the directory-to-search transition is summarised in outline"],
},
]

for p in PAGES:
    build(p)
finish()
