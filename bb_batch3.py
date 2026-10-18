#!/usr/bin/env python3
import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl")
from bb_engine import build, finish

PAGES = [
{
"slug": "Internet_backbone", "title": "Internet backbone", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "World map of submarine fibre-optic cables connecting the continents",
"body": [
"The term <b>Internet backbone</b> refers to the principal data routes between large, strategically interconnected computer networks and core routers of the [[Internet]]. These data routes are hosted by commercial, government, academic and other high-capacity network centres, as well as by [[Internet_exchange_point|Internet exchange points]] where traffic is swapped between providers.",
"The backbone consists overwhelmingly of fibre-optic trunk lines — bundles of cables on land and [[Submarine_communications_cable|submarine communications cables]] under the oceans, the longest of which span entire ocean basins. Individual optical fibres carry terabits per second using wavelength-division multiplexing, and capacity has grown by orders of magnitude since the NSFNET backbone of the late 1980s ran at 1.5 Mbit/s.",
"The largest providers, historically called Tier 1 networks, can reach every other network on the Internet without paying for transit; beneath them, regional and local [[Internet_service_provider|ISPs]] buy transit or peer at exchanges. No single organisation owns or controls the backbone — it is an emergent property of thousands of interconnection agreements coordinated by the [[Border_Gateway_Protocol|BGP]] routing system.",
],
"see_also": ["Internet_exchange_point", "Autonomous_system_(Internet)", "Internet_service_provider", "Border_Gateway_Protocol"],
"unsure": ["Whether 'Tier 1' definitions remain crisp in the modern peering ecosystem is debated"],
},
{
"slug": "Internet_exchange_point", "title": "Internet exchange point", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_backbone",
"imgbox": "Photograph of rows of networking equipment and patch cables inside a large exchange facility",
"body": [
"An <b>Internet exchange point</b> (<b>IXP</b>) is a physical infrastructure through which [[Internet_service_provider|Internet service providers]] and content delivery networks exchange Internet traffic between their networks ([[Autonomous_system_(Internet)|autonomous systems]]). IXPs are among the building blocks of the [[Internet_backbone|Internet backbone]].",
"By connecting to an exchange — typically a set of large [[Ethernet]] [[Network_switch|switches]] in a data centre — networks can hand traffic directly to dozens or hundreds of peers at a single location, instead of paying an upstream transit provider to carry it. This 'peering' keeps local traffic local, cuts cost and latency, and improves resilience. The largest exchanges, such as DE-CIX Frankfurt, AMS-IX in Amsterdam and LINX in London, move peak traffic measured in many terabits per second across hundreds of connected networks.",
"The first exchanges grew out of the regional interconnection points of the early 1990s commercial Internet. Many are operated as non-profit associations of their member networks, a governance model credited with keeping peering open and inexpensive, particularly in Europe.",
],
"see_also": ["Internet_backbone", "Autonomous_system_(Internet)", "Internet_service_provider", "Border_Gateway_Protocol"],
"unsure": ["Peak traffic figures for specific exchanges change monthly"],
},
{
"slug": "Autonomous_system_(Internet)", "title": "Autonomous system (Internet)", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Border_Gateway_Protocol",
"imgbox": "Diagram of three autonomous systems, each a cloud of routers under one administration, linked by BGP sessions",
"body": [
"An <b>autonomous system</b> (<b>AS</b>) is a collection of connected [[Internet_Protocol|Internet Protocol]] routing prefixes under the control of one or more network operators, presenting a common, clearly defined routing policy to the Internet. In other words, the Internet is not one network but a network of tens of thousands of autonomous systems — [[Internet_service_provider|ISPs]], cloud providers, universities, governments and large enterprises.",
"Each AS is identified by a unique Autonomous System Number (ASN), allocated by the regional Internet registries under [[ICANN|IANA]]. Originally 16-bit (giving AS numbers up to 65535 — famous examples include AS15169 for Google), the space was extended to 32 bits as the count of networks grew.",
"Autonomous systems exchange reachability information with the [[Border_Gateway_Protocol]] (BGP): an AS announces the address prefixes it can deliver, and its neighbours propagate the announcements according to their policies and commercial relationships. Within an AS, operators use interior [[Routing|routing]] protocols to manage their own topology.",
],
"see_also": ["Border_Gateway_Protocol", "Internet_backbone", "Internet_exchange_point", "Routing"],
"unsure": [],
},
{
"slug": "Traceroute", "title": "Traceroute", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Routing",
"imgbox": "Screenshot-style image of traceroute command output listing numbered hops with hostnames and round-trip times",
"body": [
"<b>Traceroute</b> is a computer network diagnostic command for displaying possible routes (paths) and measuring transit delays of packets across an [[Internet_Protocol]] network. On Windows it is known as <b>tracert</b>; on Unix-like systems, <b>traceroute</b>.",
"The tool works by exploiting the time-to-live (TTL) field of IP packets. It first sends a packet with TTL 1, which expires at the first [[Router_(computing)|router]], prompting that router to return an ICMP 'time exceeded' error that reveals its address and the round-trip time. Traceroute then repeats with TTL 2, 3, and so on, mapping each hop until the packet reaches its destination. The original implementation was written by Van Jacobson in 1987, from a suggestion by Steve Deering.",
"Traceroute is a first resort for diagnosing slow or broken connections: it shows where packets travel and where delays or losses begin — though modern firewalls, load balancers and MPLS tunnels can make its picture incomplete, hiding hops or showing paths that differ from the traffic a user actually sends.",
],
"see_also": ["Ping_(networking_utility)", "Routing", "Internet_Protocol", "Router_(computing)"],
"unsure": ["Attribution details of the 1987 implementation are as commonly retold"],
},
{
"slug": "Ping_(networking_utility)", "title": "Ping (networking utility)", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Routing",
"imgbox": "Terminal screenshot showing ping replies with round-trip times in milliseconds",
"body": [
"<b>Ping</b> is a computer network administration software utility used to test the reachability of a host on an [[Internet_Protocol]] network. It measures the round-trip time for messages sent from the originating host to a destination computer and echoed back to the source.",
"Ping uses the Internet Control Message Protocol (ICMP): the sender transmits an ICMP Echo Request and waits for an Echo Reply, timing the exchange and reporting packet loss. The program was written in 1983 by Mike Muuss at the US Army's Ballistic Research Laboratory. Its name comes from submarine sonar terminology — a 'ping' is the sound of an active sonar pulse — backronymed as 'Packet InterNet Groper'.",
"The output — a sequence of reply times and a summary of minimum, average and maximum latency and loss — remains the simplest health check in networking ('can you ping it?'), and 'ping' has entered everyday language for latency itself, especially among online gamers. Because ICMP can be abused in denial-of-service attacks (the historical 'ping of death' among them), some networks filter it, so silence is not always proof a host is down.",
],
"see_also": ["Traceroute", "Internet_Protocol", "Router_(computing)"],
"unsure": ["The backronym is explicitly a backronym; Muuss's own account emphasises the sonar analogy"],
},
{
"slug": "Domain_name", "title": "Domain name", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Domain_Name_System",
"imgbox": "Diagram of a fully qualified domain name broken into labels: host, second-level domain and top-level domain",
"body": [
"A <b>domain name</b> is an identification string that defines a realm of administrative autonomy, authority or control within the [[Internet]]. Domain names are used to identify network locations in a human-friendly way: instead of memorising an [[IP_address|IP address]] such as 192.0.2.1, a user types a name, and the [[Domain_Name_System|Domain Name System]] (DNS) translates it to the address computers need.",
"Domain names are formed by the rules and procedures of the DNS. A fully qualified domain name such as <i>www.example.com</i> is a hierarchy of labels separated by dots, read from the most specific on the left to the [[Top-level_domain|top-level domain]] (.com) on the right, with an implied root at the far right. Each label may contain letters, digits and hyphens, and internationalised domain names allow other scripts, encoded internally as 'punycode'.",
"Names are registered through [[Domain_name_registrar|registrars]] accredited under policies coordinated by [[ICANN]]. Registration is by subscription, usually a year at a time, and confers control of the name rather than ownership in the property sense; disputes over names that infringe trademarks are handled under the UDRP policy or in court. The right to a memorable name has commercial value — short .com names trade for large sums, and businesses build their identities on them — making the domain name one of the Internet's foundational pieces of 'real estate'.",
],
"see_also": ["Domain_Name_System", "Top-level_domain", "Domain_name_registrar", "ICANN", "Uniform_Resource_Locator"],
"unsure": [],
},
{
"slug": "Top-level_domain", "title": "Top-level domain", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Domain_name",
"imgbox": "Chart of example top-level domains: .com, .org, .net, country codes such as .uk and .jp, and newer endings like .museum and .technology",
"body": [
"A <b>top-level domain</b> (<b>TLD</b>) is one of the domains at the highest level in the hierarchical [[Domain_Name_System]] of the [[Internet]], forming the final label of a fully qualified [[Domain_name|domain name]] — the <i>com</i> in example.com.",
"The original TLDs, created in 1985, were generic: .com (commercial), .edu, .gov, .mil, .net, .org and .int, joined by two-letter country-code TLDs (ccTLDs) such as .uk, .de and .jp, assigned according to the ISO country list and delegated to national managers. Some ccTLDs were later marketed worldwide for their suggestive spellings, such as Tuvalu's .tv and Montenegro's .me.",
"From 2012, [[ICANN]]'s new gTLD programme opened applications for almost any string, adding more than a thousand new endings — .app, .shop, .music, brand names, and names in non-Latin scripts. Sponsored TLDs (.museum, .aero, .xxx) serve defined communities, and the special .arpa TLD supports Internet infrastructure, including reverse DNS lookups. Policy for the root zone is coordinated by ICANN through IANA, which maintains the authoritative list of TLDs and their operators.",
],
"see_also": ["Domain_name", "Domain_Name_System", "ICANN", "Domain_name_registrar"],
"unsure": ["Exact count of delegated new gTLDs is approximate (over 1,000)"],
},
{
"slug": "Domain_name_registrar", "title": "Domain name registrar", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Domain_name",
"imgbox": "Screenshot-style image of a registrar's domain search page showing available names and prices",
"body": [
"A <b>domain name registrar</b> is a company or organisation that manages the reservation of Internet [[Domain_name|domain names]]. A registrar must be accredited by a generic top-level domain registry and/or by [[ICANN]], and it operates in accordance with the guidelines of the designated domain name registries.",
"To register a name, a customer (the registrant) searches the registrar's storefront, pays a periodic fee, and the registrar records the name, its expiry date and its [[Name_server|nameservers]] in the registry's database. Registrars compete on price, bundled services ([[Web_page|web]] hosting, [[Email|email]], privacy/proxy registration that hides the registrant's contact details from public WHOIS lookups) and aftermarket sales of premium names.",
"Before 1999, registration for the major TLDs was a monopoly of Network Solutions under a US government agreement; ICANN's creation introduced competition, and the market now includes large retail registrars such as GoDaddy, Namecheap and Cloudflare Registrar, plus thousands of resellers. Registrar failures and hijackings can cost registrants their names, so ICANN accreditation includes escrow and transfer protections.",
],
"see_also": ["Domain_name", "ICANN", "Top-level_domain", "Domain_Name_System"],
"unsure": ["Market share ordering of the largest registrars changes over time"],
},
{
"slug": "Name_server", "title": "Name server", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Domain_Name_System",
"imgbox": "Diagram of a DNS query travelling from a resolver to root, TLD and authoritative name servers",
"body": [
"A <b>name server</b> is a computer application or server that implements a network service for providing responses to queries against a directory service — in practice, almost always the [[Domain_Name_System|Domain Name System]] (DNS), which translates human-readable [[Domain_name|domain names]] into [[IP_address|IP addresses]].",
"Two roles are commonly distinguished. <b>Authoritative</b> name servers hold the original records for a zone (a domain and its subdomains): the [[Top-level_domain|TLD]] registries run them for endings like .com, and every registered domain delegates to its own authoritative servers, which answer with final authority about addresses, mail servers (MX records) and other data. <b>Recursive resolvers</b>, usually run by [[Internet_service_provider|ISPs]] or public services such as Google Public DNS and Cloudflare's 1.1.1.1, do the legwork for users: starting from the 13 logical root server addresses, they chase referrals down the hierarchy and cache answers according to each record's time-to-live.",
"The root name servers at the top of this system are operated by twelve organisations under [[ICANN|IANA]] coordination, replicated worldwide by anycast so that the same address is answered from hundreds of physical sites — a key part of the Internet's resilience.",
],
"see_also": ["Domain_Name_System", "Domain_name", "ICANN", "Top-level_domain"],
"unsure": ["Count of root server instances via anycast is in the high hundreds to over a thousand and grows"],
},
{
"slug": "ICANN", "title": "ICANN", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Domain_name",
"imgbox": "Photograph of an ICANN public meeting with rows of delegates and interpretation booths",
"infobox": [("Founded", "18 September 1998"), ("Type", "Non-profit organisation"), ("Purpose", "Coordination of DNS, IP addresses and protocol parameters"), ("Headquarters", "Los Angeles, California, US")],
"body": [
"The <b>Internet Corporation for Assigned Names and Numbers</b> (<b>ICANN</b>) is an American multistakeholder group and nonprofit organisation responsible for coordinating the maintenance and procedures of several databases related to the namespaces and numerical spaces of the [[Internet]], ensuring the network's stable and secure operation.",
"Through its IANA (Internet Assigned Numbers Authority) functions, ICANN coordinates the allocation of [[IP_address|IP addresses]] to the regional registries, the assignment of protocol parameters defined by the [[Internet_Engineering_Task_Force]], and the [[Domain_Name_System|DNS]] root zone — the master list of [[Top-level_domain|top-level domains]] and their operators. It accredits [[Domain_name_registrar|registrars]], runs the new-gTLD programme and sets dispute policy (UDRP) for domain names.",
"ICANN was created in 1998 to take these functions over from the US government, which had funded the early network. For most of its life IANA operated under a contract with the US National Telecommunications and Information Administration; in October 2016 that stewardship was transferred to the global multistakeholder community, a transition long debated as a test of whether the Internet's core identifiers could be governed without any single government. ICANN's bottom-up, consensus-based policy development — and its occasional controversies, from the .xxx decision to the blocked sale of the .org registry in 2020 — make it the closest thing the decentralised Internet has to a government.",
],
"see_also": ["Domain_Name_System", "Domain_name", "Internet_Society", "Internet_Engineering_Task_Force", "Top-level_domain"],
"unsure": ["Details of the .org sale episode are summarised from memory"],
},
{
"slug": "File_Transfer_Protocol", "title": "File Transfer Protocol", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Screenshot-style image of a classic FTP client with local files on one side and a remote directory on the other",
"infobox": [("Abbreviation", "FTP"), ("Ports", "21 (control), 20 (data)"), ("Original RFC", "RFC 114 (1971)"), ("Purpose", "Transferring computer files")],
"body": [
"The <b>File Transfer Protocol</b> (<b>FTP</b>) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network. FTP is built on a client–server model architecture using separate control and data connections between the client and the server.",
"FTP is one of the oldest Internet protocols: the first specification was written by Abhay Bhushan in 1971 for the [[ARPANET]], and the protocol took essentially its modern form in RFC 959 (1985). A user connects to port 21, logs in (often anonymously, giving an [[Email|email]] address as a password, in the era of open software archives), and issues text commands — LIST, RETR, STOR — while files flow over a second connection. Public FTP archives were the software libraries of the early Internet, and tools like [[Archie_(search_engine)|Archie]] arose to search them.",
"FTP's weakness is that it was designed for a more trusting age: usernames, passwords and data cross the network unencrypted. Encrypted successors and alternatives — FTPS (FTP over TLS), SFTP (a different protocol riding on SSH), and above all [[HTTP]] downloads and cloud storage — displaced it, and web browsers dropped FTP support entirely in 2021. It survives in niches such as uploading files to web servers and moving data between institutional systems.",
],
"see_also": ["HTTP", "SMTP", "Internet_protocol_suite", "Archie_(search_engine)"],
"unsure": ["Browser FTP removal dates: Chrome and Firefox both removed it in 2021"],
},
{
"slug": "SMTP", "title": "SMTP", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Email",
"imgbox": "Diagram of an email's journey: sender's client to SMTP server, across the Internet to the recipient's mail server",
"infobox": [("Full name", "Simple Mail Transfer Protocol"), ("Port", "25 (relay); 587 (submission)"), ("Standard", "RFC 5321 (2008); originally RFC 821 (1982)")],
"body": [
"The <b>Simple Mail Transfer Protocol</b> (<b>SMTP</b>) is an Internet standard communication protocol for electronic mail transmission. Mail servers and other message transfer agents use SMTP to send and receive mail messages; user-level clients typically use it only for sending, retrieving mail with [[Internet_Message_Access_Protocol|IMAP]] or [[POP3]] instead.",
"SMTP was defined by Jon Postel in 1982 (RFC 821), growing out of [[ARPANET]] mail protocols of the 1970s. It is a text-based, conversational protocol: the sending server greets with HELO (or EHLO in the extended ESMTP), names the sender and recipients, transmits the message, and the receiving server accepts it for relay or delivery. Messages then hop between servers, each adding a 'Received:' header, until they reach the destination domain found through DNS MX records.",
"Because SMTP was designed when the network's users were trusted researchers, it originally had no authentication and no encryption — gaps that made [[Spam_(electronic)|spam]] and spoofing endemic and were later patched by additions such as SMTP AUTH, STARTTLS encryption, and the SPF, DKIM and DMARC anti-forgery frameworks. Despite countless predictions of email's death, SMTP remains the universal, federated backbone of electronic mail, carrying billions of messages a day between independently operated systems.",
],
"see_also": ["Email", "POP3", "Internet_Message_Access_Protocol", "Spam_(electronic)", "Domain_Name_System"],
"unsure": ["Daily email volume figures are rough industry estimates"],
},
{
"slug": "POP3", "title": "POP3", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Email",
"imgbox": "Diagram showing a mail client downloading messages from a POP3 server and deleting them from the server",
"infobox": [("Full name", "Post Office Protocol version 3"), ("Port", "110; 995 (POP3S)"), ("Standard", "RFC 1939 (1996)")],
"body": [
"<b>POP3</b>, the <b>Post Office Protocol version 3</b>, is an application-layer Internet standard protocol used by [[Email|e-mail]] clients to retrieve e-mail from a mail server. Together with [[SMTP]] (which sends mail) it formed the classic pair of email protocols for the dial-up era.",
"POP3 works like its namesake: the client connects, authenticates, downloads all waiting messages to the local machine, and — by default — deletes them from the server, then disconnects. This download-and-delete model assumed one user, one computer and expensive, intermittent connections. Its limitations became obvious when email moved to phones and multiple computers: messages lived on whichever device downloaded them first. [[Internet_Message_Access_Protocol|IMAP]], which keeps mail on the server and synchronises it across devices, therefore displaced POP3 for most users, though POP3 remains supported by mail providers and embedded in countless legacy setups.",
],
"see_also": ["SMTP", "Internet_Message_Access_Protocol", "Email"],
"unsure": [],
},
{
"slug": "Internet_Message_Access_Protocol", "title": "Internet Message Access Protocol", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Email",
"imgbox": "Diagram of one mailbox on a server being accessed simultaneously from a phone, a laptop and a web client",
"infobox": [("Abbreviation", "IMAP"), ("Port", "143; 993 (IMAPS)"), ("Designed by", "Mark Crispin (1986)"), ("Standard", "RFC 9051 (IMAP4rev2, 2021)")],
"body": [
"The <b>Internet Message Access Protocol</b> (<b>IMAP</b>) is a standard protocol for accessing [[Email|email]] held on a mail server from a client application. In current practice it is, with [[SMTP]] for sending, one of the two protocols on which most email runs.",
"Unlike [[POP3]], which downloads mail to a single device, IMAP treats the server as the home of the mailbox: the client views, searches, organises into folders and flags messages where they live, and every device sees the same state. A client can fetch just headers, download a message body on opening, and cache copies for offline reading. IMAP was designed by Mark Crispin at Stanford in 1986 and evolved through several versions to IMAP4rev1 (RFC 3501, 2003) and IMAP4rev2 (2021), with extensions for push notifications, compression and efficient resynchronisation.",
"Webmail services from Gmail to Outlook.com present IMAP mailboxes through the browser, and most mail apps on phones and desktops use IMAP underneath — a quiet piece of 1980s design that scaled to the multi-device era far better than its simpler rival.",
],
"see_also": ["POP3", "SMTP", "Email"],
"unsure": [],
},
{
"slug": "Dynamic_Host_Configuration_Protocol", "title": "Dynamic Host Configuration Protocol", "depth": 4,
"source": "https://en.wikipedia.org/wiki/IP_address",
"imgbox": "Diagram of the DHCP four-step exchange: Discover, Offer, Request, Acknowledge (DORA)",
"infobox": [("Abbreviation", "DHCP"), ("Ports", "UDP 67 (server), 68 (client)"), ("Standard", "RFC 2131 (1997)")],
"body": [
"The <b>Dynamic Host Configuration Protocol</b> (<b>DHCP</b>) is a network management protocol used on [[Internet_Protocol]] networks for automatically assigning [[IP_address|IP addresses]] and other communication parameters to devices. It is the reason a laptop joining a coffee-shop [[Wi-Fi]] network 'just works': no one typed an address.",
"When a device connects, it broadcasts a DHCP Discover message; a DHCP server (often built into the home [[Router_(computing)|router]]) answers with an Offer of an address; the device Requests it, and the server Acknowledges, granting the address as a time-limited <i>lease</i>, together with the subnet mask, default gateway and [[Domain_Name_System|DNS]] server addresses. The exchange is remembered by its initials: DORA. Leases let a network recycle addresses among far more devices than could hold them permanently, and centralise configuration so administrators change settings in one place.",
"DHCP (1993) succeeded the earlier BOOTP and is defined in RFC 2131; its [[IPv6]] counterpart, DHCPv6, complements IPv6's stateless autoconfiguration.",
],
"see_also": ["IP_address", "Router_(computing)", "User_Datagram_Protocol", "Domain_Name_System"],
"unsure": [],
},
{
"slug": "Subnetwork", "title": "Subnetwork", "depth": 4,
"source": "https://en.wikipedia.org/wiki/IP_address",
"imgbox": "Diagram of an IP address split into network prefix and host part by a subnet mask",
"body": [
"A <b>subnetwork</b>, or <b>subnet</b>, is a logical subdivision of an [[Internet_Protocol|IP]] network. The practice of dividing a network into two or more networks is called <b>subnetting</b>.",
"An [[IP_address|IP address]] consists of a network prefix and a host identifier; the subnet mask (written as dotted decimal, e.g. 255.255.255.0, or as a CIDR suffix, /24) marks where one ends and the other begins. All devices in a subnet can reach each other directly; traffic for other subnets goes through a [[Router_(computing)|router]]. Subnetting lets an organisation carve its address space into departmental networks, limits broadcast traffic, and improves security and performance.",
"Subnetting was introduced in 1985 (RFC 950) within the original classful addressing system; classless inter-domain routing (CIDR, 1993) then allowed prefixes of any length, making allocation far more efficient and slowing [[IPv4]] address exhaustion. In [[IPv6]], subnets are conventionally /64 — a single subnet holds more addresses than the entire IPv4 Internet.",
],
"see_also": ["IP_address", "IPv4", "Routing", "Router_(computing)"],
"unsure": [],
},
]

for p in PAGES:
    build(p)
finish()
