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

add(slug="Absurdism", title="Absurdism",
    infobox=[("Field", "Philosophy"), ("Key figure", "Albert Camus"), ("Core concept", "The Absurd: the conflict between the human search for meaning and the silent universe")],
    img="Sisyphus pushing his boulder up a mountain, from a stark modern illustration",
    lead="<b>Absurdism</b> is the philosophical view that the universe is irrational and meaningless and that the human search for meaning therefore collides with indifference — a conflict " + L("Albert_Camus") + " called <b>the Absurd</b>. In <i>The Myth of Sisyphus</i> (1942) Camus rejected suicide and religious 'leaps' alike, urging revolt: to live lucidly without appeal, like Sisyphus, whom 'one must imagine happy'. Absurdism shares ancestors (Kierkegaard, Nietzsche) with existentialism but diverges in refusing any escape from the absurd condition.",
    sections=[("In culture", "<p>The Theatre of the Absurd (Beckett, Ionesco) dramatised the condition, and 'absurd' entered ordinary language for the felt meaninglessness of bureaucratic modern life — Camus's own essay 'The Absurd Man' took Don Juan, the actor and the conqueror as its exemplars of quantity over hope.</p>")],
    seealso=["Albert_Camus", "Existentialism", "Nihilism", "Søren_Kierkegaard"],
    outgoing=["Albert_Camus", "Existentialism", "Nihilism", "Søren_Kierkegaard", "Philosophy"],
    unsure=[])

add(slug="Ahimsa", title="Ahimsa",
    infobox=[("Traditions", "Hinduism, Jainism, Buddhism"), ("Meaning", "Non-violence; reverence for all life"), ("Key exponents", "Mahavira; Mahatma Gandhi")],
    img="A Jain monk gently sweeping the ground before his steps so as not to harm small creatures",
    lead="<b>Ahimsa</b> (Sanskrit: 'non-harm') is the ethical principle of not causing harm to any living being, central to " + L("Jainism") + " — where it is the supreme vow, observed even toward insects — and foundational in " + L("Hinduism") + " and " + L("Buddhism") + ". The <i>Chandogya Upanishad</i> lists it among the virtues; Patanjali's Yoga makes it the first of the restraints (yamas).",
    sections=[("Gandhi and after", "<p>Mahatma Gandhi — who learned ahimsa deeply from Jain influence in Gujarat, notably Raychandbhai — made it the active force of <i>satyagraha</i>, nonviolent resistance that helped end British rule in India and inspired Martin Luther King Jr. and later movements. Jain practice remains its strictest laboratory: filtered water, no eating after dark, and vocations screened for harm.</p>")],
    seealso=["Jainism", "Mahavira", "Hinduism", "Karma"],
    outgoing=["Jainism", "Mahavira", "Hinduism", "Buddhism", "Karma"],
    unsure=[])

add(slug="Dharma", title="Dharma",
    infobox=[("Traditions", "Hinduism, Buddhism, Jainism, Sikhism"), ("Meanings", "Duty, law, cosmic order (Hindu); the Buddha's teaching (Buddhist); phenomena (Abhidharma)")],
    img="A carved dharmachakra (wheel of dharma) with eight spokes on a temple pillar",
    lead="<b>Dharma</b> (Sanskrit; Pali: <i>dhamma</i>) is a key concept of Indian religions with no single English equivalent. In " + L("Hinduism") + " it is the cosmic law and the duty, righteousness and proper conduct that uphold it — varying by caste, stage of life and circumstance, and exemplified in the epics by figures torn between conflicting dharmas. In " + L("Buddhism") + ", 'the Dharma' is the Buddha's teaching itself, one of the Three Jewels of refuge, and <i>dharmas</i> in Abhidharma philosophy are the irreducible constituents of experience.",
    sections=[("Range", "<p>Jain and Sikh uses extend the range (dharma as the medium of motion in Jain cosmology; righteous duty in Sikh ethics). The wheel of dharma (dharmachakra) symbolises the teaching's turning and stands at the centre of India's national flag, adopted from Ashoka's pillars — a reminder that dharma once named a political ideal too.</p>")],
    seealso=["Hinduism", "Buddhism", "Karma", "Gautama_Buddha"],
    outgoing=["Hinduism", "Buddhism", "Jainism", "Sikhism", "Karma", "Gautama_Buddha"],
    unsure=[])

add(slug="Samsara", title="Samsara",
    infobox=[("Traditions", "Hinduism, Buddhism, Jainism, Sikhism"), ("Meaning", "The cycle of birth, death and rebirth"), ("Escape", "Moksha (Hindu/Jain/Sikh), Nirvana (Buddhist)")],
    img="A Tibetan thangka painting of the bhavacakra, the wheel of life held by Yama, lord of death",
    lead="<b>Samsara</b> is the cycle of birth, death and rebirth to which beings are bound in the Indian religions, driven by " + L("Karma") + " and ignorance, and characterised by suffering. In Buddhism the wheel of life (<i>bhavacakra</i>) depicts six realms of rebirth — gods, demigods, humans, animals, hungry ghosts and hells — with the human realm prized as the one from which awakening is possible. Liberation from samsara is the goal: " + L("Moksha") + " for Hindus, Jains and Sikhs; " + L("Nirvana") + " for Buddhists.",
    sections=[("Origins", "<p>The doctrine appears in the early Upanishads, fused with karma doctrine, and was shared — competitively reworked — by the sramana movements of the 6th–5th centuries BC, including Buddhism and Jainism, distinguishing Indic religions from the linear eschatologies of the Abrahamic traditions.</p>")],
    seealso=["Karma", "Reincarnation", "Moksha", "Nirvana", "Dharma"],
    outgoing=["Karma", "Reincarnation", "Moksha", "Nirvana", "Dharma", "Buddhism", "Hinduism"],
    unsure=[])

add(slug="Gautama_Buddha", title="Gautama Buddha",
    infobox=[("Born", "Siddhartha Gautama, c. 563 or 480 BC, Lumbini"), ("Died", "c. 483 or 400 BC, Kushinagar"), ("Known for", "Founder of Buddhism; the Buddha ('Awakened One')"), ("Key events", "Great Renunciation; Enlightenment at Bodh Gaya; first sermon at Sarnath")],
    img="A serene seated statue of the Buddha in meditation",
    lead="The <b>Buddha</b> (Sanskrit: 'Awakened One'), born <b>Siddhartha Gautama</b>, was a sramana teacher of the 6th or 5th century BC whose teachings founded " + L("Buddhism") + ". Renouncing a sheltered princely life after encountering old age, sickness, death and an ascetic, he sought liberation first through extreme austerity, then through the 'middle way', attaining enlightenment meditating under the Bodhi tree. For 45 years he taught the Four Noble Truths and the Eightfold Path across the Ganges plain, founding an order (sangha) that carried his Dharma across Asia.",
    sections=[("Life and teaching", "<p>Traditional biographies — embellished over centuries — tell of a miraculous birth at Lumbini, the great renunciation at 29, enlightenment at Bodh Gaya, the first sermon ('setting in motion the wheel of Dharma') at Sarnath, and death (parinirvana) at Kushinagar after eating a final meal. His core teaching analyses suffering (<i>dukkha</i>) as arising from craving and ignorance, diagnosed through dependent origination, and treatable by the path of ethics, meditation and wisdom; his doctrine of <i>anatta</i> (no permanent self) distinguishes Buddhism sharply from other Indian paths. Dates are debated — scholarly consensus places him around 480–400 BC.</p>")],
    seealso=["Buddhism", "Dharma", "Karma", "Nirvana", "Mahavira"],
    outgoing=["Buddhism", "Dharma", "Karma", "Nirvana", "Mahavira", "Religion"],
    unsure=["Birth/death dates are among the most debated in ancient history; both candidate ranges given"])

add(slug="Dogen", title="Dōgen",
    infobox=[("Born", "26 January 1200, Kyoto, Japan"), ("Died", "22 September 1253"), ("School", "Soto Zen (founder in Japan)"), ("Notable work", "Shōbōgenzō ('Treasury of the True Dharma Eye')")],
    img="A portrait scroll of Dogen in monk's robes seated in meditation",
    lead="<b>Dōgen Zenji</b> (1200–1253) was a Japanese Zen Buddhist monk, writer and philosopher who founded the Soto school of " + L("Zen") + " in Japan. After study in China under Rujing, he taught that practice and enlightenment are one: seated meditation (<i>zazen</i>) in the posture of 'just sitting' (<i>shikantaza</i>) is not a means to awakening but awakening itself enacted. His masterwork, the <i>Shōbōgenzō</i>, is among the most profound philosophical texts in Japanese, exploring being-time (<i>uji</i>), Buddha-nature and language.",
    sections=[("Legacy", "<p>Dogen founded Eihei-ji, still a head temple of Soto Zen. Long a sectarian treasure, his writings were rediscovered in the 20th century and now anchor Japanese philosophy's modern canon and global Zen practice alike.</p>")],
    seealso=["Zen", "Buddhism", "Japan"],
    outgoing=["Zen", "Buddhism", "Religion", "Japan"],
    unsure=[])

add(slug="Chinese_philosophy", title="Chinese philosophy",
    infobox=[("Eras", "Hundred Schools of Thought (Spring & Autumn / Warring States); Han synthesis; Neo-Confucianism; modern"), ("Major schools", "Confucianism, Taoism, Legalism, Mohism, Buddhism (sinicised)")],
    img="A Chinese scroll painting of scholars debating beneath pine trees",
    lead="<b>Chinese philosophy</b> is the philosophical tradition of China, arising in the Spring and Autumn period with " + L("Confucius") + " and flourishing in the Warring States 'Hundred Schools of Thought' — Confucians, Taoists (" + L("Laozi") + ", " + L("Zhuangzi") + "), Mohists, Legalists, logicians and yin-yang cosmologists competing for the ear of rulers. Its characteristic concerns are ethical and political: how to order the state, cultivate the person and harmonise human life with the cosmic way (<i>dao</i>).",
    sections=[("Development", "<p>Under the Han dynasty Confucianism became orthodoxy; Buddhism's arrival (1st century AD onward) transformed all schools and provoked Neo-Confucianism's metaphysical synthesis (Zhu Xi, Wang Yangming). The 20th century brought Marxism, liberalism and a 'New Confucian' revival; contemporary Chinese philosophy debates tradition's place in a modernising superpower.</p>")],
    seealso=["Confucianism", "Taoism", "Confucius", "Buddhism", "Zen"],
    outgoing=["Confucianism", "Taoism", "Confucius", "Laozi", "Zhuangzi", "Buddhism", "Zen", "Philosophy"],
    unsure=[])

add(slug="Avesta", title="Avesta",
    infobox=[("Religion", "Zoroastrianism"), ("Language", "Avestan"), ("Contents", "Yasna (incl. the Gathas), Yashts, Vendidad, Khordeh Avesta"), ("Transmission", "Oral for centuries; written codification in Sasanian era")],
    img="An illuminated manuscript page of Avestan script",
    lead="The <b>Avesta</b> is the primary collection of sacred texts of " + L("Zoroastrianism") + ", composed in the Avestan language and transmitted orally for many centuries before being written down, in a specially devised alphabet, in the Sasanian period. Its oldest portion is the <i>Yasna</i>, whose seventeen hymns — the Gathas — are attributed to the prophet " + L("Zoroaster") + " himself and are among the oldest surviving Indo-Iranian religious poetry.",
    sections=[("Losses and contents", "<p>Sasanian tradition held that 21 books (<i>nasks</i>) existed; after the Arab conquest and centuries of attrition roughly a quarter survives: liturgy (Yasna, Visperad), hymns to divinities (Yashts), purity law and cosmology (Vendidad), and the prayer book (Khordeh Avesta). The Avesta's language, closely related to the Rigveda's Sanskrit, is a cornerstone of Indo-European studies.</p>")],
    seealso=["Zoroastrianism", "Zoroaster", "Ahura_Mazda"],
    outgoing=["Zoroastrianism", "Zoroaster", "Ahura_Mazda", "Religion"],
    unsure=["Surviving fraction (roughly a quarter) is a commonly cited estimate"])

add(slug="Baháʼu'lláh", title="Baháʼu'lláh",
    infobox=[("Born", "12 November 1817, Tehran, Persia"), ("Died", "29 May 1892, Acre, Ottoman Palestine"), ("Known for", "Founder of the Baháʼí Faith"), ("Major works", "Kitáb-i-Aqdas (Book of Laws); Kitáb-i-Íqán; The Hidden Words")],
    img="A photograph of Baháʼu'lláh in old age with a long white beard",
    lead="<b>Baháʼu'lláh</b> (1817–1892), born Mírzá Ḥusayn-ʻAlí Núrí, was the founder of the " + L("Baháʼí_Faith") + ". A Persian nobleman who became a follower of the Báb, he was imprisoned in Tehran's 'Black Pit', exiled successively to Baghdad, Constantinople, Adrianople and finally the prison-city of Acre, where he died. In Baghdad in 1863 he declared himself the Messenger foretold by the Báb; his writings — laws, mystical works, and letters to kings and popes — form the core of Baháʼí scripture.",
    sections=[("Teachings", "<p>Baháʼu'lláh taught the oneness of God, of religion (progressive revelation) and of humanity, prescribing the abolition of prejudice, equality of women and men, universal education, a world commonwealth and the harmony of science and religion. His shrine at Bahji, near Acre, is the point toward which Baháʼís turn in prayer; photographs of him are treated with great reverence and displayed only in specific settings — a sensitivity the faith's websites observe and visitors to Haifa encounter.</p>")],
    seealso=["Baháʼí_Faith", "Religion", "Iran"],
    outgoing=["Baháʼí_Faith", "Religion", "Iran"],
    unsure=[])

add(slug="Dome_of_the_Rock", title="Dome of the Rock",
    infobox=[("Location", "Temple Mount, Jerusalem"), ("Built", "691–692 AD, under Umayyad caliph Abd al-Malik"), ("Type", "Islamic shrine (not a mosque)"), ("Significance", "Oldest surviving monument of Islamic architecture; site of Muhammad's ascension (Mi'raj) in tradition")],
    img="The Dome of the Rock with its golden dome above the Temple Mount plaza",
    lead="The <b>Dome of the Rock</b> is an Islamic shrine on the " + L("Temple_Mount") + " in Jerusalem, built by the Umayyad caliph Abd al-Malik in 691–692 AD — the oldest surviving monument of Islamic architecture. Its golden dome and blue-tiled octagon shelter the Foundation Stone, from which Muslims believe Muhammad ascended to heaven on the Night Journey, and which Jewish tradition identifies with the Holy of Holies and the binding of Isaac.",
    sections=[("Architecture and history", "<p>The building's geometry, mosaics and Quranic inscriptions (among the earliest anywhere) have been admired and imitated for thirteen centuries; the exterior tiles are Ottoman (Suleiman the Magnificent), and the dome's gilding was renewed in the 20th century with Jordanian funding. It is administered with the Mount by the Waqf and remains the visual emblem of Jerusalem — and a sensitive symbol in the conflict over the city.</p>")],
    seealso=["Temple_Mount", "Al-Aqsa_Mosque", "Jerusalem", "Islam"],
    outgoing=["Temple_Mount", "Al-Aqsa_Mosque", "Jerusalem", "Islam", "Western_Wall"],
    unsure=[])

add(slug="Al-Aqsa_Mosque", title="Al-Aqsa Mosque",
    infobox=[("Location", "Southern Temple Mount (al-Haram al-Sharif), Jerusalem"), ("Religion", "Islam"), ("Significance", "Third holiest site in Islam; destination of Muhammad's Night Journey"), ("Current structure", "Repeatedly rebuilt; present form largely Ayyubid/Mamluk-era fabric over earlier foundations")],
    img="Al-Aqsa Mosque with its silver-grey dome and arched facade on the Temple Mount",
    lead="<b>Al-Aqsa Mosque</b> (al-Masjid al-Aqsa, 'the Farthest Mosque') is the congregational mosque on the southern side of the " + L("Temple_Mount") + " in Jerusalem, Islam's third-holiest site after Mecca and Medina. The Quran's account of Muhammad's Night Journey (Isra) names al-Masjid al-Aqsa as its destination; tradition adds his leading of the prophets in prayer there and ascension (Mi'raj) from the Rock beneath the neighbouring " + L("Dome_of_the_Rock") + ".",
    sections=[("History", "<p>A first prayer house rose soon after the Muslim conquest (630s–690s); the building was repeatedly felled by earthquakes and rebuilt — by Umayyads, Abbasids, Fatimids, Ayyubids and Crusaders (who made it a Templar headquarters, 'Templum Solomonis'). An arson attack by a disturbed Australian tourist in 1969 damaged its ancient minbar — an outrage that helped spur the founding of the Organisation of Islamic Cooperation. The mosque gives its name to the 2000 uprising (Second Intifada, 'al-Aqsa Intifada') and remains a flashpoint.</p>")],
    seealso=["Temple_Mount", "Dome_of_the_Rock", "Islam", "Jerusalem"],
    outgoing=["Temple_Mount", "Dome_of_the_Rock", "Islam", "Jerusalem", "Mecca"],
    unsure=["Precise dating of the earliest structures is archaeologically constrained and partly traditional"])

add(slug="Second_Temple", title="Second Temple",
    infobox=[("Location", "Temple Mount, Jerusalem"), ("Built", "c. 516 BC (dedicated); Herod's expansion from c. 20 BC"), ("Destroyed", "70 AD, by the Romans under Titus"), ("Significance", "Centre of Jewish worship; the temple of Jesus's time")],
    img="A scale model of Herod's Temple with its courts and colonnades, as displayed in Jerusalem",
    lead="The <b>Second Temple</b> was the Jewish temple in Jerusalem that stood from about 516 BC, when returning exiles from Babylon rebuilt the destroyed First (Solomonic) Temple, until Rome destroyed it in 70 AD. Massively enlarged by Herod the Great — its retaining walls, including the " + L("Western_Wall") + ", still define the " + L("Temple_Mount") + " — it was the centre of pilgrimage festivals, sacrifice and teaching in the time of Jesus, and its loss transformed Judaism from a temple cult into the rabbinic, synagogue-centred religion of the diaspora.",
    sections=[("Destruction and legacy", "<p>Titus's legions burned the Temple during the siege of Jerusalem in the First Jewish–Roman War (9th of Av, by tradition the same date as the First Temple's fall). The Arch of Titus in Rome depicts its menorah carried in triumph (the menorah now emblems the State of Israel). Judaism still mourns the destruction on Tisha B'Av, and prayers for restoration are woven through its liturgy.</p>")],
    seealso=["Western_Wall", "Temple_Mount", "Judaism", "Jerusalem"],
    outgoing=["Western_Wall", "Temple_Mount", "Judaism", "Jerusalem", "Jesus"],
    unsure=[])

add(slug="Eastern_Orthodox_Church", title="Eastern Orthodox Church",
    infobox=[("Type", "Christian communion"), ("Adherents", "c. 220 million"), ("Structure", "Autocephalous national churches in communion (Constantinople, Alexandria, Antioch, Jerusalem, Moscow, etc.)"), ("Separated from Rome", "East–West Schism, conventionally 1054")],
    img="The golden onion domes of an Orthodox cathedral against a winter sky",
    lead="The <b>Eastern Orthodox Church</b> is the second-largest Christian communion, a family of autocephalous (self-governing) churches — Greek, Russian, Serbian, Romanian, Bulgarian and others — united in faith and sacrament, with the Ecumenical Patriarch of Constantinople holding a primacy of honour. It understands itself as the church of the seven Ecumenical Councils, preserving Byzantine liturgy, iconography and monasticism, and separated from Rome in the Great Schism of 1054 over theology (the <i>filioque</i>), authority and culture.",
    sections=[("Life and theology", "<p>Orthodox theology centres on theosis — human deification by grace — and on the liturgy as heaven on earth, celebrated with icons ('windows to heaven'), incense and chant. Hesychast prayer (the Jesus Prayer) flourishes on Mount Athos, an autonomous monastic republic since Byzantine times. After communism's fall the Russian church (the largest, whose 2018 rupture with Constantinople over Ukrainian autocephaly split world Orthodoxy) regained public prominence.</p>")],
    seealso=["Christianity", "Jesus", "Church_of_the_Holy_Sepulchre", "Theology"],
    outgoing=["Christianity", "Jesus", "Church_of_the_Holy_Sepulchre", "Theology", "Religion"],
    unsure=["Adherent figure commonly cited c. 220 million"])

add(slug="Knowledge", title="Knowledge",
    infobox=[("Field", "Epistemology"), ("Classical analysis", "Justified true belief (challenged 1963)"), ("Types", "Propositional (knowledge-that); knowledge-how; knowledge by acquaintance")],
    img="An open ancient book with light falling across its pages",
    lead="<b>Knowledge</b> is a central concept of " + L("Epistemology") + ": most basically, a true relation between a subject and reality, whether as propositional knowledge (knowing <i>that</i> Paris is in France), know-how (knowing how to ride a bicycle), or acquaintance (knowing a person or a city). Plato's <i>Theaetetus</i> already canvassed the definition 'true belief with an account'; the formula 'justified true belief' reigned until Gettier's 1963 counterexamples.",
    sections=[("Contemporary work", "<p>Post-Gettier epistemology branches into externalism (knowledge as reliably produced belief), virtue epistemology, and the knowledge-first programme (Timothy Williamson) that treats knowledge as a basic mental state, unanalysable into belief plus conditions. Social epistemology studies testimony, expertise and disagreement — how nearly all of what we know we owe to others.</p>")],
    seealso=["Epistemology", "Gettier_problem", "Scepticism"],
    outgoing=["Epistemology", "Gettier_problem", "Scepticism", "Philosophy"],
    unsure=[])

add(slug="Realism_(philosophy)", title="Realism (philosophy)",
    infobox=[("Field", "Metaphysics / epistemology"), ("Thesis (general)", "Some domain exists independently of our thought or perception of it"), ("Forms", "Platonic realism (universals); scientific realism; moral realism; metaphysical realism")],
    img="A still-life painting so detailed it nearly deceives the eye, trompe-l'oeil style",
    lead="<b>Realism</b> in philosophy is a family of positions that some subject-matter exists independently of minds and their representations. In medieval debates, realism about universals meant general terms name real entities (moderately, in things — Aquinas; or before things, in Plato's Forms), opposite to " + L("Nominalism") + ". Modern forms include scientific realism (theories' unobservable posits, like electrons, really exist), moral realism (objective moral facts), and metaphysical realism about a mind-independent world.",
    sections=[("Opponents and arguments", "<p>Anti-realisms — idealism, instrumentalism, constructivism, Dummett's semantic anti-realism — press how access to a mind-independent world could be described or verified. Putnam's internal realism tried a middle path. The realism question is less a single debate than the watermark of many.</p>")],
    seealso=["Nominalism", "Ontology", "Metaphysics", "Idealism"],
    outgoing=["Nominalism", "Ontology", "Metaphysics", "Idealism", "Plato"],
    unsure=[])

add(slug="Monism", title="Monism",
    infobox=[("Field", "Metaphysics"), ("Thesis", "Reality is ultimately one (substance, kind, or whole)"), ("Key figures", "Parmenides; Spinoza; modern: Jonathan Schaffer (priority monism)"), ("Opposite", "Dualism; pluralism")],
    img="A single sphere of light containing a miniature landscape, all things in one",
    lead="<b>Monism</b> is the metaphysical view that reality is fundamentally one: one substance (Spinoza's God-or-Nature), one kind of thing (materialism or idealism), or one whole (priority monism, on which the cosmos is the single basic object and parts are derivative). Ancient monists include Parmenides, for whom being is one and unchanging, and the atomists' critics; in Indian thought Advaita Vedanta's Brahman-without-a-second is a close cousin.",
    sections=[("Forms", "<p>Substance monism (one token substance), attribute monism, and existence monism (only one object exists at all) are distinguished. Monism's appeal is unity and elegance; its burden is explaining the evident plurality and variety of the world it denies is fundamental.</p>")],
    seealso=["Baruch_Spinoza", "Dualism", "Pantheism", "Metaphysics"],
    outgoing=["Baruch_Spinoza", "Dualism", "Pantheism", "Metaphysics", "Ontology"],
    unsure=[])

add(slug="Falsifiability", title="Falsifiability",
    infobox=[("Field", "Philosophy of science"), ("Proposed by", "Karl Popper, The Logic of Scientific Discovery (1934)"), ("Criterion", "A theory is scientific if it forbids some observable states of affairs — it can be tested and potentially refuted")],
    img="A swan silhouette split half white and half black, Popper's emblem of refutation",
    lead="<b>Falsifiability</b> (refutability) is the property of a statement or theory that it can be contradicted by observation. Karl Popper made it his criterion of demarcation between science and non-science: a scientific theory must take risks — forbid outcomes — whereas, he argued, Marxist history and psychoanalysis could explain everything and so explained nothing. The sighting of one black swan falsifies 'all swans are white', which no number of white swans can verify (the " + L("Problem_of_induction") + ").",
    sections=[("Criticisms", "<p>Historians and philosophers (Kuhn, Lakatos, Feyerabend) showed scientists rarely abandon theories at a single counter-instance (the Duhem–Quine problem: tests implicate auxiliary assumptions too), so falsificationism survives more as a norm of testability than a description of practice. It remains legally and culturally influential (cited in US court rulings on creation science).</p>")],
    seealso=["Problem_of_induction", "David_Hume", "Epistemology"],
    outgoing=["Problem_of_induction", "David_Hume", "Epistemology", "Philosophy"],
    unsure=[])

add(slug="Functionalism_(philosophy_of_mind)", title="Functionalism (philosophy of mind)",
    infobox=[("Field", "Philosophy of mind"), ("Core claim", "Mental states are defined by their causal/functional roles, not their physical composition"), ("Key figures", "Hilary Putnam (early), Jerry Fodor, David Lewis")],
    img="A flowchart of inputs, internal states and outputs representing a mental process",
    lead="<b>Functionalism</b> is a theory in the philosophy of mind holding that mental states are constituted by their functional role — their relations to sensory inputs, behavioural outputs and other mental states — rather than by their internal physical makeup. Pain, on this view, is whatever state is typically caused by tissue damage and causes wincing, avoidance and the desire for relief, whether realised in neurons, silicon, or something else: mental kinds are multiply realisable, as software runs on different hardware.",
    sections=[("Influence and objections", "<p>Developed by Hilary Putnam in the 1960s under the influence of Turing machines and championed by Jerry Fodor, functionalism became the working philosophy of cognitive science and much AI research. Objections centre on qualia: inverted-spectrum and absent-qualia (Block's 'China brain') scenarios allege functional duplicates could lack experience entirely — pressing the same hard problem as " + L("Consciousness") + " itself.</p>")],
    seealso=["Philosophy_of_mind", "Consciousness", "Dualism", "Artificial_intelligence"],
    outgoing=["Philosophy_of_mind", "Consciousness", "Dualism", "Philosophy"],
    unsure=[])

print("w4 loaded", len(PAGES))

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
                        "unsure": ["Page already existed on disk when wave 4 ran"], "outgoing": [url_of(s) for s in p.get("outgoing", [])]})
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
