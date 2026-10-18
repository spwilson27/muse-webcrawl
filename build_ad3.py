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

add(slug="Beauty", title="Beauty",
    infobox=[("Field", "Aesthetics / philosophy of art"), ("Related concepts", "Sublime, taste, aesthetic judgement")],
    img="A classical marble statue of Aphrodite, the Greek ideal of beauty",
    lead="<b>Beauty</b> is a property or quality of objects, persons, places and ideas that provides pleasure to the senses or mind. Whether beauty is objective (in the object), subjective (in the eye of the beholder), or relational has been debated since antiquity: " + L("Plato") + " made Beauty itself one of the eternal Forms, medieval thinkers listed it among the transcendentals with truth and goodness, and Hume and Kant analysed it as a judgement of taste claiming universal agreement without concepts.",
    sections=[("Theories", "<p>Classical accounts tie beauty to symmetry, proportion and unity-in-variety; evolutionary psychologists to signals of health and fitness; cultural critics to power and convention. Beauty standards demonstrably vary across eras and cultures — and demonstrably converge in some respects (faces, landscapes), keeping the philosophical question alive in " + L("Aesthetics") + " and everyday life alike.</p>")],
    seealso=["Aesthetics", "Philosophy_of_art", "Sublime_(philosophy)", "Plato"],
    outgoing=["Aesthetics", "Philosophy_of_art", "Sublime_(philosophy)", "Plato", "Immanuel_Kant"],
    unsure=[])

add(slug="Philosophy_of_art", title="Philosophy of art",
    infobox=[("Field", "Aesthetics"), ("Key questions", "What is art? How is art to be interpreted and judged?"), ("Key figures", "Plato, Aristotle, Kant, Tolstoy, Danto, Dickie")],
    img="Marcel Duchamp's Fountain (1917), the readymade that redefined debates about art's nature",
    lead="The <b>philosophy of art</b> studies the nature of art, artistic creation, interpretation and evaluation. It asks what makes something a work of art at all — a question made urgent by Marcel Duchamp's readymades and conceptual art, which look like ordinary objects — and whether representation, expression or form is art's essence.",
    sections=[("Theories", "<p>Historical theories include mimesis (art as imitation), expression theory (Tolstoy: art transmits feeling), formalism (significant form), and institutional theory (George Dickie: art is what the artworld confers status on). Arthur Danto argued that indiscernible objects — Warhol's Brillo Boxes versus supermarket cartons — differ by interpretation and art-historical location. The philosophy of art is the theoretical core of " + L("Aesthetics") + ".</p>")],
    seealso=["Aesthetics", "Beauty", "Art"],
    outgoing=["Aesthetics", "Beauty", "Philosophy"],
    unsure=[])

add(slug="Sublime_(philosophy)", title="Sublime (philosophy)",
    infobox=[("Field", "Aesthetics"), ("Key figures", "Longinus; Edmund Burke (1757); Immanuel Kant (1790)")],
    img="A ship in a stormy sea beneath towering cliffs, evoking the sublime in nature",
    lead="In <b>aesthetics</b>, the <b>sublime</b> is the quality of greatness — in nature, art or ideas — that exceeds calculation and overwhelms the mind, mixing awe with terror. Edmund Burke's <i>Enquiry</i> (1757) opposed the sublime (vast, dark, powerful) to the beautiful (small, smooth, delicate); " + L("Immanuel_Kant") + " located sublimity not in objects but in the mind's discovery of its own rational vocation when imagination fails before immensity (the mathematical sublime) or might (the dynamical sublime).",
    sections=[("Legacy", "<p>The sublime shaped Romantic painting and poetry — Turner's storms, Friedrich's wanderers — and returned in 20th-century thought (Lyotard's postmodern sublime) and in discussions of technology and ecological catastrophe, where human power again confronts scales beyond comprehension.</p>")],
    seealso=["Aesthetics", "Beauty", "Immanuel_Kant"],
    outgoing=["Aesthetics", "Beauty", "Immanuel_Kant", "Philosophy"],
    unsure=[])

add(slug="Causality", title="Causality",
    infobox=[("Field", "Metaphysics / philosophy of science"), ("Key figures", "Aristotle (four causes); Hume (regularity); Kant")],
    img="A billiard ball striking another, the classic image of cause and effect",
    lead="<b>Causality</b> is the relationship between causes and effects: the idea that events bring about other events. " + L("Aristotle") + " analysed four kinds of cause (material, formal, efficient, final). " + L("David_Hume") + " famously argued that we never perceive a necessary connection between cause and effect — only constant conjunction — making causation a projection of habit, a claim " + L("Immanuel_Kant") + " answered by making causality a category the mind imposes on experience.",
    sections=[("Modern debates", "<p>Contemporary theories include counterfactual accounts (Lewis: had the cause not occurred, the effect would not), interventionism (causation as what changes under manipulation), and process theories. Physics complicates the picture: relativity constrains causal order, and quantum theory's probabilities strain classical notions, though causal reasoning remains indispensable to science and law.</p>")],
    seealso=["Metaphysics", "David_Hume", "Determinism", "Ontology"],
    outgoing=["Metaphysics", "David_Hume", "Determinism", "Immanuel_Kant", "Aristotle"],
    unsure=[])

add(slug="Compatibilism", title="Compatibilism",
    infobox=[("Field", "Philosophy (free will)"), ("Thesis", "Free will and determinism are compatible"), ("Key figures", "Hume; Harry Frankfurt; Daniel Dennett; P. F. Strawson")],
    img="A chess player choosing a move, free within the rules of the game",
    lead="<b>Compatibilism</b> is the thesis that free will and determinism can both be true — that being free consists not in escaping causation but in acting from one's own desires, reasons and character without coercion. Held in forms by " + L("David_Hume") + " and most contemporary philosophers (per professional surveys a majority), it faces the consequence argument (van Inwagen): if determinism is true, our acts are consequences of remote events beyond our control.",
    sections=[("Arguments", "<p>Harry Frankfurt's cases (1969) attack the principle that responsibility requires alternatives: an agent who acts on his own, unaware a device would have forced the same act, seems responsible anyway. P. F. Strawson grounded responsibility in reactive attitudes (resentment, gratitude) woven into human relationships; Daniel Dennett defends an 'elbow room' of evolved competence rather than metaphysical ultimacy.</p>")],
    seealso=["Free_will", "Determinism", "Moral_responsibility"],
    outgoing=["Free_will", "Determinism", "David_Hume", "Philosophy"],
    unsure=["Survey percentages (PhilPapers) intentionally left qualitative"])

add(slug="Moral_responsibility", title="Moral responsibility",
    infobox=[("Field", "Ethics / philosophy of action"), ("Key concepts", "Praise, blame, desert, excuse; reactive attitudes")],
    img="A judge's gavel resting on a sound block, symbolising accountability",
    lead="<b>Moral responsibility</b> is the status of being a proper object of praise, blame, reward or punishment for one's actions and character. Debates ask what control and knowledge responsibility requires, whether it survives determinism, and how excuses (ignorance, coercion, insanity, childhood) mitigate it. P. F. Strawson's 'Freedom and Resentment' (1962) relocated the question in our interpersonal practices.",
    sections=[("Problems", "<p>Galen Strawson's 'basic argument' claims true responsibility is impossible, since we do not choose the character from which we act, in an infinite regress. Law distinguishes responsibility's conditions carefully (mens rea, insanity defences), while neuroscience findings on impulse and brain injury keep pressure on folk concepts.</p>")],
    seealso=["Free_will", "Compatibilism", "Ethics", "Determinism"],
    outgoing=["Free_will", "Compatibilism", "Ethics", "Determinism", "Philosophy"],
    unsure=[])

add(slug="Consequentialism", title="Consequentialism",
    infobox=[("Field", "Normative ethics"), ("Core claim", "The morality of an action depends only on its consequences"), ("Best-known form", "Utilitarianism")],
    img="A railway switch (points) at a junction, recalling the trolley problem",
    lead="<b>Consequentialism</b> is the family of ethical theories holding that the consequences of an action — and only they — determine its moral status. Its best-known member, " + L("Utilitarianism") + ", evaluates outcomes by aggregate well-being; other forms value equality, knowledge or preference-satisfaction. Consequentialism contrasts with deontology (duty- and rights-based) and virtue ethics (character-based), though hybrids abound.",
    sections=[("Debates", "<p>Famous tests include the trolley problem and Bernard Williams's integrity objection (a theory that makes you a 'channel' for outcomes alienates you from your own projects). 'Rule consequentialism' evaluates rules by the optimific results of their general acceptance, hoping to recover common-sense morality; critics call the collapse into act-consequentialism or rule-worship its dilemma.</p>")],
    seealso=["Utilitarianism", "Ethics", "Deontology"],
    outgoing=["Utilitarianism", "Ethics", "Deontology", "Philosophy"],
    unsure=[])

add(slug="Deontology", title="Deontology",
    infobox=[("Field", "Normative ethics"), ("Core claim", "Morality is a matter of duties and rules; some acts are required or forbidden regardless of consequences"), ("Key figure", "Immanuel Kant")],
    img="An engraved stone plaque of the Ten Commandments, emblem of duty-based morality",
    lead="<b>Deontology</b> (from Greek <i>deon</i>, duty) is the normative ethical position that morality is determined by duties and rules: some actions — lying, killing the innocent — are wrong in themselves, even when they would produce better outcomes. Its paradigm is " + L("Immanuel_Kant") + "'s ethics of the " + L("Categorical_imperative") + ", where persons must always be treated as ends, never merely as means.",
    sections=[("Forms and debates", "<p>Deontological constraints structure law and rights-talk (rights as 'trumps', Nozick); the view must answer what to do when duties conflict (W. D. Ross proposed prima facie duties weighed by judgement) and the 'paradox of deontology' — why not violate a constraint to minimise identical violations by others. Divine-command theory is a theological deontology; contractualism (Scanlon) grounds duties in justifiability to others.</p>")],
    seealso=["Categorical_imperative", "Immanuel_Kant", "Ethics", "Consequentialism"],
    outgoing=["Categorical_imperative", "Immanuel_Kant", "Ethics", "Consequentialism", "Utilitarianism"],
    unsure=[])

add(slug="Original_sin", title="Original sin",
    infobox=[("Tradition", "Christian theology"), ("Source narrative", "Adam and Eve's fall (Genesis 3)"), ("Systematised by", "Augustine of Hippo"), ("Related doctrines", "The Fall, concupiscence, baptism, Pelagian controversy")],
    img="A medieval painting of Adam and Eve eating the forbidden fruit in Eden",
    lead="<b>Original sin</b> is the Christian doctrine that humanity inherits a fallen condition from Adam and Eve's first disobedience in Eden. " + L("Augustine_of_Hippo", "Augustine") + ", reading Paul's letters, taught that Adam's sin is transmitted to all descendants, inclining the will to evil (<i>concupiscence</i>) and necessitating grace, administered in baptism. The Eastern churches speak instead of 'ancestral sin', emphasising mortality more than inherited guilt.",
    sections=[("Debates", "<p>Pelagius denied inherited sin and stressed free will, provoking Augustine's fiercest controversy and conciliar condemnation. Original sin underlies Christian doctrines of baptism (including infants) and redemption, and shaped Western ideas of human nature; critics from the Enlightenment onward object that inherited guilt is unjust, while theologians reply with corporate and structural readings of sin.</p>")],
    seealso=["Augustine_of_Hippo", "Christianity", "Bible", "Theology"],
    outgoing=["Augustine_of_Hippo", "Christianity", "Bible", "Theology", "Philosophy_of_religion"],
    unsure=[])

add(slug="Ahura_Mazda", title="Ahura Mazda",
    infobox=[("Religion", "Zoroastrianism"), ("Role", "Supreme god; uncreated creator; 'the Wise Lord'"), ("Opposed by", "Angra Mainyu (Ahriman), spirit of destruction"), ("Symbol", "The Faravahar (winged disc with figure) — commonly though debatably associated")],
    img="The Faravahar: a winged sun disc with a bearded human figure, carved in stone at Persepolis",
    lead="<b>Ahura Mazda</b> ('the Wise Lord') is the supreme deity of " + L("Zoroastrianism") + ", proclaimed by the prophet " + L("Zoroaster") + " as the uncreated creator of all that is good. In Zoroaster's Gathas, Ahura Mazda is wholly wise and benevolent, author of <i>asha</i> (truth and order), and is attended by the Amesha Spentas ('Bounteous Immortals'), aspects or archangels of his nature. Against him stands Angra Mainyu, the destructive spirit, whose lie (<i>druj</i>) humans must resist with good thoughts, words and deeds.",
    sections=[("Theology", "<p>Whether Zoroastrianism is purely monotheistic or dualistic is debated by scholars: the Gathas oppose Mazda to the hostile spirit, but Mazda remains supreme and will triumph at the final renovation (<i>Frashokereti</i>), when the dead rise and evil is destroyed. The name survives in the car company Mazda, chosen partly in his honour.</p>")],
    seealso=["Zoroastrianism", "Zoroaster", "Iran"],
    outgoing=["Zoroastrianism", "Zoroaster", "Religion"],
    unsure=["Frashokereti and Amesha Spenta details reflect standard summaries"])

add(slug="Parsis", title="Parsis",
    infobox=[("Religion", "Zoroastrianism"), ("Location", "Primarily Mumbai and Gujarat, India; worldwide diaspora"), ("Origin", "Zoroastrian refugees from Persia, c. 8th–10th century AD"), ("Language", "Gujarati")],
    img="A Parsi fire temple (agiary) facade in Mumbai with winged Faravahar motifs",
    lead="The <b>Parsis</b> are an ethnoreligious group of " + L("Zoroastrianism", "Zoroastrians") + " in India, descended from Persian refugees who fled the Islamisation of Iran between roughly the 8th and 10th centuries AD and settled in Gujarat — the name means simply 'Persians'. Small in number (fewer than 60,000 in India by recent censuses) but disproportionately prominent, Parsis founded major Indian industrial houses (Tata, Godrej, Wadia), shaped Bombay's commerce and philanthropy, and produced figures from Dadabhai Naoroji to Freddie Mercury (born Farrokh Bulsara).",
    sections=[("Community today", "<p>Parsi identity traditionally passes by birth (usually patrilineal); debates over accepting interfaith spouses and converts are intense because numbers are shrinking through late marriage, low fertility and emigration. Distinctive institutions include the fire temples (agiaries) and the Towers of Silence at Doonger Malabar Hill, Mumbai, where the dead were traditionally exposed to vultures — a practice in crisis since India's vulture populations collapsed in the 1990s.</p>")],
    seealso=["Zoroastrianism", "Zoroaster", "Mumbai", "India"],
    outgoing=["Zoroastrianism", "Zoroaster", "India", "Religion"],
    unsure=["Population figures (2011 census c. 57,000 in India) from memory"])

add(slug="Pessimism", title="Philosophical pessimism",
    infobox=[("Field", "Philosophy"), ("Key figures", "Arthur Schopenhauer; Giacomo Leopardi; Emil Cioran"), ("Core claim", "Life involves unavoidable suffering that outweighs its goods; existence may be worse than non-existence")],
    img="A lone figure seated in a bleak landscape under grey clouds",
    lead="<b>Philosophical pessimism</b> is the view that life is predominantly bad — that suffering is structural and outweighs happiness, and in strong forms that it would have been better never to exist. Its classical system is " + L("Arthur_Schopenhauer") + "'s: the world as blind striving Will condemns beings to want, suffer, and bore themselves in alternation, with salvation only in denying the will. Leopardi gave pessimism poetic form in Italy.",
    sections=[("Modern forms", "<p>Contemporary pessimism includes David Benatar's anti-natalism (<i>Better Never to Have Been</i>, 2006), arguing coming into existence is always a harm, and debates with optimists over progress data (Pinker) and over whether pessimism is a judgement or a temperament. Buddhist diagnoses of <i>dukkha</i> are a convergent ancient parallel.</p>")],
    seealso=["Arthur_Schopenhauer", "Buddhism", "Philosophy"],
    outgoing=["Arthur_Schopenhauer", "Buddhism", "Philosophy", "Nihilism"],
    unsure=[])

add(slug="German_idealism", title="German idealism",
    infobox=[("Era", "Late 18th – mid 19th century"), ("Key figures", "Kant, Fichte, Schelling, Hegel"), ("Reaction to", "Kant's critical philosophy")],
    img="A portrait gallery of the German idealists: Kant, Fichte, Schelling and Hegel",
    lead="<b>German idealism</b> is the philosophical movement that developed in Germany between the 1780s and 1840s out of " + L("Immanuel_Kant") + "'s critical philosophy. Kant's successors judged his thing-in-itself an inconsistent leftover: Fichte founded everything on the self-positing I; Schelling balanced subject with nature; and G. W. F. Hegel's absolute idealism presented reality as Spirit coming to know itself through history's dialectic — a system that dominated German thought until its fracture into Right and Left Hegelian camps (the latter producing Marx).",
    sections=[("Legacy", "<p>The movement reshaped theology, historiography, aesthetics and political thought; its eclipse by positivism and analytic philosophy hid debts that 20th-century scholarship (and the 'Pittsburgh school' of Sellars, Brandom, McDowell) has recovered, reconnecting Hegel to contemporary debates.</p>")],
    seealso=["Immanuel_Kant", "Idealism", "Karl_Marx", "Philosophy"],
    outgoing=["Immanuel_Kant", "Idealism", "Karl_Marx", "Philosophy"],
    unsure=[])

add(slug="Nominalism", title="Nominalism",
    infobox=[("Field", "Metaphysics"), ("Issue", "The problem of universals"), ("Key figures", "Roscelin; William of Ockham; modern: Nelson Goodman, W. V. O. Quine")],
    img="A collection of individual roses, each unique, under the general word 'rose'",
    lead="<b>Nominalism</b> is the metaphysical view that universals and abstract objects do not exist independently: only particular things exist, and general terms ('redness', 'humanity') are names (<i>nomina</i>) or concepts grouping resembling particulars. Opposed by realism (Plato's Forms, medieval moderate realism), nominalism was championed by William of Ockham, whose razor ('entities must not be multiplied beyond necessity') is its methodological emblem.",
    sections=[("Stakes", "<p>The medieval problem of universals bore on theology (the Trinity, transubstantiation) and science alike. Modern nominalism, revived by Goodman and Quine, tries to do mathematics and science without abstract objects — a programme whose difficulty is measured by the apparent indispensability of numbers.</p>")],
    seealso=["Ontology", "Metaphysics", "Plato", "Scholasticism"],
    outgoing=["Ontology", "Metaphysics", "Plato", "Scholasticism", "Philosophy"],
    unsure=[])

add(slug="Mereology", title="Mereology",
    infobox=[("Field", "Metaphysics / logic"), ("Subject", "Relations between parts and wholes"), ("Term coined by", "Stanisław Leśniewski (1916)")],
    img="Nested wooden dolls illustrating part-whole relations",
    lead="<b>Mereology</b> is the formal study of parts and the wholes they form — the branch of " + L("Ontology") + " and logic concerned with parthood. It asks deceptively simple questions: when do parts compose a further object (does a heap of planks make a ship? do atoms compose a table?), whether composition is unrestricted (any plurality forms a whole), and how objects persist through part-change — puzzles classed since Plutarch under the Ship of Theseus.",
    sections=[("Positions", "<p>Mereological universalism says any two things have a sum; nihilism says only simples exist; moderate views restrict composition to cases like living organisms (van Inwagen). The logic of parthood underlies work in formal ontology, computer science and linguistics (mass nouns, plurals).</p>")],
    seealso=["Ontology", "Metaphysics"],
    outgoing=["Ontology", "Metaphysics", "Philosophy"],
    unsure=[])

add(slug="Odysseus", title="Odysseus",
    infobox=[("Tradition", "Greek mythology"), ("Home", "Ithaca"), ("Consort", "Penelope"), ("Known for", "Hero of the Odyssey; deviser of the Trojan Horse")],
    img="Odysseus tied to the mast of his ship, listening to the Sirens, from a Greek vase painting",
    lead="<b>Odysseus</b> (Roman: Ulysses) is a legendary Greek king of Ithaca and the hero of Homer's <i>Odyssey</i>. Famed for cunning (<i>metis</i>) as much as courage, he devised the wooden horse that ended the Trojan War, then spent ten years wandering home — past the Cyclops Polyphemus, Circe, the Sirens, Scylla and Charybdis, and the cave of Calypso — to find his wife Penelope beset by suitors he then slew.",
    sections=[("Legacy", "<p>Odysseus embodies the wily survivor: Dante places him in Hell for fraud yet gives him a magnificent final voyage; Tennyson's 'Ulysses' makes him the emblem of restless striving ('to strive, to seek, to find, and not to yield'); Joyce's <i>Ulysses</i> maps his day onto Dublin. He remains Greek mythology's most human hero.</p>")],
    seealso=["Greek_mythology", "Heracles", "Mythology", "Ancient_Greece"],
    outgoing=["Greek_mythology", "Heracles", "Mythology", "Ancient_Greece"],
    unsure=[])

add(slug="Consciousness", title="Consciousness",
    infobox=[("Field", "Philosophy of mind / cognitive science"), ("Key problems", "The hard problem (Chalmers); qualia; access vs phenomenal consciousness")],
    img="A glowing silhouette of a human head in profile against darkness",
    lead="<b>Consciousness</b> is the state or quality of being aware of one's surroundings, thoughts and feelings — most intractably, the subjective, first-person character of experience: what it is <i>like</i> to see red or feel pain. David Chalmers's 'hard problem' (1995) asks why physical processing in the brain is accompanied by experience at all, distinguishing it from the 'easy' problems of function and report.",
    sections=[("Theories", "<p>Positions range from dualism and panpsychism (experience as fundamental and widespread) to physicalist theories: global workspace theory (Baars, Dehaene), integrated information theory (Tononi), higher-order and illusionist accounts (Dennett, Frankish). Thought experiments structure debate — Nagel's bat, Jackson's colour-scientist Mary, philosophical zombies. Consciousness studies is now an interdisciplinary science, though no theory commands consensus.</p>")],
    seealso=["Philosophy_of_mind", "Dualism", "Metaphysics"],
    outgoing=["Philosophy_of_mind", "Dualism", "Metaphysics", "Philosophy"],
    unsure=[])

add(slug="Friedrich_Engels", title="Friedrich Engels",
    infobox=[("Born", "28 November 1820, Barmen, Prussia"), ("Died", "5 August 1895, London"), ("Known for", "Co-founder of Marxism with Karl Marx; author of The Condition of the Working Class in England (1845)")],
    img="A photograph of Friedrich Engels with a full beard in middle age",
    lead="<b>Friedrich Engels</b> (1820–1895) was a German philosopher, political theorist and industrialist who, with " + L("Karl_Marx") + ", founded the theory known as Marxism. Sent to manage his family's Manchester cotton mills, he documented working-class misery in <i>The Condition of the Working Class in England</i> (1845), co-wrote <i>The Communist Manifesto</i> (1848), financed Marx's research for decades, and after Marx's death edited volumes II and III of <i>Das Kapital</i> and systematised their joint doctrine in works like <i>Anti-Dühring</i> and <i>Socialism: Utopian and Scientific</i>.",
    sections=[("Assessment", "<p>Scholars debate how far 'Engelsism' — a dialectics of nature extended beyond history — simplifies or distorts Marx; no one disputes that without Engels's money, editing and popularisation, Marxism as the world knows it would not exist.</p>")],
    seealso=["Karl_Marx", "Communism", "Historical_materialism"],
    outgoing=["Karl_Marx", "Communism", "Historical_materialism", "Philosophy"],
    unsure=[])

add(slug="Historical_materialism", title="Historical materialism",
    infobox=[("Field", "Philosophy of history / sociology"), ("Formulated by", "Karl Marx and Friedrich Engels"), ("Core claim", "Material (economic) conditions fundamentally shape society and its ideas")],
    img="A 19th-century Manchester cotton mill, emblem of the industrial base Marx analysed",
    lead="<b>Historical materialism</b> is the Marxist theory of history: societies develop through stages defined by their mode of production, and the economic 'base' — forces and relations of production — conditions the legal, political and ideological 'superstructure'. History's motor, on this account, is class struggle over the material conditions of life. Marx sketched the theory in <i>The German Ideology</i> (1846, with " + L("Friedrich_Engels", "Engels") + ") and the 1859 <i>Preface</i>.",
    sections=[("Debates", "<p>Twentieth-century Marxists disputed its determinism: Gramsci's hegemony, Althusser's relative autonomy and analytical Marxism (G. A. Cohen's rigorous reconstruction) softened or formalised the base–superstructure claim. As historiography, its influence reached far beyond Marxists — into the Annales school and social history generally.</p>")],
    seealso=["Karl_Marx", "Friedrich_Engels", "Communism", "Socialism"],
    outgoing=["Karl_Marx", "Friedrich_Engels", "Communism", "Socialism", "Philosophy"],
    unsure=[])

add(slug="Folklore", title="Folklore",
    infobox=[("Field", "Folkloristics / anthropology"), ("Forms", "Myths, legends, folktales, proverbs, songs, customs, material culture"), ("Term coined", "1846 (William Thoms)")],
    img="An elder telling stories to children around a fire at night",
    lead="<b>Folklore</b> is the expressive culture shared by a group — its myths, legends, folktales, jokes, proverbs, songs, dances, costumes, crafts and customs — transmitted informally, often orally, and varying in the telling. The word was coined in 1846 by William Thoms (replacing 'popular antiquities'); the discipline that studies it, folkloristics, emerged with collectors like the Brothers Grimm, whose <i>Children's and Household Tales</i> (1812) both preserved and reshaped German tradition.",
    sections=[("Study", "<p>Scholars classify tales by motif (the Aarne–Thompson–Uther index), analyse their structure (Propp's morphology of the folktale), and debate function: entertainment, education, social control, the venting of forbidden wishes. Digital culture has revived the field — internet memes and urban legends are folklore in real time.</p>")],
    seealso=["Mythology", "Greek_mythology", "Religion", "Culture"],
    outgoing=["Mythology", "Greek_mythology", "Norse_mythology", "Religion"],
    unsure=[])

print("w3 loaded", len(PAGES))

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
                        "unsure": ["Page already existed on disk when wave 3 ran"], "outgoing": [url_of(s) for s in p.get("outgoing", [])]})
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
