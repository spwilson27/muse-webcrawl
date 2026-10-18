#!/usr/bin/env python3
import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl")
from bb_engine import build, finish

PAGES = [
{
"slug": "Transmission_Control_Protocol", "title": "Transmission Control Protocol", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_protocol_suite",
"imgbox": "Diagram of the TCP three-way handshake: SYN, SYN-ACK, ACK, followed by data transfer",
"infobox": [("Layer", "Transport"), ("Standard", "RFC 793 (1981); RFC 9293 (2022)"), ("Abbreviation", "TCP")],
"body": [
"The <b>Transmission Control Protocol</b> (<b>TCP</b>) is one of the main protocols of the [[Internet_protocol_suite|Internet protocol suite]]. It originated in the initial network implementation in which it complemented the [[Internet_Protocol]] (IP), so the whole suite is commonly called [[TCP/IP_model|TCP/IP]]. TCP provides reliable, ordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating via an IP network.",
"Major Internet applications such as the [[World_Wide_Web]], [[Email|email]], remote administration, and file transfer rely on TCP. Applications that do not require reliable data stream service may use the [[User_Datagram_Protocol]] (UDP) instead, which provides a connectionless datagram service that prioritises time over reliability.",
("h2", "How it works"),
"Before exchanging data, two hosts perform a <b>three-way handshake</b> (SYN, SYN-ACK, ACK) to establish a connection and synchronise sequence numbers. Data is then sent as numbered segments; the receiver acknowledges receipt, lost segments are retransmitted, and flow control and congestion control algorithms adjust the sending rate to the receiver's capacity and the network's condition. TCP's congestion control — slow start, congestion avoidance, and their modern descendants such as CUBIC and BBR — is a major reason the shared Internet does not collapse under load.",
"The protocol was specified by [[Vint_Cerf]] and [[Bob_Kahn|Robert Kahn]] in the 1970s and standardised as RFC 793 in 1981; a modernised revision, RFC 9293, was published in 2022.",
],
"see_also": ["User_Datagram_Protocol", "Internet_protocol_suite", "Internet_Protocol", "Packet_switching"],
"unsure": ["Precise market share of CUBIC vs BBR congestion control is not public"],
},
{
"slug": "Internet_Protocol", "title": "Internet Protocol", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_protocol_suite",
"imgbox": "Diagram of an IP packet being routed hop-by-hop across several networks from source to destination",
"body": [
"The <b>Internet Protocol</b> (<b>IP</b>) is the network layer communications protocol in the [[Internet_protocol_suite|Internet protocol suite]] for relaying datagrams across network boundaries. Its routing function enables internetworking and essentially establishes the [[Internet]].",
"IP has the task of delivering packets from the source host to the destination host based solely on the [[IP_address|IP addresses]] in the packet headers. For this purpose, IP defines packet structures that encapsulate the data to be delivered, and addressing methods that label the datagram with source and destination information. IP makes no guarantees: packets may be lost, duplicated, reordered or corrupted — a 'best effort' service on which the transport protocols, principally [[Transmission_Control_Protocol|TCP]], build reliability.",
("h2", "Versions"),
"The first major version, [[IPv4]], still carries a large share of traffic decades after its 1981 standardisation. Its successor, [[IPv6]], with 128-bit addresses and a simplified header, was designed in the 1990s and is deployed alongside it. (Version numbers 5 and 7–9 were assigned to experimental or abandoned designs, which is why the successor to version 4 is version 6.)",
"IP was designed by [[Vint_Cerf]] and [[Bob_Kahn|Robert Kahn]] as part of their 1974 paper on packet network intercommunication — the paper often called the birth certificate of the Internet.",
],
"see_also": ["IPv4", "IPv6", "IP_address", "Routing", "Transmission_Control_Protocol"],
"unsure": [],
},
{
"slug": "Ethernet", "title": "Ethernet", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Computer_network",
"imgbox": "Photograph of yellow Ethernet cables plugged into a network switch",
"infobox": [("Invented", "1973–1974, Xerox PARC"), ("Inventors", "Robert Metcalfe, David Boggs"), ("Standard", "IEEE 802.3"), ("Typical speeds", "100 Mbit/s – 400 Gbit/s")],
"body": [
"<b>Ethernet</b> is a family of wired computer networking technologies commonly used in [[Local_area_network|local area networks]] (LANs), and also in metropolitan and wide area networks. It was commercialised in 1980 and first standardised in 1983 as IEEE 802.3, and has since become the dominant wired networking technology in homes, offices and data centres.",
"Ethernet was developed at Xerox PARC by Robert Metcalfe and David Boggs in 1973–1974, inspired by the ALOHAnet radio network; Metcalfe's memo sketching the idea is dated 22 May 1973, a day sometimes celebrated as Ethernet's birthday. The name comes from the 'luminiferous ether' once thought to carry light — here, the cable carrying signals to every station.",
("h2", "Evolution"),
"Early Ethernet shared a single coaxial cable among all stations, using CSMA/CD to arbitrate collisions: a station listened before talking and backed off if two talked at once. Speeds climbed from the experimental 2.94 Mbit/s to 10 Mbit/s (1980s), 100 Mbit/s Fast Ethernet (1995), Gigabit Ethernet (1998) and 10, 40, 100 and 400 gigabit versions. Modern networks use twisted-pair or fibre cabling in a star topology centred on [[Network_switch|switches]], which forward frames only to the destination port and have made collisions — and CSMA/CD — largely historical. Each Ethernet interface carries a globally unique 48-bit MAC address assigned by its manufacturer.",
],
"see_also": ["Local_area_network", "Wi-Fi", "Network_switch", "Computer_network"],
"unsure": ["400 Gbit/s standardisation dates (802.3bs, 2017)"],
},
{
"slug": "Wi-Fi", "title": "Wi-Fi", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Computer_network",
"imgbox": "The Wi-Fi logo, a stylised radio-wave symbol in black and white",
"infobox": [("Standard", "IEEE 802.11"), ("Brand owner", "Wi-Fi Alliance"), ("Introduced", "1997 (standard); 1999 (brand)"), ("Bands", "2.4 GHz, 5 GHz, 6 GHz")],
"body": [
"<b>Wi-Fi</b> is a family of wireless network protocols based on the IEEE 802.11 standards, commonly used for [[Local_area_network|local area networking]] of devices and for Internet access. A device equipped with Wi-Fi can connect to a network through a wireless access point — the box most homes call a router — which bridges the wireless and wired worlds.",
"The name, coined in 1999 by branding firm Interbrand for the industry consortium now called the Wi-Fi Alliance, is often said to play on 'hi-fi' (high fidelity); it is not officially short for 'wireless fidelity'. The underlying technology's roots reach back to a 1985 US regulatory decision opening unlicensed spectrum bands, and to work by a CSIRO team in Australia whose patents on multipath signal processing became foundational.",
("h2", "Generations"),
"Successive 802.11 amendments have multiplied speed and capacity: 802.11b (1999, 11 Mbit/s) brought mass adoption, aided by Apple's AirPort base station; 802.11g and n added speed; 802.11ac (Wi-Fi 5) moved to the 5 GHz band; Wi-Fi 6/6E (802.11ax) added the 6 GHz band and better handling of crowded areas; and Wi-Fi 7 (802.11be) pushes theoretical rates beyond 40 Gbit/s. Security evolved from the broken WEP through WPA and WPA2 to WPA3. Wi-Fi competes and coexists with wired [[Ethernet]] and mobile cellular data, and now carries the majority of the world's Internet traffic within buildings.",
],
"see_also": ["Ethernet", "Local_area_network", "Router_(computing)", "Computer_network"],
"unsure": ["Claimed share of global traffic over Wi-Fi varies by measurement source"],
},
{
"slug": "Local_area_network", "title": "Local area network", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Computer_network",
"imgbox": "Diagram of a small LAN: several computers and a printer connected through a switch and router",
"body": [
"A <b>local area network</b> (<b>LAN</b>) is a computer network that interconnects computers within a limited area such as a residence, school, laboratory, university campus or office building. By contrast, a [[Wide_area_network|wide area network]] (WAN) covers a much larger area and typically leases telecommunications circuits.",
"The two dominant LAN technologies are wired [[Ethernet]] and wireless [[Wi-Fi]] (WLAN). Within the LAN, [[Network_switch|switches]] forward traffic between devices, printers and servers are shared, and a [[Router_(computing)|router]] usually provides the single connection outward to the WAN and the [[Internet]]. Devices on the same LAN are typically given private [[IP_address|IP addresses]] and are reachable to each other directly, while outsiders see only the router's public address.",
"LANs emerged in the late 1970s with technologies such as ARCNET and Ethernet, replacing terminal-to-mainframe wiring with peer networking. LAN parties, office file sharing and home networks followed; today the distinction between a home LAN and the cloud services it reaches is increasingly blurred, but the local network remains the unit of trust and administration inside a building.",
],
"see_also": ["Ethernet", "Wi-Fi", "Wide_area_network", "Network_switch"],
"unsure": [],
},
{
"slug": "Wide_area_network", "title": "Wide area network", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Computer_network",
"imgbox": "Map diagram of a WAN linking office sites in several cities through a provider's backbone",
"body": [
"A <b>wide area network</b> (<b>WAN</b>) is a telecommunications network that extends over a large geographic area, typically a city, country, or intercontinental distances. Wide area networks are used to connect [[Local_area_network|local area networks]] and other networks together so that users and computers in one location can communicate with users and computers in other locations.",
"The largest WAN in existence is the [[Internet]] itself. Organisational WANs are built from leased lines, [[Modem|broadband]] links, MPLS services or encrypted tunnels ([[Virtual_private_network|VPNs]]) over the public Internet, and increasingly from software-defined WAN (SD-WAN) services that steer traffic dynamically between them. Because WAN links are slower, dearer and higher-latency than LAN links, WAN design focuses on prioritising important traffic and tolerating failure at any single site.",
"Historically, WANs ran protocols such as X.25 and Frame Relay over telephone infrastructure; today almost all WAN traffic is [[Internet_Protocol|IP]], carried on fibre-optic [[Internet_backbone|backbones]] and submarine cables.",
],
"see_also": ["Local_area_network", "Internet_backbone", "Virtual_private_network", "Computer_network"],
"unsure": [],
},
{
"slug": "Router_(computing)", "title": "Router (computing)", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Routing",
"imgbox": "Photograph of a home router with antennas and Ethernet ports",
"body": [
"A <b>router</b> is a networking device that forwards data packets between computer networks. Routers perform the traffic-directing functions on the [[Internet]]: a data packet is typically forwarded from one router to another through the networks that constitute an internetwork until it reaches its destination node.",
"A router is connected to two or more data lines from different IP networks. When a packet arrives, the router reads the destination [[IP_address|address]] in its header, consults its routing table — built by [[Routing|routing protocols]] or configured manually — and sends the packet out the appropriate interface toward its destination. The home devices usually called routers typically combine several functions in one box: a router proper, a [[Network_switch|switch]], a wireless access point for [[Wi-Fi]], a [[Modem|modem]] interface, a firewall and a DHCP server that assigns addresses to the household's devices.",
"At the network core, carrier-grade routers from vendors such as Cisco (whose founders commercialised the router in the 1980s) and Juniper move terabits per second between [[Internet_service_provider|providers]]. The first true routers — then called gateways — were the Interface Message Processors of the [[ARPANET]] and their successors designed in the 1970s.",
],
"see_also": ["Routing", "Network_switch", "Modem", "IP_address", "Border_Gateway_Protocol"],
"unsure": ["Cisco founding story (1984, Bosack and Lerner) is well documented but details of the Stanford connection are retold in many versions"],
},
{
"slug": "Network_switch", "title": "Network switch", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Ethernet",
"imgbox": "Photograph of a rack-mounted 24-port Ethernet switch in a wiring cabinet",
"body": [
"A <b>network switch</b> is a networking device that connects devices on a computer network by using packet switching to receive and forward data to the destination device. In an [[Ethernet]] [[Local_area_network|LAN]], a switch sits at the centre of a star topology and learns which MAC address is reachable on each port, so a frame is sent only where it needs to go.",
"Switches replaced the older network hub, which broadcast every frame to every port — wasting bandwidth and letting any device eavesdrop on all traffic. By maintaining a table mapping addresses to ports, a switch gives each connected pair the medium's full bandwidth and divides the network into separate collision domains. Managed switches add features such as VLANs (logically separate networks on the same hardware), link aggregation and quality-of-service controls, and are a standard fixture of office and data-centre networks, where top-of-rack switches connect servers at 10–100 Gbit/s.",
],
"see_also": ["Ethernet", "Router_(computing)", "Local_area_network"],
"unsure": [],
},
{
"slug": "Modem", "title": "Modem", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_service_provider",
"imgbox": "Photograph of a 1990s external dial-up modem with status lights",
"body": [
"A <b>modem</b> (from <i>modulator–demodulator</i>) is a hardware device that converts data from a digital format into a format suitable for an analog transmission medium, such as telephone lines or radio, and converts incoming analog signals back again. Modems let computers communicate over infrastructure that was never designed for data.",
"The classic dial-up modem modulated data into audio tones within the voice band of a telephone call. Speeds climbed from 300 bit/s in the 1960s to the 56 kbit/s of the 1990s home Internet era, accompanied by the famous screeching handshake as two modems negotiated. Voiceband modems gave way to broadband technologies that use far wider frequency ranges on the same wires — [[Digital_subscriber_line|DSL]] — or on cable television networks ([[Cable_modem|cable modems]]), and to fibre terminals (ONTs) that perform the analogous conversion for light. Cellular modems and the modem functions inside every smartphone apply the same principle to radio. The word survives in 'cable modem' and settings menus long after pure analog modulation became a niche.",
],
"see_also": ["Digital_subscriber_line", "Cable_modem", "Internet_service_provider", "Broadband"],
"unsure": [],
},
{
"slug": "Internet_service_provider", "title": "Internet service provider", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Photograph of an ISP's network operations centre with rows of server racks",
"body": [
"An <b>Internet service provider</b> (<b>ISP</b>) is an organisation that provides services for accessing, using, managing or participating in the [[Internet]]. ISPs can be organised in various forms, such as commercial, community-owned, non-profit, or otherwise privately owned.",
"Historically, Internet access began with university and research networks, then reached the public in the early 1990s through dial-up providers — companies such as CompuServe, AOL and thousands of local firms sold timed or flat-rate access over telephone lines with a [[Modem|modem]]. As [[Broadband|broadband]] arrived, access consolidated around telephone companies (DSL, then fibre) and cable companies, with mobile operators joining as 3G and 4G spread. ISPs interconnect with each other at [[Internet_exchange_point|Internet exchange points]] and through transit agreements, forming the tiers of the [[Internet_backbone|backbone]].",
"Beyond connectivity, ISPs typically provide [[Email|email]] accounts, [[Web_page|web]] hosting, [[Domain_name|domain name]] registration and customer routers. Their role in carrying all traffic has made them central to policy debates, including [[Net_neutrality|net neutrality]] — whether providers may favour or throttle particular services — and data-retention and lawful-access laws.",
],
"see_also": ["Broadband", "Modem", "Internet_backbone", "Net_neutrality", "Internet_exchange_point"],
"unsure": [],
},
{
"slug": "Broadband", "title": "Broadband", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet_service_provider",
"imgbox": "Photograph of a fibre-optic cable bundle with light shining from the strands",
"body": [
"In telecommunications, <b>broadband</b> is the wide-bandwidth data transmission that transports multiple signals at once; in common usage it simply means fast, always-on Internet access, in contrast to the dial-up [[Modem|modems]] that preceded it. Regulators define it by speed thresholds that keep rising — the US Federal Communications Commission raised its benchmark to 100 Mbit/s download and 20 Mbit/s upload in 2024.",
"The main fixed broadband technologies are [[Digital_subscriber_line|DSL]] over telephone lines, [[Cable_modem|cable]] over television networks, and fibre to the premises (FTTP), which offers gigabit speeds and the lowest latency and has become the preferred build in many countries. Fixed-wireless and satellite services — including low-Earth-orbit constellations such as Starlink — extend broadband to rural areas that cables have not reached.",
"Broadband's arrival in the 2000s changed what the Internet was for: always-on connections enabled the modern [[World_Wide_Web|web]] of streaming video, cloud services, video calls and online gaming, and made the connection a household utility comparable to electricity. Coverage and affordability gaps — the 'digital divide' — remain a major policy concern worldwide.",
],
"see_also": ["Digital_subscriber_line", "Cable_modem", "Internet_service_provider", "Modem"],
"unsure": ["FCC benchmark change to 100/20 in 2024 is recalled with moderate confidence"],
},
{
"slug": "Digital_subscriber_line", "title": "Digital subscriber line", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Broadband",
"imgbox": "Diagram showing DSL data travelling over a telephone line's high frequencies while voice uses the low band, separated by filters",
"body": [
"<b>Digital subscriber line</b> (<b>DSL</b>) is a family of technologies used to transmit digital data over telephone lines. DSL delivers Internet access by using the unused high-frequency capacity of the copper pair that already carried voice calls, so the telephone line can carry both simultaneously, split by simple filters at the customer's premises.",
"The most common form, ADSL (asymmetric DSL), provides faster download than upload, reflecting home usage patterns; speeds fall with distance from the exchange, from tens of megabits per second nearby to a few megabits several kilometres away. Later variants pushed further: ADSL2+, and VDSL/VDSL2, which achieve 50–100+ Mbit/s over short loops, often to a street cabinet fed by fibre (FTTC).",
"DSL was the first mass-market [[Broadband|broadband]] in many countries in the early 2000s, competing with [[Cable_modem|cable modems]]. It is now being retired in favour of full-fibre networks in numerous markets, though it remains in service for hundreds of millions of lines worldwide.",
],
"see_also": ["Broadband", "Modem", "Cable_modem", "Internet_service_provider"],
"unsure": ["Worldwide DSL line count is approximate"],
},
{
"slug": "Cable_modem", "title": "Cable modem", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Broadband",
"imgbox": "Photograph of a cable modem with coaxial cable and Ethernet connections",
"body": [
"A <b>cable modem</b> is a type of network bridge that provides bidirectional data communication via radio frequency channels on a hybrid fibre-coaxial (HFC) television network. Cable modems are primarily used to deliver [[Broadband|broadband]] Internet access in competition with [[Digital_subscriber_line|DSL]].",
"Cable systems send data using the DOCSIS standard (Data Over Cable Service Interface Specification), developed by CableLabs in the 1990s. Successive versions raised speeds dramatically: DOCSIS 3.0 bonded multiple television channels together, and DOCSIS 3.1 uses OFDM modulation to offer gigabit downstream service to tens of millions of homes, especially in North America where cable became the leading broadband platform. Subscribers share the capacity of their neighbourhood node, so speeds vary with local load.",
"As with DSL, cable networks are gradually being overbuilt or replaced by fibre to the premises, but the [[Modem|modem]] in the home — a small box translating between coax and [[Ethernet]] — remains the face of the connection for many households.",
],
"see_also": ["Modem", "Broadband", "Digital_subscriber_line", "Internet_service_provider"],
"unsure": [],
},
]

for p in PAGES:
    build(p)
finish()
