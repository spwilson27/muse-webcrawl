#!/usr/bin/env python3
import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl")
from bb_engine import build, finish

PAGES = [
{
"slug": "Encryption", "title": "Encryption", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Secure_Shell",
"imgbox": "Diagram of a plaintext message being scrambled into ciphertext by a key and unscrambled at the other end",
"body": [
"<b>Encryption</b> is the process of encoding information so that only authorised parties can access it, converting the original representation (plaintext) into an alternative form known as ciphertext. Encryption does not itself prevent interference or interception, but denies the intelligible content to would-be interceptors — the foundation on which privacy and security on the [[Internet]] are built.",
"Modern encryption rests on mathematics rather than secrecy of method. Symmetric algorithms (such as AES) use one shared key and carry the bulk of the world's encrypted data; public-key cryptography, published by Diffie and Hellman in 1976 and made practical by RSA in 1977, uses key pairs — one public, one private — so strangers can establish secrets over an open channel and sign messages digitally. The [[Internet_protocol_suite|protocols]] that use them are everywhere: TLS behind [[HTTPS]], [[Secure_Shell|SSH]] for administration, Signal-protocol encryption inside messaging apps.",
"Encryption is also a political question. The US government once classified strong cryptography as a munition, fought the distribution of PGP in the 1990s 'crypto wars', and periodically seeks mandated access ('going dark' debates), while cryptographers argue that any backdoor weakens security for everyone. The direction of travel, though, has been one-way: encryption went from a military technology to the default state of web traffic and personal messaging within one generation.",
],
"see_also": ["HTTPS", "Secure_Shell", "Public_key_certificate", "Virtual_private_network", "Password"],
"unsure": [],
},
{
"slug": "Internet_forum", "title": "Internet forum", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Bulletin_board_system",
"imgbox": "Screenshot-style image of a forum index page listing discussion boards with thread and post counts",
"body": [
"An <b>Internet forum</b>, or message board, is an online discussion site where people hold conversations in the form of posted messages. Forums are the direct descendants of [[Bulletin_board_system|bulletin board systems]] and [[Usenet]], organised hierarchically into categories, sub-forums and threads; unlike chat, messages are asynchronous and archived, so discussions accumulate into searchable public knowledge over years.",
"Forum software (phpBB, vBulletin, XenForo, Discourse) powered the 2000s golden age of niche communities: car clubs, support groups, hobbyists and gamers built vast threaded archives, with their own norms — moderators, sticky threads, signatures, post counts as status. Many famous support resources (and infamous communities, from Something Awful to 4chan, itself an imageboard variant) are forums in structure.",
"From the 2010s, algorithmic social media and centralised platforms — Reddit (a network of forum-like 'subreddits'), Facebook Groups, Discord servers — absorbed much forum activity, and many independent forums closed, taking their archives with them. The format survives because its virtues are real: chronological, topic-first, searchable discussion that a feed cannot replicate, and communities that own their own ground.",
],
"see_also": ["Bulletin_board_system", "Usenet", "Instant_messaging", "Social_media"],
"unsure": [],
},
{
"slug": "Web_hosting_service", "title": "Web hosting service", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Web_server",
"imgbox": "Photograph of a technician sliding a blade server into a rack at a hosting facility",
"body": [
"A <b>web hosting service</b> is a type of Internet hosting service that hosts [[Website|websites]] for clients; it offers the facilities required for them to create and maintain a site and makes it accessible on the [[World_Wide_Web]]. Web hosts are companies that provide space on a server they own or lease, plus [[Internet]] connectivity in a [[Data_center|data centre]].",
"The industry's classic tiers are: <b>shared hosting</b>, where hundreds of sites share one [[Web_server|server]] (cheap, the launchpad of the early web's GeoCities-era homepages and later [[WordPress]] blogs); <b>virtual private servers</b>, giving each customer a virtual machine; <b>dedicated hosting</b> of an entire physical machine; and <b>colocation</b>, where customers rent rack space for their own hardware. Reseller hosting and managed WordPress hosting fill the niches between.",
"From the 2010s, cloud platforms (Amazon Web Services and its rivals) and developer platforms (GitHub Pages, Netlify, Vercel) changed the market's centre of gravity: hosting became programmable infrastructure billed by the second, and static sites could be hosted free. The neighbourhood web host with a cPanel login nevertheless persists for millions of small sites — a reminder that 'the cloud' is, at bottom, someone's rack in someone's data centre.",
],
"see_also": ["Web_server", "Data_center", "Domain_name_registrar", "WordPress", "Cloud_computing"],
"unsure": [],
},
{
"slug": "Internet_meme", "title": "Internet meme", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "A collage of generic meme-format images: a distracted boyfriend stock photo and a cat at a dinner table (descriptions in text under each)",
"body": [
"An <b>Internet meme</b> is an idea, behaviour or style (meme) that spreads by imitation from person to person via the [[Internet]], usually for humorous purposes and typically as an image, video, GIF or catchphrase remixed by each new poster. The word derives from Richard Dawkins's 1976 concept of the <i>meme</i> as a unit of cultural transmission, analogous to a gene.",
"Early Internet memes were text and ritual: 'emoticons', ASCII art, chain emails, the Dancing Baby animation (1996), 'All your base are belong to us' (2001) and the spread of LOLcats and demotivational posters through [[Internet_forum|forums]]. Social media industrialised the form: image macros with Impact-font captions, reaction GIFs, TikTok sounds and endlessly re-captioned templates (Distracted Boyfriend, Woman Yelling at a Cat, Drake Posting) became a vernacular language — jokes whose grammar is the shared reference itself.",
"Memes are not only jokes: they are a compression format for opinion and identity, used in marketing, fandom, political campaigning and propaganda alike, moving at the speed of the feed and often dead within weeks. Their study — memetics reborn as internet studies — treats them as primary evidence of how culture now reproduces: variation, selection and inheritance at planetary scale.",
],
"see_also": ["Internet", "Internet_forum", "Social_media", "Usenet"],
"unsure": ["Specific meme examples dated by first wide circulation, which is fuzzy by nature"],
},
{
"slug": "CAPTCHA", "title": "CAPTCHA", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Web_page",
"imgbox": "Screenshot-style image of a distorted-text CAPTCHA challenge with wavy letters",
"body": [
"A <b>CAPTCHA</b> (a contrived acronym for 'Completely Automated Public Turing test to tell Computers and Humans Apart') is a type of challenge–response test used in computing to determine whether the user is human in order to deter bot attacks and spam. The classic form asks the user to type letters and numbers shown in a distorted image that automated software (supposedly) cannot read.",
"CAPTCHAs were developed around 1997–2000 at AltaVista (to stop bots submitting URLs) and given their name and popular form at Carnegie Mellon University by Luis von Ahn and colleagues. Their arms race with OCR and machine learning escalated distortions until the tests annoyed humans more than bots. Von Ahn's reCAPTCHA (2007, acquired by Google in 2009) turned the work to account — transcribing books and, later, labelling street imagery — and its second version replaced typing with a behavioural checkbox ('I'm not a robot'), while version 3 scores users invisibly.",
"The acronym is a trademark of Carnegie Mellon. CAPTCHAs remain a friction point in web accessibility and a philosophical curiosity: a reverse Turing test, administered billions of times, whose difficulty for machines collapsed as AI improved — pushing the web toward passkeys, device attestation and proof-of-personhood schemes.",
],
"see_also": ["Spam_(electronic)", "Malware", "Password", "Web_page"],
"unsure": ["AltaVista priority vs CMU development is presented as the standard account; details vary by source"],
},
{
"slug": "Password", "title": "Password", "depth": 3,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Screenshot-style image of a login form's password field showing masked dots and a strength meter",
"body": [
"A <b>password</b> is a secret word, phrase, or string of characters used to confirm a user's identity in an authentication process. Passwords have guarded everything since Roman sentries' watchwords; in computing they date to the first time-sharing systems of the early 1960s (MIT's CTSS), where — legend records — the first password theft followed within years, a user printing the master password file to use others' time.",
"Good password practice is a fight between human memory and machine guessing. Systems should store passwords only as salted cryptographic hashes, never in plaintext; users are told to choose long, unique passwords per site — advice impossible to follow unaided across hundreds of accounts, hence password managers, which generate and store random passwords behind one master password. Breach databases of billions of real passwords feed 'credential stuffing' attacks, which is why reuse is the cardinal sin and why [[Phishing|phishing]] and [[Multi-factor_authentication|multi-factor authentication]] dominate modern account security.",
"The industry has long predicted the password's death; the passkey standard (FIDO2/WebAuthn, adopted by Apple, Google and Microsoft in the 2020s) — cryptographic keys unlocked by biometrics, synced across devices, and un-phishable — is the first successor with real momentum, though the humble password field remains the web's most common doorway.",
],
"see_also": ["Multi-factor_authentication", "Phishing", "Encryption", "CAPTCHA", "Public_key_certificate"],
"unsure": ["CTSS password-theft anecdote (Allan Scherr, 1962) is the standard retelling"],
},
{
"slug": "Multi-factor_authentication", "title": "Multi-factor authentication", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Password",
"imgbox": "Photograph of a smartphone showing a six-digit one-time code next to a laptop login screen",
"body": [
"<b>Multi-factor authentication</b> (<b>MFA</b>) is an electronic authentication method in which a user is granted access to a [[Website|website]] or application only after successfully presenting two or more pieces of evidence ('factors') to an authentication mechanism. The classic taxonomy: something you <i>know</i> (a [[Password|password]]), something you <i>have</i> (a phone, a hardware key), and something you <i>are</i> (a fingerprint or face). Two-factor authentication (2FA) is the common two-factor subset.",
"MFA became mainstream as password-only security failed: banks issued hardware tokens in the 2000s, Google added 2-Step Verification in 2011, and time-based one-time codes (TOTP, from authenticator apps) and push approvals spread through the following decade with the growth of [[Phishing|phishing]] and credential stuffing. Not all factors are equal — SMS codes can be intercepted or SIM-swapped, app codes can be phished in real time, while FIDO2/WebAuthn hardware keys and passkeys cryptographically bind the login to the real site and resist phishing outright.",
"Regulators and platforms increasingly require MFA for administrators, developers and financial accounts, and large providers have made it default-on for billions of users. It is now regarded, along with prompt patching, as the single most effective consumer security measure — blocking the overwhelming majority of automated account-takeover attacks in published studies.",
],
"see_also": ["Password", "Phishing", "Encryption", "CAPTCHA"],
"unsure": ["Effectiveness statistics quoted vary by study (Microsoft's often-cited figure is >99% of automated attacks blocked)"],
},
{
"slug": "Public_key_certificate", "title": "Public key certificate", "depth": 4,
"source": "https://en.wikipedia.org/wiki/HTTPS",
"imgbox": "Diagram of a certificate chain: a site's certificate signed by an intermediate CA, signed by a root CA",
"body": [
"In cryptography, a <b>public key certificate</b>, also known as a digital certificate or identity certificate, is an electronic document used to prove the validity of a public key. The certificate includes the key itself, information about the identity of its owner (the 'subject', such as a [[Domain_name|domain name]]), and the digital signature of the entity that verified the certificate's contents — its issuer, a [[Certificate_authority|certificate authority]].",
"Certificates (in the X.509 format) are the trust machinery of the web: when a browser makes an [[HTTPS]] connection, the server presents a certificate for its domain; the browser verifies the signature chain up to a root authority built into its trust store, checks the name and expiry, and only then proceeds. Variants by validation level — domain-validated (DV), organisation-validated (OV) and extended validation (EV) — reflect how thoroughly the issuer checked the applicant; modern browsers treat them alike in the interface, showing only the padlock.",
"The system's weak points are its authorities: any trusted CA can issue for any domain, so compromises (DigiNotar's 2011 breach and collapse) and mis-issuance led to Certificate Transparency — public, append-only logs of every issued certificate, now required by browsers — and to steadily shorter certificate lifetimes, pushing the web toward automated renewal.",
],
"see_also": ["Certificate_authority", "HTTPS", "Encryption", "Let's_Encrypt"],
"unsure": [],
},
{
"slug": "Certificate_authority", "title": "Certificate authority", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Public_key_certificate",
"imgbox": "Photograph of a high-security CA signing ceremony with hardware security modules behind glass",
"body": [
"In cryptography, a <b>certificate authority</b> or <b>certification authority</b> (<b>CA</b>) is an entity that stores, signs, and issues digital certificates. A CA acts as a trusted third party — trusted both by the subject (owner) of the [[Public_key_certificate|certificate]] and by the party relying upon the certificate — and its root certificates are distributed in the trust stores of browsers and operating systems, which is what makes [[HTTPS]] work at Internet scale.",
"CAs validate that an applicant controls the domain named in the certificate (and, for higher-assurance certificates, the applicant's legal identity) before issuing. The industry is governed by the CA/Browser Forum's Baseline Requirements and policed by the browser root programmes, which can distrust a misbehaving CA — an existential sanction, applied in the past to DigiNotar (2011, after a breach produced fraudulent certificates used in interception) and to Symantec's CA business (2017–2018, after systematic mis-issuance).",
"The market was transformed by [[Let's_Encrypt]] (2015), a non-profit CA issuing free, automated, domain-validated certificates, which made HTTPS the web's default; the largest commercial CAs (DigiCert, Sectigo, GoDaddy) remain significant, and the total population of trusted roots numbers in the dozens of organisations.",
],
"see_also": ["Public_key_certificate", "HTTPS", "Let's_Encrypt", "Encryption"],
"unsure": [],
},
{
"slug": "Let's_Encrypt", "title": "Let's Encrypt", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Certificate_authority",
"imgbox": "The Let's Encrypt logo: a rising sun over a horizon in blue and orange",
"infobox": [("Launched", "12 April 2016 (announced 2014)"), ("Operator", "Internet Security Research Group (ISRG)"), ("Type", "Non-profit [[Certificate_authority|certificate authority]]"), ("Cost", "Free")],
"body": [
"<b>Let's Encrypt</b> is a non-profit [[Certificate_authority|certificate authority]] providing free [[Public_key_certificate|TLS certificates]], launched on 12 April 2016 and operated by the Internet Security Research Group. Its mission is a web that is [[HTTPS]]-encrypted by default: by making certificates free, automatic and easy (via the ACME protocol and tools such as Certbot), it removed the cost and bureaucracy that had kept most of the web unencrypted.",
"The service began as a project of the Electronic Frontier Foundation, Mozilla and the University of Michigan, with Cisco and Akamai as founding sponsors. Its growth was rapid: 100 million certificates within 14 months of launch, and by the early 2020s it was serving certificates for hundreds of millions of websites — the majority of the web's certificates — issuing over a million new ones on a typical day, each valid for 90 days to encourage automation.",
"Let's Encrypt is widely credited, alongside browser pressure, with tipping HTTPS from a minority practice for banks and shops into the web's default state — arguably the largest successful security deployment in Internet history, achieved by giving the product away.",
],
"see_also": ["Certificate_authority", "Public_key_certificate", "HTTPS", "Encryption"],
"unsure": ["Milestone dates: public launch April 2016 and 100-millionth certificate June 2017 are the commonly cited figures"],
},
{
"slug": "Tor_(network)", "title": "Tor (network)", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Internet",
"imgbox": "Diagram of onion routing: a message wrapped in three layers of encryption passing through three relays",
"body": [
"<b>Tor</b> is free and open-source software for enabling anonymous communication. It directs [[Internet]] traffic via a free overlay network consisting of more than several thousand relays, using a technique called <i>onion routing</i>: traffic is wrapped in successive layers of [[Encryption|encryption]] and bounced through (typically) three volunteer-run relays, each of which knows only its predecessor and successor, so no single point can link a user to their destination.",
"Onion routing was developed in the mid-1990s at the US Naval Research Laboratory to protect government communications; the Tor code was released under a free licence in 2002–2003, championed by Roger Dingledine and Nick Mathewson, and is maintained by the non-profit Tor Project. The Tor Browser — a hardened [[Firefox]] derivative — is the usual way in. Tor also hosts <i>onion services</i> (sites reachable only inside the network, with addresses ending in .onion), used by news organisations (SecureDrop whistleblowing), social networks and ordinary services as well as by illicit markets.",
"Tor's users include journalists, activists and dissidents evading censorship, law enforcement, and ordinary people avoiding tracking; its anonymity is strong but not absolute — well-resourced adversaries correlating traffic at both ends remain the documented threat. Like encryption itself, it is a tool whose politics follow its users.",
],
"see_also": ["Dark_web", "Encryption", "Virtual_private_network", "Firefox", "Internet"],
"unsure": ["Relay counts and user numbers fluctuate; kept general"],
},
{
"slug": "Dark_web", "title": "Dark web", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Tor_(network)",
"imgbox": "Stylised graphic of an iceberg: the small visible surface web above water, the vast deep web below, and a small dark section at the base",
"body": [
"The <b>dark web</b> is the [[World_Wide_Web]] content that exists on <i>darknets</i>: overlay networks that use the [[Internet]] but require specific software, configurations, or authorisation to access. The best known is [[Tor_(network)|Tor]], whose '.onion' services are unreachable by ordinary browsers; others include I2P and Freenet.",
"The dark web is a small part of the [[Deep_web|deep web]] — the far larger body of content search engines do not index (webmail inboxes, banking portals, paywalled and database-driven pages), most of it mundane. The dark web proper mixes the legitimate and the illicit: whistleblowing platforms (SecureDrop, used by major newspapers), mirrors of news and social sites for censored countries, privacy-conscious services — and the cryptomarkets for drugs and stolen data that dominate its press image, beginning with Silk Road (2011–2013), whose founder Ross Ulbricht's prosecution became a cause célèbre.",
"Journalistic coverage often exaggerates its size: studies consistently find the dark web is tiny compared to the surface web, and largely inactive or fraudulent in its criminal corners. Its significance is less its scale than its existence proof — that the Internet's architecture still permits publishing that no authority can easily switch off, for purposes noble and base alike.",
],
"see_also": ["Tor_(network)", "Deep_web", "Encryption", "Internet"],
"unsure": ["Size estimates of the dark web vary in method and are kept qualitative"],
},
{
"slug": "Deep_web", "title": "Deep web", "depth": 4,
"source": "https://en.wikipedia.org/wiki/Dark_web",
"imgbox": "Diagram of an iceberg showing the small indexed surface web above the waterline and the large unindexed deep web beneath",
"body": [
"The <b>deep web</b> consists of parts of the [[World_Wide_Web]] whose contents are not indexed by standard web search engines. The term was coined by Michael K. Bergman in a 2001 paper, which estimated the deep web at hundreds of times the size of the 'surface web' — though the estimate reflects that most web content is generated dynamically or sits behind forms and logins, rather than anything sinister.",
"Everyday examples of deep web content include webmail inboxes, online banking, subscription publications, corporate intranets, medical records, academic databases and the results of any query-driven search: pages that exist only when a specific request generates them, or that require authentication. Search crawlers cannot log in, submit every form, or see behind paywalls, so this content — the bulk of the web by volume — is invisible to [[Google_Search|Google]] and its rivals.",
"The deep web is routinely confused with the [[Dark_web|dark web]], the small, intentionally hidden subset accessible only through anonymising networks such as [[Tor_(network)|Tor]]. Conflating the two — mundane privacy with criminal concealment — is one of the durable errors of Internet journalism.",
],
"see_also": ["Dark_web", "Tor_(network)", "Search_engine", "World_Wide_Web"],
"unsure": ["Bergman's 2001 size estimate (400-550x) is famous but methodologically dated"],
},
]

for p in PAGES:
    build(p)
finish()
