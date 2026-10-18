#!/usr/bin/env python3
# Crawler AD builder: Philosophy & Religion branch. All content from memory.
import os, json, datetime, urllib.parse

ROOT = "/home/hatch/workspace/muse-webcrawl"
WIKI = os.path.join(ROOT, "web/en.wikipedia.org/wiki")
LEDGER = os.path.join(ROOT, "ledgers/crawler-AD.jsonl")
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()

CSS = """body{font-family:sans-serif;margin:0;color:#202122;background:#fff;font-size:14px;line-height:1.65}
a{color:#0645ad;text-decoration:none}a:hover{text-decoration:underline}
.top{background:#f8f9fa;border-bottom:1px solid #a7d7f9;padding:8px 18px;font-family:Georgia,serif;font-size:20px}
.wrap{max-width:960px;margin:0 auto;padding:18px 22px}
h1{font-family:Georgia,serif;font-weight:normal;font-size:28px;border-bottom:1px solid #a2a9b1;padding-bottom:4px}
h2{font-family:Georgia,serif;font-weight:normal;font-size:21px;border-bottom:1px solid #a2a9b1;margin-top:24px}
h3{font-family:Georgia,serif;font-weight:normal;font-size:16.5px;margin-top:18px}
.infobox{float:right;width:270px;border:1px solid #a2a9b1;background:#f8f9fa;font-size:12.5px;margin:4px 0 14px 18px;border-collapse:collapse}
.infobox th{background:#eaf3ff;padding:5px 8px;text-align:center;font-size:14px}
.infobox td{padding:4px 8px;border-top:1px solid #eaecf0;vertical-align:top}
.infobox td:first-child{font-weight:bold;width:38%}
.imgbox{border:1px solid #c8ccd1;background:#f8f9fa;color:#54595d;padding:20px 10px;text-align:center;font-size:12px;margin:8px 0}
.imgbox img{max-width:100%}
.hat{font-size:13px;color:#54595d;font-style:italic}
.thumb{float:right;clear:right;width:230px;border:1px solid #c8ccd1;background:#f8f9fa;padding:4px;margin:4px 0 12px 16px;font-size:12px;color:#202122}
.thumb .imgbox{margin:0;border:none}
.thumb p{margin:4px 2px}
footer{border-top:1px solid #a2a9b1;margin-top:30px;padding-top:8px;font-size:12px;color:#54595d;clear:both}"""

def L(slug, text=None):
    """link to another wiki page in same folder space"""
    return '<a href="../%s/index.html">%s</a>' % (slug, text if text is not None else slug.replace("_", " "))

def page_html(p):
    ib = ""
    if p.get("infobox"):
        rows = "".join('<tr><td>%s</td><td>%s</td></tr>' % (k, v) for k, v in p["infobox"])
        ib = '<table class="infobox"><tr><th colspan="2">%s</th></tr>%s</table>' % (p["title"], rows)
    lead_img = ""
    if p.get("img"):
        lead_img = '<div class="imgbox">[Image: %s]</div>' % p["img"]
    body_secs = ""
    for h, html in p["sections"]:
        body_secs += "<h2>%s</h2>%s" % (h, html)
    seealso = ""
    if p.get("seealso"):
        links = ", ".join(L(s) for s in p["seealso"])
        seealso = '<h2>See also</h2><p>%s</p>' % links
    return ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><title>%s - Wikipedia</title>'
            '<style>%s</style></head>\n<body><div class="top">Wikipedia <span style="font-size:12px;color:#54595d">'
            'The Free Encyclopedia</span></div>\n<div class="wrap"><p class="hat">From Wikipedia, the free encyclopedia</p>\n'
            '<h1>%s</h1>%s%s<p>%s</p>%s%s'
            '<footer>Retrieved from "https://en.wikipedia.org/wiki/%s" &middot; This page is a from-memory recreation for the muse-webcrawl experiment.</footer></div></body></html>'
            ) % (p["title"], CSS, p["title"], ib, lead_img, p["lead"], body_secs, seealso, p["slug"])

PAGES = []
def add(**kw):
    PAGES.append(kw)

add(slug="Epicurus", title="Epicurus",
    infobox=[("Born", "341 BC, Samos"), ("Died", "270 BC, Athens"), ("School", "Epicureanism (founder)"), ("Notable ideas", "Pleasure as absence of pain (ataraxia, aponia); the tetrapharmakos; atomic swerve")],
    img="A marble bust of Epicurus",
    lead="<b>Epicurus</b> (341–270 BC) was an ancient Greek philosopher who founded Epicureanism, one of the most influential schools of the Hellenistic world. In his Athens school, the Garden — unusually open to women and slaves — he taught that pleasure, correctly understood as the absence of pain in body (<i>aponia</i>) and trouble in mind (<i>ataraxia</i>), is the goal of life; most desires are empty, friendships are life's greatest security, and the gods, though real, do not intervene — so death is nothing to us, 'for when we exist, death is not; and when death exists, we are not'.",
    sections=[("Physics and legacy", "<p>Epicurus adopted Democritus's atomism, adding a random 'swerve' (<i>clinamen</i>) to break causal chains and make free will possible — expounded in Lucretius's Latin poem <i>De Rerum Natura</i>, whose rediscovery in 1417 helped ignite the Renaissance. Slender surviving letters and maxims belie the school's 700-year life; his name survives distorted in 'epicurean' indulgence, almost the opposite of his frugal doctrine.</p>")],
    seealso=["Stoicism", "Philosophy", "Ataraxia"],
    outgoing=["Stoicism", "Philosophy", "Ancient_Greece"],
    unsure=[])

add(slug="Diogenes", title="Diogenes",
    infobox=[("Born", "c. 412 BC, Sinope"), ("Died", "323 BC, Corinth"), ("School", "Cynicism"), ("Known for", "Living in a tub; the lantern search for an honest man; defacing the currency")],
    img="A classical painting of Diogenes seated in his large ceramic tub, lantern beside him",
    lead="<b>Diogenes of Sinope</b> (c. 412 – 323 BC) was a Greek philosopher and archetypal Cynic, who made a virtue of poverty and shamelessness. Exiled from Sinope for defacing the currency, he lived in Athens and Corinth in a large ceramic jar (a <i>pithos</i>, often rendered 'tub'), owned only a cloak, staff and wooden bowl — the last discarded on seeing a child drink from cupped hands — and performed his philosophy in public: searching with a lantern in daylight for an honest man, and, when Alexander the Great offered him any favour, asking him to stop blocking the sun.",
    sections=[("Legacy", "<p>Diogenes' anecdotes, preserved by Diogenes Laertius, made him philosophy's great performance artist: his life was his argument that civilisation's conventions are mostly fraud and that happiness needs nothing. The Cynics influenced " + L("Stoicism") + " (Zeno studied with Diogenes' pupil Crates) and, in modern usage, inverted: 'cynic' now means a sneering unbeliever in motives, nearly reversing his idealistic scorn.</p>")],
    seealso=["Stoicism", "Zeno_of_Citium", "Philosophy"],
    outgoing=["Stoicism", "Zeno_of_Citium", "Philosophy", "Ancient_Greece"],
    unsure=["Anecdotes are traditional and partly apocryphal; dates approximate"])

add(slug="Plotinus", title="Plotinus",
    infobox=[("Born", "204/5 AD, Egypt"), ("Died", "270 AD, Campania"), ("School", "Neoplatonism (founder)"), ("Notable work", "The Enneads (edited by Porphyry)")],
    img="A Roman marble bust traditionally identified as Plotinus",
    lead="<b>Plotinus</b> (204/5–270 AD) was a philosopher of Greek descent born in Egypt, the founder of Neoplatonism — the last great system of ancient pagan philosophy. Studying in Alexandria under Ammonius Saccas, he settled in Rome and taught that all reality emanates from the One, an ineffable source beyond being, descending through Intellect (<i>Nous</i>) and Soul to the material world, and that the soul's task is return ('the flight of the alone to the Alone').",
    sections=[("Influence", "<p>His lectures, edited by his pupil Porphyry as the <i>Enneads</i>, profoundly shaped Christian theology (via Augustine and Pseudo-Dionysius), Islamic philosophy, Jewish thought and Renaissance Platonism (Ficino). Porphyry's biography describes a man seemingly ashamed of his body who reportedly attained ecstatic union with the One four times.</p>")],
    seealso=["Plato", "Augustine_of_Hippo", "Philosophy", "Mysticism"],
    outgoing=["Plato", "Augustine_of_Hippo", "Philosophy", "Mysticism"],
    unsure=[])

add(slug="Hypatia", title="Hypatia",
    infobox=[("Born", "c. 350–370 AD, Alexandria, Egypt"), ("Died", "March 415 AD, Alexandria"), ("Fields", "Mathematics, astronomy, Neoplatonist philosophy"), ("Father", "Theon of Alexandria")],
    img="A painting of Hypatia teaching in Alexandria",
    lead="<b>Hypatia</b> (born c. 350–370; died 415 AD) was a Hellenistic Neoplatonist philosopher, astronomer and mathematician who lived in Alexandria, Egypt, then part of the Eastern Roman Empire. Head of the city's Platonist school, she taught mathematics and philosophy to students from across the Mediterranean, edited and commented on works of Apollonius, Diophantus and Ptolemy, and advised the imperial prefect Orestes. In 415, amid a power struggle between Orestes and Bishop Cyril, a Christian mob seized and murdered her — an atrocity that made her an enduring symbol of learning martyred by fanaticism.",
    sections=[("Sources and legacy", "<p>Accounts come from Socrates of Constantinople's church history (sympathetic), Damascius (pagan, bitter), and letters of her pupil Synesius. Details popularly attached to her — inventing the hydrometer, the sack of the Great Library at her death — are later accretions. She remains the most famous woman philosopher of antiquity, reclaimed by feminists, scientists and novelists (Kingsley's <i>Hypatia</i>, the film <i>Agora</i>).</p>")],
    seealso=["Plotinus", "Philosophy", "Alexandria"],
    outgoing=["Plotinus", "Philosophy", "Mysticism"],
    unsure=["Birth year uncertain within c. 350–370; details of teaching largely from letters of Synesius"])

add(slug="Boethius", title="Boethius",
    infobox=[("Born", "c. 477, Rome"), ("Died", "524, Pavia"), ("Notable work", "The Consolation of Philosophy (written in prison, c. 524)"), ("Known for", "Transmitting Greek logic to the Latin Middle Ages; 'the last of the Romans'")],
    img="A medieval manuscript illumination of Boethius in prison visited by Lady Philosophy",
    lead="<b>Anicius Manlius Severinus Boethius</b> (c. 477–524) was a Roman senator, consul and philosopher of the Ostrogothic kingdom, whose translations and commentaries on Aristotle's logic preserved Greek philosophy for the Latin West. Imprisoned on (probably fabricated) treason charges by King Theodoric, he wrote in prison his masterpiece, <i>The Consolation of Philosophy</i> — a dialogue with Lady Philosophy on fortune, providence and free will — before being executed in 524.",
    sections=[("Influence", "<p>The <i>Consolation</i>, with its image of Fortune's wheel, was among the most copied and translated books of the Middle Ages (into English by Alfred the Great, Chaucer and Elizabeth I). His project — to translate all of Plato and Aristotle and show their harmony — died with him, leaving the West with fragments of Greek learning for six centuries.</p>")],
    seealso=["Philosophy", "Augustine_of_Hippo", "Scholasticism", "Free_will"],
    outgoing=["Philosophy", "Augustine_of_Hippo", "Scholasticism", "Free_will"],
    unsure=[])

add(slug="Anselm_of_Canterbury", title="Anselm of Canterbury",
    infobox=[("Born", "1033, Aosta, Italy"), ("Died", "21 April 1109, Canterbury, England"), ("Known for", "Ontological argument (Proslogion, 1078); satisfaction theory of atonement (Cur Deus Homo)")],
    img="A stained-glass portrait of Saint Anselm in archbishop's vestments",
    lead="<b>Saint Anselm of Canterbury</b> (1033–1109) was an Italian Benedictine monk, abbot and Archbishop of Canterbury, called the father of " + L("Scholasticism") + ". His motto 'faith seeking understanding' produced the " + L("Ontological_argument", "ontological argument") + " for God's existence in the <i>Proslogion</i> (1078) and, in <i>Cur Deus Homo</i>, the satisfaction theory of atonement: Christ's death repays the infinite debt human sin owes God's honour.",
    sections=[("Career", "<p>Anselm twice clashed with kings (William II, Henry I) over investiture and was exiled; his rigorous, prayerful treatises modelled the scholastic method of reasoned inquiry within faith. He was canonised (1494 in the usual reckoning) and declared a Doctor of the Church in 1720.</p>")],
    seealso=["Ontological_argument", "Scholasticism", "Thomas_Aquinas", "Theology"],
    outgoing=["Ontological_argument", "Scholasticism", "Thomas_Aquinas", "Theology", "Philosophy_of_religion"],
    unsure=["Canonisation date accounts vary (1494 by Alexander VI is commonly cited)"])

add(slug="William_of_Ockham", title="William of Ockham",
    infobox=[("Born", "c. 1287, Ockham, Surrey, England"), ("Died", "1347, Munich"), ("School", "Scholasticism; nominalism"), ("Known for", "Occam's razor; nominalism; political writings against papal power")],
    img="A sketch portrait of William of Ockham from a manuscript, in Franciscan habit",
    lead="<b>William of Ockham</b> (c. 1287–1347) was an English Franciscan friar and scholastic philosopher, a leading figure of late medieval thought. His principle of parsimony — 'entities must not be multiplied beyond necessity', <b>Occam's razor</b> — and his nominalism (universals are names, not things) pared metaphysics to a lean ontology of individuals. Summoned to Avignon on heresy charges, he fled to the court of Emperor Louis IV in Munich and spent his last decades writing explosive tracts on poverty, heresy and the limits of papal power.",
    sections=[("Thought", "<p>Ockham's logic (<i>Summa Logicae</i>) and his voluntarist theology — God's absolute power unconstrained even by logical-looking necessities — are often (too simply) cast as dissolving the scholastic synthesis and clearing ground for modern science and political theory. He probably died in the Black Death of 1347–49.</p>")],
    seealso=["Nominalism", "Scholasticism", "Thomas_Aquinas", "Metaphysics"],
    outgoing=["Nominalism", "Scholasticism", "Thomas_Aquinas", "Metaphysics", "Philosophy"],
    unsure=["Razor's exact Latin formula is a later crystallisation of his repeated principle"])

add(slug="Thomas_Hobbes", title="Thomas Hobbes",
    infobox=[("Born", "5 April 1588, Westport, England"), ("Died", "4 December 1679, Hardwick Hall"), ("Notable work", "Leviathan (1651)"), ("Notable ideas", "Social contract; state of nature as 'war of all against all'; materialism")],
    img="A portrait of Thomas Hobbes in old age with a long white beard",
    lead="<b>Thomas Hobbes</b> (1588–1679) was an English philosopher whose <i>Leviathan</i> (1651), written amid civil war, founded modern political philosophy's " + L("Social_contract") + " tradition. Hobbes argued that humans in the state of nature — equal, fearful and competing — live lives 'solitary, poor, nasty, brutish, and short', and rationally surrender nearly all rights to an absolute sovereign for security; his materialism made even thought a kind of motion.",
    sections=[("Life and thought", "<p>Educated at Oxford, tutor to the Cavendish family, Hobbes travelled with Francis Bacon, translated Thucydides, and quarrelled with Descartes and the Royal Society alike. <i>Leviathan</i>'s psychology of fear and glory, its covenant theory and its Erastian subordination of church to state scandalised contemporaries ('the Monster of Malmesbury') and still structure debates on authority, anarchy and international relations realism.</p>")],
    seealso=["Social_contract", "John_Locke", "Philosophy"],
    outgoing=["Social_contract", "John_Locke", "Philosophy"],
    unsure=[])

add(slug="Voltaire", title="Voltaire",
    infobox=[("Born", "21 November 1694, Paris, France"), ("Died", "30 May 1778, Paris"), ("Real name", "François-Marie Arouet"), ("Notable works", "Candide (1759); Letters on the English (1733); Treatise on Tolerance (1763)"), ("Causes", "Freedom of speech and religion; against fanaticism ('Écrasez l'infâme')")],
    img="A portrait of Voltaire in old age, sharp-featured and smiling wryly, by Houdon",
    lead="<b>Voltaire</b> (1694–1778), pen name of François-Marie Arouet, was a French Enlightenment writer, philosopher and historian, the age's most famous champion of civil liberties. Imprisoned in the Bastille and exiled to England, he returned with <i>Letters on the English</i> praising British tolerance and science; his novella <i>Candide</i> (1759) satirised Leibnizian optimism ('all is for the best') after the Lisbon earthquake, and his campaigns for victims of religious persecution — the Calas and Sirven cases — made 'Écrasez l'infâme' ('crush the infamous') the war-cry against fanaticism.",
    sections=[("Thought", "<p>A deist who built a church while savaging churches' intolerance, Voltaire defended freedom of expression with unmatched wit ('I disapprove of what you say, but I will defend to the death your right to say it' is his biographer's paraphrase, not his sentence). His histories, plays, dictionary and vast correspondence made him Europe's literary dictator; his return to Paris in 1778 was a national apotheosis.</p>")],
    seealso=["Enlightenment", "Philosophy", "Atheism", "Jean-Jacques_Rousseau"],
    outgoing=["Enlightenment", "Philosophy", "Jean-Jacques_Rousseau", "Immanuel_Kant"],
    unsure=[])

add(slug="Jean-Jacques_Rousseau", title="Jean-Jacques Rousseau",
    infobox=[("Born", "28 June 1712, Geneva"), ("Died", "2 July 1778, Ermenonville, France"), ("Notable works", "Discourse on Inequality (1755); The Social Contract (1762); Émile (1762); Confessions (1782)"), ("Notable ideas", "Noble savage (phrase not his); general will; amour de soi vs amour-propre")],
    img="A portrait of Jean-Jacques Rousseau in Armenian-style dress, by Allan Ramsay",
    lead="<b>Jean-Jacques Rousseau</b> (1712–1778) was a Genevan philosopher, writer and composer whose thought transformed politics, education and literature. His <i>Discourse on Inequality</i> blamed civilisation and property for corrupting natural human goodness and pity; <i>The Social Contract</i> (1762) opened 'Man is born free, and everywhere he is in chains' and grounded legitimacy in the general will; <i>Émile</i> revolutionised educational thought; and his <i>Confessions</i> invented modern autobiography.",
    sections=[("Influence and turmoil", "<p>Persecuted for <i>Émile</i>'s religious profession, hounded across Europe, increasingly paranoid, Rousseau quarrelled with Hume and the philosophes who had been his friends. The French Revolution canonised him (his remains moved to the Panthéon in 1794); his legacy splits between democratic theory and critics, from Burke to Popper, who read totalitarian seeds in the general will.</p>")],
    seealso=["Social_contract", "Enlightenment", "John_Locke", "Voltaire"],
    outgoing=["Social_contract", "Enlightenment", "John_Locke", "Voltaire", "Immanuel_Kant"],
    unsure=[])

add(slug="Mary_Wollstonecraft", title="Mary Wollstonecraft",
    infobox=[("Born", "27 April 1759, London, England"), ("Died", "10 September 1797, London"), ("Notable work", "A Vindication of the Rights of Woman (1792)"), ("Known for", "Foundational feminist philosopher")],
    img="A portrait of Mary Wollstonecraft by John Opie, in a white dress with loose hair",
    lead="<b>Mary Wollstonecraft</b> (1759–1797) was an English writer and philosopher, author of <i>A Vindication of the Rights of Woman</i> (1792), one of the earliest works of feminist philosophy. Against Rousseau and the conventions of female education she argued that women appear intellectually inferior only because they are denied education: give them the same cultivation of reason and virtue, economic independence and civil standing, and the supposed inferiority would vanish.",
    sections=[("Life and legacy", "<p>Wollstonecraft answered Burke's <i>Reflections</i> with <i>A Vindication of the Rights of Men</i> (1790), reported from revolutionary Paris, and scandalised Georgian England with her unconventional life — an irregular union, a child out of wedlock, marriage to William Godwin. She died of puerperal fever days after giving birth to her second daughter, Mary Shelley. Godwin's candid <i>Memoirs</i> wrecked her reputation for a century; 20th-century feminists restored her as a founding thinker.</p>")],
    seealso=["Feminism", "Enlightenment", "Jean-Jacques_Rousseau", "John_Stuart_Mill"],
    outgoing=["Enlightenment", "Jean-Jacques_Rousseau", "John_Stuart_Mill", "Philosophy"],
    unsure=[])

add(slug="Theravada", title="Theravada",
    infobox=[("Type", "School of Buddhism ('School of the Elders')"), ("Regions", "Sri Lanka, Thailand, Myanmar, Cambodia, Laos"), ("Scriptures", "Pali Canon (Tipitaka)"), ("Goal", "Arhatship; nirvana")],
    img="A Buddha image in a Thai wat (temple)",
    lead="<b>Theravada</b> ('Teaching of the Elders') is the school of " + L("Buddhism") + " dominant in Sri Lanka and Southeast Asia (Thailand, Myanmar, Cambodia, Laos), claiming descent from the earliest Buddhist community and preserving its canon in Pali — the Tipitaka, closed in written form in Sri Lanka in the 1st century BC. Its ideal is the arhat who, following the Buddha's path of ethics, meditation and wisdom through the Visuddhimagga's classic manual, attains " + L("Nirvana") + " and ends rebirth.",
    sections=[("Practice and modernity", "<p>Theravada societies ordain most young men temporarily as monks; the forest tradition (Ajahn Chah, Ajahn Mun) revived austere meditation, while the vipassana movement (Mahasi Sayadaw, S. N. Goenka) carried insight meditation worldwide and into secular mindfulness. Its conservative self-image contrasts with Mahayana's bodhisattva ideal, though mutual influence is old and growing.</p>")],
    seealso=["Buddhism", "Gautama_Buddha", "Mahayana", "Nirvana"],
    outgoing=["Buddhism", "Gautama_Buddha", "Nirvana", "Religion", "Zen"],
    unsure=[])

add(slug="Mahayana", title="Mahayana",
    infobox=[("Type", "Major branch of Buddhism ('Great Vehicle')"), ("Regions", "China, Japan, Korea, Vietnam, Tibet (Vajrayana often counted within or beside it)"), ("Key texts", "Prajnaparamita sutras; Lotus Sutra; Heart Sutra"), ("Ideal", "The bodhisattva who liberates all beings")],
    img="A statue of Avalokiteshvara (Guanyin), bodhisattva of compassion, with serene expression",
    lead="<b>Mahayana</b> ('Great Vehicle') is one of the two main branches of " + L("Buddhism") + ", arising in India around the 1st century BC–1st century AD and spreading along the Silk Road to become dominant in East and Central Asia. Its hallmarks are the bodhisattva ideal — postponing one's own final nirvana to liberate all beings — the philosophy of emptiness (<i>sunyata</i>) in Nagarjuna's Madhyamaka, and devotion to celestial buddhas and bodhisattvas such as Avalokiteshvara (Guanyin/Kannon), the embodiment of compassion.",
    sections=[("Schools", "<p>Mahayana flowered into Pure Land devotion (rebirth in Amitabha's paradise), Chan/" + L("Zen") + " meditation, Tiantai and Huayan systematics in China, and — interwoven with tantric practice — Tibetan " + L("Tibetan_Buddhism") + ". Its sutras present themselves as the Buddha's deeper teaching, a claim Theravada does not accept for its Pali canon; modern scholarship treats both canons as layered historical products.</p>")],
    seealso=["Buddhism", "Theravada", "Tibetan_Buddhism", "Zen", "Nirvana"],
    outgoing=["Buddhism", "Theravada", "Tibetan_Buddhism", "Zen", "Nirvana", "Gautama_Buddha"],
    unsure=[])

add(slug="Tibetan_Buddhism", title="Tibetan Buddhism",
    infobox=[("Type", "Vajrayana Buddhism"), ("Regions", "Tibet, Bhutan, Himalayas, Mongolia"), ("Major schools", "Nyingma, Kagyu, Sakya, Gelug"), ("Spiritual leader (Gelug)", "The Dalai Lama"), ("Key practices", "Tantra, guru yoga, debate, sand mandalas")],
    img="Prayer flags at a Himalayan pass",
    lead="<b>Tibetan Buddhism</b> is the form of Buddhism practised in Tibet, Bhutan, the Himalayas and Mongolia, a Vajrayana tradition combining Indian Mahayana philosophy, tantric ritual and meditation, and Tibet's indigenous Bon influences. Introduced from the 7th century and established by gurus such as Padmasambhava, it produced four major schools — Nyingma, Kagyu, Sakya and Gelug — the last headed by the Dalai Lamas, who governed Tibet until 1959.",
    sections=[("In exile and the world", "<p>After the failed 1959 uprising against Chinese rule, the 14th " + L("Dalai_Lama") + " and some 80,000 Tibetans fled to India, re-establishing monasteries at Dharamsala and in Karnataka. Tibetan Buddhism then spread globally (Chögyam Trungpa, the FPMT network), while inside Tibet it endures under tight state control. Its arts — thangka painting, sand mandalas dissolved to teach impermanence, masked cham dances — are world-famous.</p>")],
    seealso=["Buddhism", "Dalai_Lama", "Mahayana", "Zen"],
    outgoing=["Buddhism", "Dalai_Lama", "Mahayana", "Religion"],
    unsure=["Refugee figures (c. 80,000 initially; more since) approximate"])

add(slug="Sunni_Islam", title="Sunni Islam",
    infobox=[("Type", "Largest branch of Islam (c. 87–90% of Muslims)"), ("Name from", "Sunnah — the practice of the Prophet Muhammad"), ("Law schools", "Hanafi, Maliki, Shafi'i, Hanbali"), ("Theology schools", "Ash'ari, Maturidi, Athari")],
    img="Muslims at prayer in rows inside a large mosque",
    lead="<b>Sunni Islam</b> is the largest branch of " + L("Islam") + ", followed by roughly nine in ten of the world's Muslims. Sunnis hold that the Muslim community rightly chose Abu Bakr as the Prophet Muhammad's successor (caliph) by consensus, and they ground law and doctrine in the Quran and the Prophet's sunnah as preserved in hadith collections. Four legal schools (Hanafi, Maliki, Shafi'i, Hanbali) coexist as equally valid interpretations.",
    sections=[("Diversity", "<p>'Sunni' covers enormous diversity — from Sufi orders to scripturalist Salafi movements — united by the six articles of faith and, traditionally, deference to scholarly consensus and the caliphate's historical legitimacy. The Sunni–Shia split began as a succession dispute in 632 and hardened over centuries of theology and politics, though on most daily practice the branches closely resemble each other.</p>")],
    seealso=["Islam", "Shia_Islam", "Sufism", "Quran"],
    outgoing=["Islam", "Shia_Islam", "Sufism", "Quran", "Muhammad"],
    unsure=["Percentage range 87–90% is the standard estimate"])

add(slug="Shia_Islam", title="Shia Islam",
    infobox=[("Type", "Second-largest branch of Islam (c. 10–13% of Muslims)"), ("Core belief", "Leadership (Imamate) belongs to Ali and the Prophet's household (Ahl al-Bayt)"), ("Largest group", "Twelver Shia (Iran, Iraq, Azerbaijan, Bahrain, Lebanon)")],
    img="Shia pilgrims gathered at the Imam Husayn shrine in Karbala during Arbaeen",
    lead="<b>Shia Islam</b> is the second-largest branch of " + L("Islam") + ", distinguished by the belief that leadership of the community after Muhammad belonged by divine designation to his cousin and son-in-law Ali and to Imams descended from him. The martyrdom of Ali's son Husayn at Karbala in 680 — commemorated each year at Ashura with mourning processions — forged Shia identity around righteous suffering and resistance to tyranny.",
    sections=[("Branches and today", "<p>The largest group, Twelvers, await the return of the twelfth Imam, the Mahdi, in occultation since 874; Ismailis follow a living Imam (the Aga Khan); Zaydis survive mainly in Yemen. Twelver clerical hierarchy (marja' al-taqlid) and Iran's post-1979 doctrine of guardianship of the jurist (<i>velayat-e faqih</i>) give Shia Islam distinctive political forms; centres of learning at Najaf and Qom anchor its scholarship.</p>")],
    seealso=["Islam", "Sunni_Islam", "Sufism", "Quran"],
    outgoing=["Islam", "Sunni_Islam", "Quran", "Muhammad", "Religion"],
    unsure=["Percentage estimates vary (10–13% commonly cited)"])

add(slug="Roman_Catholic_Church", title="Catholic Church",
    infobox=[("Type", "Largest Christian church"), ("Adherents", "c. 1.4 billion baptised"), ("Head", "The Pope (Bishop of Rome); headquarters Vatican City"), ("Structure", "Latin Church + 23 Eastern Catholic Churches in communion")],
    img="St Peter's Basilica and Square in Vatican City filled with pilgrims",
    lead="The <b>Catholic Church</b> is the largest Christian church, with about 1.4 billion baptised members, in full communion with the Pope, the Bishop of Rome, whom Catholics hold to be the successor of Saint Peter. Centred on the Eucharist and seven sacraments, governed by canon law and a global hierarchy of bishops, religious orders and parishes, it is history's oldest continuously operating international institution — and the tradition of " + L("Thomas_Aquinas") + ", " + L("Augustine_of_Hippo") + " and the medieval universities.",
    sections=[("History in brief", "<p>Emerging from the early church, Catholicism split with Orthodoxy in 1054 and with Protestantism in the 16th century, answered by the Counter-Reformation (Council of Trent) and global missions; the Second Vatican Council (1962–65) under John XXIII and Paul VI modernised liturgy and relations with other faiths. Contemporary challenges include clergy sexual-abuse scandals, secularisation in Europe, and explosive growth in Africa and Asia shifting the church's centre of gravity southward.</p>")],
    seealso=["Christianity", "Vatican_City", "Thomas_Aquinas", "Protestant_Reformation"],
    outgoing=["Christianity", "Vatican_City", "Thomas_Aquinas", "Augustine_of_Hippo", "Protestant_Reformation", "Religion"],
    unsure=["Membership figures are church-reported baptised counts (c. 1.38–1.4 billion)"])

add(slug="Calvinism", title="Calvinism",
    infobox=[("Type", "Reformed Protestant tradition"), ("Founder figure", "John Calvin (1509–1564)"), ("Key doctrines", "Sovereignty of God; predestination; the five points (TULIP, summarised 1618–19)"), ("Churches", "Reformed, Presbyterian, many Congregational and Baptist bodies")],
    img="A plain whitewashed Reformed church interior in Geneva, stripped of images",
    lead="<b>Calvinism</b> (Reformed theology) is the Protestant tradition flowing from John Calvin's Geneva, systematised in his <i>Institutes of the Christian Religion</i> (final edition 1559). It stresses God's absolute sovereignty, scripture's authority, and — in its later five-point summary (TULIP) — total depravity, unconditional election, limited atonement, irresistible grace and perseverance of the saints: salvation wholly by grace, predestined, yet lived in disciplined worldly vocation.",
    sections=[("Influence", "<p>Reformed churches spread to France (Huguenots), the Netherlands, Scotland (Presbyterianism under Knox), and Puritan New England; Weber famously linked its inner-worldly asceticism to capitalism's spirit — a thesis debated ever since. Modern neo-Calvinism (Kuyper) and the global Reformed resurgence keep it a major theological current.</p>")],
    seealso=["Protestant_Reformation", "Martin_Luther", "Christianity", "John_Calvin"],
    outgoing=["Protestant_Reformation", "Martin_Luther", "Christianity", "Religion"],
    unsure=[])

add(slug="John_Calvin", title="John Calvin",
    infobox=[("Born", "10 July 1509, Noyon, France"), ("Died", "27 May 1564, Geneva"), ("Notable work", "Institutes of the Christian Religion (1536; enlarged to 1559)"), ("Known for", "Leading the Reformation in Geneva; Reformed theology")],
    img="A portrait of John Calvin with a long face and dark scholar's cap",
    lead="<b>John Calvin</b> (1509–1564) was a French theologian, pastor and ecclesiastical statesman, the principal figure of the Reformed branch of the Protestant " + L("Protestant_Reformation", "Reformation") + ". His <i>Institutes of the Christian Religion</i>, published at 26 and expanded across his life, is Protestantism's most systematic theology. Called to Geneva, he made the city a disciplined 'Protestant Rome' — academy, consistory, refugee hub — whose model and martyrs spread Reformed faith across Europe.",
    sections=[("Controversies", "<p>Calvin's Geneva banished and, in the famous 1553 case of Michael Servetus (burned for heresy with Calvin's approval of the sentence though not the method), executed dissenters — facts his critics weaponise and his defenders contextualise. His doctrines of predestination and church discipline shaped Puritanism and modern Presbyterian and Reformed churches.</p>")],
    seealso=["Calvinism", "Protestant_Reformation", "Martin_Luther", "Christianity"],
    outgoing=["Calvinism", "Protestant_Reformation", "Martin_Luther", "Christianity"],
    unsure=[])

add(slug="Rastafari", title="Rastafari",
    infobox=[("Type", "Religious and social movement"), ("Origin", "Jamaica, 1930s"), ("Central figure", "Haile Selassie I of Ethiopia, regarded as God incarnate"), ("Practices", "Ital diet, dreadlocks, ganja as sacrament (contested), reggae")],
    img="A Rastafari elder with long dreadlocks in the colours of Ethiopia, green gold and red",
    lead="<b>Rastafari</b> is a religious and social movement that developed in Jamaica in the 1930s, after the coronation of Haile Selassie I as emperor of Ethiopia — whom followers regard as God (Jah) incarnate, the returned messiah foretold in prophecy. Born among poor Afro-Jamaicans under colonial rule, it proclaims Africa (Zion) as the true home, denounces the Western world-system as Babylon, and sanctifies dreadlocks, ital (natural) food, and — in many mansions (denominations) — cannabis as a sacrament.",
    sections=[("Spread and legacy", "<p>Reggae, above all Bob Marley, carried Rastafari worldwide in the 1970s; its language (I-and-I), colours and dreadlocked iconography became global culture. There is no central authority: mansions (Nyahbinghi, Bobo Ashanti, Twelve Tribes) differ in doctrine, and Haile Selassie's own Ethiopian Orthodox faith denied his divinity — a tension believers resolve variously. Ethiopia's Shashamane land grant hosts a small repatriated community.</p>")],
    seealso=["Religion", "Jamaica", "Ethiopia", "Christianity"],
    outgoing=["Religion", "Christianity", "Bible"],
    unsure=["Follower counts (c. 600,000–1 million globally) are rough"])

add(slug="Wicca", title="Wicca",
    infobox=[("Type", "Modern Pagan / neopagan religion"), ("Popularised by", "Gerald Gardner (from 1954)"), ("Deities", "The Goddess and the Horned God (forms vary)"), ("Ethic", "The Wiccan Rede: 'An it harm none, do what ye will'")],
    img="A Wiccan altar with candles, a chalice, an athame knife and a pentacle under moonlight",
    lead="<b>Wicca</b> is a modern Pagan religion developed in England in the mid-20th century and publicly introduced by Gerald Gardner, who claimed it preserved an ancient witch-cult — a genealogy scholars now treat as creative synthesis of folklore, ceremonial magic and nature religion. Wiccans typically honour a Goddess and a Horned God, celebrate eight seasonal festivals (the Wheel of the Year: solstices, equinoxes, and cross-quarter days such as Samhain and Beltane), and practise ritual magic in covens or solitary form under the ethic of the Rede.",
    sections=[("Diversity", "<p>Traditions range from Gardnerian and Alexandrian initiatory lines to eclectic, solitary and feminist (Dianic) currents; Wicca seeded the broader neopagan movement and much of modern occult publishing. Legal recognition (notably in the US) and census counts show steady growth, though self-identification ranges widely (from hundreds of thousands to millions).</p>")],
    seealso=["Religion", "Mythology", "Folklore"],
    outgoing=["Religion", "Mythology", "Folklore"],
    unsure=["Adherent estimates vary enormously; Gardner's ancient-survival claim is not accepted by historians"])

add(slug="Scientology", title="Scientology",
    infobox=[("Type", "New religious movement"), ("Founder", "L. Ron Hubbard (1911–1986)"), ("Founded", "1953–54 (Church of Scientology, US)"), ("Key text", "Dianetics (1950)"), ("Practices/beliefs", "Auditing with the E-meter; thetans; Xenu narrative in confidential OT materials")],
    img="The Scientology cross symbol displayed on a church building",
    lead="<b>Scientology</b> is a set of beliefs and practices created by American author L. Ron Hubbard, launched as the self-help system Dianetics (1950) and reorganised as a church in the 1950s. Scientologists hold that humans are immortal spiritual beings (thetans) whose traumatic memories (engrams) can be cleared through counselling called auditing, progressing up a 'Bridge to Total Freedom'; advanced confidential materials describe a cosmic narrative involving a galactic ruler named Xenu — material the church neither confirms nor denies to outsiders and members may not discuss.",
    sections=[("Controversy", "<p>The movement's celebrity members (Tom Cruise, John Travolta) and aggressive litigation brought fame; its tax status varies (religion in the US, contested elsewhere — banned or monitored at times in Russia and Germany), and defectors' accounts of disconnection and the Sea Org's discipline draw persistent criticism the church rebuts as religious bigotry. Membership figures are sharply disputed (church claims in millions; scholars suggest tens of thousands of active members).</p>")],
    seealso=["Religion", "New_religious_movement"],
    outgoing=["Religion"],
    unsure=["Membership and details of confidential doctrines are contested between the church and critics; presented neutrally from memory"])

add(slug="Eudaimonia", title="Eudaimonia",
    infobox=[("Field", "Ancient Greek ethics"), ("Translation", "'Flourishing', 'well-being', literally 'good spirit'"), ("Key thinkers", "Aristotle (Nicomachean Ethics); the Stoics; Epicurus")],
    img="A Greek laurel wreath and olive branch on a marble plinth",
    lead="<b>Eudaimonia</b> is the ancient Greek concept — usually translated 'flourishing' or 'well-being' — of living and doing well, the highest human good in classical ethics. In " + L("Aristotle") + "'s <i>Nicomachean Ethics</i> it is activity of the soul in accordance with virtue over a complete life: not a feeling but an achievement, combining excellent reasoning, character virtues learned by habit, friendship and enough external goods not to be crushed by fortune.",
    sections=[("Schools and revival", "<p>Stoics radicalised eudaimonia into virtue alone sufficing even on the rack; Epicurus identified it with untroubled pleasure. Modern virtue ethics and positive psychology (flourishing measures, PERMA) consciously revive the concept, distinguishing it from hedonic happiness as mere pleasant feeling.</p>")],
    seealso=["Aristotle", "Ethics", "Stoicism", "Epicurus"],
    outgoing=["Aristotle", "Ethics", "Stoicism", "Epicurus", "Philosophy"],
    unsure=[])

add(slug="Logos", title="Logos",
    infobox=[("Field", "Greek philosophy and theology"), ("Meanings", "Word, reason, account, principle, discourse"), ("Key users", "Heraclitus; the Stoics; Philo; the Gospel of John")],
    img="The Greek word ΛΟΓΟΣ carved in stone in classical lettering",
    lead="<b>Logos</b> (Greek: 'word, reason, account') is one of the most fertile concepts in Western thought. Heraclitus made it the rational order of the cosmos that most men fail to grasp; the Stoics identified it with the divine reason pervading nature (the <i>logos spermatikos</i>, seminal reason in each person); Philo of Alexandria mediated it toward Judaism; and the Gospel of John opens by identifying the Logos — 'In the beginning was the Word' — with God and then with Christ, a fusion that structured Christian theology.",
    sections=[("Afterlife", "<p>Derivatives mark whole disciplines (-logy), logic itself, and modern notions of argument and discourse; philosophers from Hegel to Derrida keep re-reading the term, and 'logocentrism' names the alleged Western privileging of speech and reason.</p>")],
    seealso=["Stoicism", "Philosophy", "Theology", "Bible"],
    outgoing=["Stoicism", "Philosophy", "Theology", "Bible", "John_Locke"],
    unsure=[])

print("w5 loaded", len(PAGES))

# ---------------- BUILD ----------------
def url_of(slug):
    return "https://en.wikipedia.org/wiki/" + slug

built, skipped, all_outgoing = [], [], {}
records = []
for p in PAGES:
    path = os.path.join(WIKI, p["slug"], "index.html")
    local = "web/en.wikipedia.org/wiki/%s/index.html" % p["slug"]
    url = url_of(p["slug"])
    for s in p.get("outgoing", []):
        all_outgoing.setdefault(url_of(s), url)
    if os.path.exists(path):
        records.append({"url": url, "local_path": local, "source_url": "https://en.wikipedia.org/wiki/Philosophy",
                        "depth": 8, "status": "skipped-duplicate", "crawler": "AD", "built_at": None,
                        "unsure": ["Page already existed on disk when wave 5 ran"], "outgoing": [url_of(s) for s in p.get("outgoing", [])]})
        skipped.append(url)
        continue
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page_html(p))
    records.append({"url": url, "local_path": local, "source_url": "https://en.wikipedia.org/wiki/Philosophy",
                    "depth": 8, "status": "built", "crawler": "AD", "built_at": NOW,
                    "unsure": p.get("unsure", []), "outgoing": [url_of(s) for s in p.get("outgoing", [])]})
    built.append(url)

built_set = set(built)
existing_records = set()
if os.path.exists(LEDGER):
    for line in open(LEDGER, encoding="utf-8"):
        try:
            r = json.loads(line)
            existing_records.add((r.get("url"), r.get("status")))
        except Exception:
            pass
for target, source in sorted(all_outgoing.items()):
    if target in built_set:
        continue
    slug = target.split("/wiki/")[-1]
    path = os.path.join(WIKI, urllib.parse.unquote(slug), "index.html")
    if os.path.exists(path):
        continue
    if (target, "queued") in existing_records:
        continue
    records.append({"url": target, "local_path": "web/en.wikipedia.org/wiki/%s/index.html" % slug,
                    "source_url": source, "depth": 9, "status": "queued", "crawler": "AD", "built_at": None,
                    "unsure": [], "outgoing": []})

with open(LEDGER, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("BUILT:", len(built))
for u in built: print("  ", u)
print("SKIPPED-DUP:", len(skipped), skipped)
print("QUEUED new records:", sum(1 for r in records if r["status"] == "queued"))
