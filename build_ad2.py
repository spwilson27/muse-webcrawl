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

add(slug="Zeno_of_Citium", title="Zeno of Citium",
    infobox=[("Born", "c. 334 BC, Citium, Cyprus"), ("Died", "c. 262 BC, Athens"), ("School", "Stoicism (founder)")],
    img="A marble bust of Zeno of Citium, bearded and thoughtful",
    lead="<b>Zeno of Citium</b> (c. 334 – c. 262 BC) was a Hellenistic philosopher from Cyprus who founded the Stoic school in Athens around 300 BC. A Phoenician-Greek merchant who turned to philosophy after a shipwreck — remarking, tradition says, that he had made a prosperous voyage when he was wrecked — he taught in the Painted Porch (<i>Stoa Poikile</i>), from which " + L("Stoicism") + " takes its name.",
    sections=[("Teaching", "<p>Zeno divided philosophy into logic, physics and ethics (compared to an egg, or a garden's fence, soil and fruit). He taught that the universe is a rational, providential organism governed by the divine <i>logos</i>, and that happiness is a 'good flow of life' achieved by living in agreement with nature. Little of his writing survives; his doctrines were preserved and developed by successors such as Cleanthes and Chrysippus.</p>")],
    seealso=["Stoicism", "Marcus_Aurelius", "Epictetus", "Seneca"],
    outgoing=["Stoicism", "Marcus_Aurelius", "Epictetus", "Seneca", "Philosophy"],
    unsure=["Shipwreck story is traditional anecdote (Diogenes Laertius)"])

add(slug="Seneca", title="Seneca the Younger",
    infobox=[("Born", "c. 4 BC, Cordoba, Hispania"), ("Died", "65 AD, Rome"), ("School", "Stoicism"), ("Notable works", "Letters to Lucilius; Moral Essays; tragedies")],
    img="An ancient marble bust identified as Seneca, gaunt with unkempt hair",
    lead="<b>Lucius Annaeus Seneca</b> (c. 4 BC – 65 AD), usually known as <b>Seneca the Younger</b>, was a Roman Stoic philosopher, statesman and playwright, tutor and advisor to the emperor Nero. His <i>Letters to Lucilius</i> and essays made " + L("Stoicism") + " practical and literary: reflections on time ('On the Shortness of Life'), anger, wealth and death that remain widely read. Implicated (perhaps falsely) in the Pisonian conspiracy, he was ordered by Nero to commit suicide, which he did in the manner of Socrates.",
    sections=[("Life and tension", "<p>Seneca's career embodied tensions he himself examined: a preacher of simplicity who amassed a huge fortune at court, exiled to Corsica under Claudius, then recalled to tutor Nero, whose early reign he guided with Burrus before Nero's tyranny deepened. His tragedies influenced Renaissance drama, and his Christian admirers so esteemed him that a forged correspondence with Saint Paul circulated in the Middle Ages.</p>")],
    seealso=["Stoicism", "Marcus_Aurelius", "Epictetus", "Zeno_of_Citium"],
    outgoing=["Stoicism", "Marcus_Aurelius", "Epictetus", "Zeno_of_Citium", "Roman_Empire"],
    unsure=[])

add(slug="Zeus", title="Zeus",
    infobox=[("Religion", "Ancient Greek religion"), ("Abode", "Mount Olympus"), ("Symbols", "Thunderbolt, eagle, oak, aegis"), ("Parents", "Cronus and Rhea"), ("Consort", "Hera (among others)")],
    img="The Artemision Bronze: a majestic statue of Zeus hurling a thunderbolt",
    lead="<b>Zeus</b> is the sky and thunder god in ancient Greek religion and mythology, who rules as king of the gods of Mount Olympus. Son of the Titans Cronus and Rhea, he overthrew his father's generation in the Titanomachy, divided the cosmos with his brothers Poseidon (sea) and Hades (underworld), and thereafter upheld order, law and fate — hurling thunderbolts at transgressors while fathering gods and heroes in countless myths.",
    sections=[("Cult and legacy", "<p>Zeus was worshipped across the Greek world, most famously at Olympia, where the Olympic Games were held in his honour and Pheidias' colossal gold-and-ivory statue of him stood as one of the Seven Wonders. The Romans identified him with Jupiter. His myths — the births of Athena from his head and Dionysus from his thigh, his transformations to approach mortal women — were retold by artists from Phidias to Rubens and remain staples of Western culture.</p>")],
    seealso=["Greek_mythology", "Mythology", "Heracles", "Ancient_Greece"],
    outgoing=["Greek_mythology", "Mythology", "Heracles", "Ancient_Greece", "Olympic_Games"],
    unsure=[])

add(slug="Odin", title="Odin",
    infobox=[("Religion", "Norse mythology"), ("Symbols", "Spear Gungnir, ravens Huginn and Muninn, eight-legged horse Sleipnir"), ("Consort", "Frigg"), ("Fate", "To be killed by the wolf Fenrir at Ragnarök")],
    img="Odin depicted as a one-eyed old traveller in a wide-brimmed hat and cloak, with two ravens",
    lead="<b>Odin</b> is the chief god of " + L("Norse_mythology") + ", associated with wisdom, war, poetry, death and magic. One-eyed — he surrendered an eye at Mimir's well for wisdom — he hung himself on the world tree Yggdrasil for nine nights to win the secret of the runes, and rides the eight-legged horse Sleipnir, attended by the ravens Huginn (thought) and Muninn (memory). Foreknowing his doom, he gathers slain heroes in Valhalla to fight at Ragnarök, where the wolf Fenrir will kill him.",
    sections=[("Legacy", "<p>Odin's name survives in Wednesday (Woden's day). Tacitus identified him with Mercury; medieval sources present him as a euhemerised travelling king. Modern retellings, from Wagner to Neil Gaiman's <i>American Gods</i>, centre his hunger for knowledge at any price.</p>")],
    seealso=["Norse_mythology", "Thor", "Mythology", "Vikings"],
    outgoing=["Norse_mythology", "Thor", "Mythology", "Vikings"],
    unsure=[])

add(slug="Thor", title="Thor",
    infobox=[("Religion", "Norse mythology"), ("Symbols", "Hammer Mjölnir, belt Megingjörð, iron gloves"), ("Parents", "Odin and Jörð (Earth)"), ("Consort", "Sif")],
    img="Thor raising his hammer Mjölnir amid lightning, red-bearded and mighty",
    lead="<b>Thor</b> is the Norse god of thunder, storms and the protection of humankind, the foremost defender of the gods against the giants. Red-bearded and immense in strength, he wields the short-handled hammer Mjölnir, wears a belt that doubles his strength, and drives a chariot pulled by two goats. Of all the Norse gods he was the most widely worshipped, his hammer worn as a protective amulet across the Viking world.",
    sections=[("Myths and fate", "<p>Famous tales include Thor's fishing for the World Serpent Jörmungandr, his journey to the giant Útgarða-Loki, where illusions trick him, and the theft of his hammer by the giant Thrym, recovered when Thor disguises himself as the bride. At Ragnarök Thor will kill the World Serpent and take nine steps before falling to its venom.</p>")],
    seealso=["Norse_mythology", "Odin", "Mythology", "Vikings"],
    outgoing=["Norse_mythology", "Odin", "Mythology", "Vikings"],
    unsure=[])

add(slug="Heracles", title="Heracles",
    infobox=[("Religion", "Greek mythology"), ("Parents", "Zeus and Alcmene"), ("Symbols", "Lion skin, club, bow"), ("Known for", "The Twelve Labours")],
    img="The Farnese Hercules: a massive marble statue of Heracles leaning wearily on his club",
    lead="<b>Heracles</b> (Roman: Hercules) is the greatest hero of " + L("Greek_mythology") + ", a son of " + L("Zeus") + " famed for superhuman strength and for completing the Twelve Labours imposed by King Eurystheus — including slaying the Nemean lion and the Hydra, cleaning the Augean stables, and fetching Cerberus from the underworld. Driven mad by Hera, he had killed his own family, and the labours were penance; on death by a poisoned robe he was lifted to Olympus as a god.",
    sections=[("Legacy", "<p>Heracles was worshipped as both hero and god across the Greek and Roman worlds, patron of gymnasiums and model of virtue through toil — the philosopher Prodicus' tale of Heracles at the crossroads, choosing Virtue's hard path over Vice's easy one, became a moral staple. His name echoes in the Pillars of Hercules at Gibraltar and in countless artworks.</p>")],
    seealso=["Greek_mythology", "Zeus", "Mythology"],
    outgoing=["Greek_mythology", "Zeus", "Mythology", "Ancient_Greece"],
    unsure=[])

add(slug="Rationalism", title="Rationalism",
    infobox=[("Field", "Epistemology"), ("Key figures", "René Descartes, Baruch Spinoza, Gottfried Wilhelm Leibniz"), ("Opposed by", "Empiricism")],
    img="A geometric diagram symbolising knowledge deduced from first principles",
    lead="<b>Rationalism</b> is the epistemological view that reason is the chief source and test of knowledge — that reality has an intrinsically logical structure accessible to deduction from innate, self-evident principles. In its classic 17th-century forms (" + L("René_Descartes", "Descartes") + ", " + L("Baruch_Spinoza", "Spinoza") + ", " + L("Gottfried_Wilhelm_Leibniz", "Leibniz") + "), rationalism held that significant knowledge is a priori: gained independently of sense experience, as in mathematics, which rationalists took as the model of all knowing.",
    sections=[("Debate with empiricism", "<p>The textbook contrast sets rationalists against British empiricists (" + L("John_Locke") + ", " + L("George_Berkeley") + ", " + L("David_Hume") + "), who grounded knowledge in experience. " + L("Immanuel_Kant") + " sought to synthesise the two: concepts without intuitions are empty, intuitions without concepts are blind. Modern scholars caution that the rationalist/empiricist boxes simplify the actual views of all six philosophers.</p>")],
    seealso=["Empiricism", "Epistemology", "René_Descartes"],
    outgoing=["Empiricism", "Epistemology", "René_Descartes", "Baruch_Spinoza", "John_Locke", "David_Hume", "Immanuel_Kant"],
    unsure=[])

add(slug="Empiricism", title="Empiricism",
    infobox=[("Field", "Epistemology"), ("Key figures", "John Locke, George Berkeley, David Hume"), ("Opposed by", "Rationalism")],
    img="An eye observing light through a prism, symbolising knowledge from the senses",
    lead="<b>Empiricism</b> is the theory that knowledge comes primarily from sensory experience. Against the rationalists' innate ideas, empiricists such as " + L("John_Locke") + " held that the mind begins as a blank slate (<i>tabula rasa</i>) inscribed by sensation and reflection. " + L("George_Berkeley") + " radicalised the position into idealism; " + L("David_Hume") + " pressed it toward scepticism about causation and induction — conclusions that awoke " + L("Immanuel_Kant") + " from his dogmatic slumber.",
    sections=[("Legacy", "<p>Empiricism underlies the scientific method's emphasis on observation and experiment, and reappears in logical positivism (the Vienna Circle) and in contemporary naturalised epistemology. In science studies 'empirical' simply means based on observation or experiment rather than theory alone.</p>")],
    seealso=["Rationalism", "Epistemology", "John_Locke", "David_Hume", "Scepticism"],
    outgoing=["Rationalism", "Epistemology", "John_Locke", "George_Berkeley", "David_Hume", "Immanuel_Kant", "Scepticism", "Tabula_rasa"],
    unsure=[])

add(slug="Scepticism", title="Scepticism",
    infobox=[("Field", "Epistemology"), ("Ancient school", "Pyrrhonism (Pyrrho, Sextus Empiricus)"), ("Key modern figure", "David Hume; René Descartes (methodical doubt)")],
    img="A figure standing at a crossroads in fog, symbolising suspended judgement",
    lead="<b>Philosophical scepticism</b> is the family of positions questioning the possibility of knowledge or justified certainty. Ancient Pyrrhonists, following Pyrrho and recorded by Sextus Empiricus, suspended judgement (<i>epoché</i>) about all non-evident matters and reported attaining tranquillity thereby. In the modern era, " + L("René_Descartes", "Descartes") + " used sceptical scenarios — dreams, a deceiving demon — as a tool to find indubitable foundations, while " + L("David_Hume") + " drew lasting sceptical conclusions about induction, causation and the external world.",
    sections=[("Responses", "<p>Replies include Kant's transcendental arguments, G. E. Moore's appeal to common sense ('here is a hand'), and externalist theories on which knowledge does not require ruling out sceptical possibilities from the inside. Academic (as opposed to Pyrrhonian) scepticism asserts that nothing can be known — a claim critics charge is self-refuting.</p>")],
    seealso=["Epistemology", "David_Hume", "René_Descartes", "Empiricism"],
    outgoing=["Epistemology", "David_Hume", "René_Descartes", "Empiricism", "Philosophy"],
    unsure=[])

add(slug="Problem_of_induction", title="Problem of induction",
    infobox=[("Field", "Epistemology / philosophy of science"), ("Formulated by", "David Hume (1739)"), ("Responses", "Karl Popper's falsificationism; Bayesianism; pragmatic vindications")],
    img="A black swan among white swans, the classic image of induction's risk",
    lead="The <b>problem of induction</b> is the philosophical question of whether inductive reasoning — inferring general laws or future events from observed regularities — can ever be justified. " + L("David_Hume") + " argued in 1739 that such inference assumes nature's uniformity, which cannot itself be proved without circularity: the sun's past risings do not logically guarantee tomorrow's. All observed swans being white never entailed that no black swans exist — as Australia's proved.",
    sections=[("Significance", "<p>The problem reshaped the philosophy of science. Karl Popper concluded science never confirms but only falsifies, replacing induction with conjecture and refutation; Nelson Goodman's 'new riddle' (grue) showed the problem is deeper than counting instances. Hume himself treated inductive habit as natural and unavoidable — custom, not reason, is 'the great guide of human life'.</p>")],
    seealso=["David_Hume", "Epistemology", "Philosophy_of_science", "Falsifiability"],
    outgoing=["David_Hume", "Epistemology", "Philosophy"],
    unsure=[])

add(slug="Gettier_problem", title="Gettier problem",
    infobox=[("Field", "Epistemology"), ("Published", "Edmund Gettier, 'Is Justified True Belief Knowledge?', Analysis (1963)")],
    img="The three-page 1963 issue of the journal Analysis containing Gettier's paper",
    lead="The <b>Gettier problem</b> is a challenge to the classical analysis of knowledge as justified true belief, posed by Edmund Gettier in a three-page paper in 1963. Gettier described cases in which a person has a belief that is both true and justified, yet intuitively is not knowledge because its truth is a matter of luck — for instance, inferring a true conclusion from a justified but false premise.",
    sections=[("Aftermath", "<p>The paper overturned consensus in epistemology overnight. Proposed repairs added a fourth condition (no false lemmas, defeasibility, causal connection), while others abandoned the analysis project (relying on reliabilism or knowledge-first approaches). The problem's fame vastly exceeds its length, and it remains a standard test for any theory of knowledge.</p>")],
    seealso=["Epistemology", "Knowledge"],
    outgoing=["Epistemology", "Philosophy"],
    unsure=[])

add(slug="Cogito_ergo_sum", title="Cogito, ergo sum",
    infobox=[("Phrase", "Latin: 'I think, therefore I am'"), ("Author", "René Descartes"), ("First published", "Discourse on the Method (1637, in French: je pense, donc je suis); Latin form in Principles of Philosophy (1644)")],
    img="The title page of Descartes' Discourse on the Method, 1637",
    lead="<b>Cogito, ergo sum</b> — 'I think, therefore I am' — is the famous conclusion by which " + L("René_Descartes") + " emerged from methodical doubt. Having supposed that dreams, error or a malicious demon might deceive him about everything else, Descartes found one truth that survives all doubt: that he who doubts and thinks must exist as a thinking thing. It becomes the first principle of his philosophy, the fixed point from which knowledge is rebuilt.",
    sections=[("Criticisms", "<p>Philosophers have questioned whether the cogito is an inference at all (Descartes said it is an intuition), whether 'I' is smuggled in (Lichtenberg suggested only 'it thinks' is warranted), and whether Augustine's earlier 'if I am deceived, I exist' anticipates it. It remains philosophy's most quoted sentence.</p>")],
    seealso=["René_Descartes", "Epistemology", "Rationalism"],
    outgoing=["René_Descartes", "Epistemology", "Rationalism", "Augustine_of_Hippo"],
    unsure=["Exact priority/anticipations (Augustine, Avicenna) are standard scholarly caveats"])

add(slug="Idealism", title="Idealism",
    infobox=[("Field", "Metaphysics"), ("Key figures", "George Berkeley (subjective idealism); Immanuel Kant (transcendental idealism); G. W. F. Hegel (absolute idealism)")],
    img="A translucent image of a tree dissolving into perceptions, evoking Berkeley's philosophy",
    lead="<b>Idealism</b> is the family of metaphysical views asserting that reality is fundamentally mental, immaterial, or otherwise dependent on mind. " + L("George_Berkeley") + "'s subjective idealism holds that physical objects are bundles of ideas whose being is to be perceived; " + L("Immanuel_Kant") + "'s transcendental idealism holds that space, time and the categories are forms our mind imposes on an unknowable thing-in-itself; Hegel's absolute idealism sees reality as the self-unfolding of Spirit or the Absolute Idea.",
    sections=[("Influence", "<p>Idealism dominated 19th-century philosophy in Germany and Britain (F. H. Bradley, T. H. Green) before the analytic revolt of Moore and Russell. Its motifs persist in debates about consciousness, constructivism and the interpretation of quantum mechanics, and parallels are drawn (controversially) with Indian philosophies such as Advaita Vedanta and Yogacara Buddhism.</p>")],
    seealso=["George_Berkeley", "Immanuel_Kant", "Metaphysics", "German_idealism"],
    outgoing=["George_Berkeley", "Immanuel_Kant", "Metaphysics", "German_idealism", "Philosophy"],
    unsure=[])

add(slug="Dualism", title="Dualism",
    infobox=[("Field", "Philosophy of mind / metaphysics"), ("Key figure", "René Descartes"), ("Alternatives", "Monism, physicalism")],
    img="A silhouette of a head split between a glowing mind and a mechanical brain",
    lead="<b>Dualism</b> in the philosophy of mind is the view that mind and body — or mental and physical properties — are fundamentally different kinds of thing. " + L("René_Descartes", "Descartes") + "'s substance dualism posits thinking substance distinct from extended matter, raising the interaction problem Princess Elisabeth of Bohemia pressed on him: how can an immaterial mind move a material body? Property dualists hold instead that one substance has irreducibly mental properties.",
    sections=[("Debate", "<p>Dualism draws support from the apparent gap between subjective experience and physical description (qualia, the knowledge argument) and faces objections from neuroscience's tight mind–brain correlation, causal closure of the physical, and Occam's razor. It remains a minority but persistent position, defended by philosophers such as David Chalmers in property-dualist form.</p>")],
    seealso=["Philosophy_of_mind", "René_Descartes", "Metaphysics"],
    outgoing=["Philosophy_of_mind", "René_Descartes", "Metaphysics", "Consciousness"],
    unsure=[])

add(slug="Determinism", title="Determinism",
    infobox=[("Field", "Metaphysics"), ("Thesis", "Every event is necessitated by antecedent conditions and the laws of nature"), ("Key debate", "Compatibility with free will")],
    img="A row of falling dominoes, the standard image of causal determinism",
    lead="<b>Determinism</b> is the philosophical view that all events, including human choices, are completely determined by previously existing causes together with the laws of nature. Laplace imagined an intellect knowing all positions and forces could predict the entire future. Determinism's most debated consequence concerns " + L("Free_will") + ": compatibilists argue freedom can coexist with determination, incompatibilists deny it, and hard determinists accept the loss of free will.",
    sections=[("Variants", "<p>Causal determinism is distinguished from theological predestination and from fatalism (which skips the causal chain). Quantum mechanics is often said to introduce indeterminism, though its interpretations differ, and randomness in any case does not by itself restore free will — a point philosophers underline.</p>")],
    seealso=["Free_will", "Metaphysics", "Compatibilism", "Causality"],
    outgoing=["Free_will", "Metaphysics", "Compatibilism", "Philosophy"],
    unsure=[])

add(slug="Theology", title="Theology",
    infobox=[("Field", "Religious studies / philosophy"), ("Scope", "Study of God and religious belief within traditions")],
    img="A medieval university lecture hall with scholars disputing a theological text",
    lead="<b>Theology</b> is the systematic study of the nature of God and of religious belief from within (or in dialogue with) a faith tradition. In Christianity it spans biblical studies, church history, systematics (doctrines of God, Christ, salvation) and practical theology; analogous disciplines exist in Islam (<i>kalam</i>), Judaism and Hindu thought (where the term is applied by analogy). " + L("Thomas_Aquinas") + " called it a science, with revealed principles; modern universities also teach it in historical and comparative modes.",
    sections=[("Branches and debates", "<p>Natural theology reasons about God without revelation — the project " + L("Philosophy_of_religion") + " shares — while revealed theology works from scripture and tradition. Major modern currents include neo-orthodoxy (Karl Barth), liberation theology (Gustavo Gutiérrez), feminist and process theologies, each re-reading the sources under new questions.</p>")],
    seealso=["Philosophy_of_religion", "Thomas_Aquinas", "Religion"],
    outgoing=["Philosophy_of_religion", "Thomas_Aquinas", "Religion", "Philosophy"],
    unsure=[])

add(slug="Problem_of_evil", title="Problem of evil",
    infobox=[("Field", "Philosophy of religion"), ("Classical formulation", "Attributed to Epicurus (via Lactantius and Hume)"), ("Key responses", "Free will defence (Plantinga); soul-making theodicy (Hick)")],
    img="A ruined church after an earthquake, evoking the Lisbon earthquake of 1755 that shook Enlightenment faith",
    lead="The <b>problem of evil</b> is the question of how to reconcile the existence of evil and suffering with a God who is omniscient, omnipotent and wholly good. In its logical form it alleges outright inconsistency; in its evidential form it argues that the amount and distribution of suffering — animal pain, children's diseases, disasters like the Lisbon earthquake of 1755 — make theism improbable. It is widely considered the strongest argument for " + L("Atheism") + ".",
    sections=[("Responses", "<p>Theodicies attempt justification: Augustine and Leibniz treat evil as privation and a by-product of a best possible order; John Hick's 'soul-making' sees suffering as necessary for moral growth. Alvin Plantinga's free will defence, not a theodicy but a defence, argues it is possible that even God cannot create free creatures who never choose evil — widely taken to defeat the logical form. Sceptical theism questions our ability to judge God's reasons at all. The Book of Job is the tradition's own refusal of easy answers.</p>")],
    seealso=["Philosophy_of_religion", "Atheism", "Theology", "Augustine_of_Hippo"],
    outgoing=["Philosophy_of_religion", "Atheism", "Theology", "Augustine_of_Hippo", "David_Hume"],
    unsure=["Epicurus attribution is via later sources; flagged as traditional"])

add(slug="Ontological_argument", title="Ontological argument",
    infobox=[("Field", "Philosophy of religion"), ("First formulation", "Anselm of Canterbury, Proslogion (1078)"), ("Key critics", "Gaunilo; Aquinas; Kant")],
    img="A page of Anselm's Proslogion in a medieval manuscript",
    lead="The <b>ontological argument</b> is an a priori argument for God's existence, first given by Anselm of Canterbury in 1078: God, defined as 'that than which nothing greater can be conceived', must exist in reality as well as in the understanding, since existing in reality is greater. " + L("René_Descartes", "Descartes") + " included existence in God's essence as a triangle includes its angles; " + L("Immanuel_Kant") + " objected that existence is not a real predicate — a hundred real thalers contain no more than a hundred possible ones.",
    sections=[("Modern versions", "<p>Alvin Plantinga's modal version argues that if a maximally great being is possible, then (given the logic of possible worlds, S5) it exists in every world including ours. Gaunilo's parody — the perfect lost island — is the oldest rebuttal, and debate over whether it succeeds continues; the argument remains philosophy's most discussed 'proof' precisely because intuitions about it split so cleanly.</p>")],
    seealso=["Philosophy_of_religion", "Thomas_Aquinas", "Immanuel_Kant", "René_Descartes"],
    outgoing=["Philosophy_of_religion", "Thomas_Aquinas", "Immanuel_Kant", "René_Descartes"],
    unsure=[])

add(slug="Faith", title="Faith",
    infobox=[("Field", "Religion / philosophy of religion"), ("Related concepts", "Belief, trust, hope; fideism vs evidentialism")],
    img="Candles lit in a dark cathedral as votive offerings",
    lead="<b>Faith</b> is confidence or trust in a person, thing or doctrine. In religion it typically means trust in God and acceptance of teachings held to be revealed; the Christian tradition's epistle to the Hebrews calls it 'the assurance of things hoped for, the conviction of things not seen'. Philosophers debate its relation to evidence: evidentialists require proportioning belief to proof, while fideists and thinkers like " + L("Søren_Kierkegaard") + " — for whom faith begins precisely where thinking leaves off — defend commitment beyond or against probability.",
    sections=[("Models", "<p>Analyses distinguish faith as belief-that (assent to propositions), faith as trust-in (affective reliance on a person), and faith as commitment expressed in action. Aquinas integrated faith with reason as assent of the intellect moved by the will and grace; modern debates ask whether religious faith is more like ordinary interpersonal trust than like hypothesis-belief.</p>")],
    seealso=["Søren_Kierkegaard", "Philosophy_of_religion", "Theology", "Religion"],
    outgoing=["Søren_Kierkegaard", "Philosophy_of_religion", "Theology", "Religion", "Thomas_Aquinas"],
    unsure=[])

print("w2 part1 loaded", len(PAGES))

add(slug="Mysticism", title="Mysticism",
    infobox=[("Field", "Religion / spirituality"), ("Focus", "Direct experiential union or communion with ultimate reality"), ("Traditions", "Christian mysticism, Sufism, Kabbalah, Hindu and Buddhist contemplative paths")],
    img="A shaft of light falling through darkness onto a meditating figure",
    lead="<b>Mysticism</b> is the pursuit and experience of direct, unmediated communion with ultimate reality — often described as union with God or the absolute — reported across the world's religions. Mystics such as Meister Eckhart, Teresa of Ávila, Ibn Arabi and the authors of the Upanishads describe states transcending ordinary subject–object awareness, frequently declared ineffable and paradoxical.",
    sections=[("Study", "<p>William James's <i>Varieties of Religious Experience</i> (1902) catalogued mystical states by four marks — ineffability, noetic quality, transiency, passivity — and perennialists (Aldous Huxley) claimed a common core across traditions, while constructivists (Steven Katz) argue experience is always shaped by prior concepts. Mystical practice — meditation, contemplation, dhikr, hesychasm — is cultivated within most major traditions, sometimes eyed warily by their authorities.</p>")],
    seealso=["Sufism", "Religion", "Meditation", "Upanishads"],
    outgoing=["Sufism", "Religion", "Upanishads", "Philosophy_of_religion"],
    unsure=[])

add(slug="Rumi", title="Rumi",
    infobox=[("Born", "30 September 1207, Balkh (or Wakhsh)"), ("Died", "17 December 1273, Konya, Seljuk Sultanate of Rum"), ("Known for", "Masnavi; Divan of Shams; founder-figure of the Mevlevi Sufi order"), ("Also known as", "Jalal ad-Din Muhammad Rumi; Mevlana")],
    img="A Persian miniature painting of Rumi and Shams Tabrizi in conversation",
    lead="<b>Jalāl ad-Dīn Muhammad Rūmī</b> (1207–1273), known simply as <b>Rumi</b>, was a Persian Sufi mystic and poet whose works are among the most beloved in world literature. His six-volume <i>Masnavi</i> — didactic stories in rhyming couplets exploring divine love — has been called 'the Quran in Persian', and his lyrical <i>Divan</i>, dedicated to his transformative friend Shams Tabrizi, made him, in modern translation (notably Coleman Barks's versions), reputedly the best-selling poet in the United States.",
    sections=[("Life", "<p>Born in Balkh, Rumi migrated with his family across the Muslim world ahead of the Mongol invasions, settling in Konya. A respected scholar-teacher, he was transformed in 1244 by meeting the wandering dervish Shams Tabrizi; Shams's disappearance (and presumed murder) plunged Rumi into grief and poetry. After his death his son Sultan Walad organised the Mevlevi order, the 'whirling dervishes'. His shrine in Konya remains a place of pilgrimage; his funeral was attended by mourners of every faith in the city.</p>")],
    seealso=["Sufism", "Islam", "Mysticism", "Poetry"],
    outgoing=["Sufism", "Islam", "Mysticism", "Religion"],
    unsure=["Birthplace (Balkh vs Wakhsh) disputed; 'best-selling poet' claim is a commonly repeated publishing factoid"])

add(slug="Scholasticism", title="Scholasticism",
    infobox=[("Era", "c. 1100–1700"), ("Centres", "Medieval universities: Paris, Oxford, Bologna"), ("Key figures", "Anselm, Abelard, Albertus Magnus, Thomas Aquinas, Duns Scotus, William of Ockham"), ("Method", "Quaestio: objections, sed contra, response, replies")],
    img="Medieval scholars disputing in a university hall, from a manuscript illumination",
    lead="<b>Scholasticism</b> is the system of theology and philosophy taught in the medieval European universities, characterised by rigorous dialectical method: a question is posed, objections marshalled, an authoritative counter-text cited (<i>sed contra</i>), a determination given, and each objection answered in turn. Its monuments are the summae of " + L("Thomas_Aquinas") + " and the commentaries on Peter Lombard's <i>Sentences</i> and on " + L("Aristotle") + ".",
    sections=[("Development", "<p>Fed by translations of Aristotle, Avicenna and " + L("Averroes") + " from Arabic, scholasticism integrated faith and reason at the new universities. Franciscan (Scotus) and Dominican (Thomist) schools diverged over universals, individuation and the will; nominalists like William of Ockham unsettled the synthesis. Long derided by humanists and early moderns as hair-splitting, it is now studied as a sophisticated research culture that invented much of the university's intellectual machinery.</p>")],
    seealso=["Thomas_Aquinas", "Averroes", "Aristotle", "Theology"],
    outgoing=["Thomas_Aquinas", "Averroes", "Maimonides", "Aristotle", "Theology", "Philosophy"],
    unsure=[])

add(slug="Islamic_philosophy", title="Islamic philosophy",
    infobox=[("Era", "9th century – present"), ("Key figures", "Al-Kindi, Al-Farabi, Avicenna, Al-Ghazali, Averroes, Mulla Sadra"), ("Centres", "Baghdad, Córdoba, Persia")],
    img="Scholars working in the House of Wisdom, Baghdad, from a manuscript painting",
    lead="<b>Islamic philosophy</b> (<i>falsafa</i>) is the tradition of philosophical inquiry in the Islamic world, beginning with the Graeco-Arabic translation movement centred on Abbasid Baghdad's House of Wisdom. Thinkers such as al-Kindi, al-Farabi and Avicenna (Ibn Sina) developed Aristotelian and Neoplatonic systems of extraordinary sophistication; " + L("Al-Ghazali") + "'s theological critique and " + L("Averroes") + "'s rejoinder define its classic debate, and its transmission to Latin Europe transformed scholasticism.",
    sections=[("Major themes", "<p>Central problems included the eternity versus creation of the world, the nature of the intellect and soul, prophecy, and God's knowledge of particulars. Avicenna's 'flying man' thought experiment (self-awareness without senses) and his essence–existence distinction influenced thinkers from Aquinas to Descartes. The tradition continued vigorously in Persia (Suhrawardi's Illuminationism, Mulla Sadra) even where it waned in the Arab west.</p>")],
    seealso=["Averroes", "Al-Ghazali", "Islam", "Thomas_Aquinas"],
    outgoing=["Averroes", "Al-Ghazali", "Islam", "Thomas_Aquinas", "Scholasticism", "Philosophy"],
    unsure=[])

add(slug="Jewish_philosophy", title="Jewish philosophy",
    infobox=[("Era", "Hellenistic period – present"), ("Key figures", "Philo, Saadia Gaon, Maimonides, Spinoza (by origin), Buber, Levinas")],
    img="The title page of an early printed edition of Maimonides' Guide for the Perplexed",
    lead="<b>Jewish philosophy</b> is the engagement of Jewish thinkers with general philosophical questions and the philosophical interpretation of Judaism, running from Philo of Alexandria's allegorical fusion of Torah and Plato through the medieval rationalism of Saadia Gaon and " + L("Maimonides") + " to modern figures such as Martin Buber (<i>I and Thou</i>), Franz Rosenzweig and Emmanuel Levinas.",
    sections=[("Themes", "<p>Recurring questions include creation versus eternity, divine attributes and negative theology, the reasons for the commandments, election and universalism, theodicy after catastrophe — searingly after the Holocaust — and the relation of halakha (law) to ethics. Kabbalah offered a theosophical counterpoint to rationalism, and the two currents repeatedly fertilised each other.</p>")],
    seealso=["Maimonides", "Judaism", "Baruch_Spinoza", "Theology"],
    outgoing=["Maimonides", "Judaism", "Baruch_Spinoza", "Theology", "Philosophy"],
    unsure=[])

add(slug="Mencius", title="Mencius",
    infobox=[("Born", "372 BC, State of Zou, China"), ("Died", "289 BC"), ("School", "Confucianism"), ("Notable work", "Mencius (Mengzi), one of the Four Books"), ("Also known as", "Mengzi; 'Second Sage'")],
    img="A traditional portrait of Mencius in scholar's robes",
    lead="<b>Mencius</b> (372–289 BC), known in Chinese as <b>Mengzi</b>, was a Chinese Confucian philosopher, the most famous after " + L("Confucius") + " himself and honoured as the 'Second Sage'. The book bearing his name records his dialogues with kings and rival thinkers, defending Confucius's teaching with the doctrine that human nature is innately good: everyone has 'sprouts' of virtue — compassion, shame, deference, approval/disapproval — that need only cultivation, as shown by the spontaneous alarm anyone feels seeing a child about to fall into a well.",
    sections=[("Political thought", "<p>Mencius taught that the people are the most important element in a state, the ruler the least; a king who mutilates benevolence and righteousness is a 'mere fellow' whose removal is not regicide — a justification of rebellion that made his book suspect to autocrats (the Ming founder tried to censor it). His mother, who moved house three times for his education, is a Chinese cultural icon of parenting.</p>")],
    seealso=["Confucianism", "Confucius", "Analects"],
    outgoing=["Confucianism", "Confucius", "Analects", "Philosophy"],
    unsure=["Dates conventional (372–289 BC)"])

add(slug="Zhuangzi", title="Zhuangzi",
    infobox=[("Born", "c. 369 BC, Meng, China"), ("Died", "c. 286 BC"), ("School", "Taoism"), ("Notable work", "Zhuangzi (the 'Inner Chapters' attributed to him)")],
    img="A Chinese painting of Zhuangzi dreaming he is a butterfly",
    lead="<b>Zhuangzi</b> (c. 369 – c. 286 BC), also known as Zhuang Zhou, was an influential Chinese philosopher of the Warring States period and, with " + L("Laozi") + ", a founder of " + L("Taoism") + ". The book named after him — part philosophy, part fantastical anecdote — is among the most playful and profound in world literature: Zhuangzi dreamed he was a butterfly, and on waking could not tell whether he was a man who had dreamed of being a butterfly, or a butterfly now dreaming it is a man.",
    sections=[("Thought", "<p>Zhuangzi relativises human distinctions — life and death, big and small, this and that — urging free wandering (<i>xiaoyao you</i>) in accord with the transformations of the Tao. He satirised Confucian moralising and the ambition of rulers, refused office ('I would rather drag my tail in the mud'), and praised uselessness: the gnarled tree survives because no one can use it. His sceptical, perspectival writing influenced Chinese Buddhism and all later East Asian aesthetics.</p>")],
    seealso=["Taoism", "Laozi", "Tao_Te_Ching", "Confucianism"],
    outgoing=["Taoism", "Laozi", "Tao_Te_Ching", "Confucianism", "Philosophy"],
    unsure=["Dates approximate; text layered with later chapters"])

add(slug="I_Ching", title="I Ching",
    infobox=[("Also known as", "Book of Changes; Yi Jing"), ("Language", "Chinese"), ("Date", "Core text c. 9th century BC; commentaries ('Ten Wings') later"), ("Use", "Divination by yarrow stalks or coins; philosophy of change")],
    img="A diagram of the 64 hexagrams of the I Ching arranged in a circle",
    lead="The <i><b>I Ching</b></i> (<i>Book of Changes</i>) is an ancient Chinese divination manual and one of the oldest Chinese classics. Its core consists of 64 hexagrams — figures of six broken and unbroken lines — each with cryptic judgements and line texts, consulted traditionally by casting yarrow stalks or coins. Appended commentaries, the 'Ten Wings' traditionally ascribed to " + L("Confucius") + ", transformed it into a philosophy of change, yin and yang, and timely action, studied by scholars and rulers for over two millennia.",
    sections=[("Influence", "<p>The <i>I Ching</i> structured Chinese cosmology alongside " + L("Confucianism") + " and " + L("Taoism") + "; Leibniz, receiving its hexagram order from China, saw in it a confirmation of binary arithmetic, and C. G. Jung's foreword to the Wilhelm translation made it famous in the West as a vehicle of 'synchronicity'. It remains in daily use as a book of wisdom and oracle.</p>")],
    seealso=["Confucianism", "Taoism", "Yin_and_yang", "Confucius"],
    outgoing=["Confucianism", "Taoism", "Yin_and_yang", "Confucius", "Philosophy"],
    unsure=["Confucius's authorship of the Wings is traditional, not historical consensus"])

add(slug="Upanishads", title="Upanishads",
    infobox=[("Tradition", "Hinduism (Shruti)"), ("Language", "Sanskrit"), ("Date", "Principal Upanishads composed c. 800–200 BC"), ("Core concepts", "Atman (self), Brahman (ultimate reality), moksha, karma, samsara")],
    img="An ancient palm-leaf manuscript of Sanskrit text",
    lead="The <b>Upanishads</b> are late Vedic Sanskrit texts of religious teaching and philosophical speculation, forming the concluding part of the Vedas ('Vedanta' = 'end of the Veda') and the foundation of " + L("Hinduism") + "'s philosophy. In dialogues between teachers and students they teach that Atman, the inmost self, is identical with Brahman, the ground of all reality — 'That thou art' (<i>tat tvam asi</i>) — and that realising this identity liberates one from rebirth.",
    sections=[("Influence", "<p>Of more than 200 Upanishads, about a dozen 'principal' ones are earliest and most authoritative, commented on by Shankara and every Vedanta school. Arthur Schopenhauer read a Latin translation nightly and called them 'the consolation of my life and of my death'; they influenced modern figures from Yeats to Schrödinger, and remain Hinduism's most philosophical layer, shifting religion from ritual sacrifice toward interior knowledge.</p>")],
    seealso=["Hinduism", "Karma", "Moksha", "Arthur_Schopenhauer"],
    outgoing=["Hinduism", "Karma", "Moksha", "Arthur_Schopenhauer", "Religion"],
    unsure=[])

add(slug="Moksha", title="Moksha",
    infobox=[("Traditions", "Hinduism, Jainism, Sikhism (as mukti)"), ("Meaning", "Liberation from samsara, the cycle of rebirth")],
    img="A lotus flower opening at sunrise, symbolising liberation and awakening",
    lead="<b>Moksha</b> (Sanskrit: 'release, liberation') is the final release from <i>samsara</i>, the cycle of birth, death and rebirth, in " + L("Hinduism") + ", " + L("Jainism") + " and " + L("Sikhism") + ". In Hindu thought it is the fourth and highest aim of life (after dharma, artha and kama), attained through self-knowledge, devotion or disciplined action, when the soul recognises its true nature and is no longer bound by " + L("Karma") + ".",
    sections=[("Paths", "<p>The Bhagavad Gita integrates three paths: knowledge (jnana), devotion (bhakti) and selfless action (karma yoga). Vedanta schools dispute the result's nature — for Advaita, total identity of self and Brahman; for Dvaita, eternal loving distinction. Jain moksha is the soul's ascent to the top of the universe after all karma is shed; Sikh mukti is union with God through devotion and grace while living righteously in the world.</p>")],
    seealso=["Karma", "Hinduism", "Nirvana", "Reincarnation", "Upanishads"],
    outgoing=["Karma", "Hinduism", "Jainism", "Sikhism", "Nirvana", "Reincarnation", "Upanishads"],
    unsure=[])

add(slug="Nirvana", title="Nirvana",
    infobox=[("Traditions", "Buddhism, Hinduism, Jainism"), ("Meaning", "Extinction of craving and suffering; awakening; liberation")],
    img="A serene Buddha statue at dawn with soft light, evoking nirvana",
    lead="<b>Nirvana</b> (Sanskrit <i>nirvāṇa</i>, 'blowing out') is the ultimate goal of " + L("Buddhism") + ": the extinction of the fires of greed, hatred and delusion, the end of suffering (<i>dukkha</i>) and of rebirth. The Buddha taught it as attainable in this life through the Noble Eightfold Path; his own final passing into <i>parinirvana</i> at death ended all remaining conditions of existence. What nirvana is positively like, the Buddha characteristically left in large part unsaid — it is not annihilation, since there is no permanent self to annihilate.",
    sections=[("Interpretations", "<p>Theravada emphasises the arhat's nirvana; Mahayana exalts the bodhisattva who postpones final entry to liberate all beings, and in some schools (notably with Buddha-nature teaching) nirvana and samsara are declared non-dual. In the West the word entered popular culture — and a famous band name — as shorthand for blissful peace, a loose borrowing from its precise soteriological sense.</p>")],
    seealso=["Buddhism", "Karma", "Moksha", "Reincarnation"],
    outgoing=["Buddhism", "Karma", "Moksha", "Reincarnation", "Religion"],
    unsure=[])

add(slug="Reincarnation", title="Reincarnation",
    infobox=[("Traditions", "Hinduism, Buddhism, Jainism, Sikhism; also many indigenous and new religious movements"), ("Related concepts", "Samsara, karma, moksha/nirvana"), ("Also known as", "Metempsychosis; transmigration; rebirth")],
    img="A circular mosaic depicting the wheel of life with its six realms of rebirth",
    lead="<b>Reincarnation</b> is the religious or philosophical belief that the soul or consciousness, after death, begins a new life in a new body. It is central to the Indian religions — " + L("Hinduism") + ", " + L("Buddhism") + ", " + L("Jainism") + ", " + L("Sikhism") + " — where rebirth within <i>samsara</i> is governed by " + L("Karma") + " and liberation from the wheel is the ultimate goal. Versions appear in Greek thought (Pythagoras, Plato's Myth of Er), some indigenous traditions worldwide, and modern Theosophy and New Age movements.",
    sections=[("Variations and study", "<p>Buddhist rebirth explicitly denies a permanent soul, explaining continuity by causal process rather than an entity that migrates — a subtlety often missed in popular accounts. Western researchers such as Ian Stevenson collected children's reports of past-life memories, findings mainstream science treats cautiously; meanwhile belief in reincarnation polls surprisingly high even in historically Christian countries.</p>")],
    seealso=["Karma", "Moksha", "Nirvana", "Hinduism", "Buddhism"],
    outgoing=["Karma", "Moksha", "Nirvana", "Hinduism", "Buddhism", "Jainism", "Sikhism", "Plato"],
    unsure=["Poll figures for Western belief intentionally left general"])

add(slug="Kami", title="Kami",
    infobox=[("Tradition", "Shinto (Japan)"), ("Nature", "Spirits/deities of places, natural phenomena, ancestors and concepts"), ("Notable kami", "Amaterasu (sun), Susanoo (storm), Inari (rice/foxes), Hachiman (war)")],
    img="A small wooden Shinto shrine in a forest, hung with sacred shimenawa rope",
    lead="<b>Kami</b> are the spirits worshipped in Japan's " + L("Shinto") + " tradition. The word is often translated 'gods' or 'deities', but kami range from great mythological beings such as Amaterasu, the sun goddess, to the spirits of particular mountains, rivers, trees, rocks, ancestors, and even revered persons and natural forces. An old phrase speaks of <i>yaoyorozu no kami</i> — 'eight million kami' — meaning an innumerable host.",
    sections=[("Veneration", "<p>Kami are enshrined in shrines (<i>jinja</i>) where a sacred object (<i>shintai</i>) houses their presence; worship aims at purity, gratitude, and requests for blessing rather than doctrine or moral command. The syncretic history with Buddhism made many kami also guardians or manifestations of buddhas, a fusion largely (but never completely) undone in the Meiji separation edicts of 1868.</p>")],
    seealso=["Shinto", "Animism", "Japan"],
    outgoing=["Shinto", "Animism", "Religion", "Japan"],
    unsure=[])

add(slug="Animism", title="Animism",
    infobox=[("Field", "Anthropology of religion"), ("Term coined/used by", "E. B. Tylor, Primitive Culture (1871)"), ("Core idea", "Spirits inhabit natural objects, places and beings")],
    img="Carved totem poles against a Pacific Northwest forest, representing ancestral spirits",
    lead="<b>Animism</b> (from Latin <i>anima</i>, 'soul, spirit') is the belief that objects, places and creatures possess distinct spiritual essences. The anthropologist E. B. Tylor made it the centrepiece of his theory of religion's origin in <i>Primitive Culture</i> (1871): from dreams and death, early humans inferred souls, then spirits everywhere. Long treated by scholars as a 'primitive' stage, animism is now studied more respectfully as a relational ontology — prominent in many Indigenous traditions and in Japan's " + L("Shinto") + " — in which personhood extends beyond humans.",
    sections=[("New animism", "<p>Contemporary anthropologists (Nurit Bird-David, Philippe Descola) describe animist worlds as webs of social relations with non-human persons, challenging the nature/culture split. Elements of animist sensibility appear in modern environmental ethics and in philosophical panpsychism's revival.</p>")],
    seealso=["Shinto", "Kami", "Religion", "Folklore"],
    outgoing=["Shinto", "Kami", "Religion", "Folklore"],
    unsure=[])

add(slug="Agnosticism", title="Agnosticism",
    infobox=[("Field", "Philosophy of religion / epistemology"), ("Term coined by", "Thomas Henry Huxley (1869)"), ("Position", "The existence of God is unknown or unknowable")],
    img="A question mark formed by clouds in a twilight sky",
    lead="<b>Agnosticism</b> is the view that the existence of God, or of the divine and supernatural generally, is unknown or unknowable. The word was coined by the biologist Thomas Henry Huxley in 1869 for a method as much as a creed: follow reason as far as it goes and do not pretend conclusions are certain when they are not demonstrated. In contemporary taxonomy (popularised by " + L("Atheism", "Dawkins") + ") belief and knowledge are separated: one may be an agnostic atheist (no belief, no claim to know) or an agnostic theist.",
    sections=[("Forms", "<p>Weak agnosticism suspends judgement for want of evidence; strong agnosticism holds the question unanswerable in principle; agnostic theism and 'apatheism' mark further positions. As a self-description in surveys, agnosticism has grown steadily in Western countries alongside the religiously unaffiliated 'nones'.</p>")],
    seealso=["Atheism", "Philosophy_of_religion", "Secularism"],
    outgoing=["Atheism", "Philosophy_of_religion", "Secularism", "Religion"],
    unsure=[])

add(slug="Phenomenology", title="Phenomenology",
    infobox=[("Field", "Philosophy"), ("Founder", "Edmund Husserl"), ("Key figures", "Martin Heidegger, Maurice Merleau-Ponty, Jean-Paul Sartre"), ("Slogan", "'Back to the things themselves'")],
    img="A hand reaching toward light through mist, suggesting experience as it appears",
    lead="<b>Phenomenology</b> is a philosophical movement founded by Edmund Husserl around 1900 that studies the structures of experience as experienced from the first-person point of view. Its method — 'back to the things themselves' — brackets assumptions about the external world (<i>epoché</i>) to describe how phenomena appear to consciousness, whose essential mark is intentionality: consciousness is always consciousness <i>of</i> something.",
    sections=[("Development", "<p>Husserl's student Martin Heidegger transformed phenomenology into fundamental ontology in <i>Being and Time</i> (1927), analysing human existence (Dasein) through care, anxiety and being-toward-death. Maurice Merleau-Ponty centred the lived body; " + L("Jean-Paul_Sartre") + " and " + L("Simone_de_Beauvoir") + " carried it into existentialism and ethics. It remains influential in philosophy of mind, cognitive science (embodied approaches) and qualitative research methods.</p>")],
    seealso=["Existentialism", "Jean-Paul_Sartre", "Simone_de_Beauvoir", "Philosophy_of_mind"],
    outgoing=["Existentialism", "Jean-Paul_Sartre", "Simone_de_Beauvoir", "Philosophy_of_mind", "Philosophy"],
    unsure=[])

add(slug="Analytic_philosophy", title="Analytic philosophy",
    infobox=[("Field", "Philosophy"), ("Origins", "Cambridge and Vienna, early 20th century"), ("Key figures", "Gottlob Frege, Bertrand Russell, G. E. Moore, Ludwig Wittgenstein, W. V. O. Quine")],
    img="A page of Frege's Begriffsschrift with its two-dimensional logical notation",
    lead="<b>Analytic philosophy</b> is the dominant tradition of academic philosophy in the English-speaking world and much of northern Europe, characterised by emphasis on clarity, argument and the analysis of language and concepts. It arose around 1900 with Frege's logic, " + L("Bertrand_Russell") + "'s theory of descriptions, Moore's defence of common sense, and the early " + L("Ludwig_Wittgenstein") + ", and passed through logical positivism and ordinary-language philosophy into today's pluralistic mainstream.",
    sections=[("Themes", "<p>Analytic philosophy is a style more than a doctrine: its practitioners work on mind, language, metaphysics, ethics and science with formal tools where useful. Its supposed opposite, 'continental philosophy' (phenomenology, existentialism, post-structuralism), marks a sociological divide that recent decades have made more porous.</p>")],
    seealso=["Ludwig_Wittgenstein", "Bertrand_Russell", "Logic", "Philosophy_of_language"],
    outgoing=["Ludwig_Wittgenstein", "Bertrand_Russell", "Logic", "Philosophy_of_language", "Phenomenology"],
    unsure=[])

add(slug="Philosophy_of_language", title="Philosophy of language",
    infobox=[("Field", "Philosophy"), ("Key topics", "Meaning, reference, truth, speech acts"), ("Key figures", "Frege, Russell, Wittgenstein, Austin, Grice, Kripke")],
    img="Speech bubbles containing symbols and pictures, representing meaning and reference",
    lead="<b>Philosophy of language</b> studies the nature of language, meaning and reference, and language's relation to mind and world. Central questions include how words refer (Frege's distinction between sense and reference — 'morning star' and 'evening star'), how sentences get truth-values, what speakers <i>do</i> with words (J. L. Austin's speech acts), and how conversation works beyond literal meaning (H. P. Grice's implicature).",
    sections=[("Turns and figures", "<p>The 'linguistic turn' made language philosophy's central medium: " + L("Ludwig_Wittgenstein") + "'s later work dissolved traditional problems into language-games, while Saul Kripke's <i>Naming and Necessity</i> (1972 lectures) revived metaphysics within the analytic mainstream by distinguishing rigid designators and necessary a posteriori truths.</p>")],
    seealso=["Analytic_philosophy", "Ludwig_Wittgenstein", "Logic"],
    outgoing=["Analytic_philosophy", "Ludwig_Wittgenstein", "Logic", "Philosophy"],
    unsure=[])

add(slug="Natural_law", title="Natural law",
    infobox=[("Field", "Ethics / legal philosophy"), ("Key figures", "Thomas Aquinas; Hugo Grotius; John Locke (natural rights)"), ("Core claim", "Moral principles are grounded in nature/reason and bind all positive law")],
    img="A stone tablet carved with scales, symbolising law written into nature",
    lead="<b>Natural law</b> is a theory in ethics and jurisprudence that certain values and rights are inherent in human nature and the order of the world, knowable by reason, and provide a standard against which human ('positive') law is judged. " + L("Thomas_Aquinas") + " systematised it as rational creatures' participation in God's eternal law: its first precept is that good is to be done and evil avoided, from which practical reason derives the goods of life, procreation, knowledge and society.",
    sections=[("Legacy", "<p>Through Grotius and " + L("John_Locke") + ", natural-law ideas fed the doctrine of natural rights and modern human-rights law; the Nuremberg tribunals' appeal to laws above statutes revived the tradition against legal positivism. Contemporary 'new natural law' theorists (John Finnis) remain influential, and disputed, in debates on law and morality.</p>")],
    seealso=["Thomas_Aquinas", "Ethics", "John_Locke", "Scholasticism"],
    outgoing=["Thomas_Aquinas", "Ethics", "John_Locke", "Scholasticism", "Philosophy"],
    unsure=[])

add(slug="Social_contract", title="Social contract",
    infobox=[("Field", "Political philosophy"), ("Key figures", "Thomas Hobbes, John Locke, Jean-Jacques Rousseau, John Rawls"), ("Core idea", "Political authority rests on (actual or hypothetical) consent of the governed")],
    img="Citizens gathered to sign a foundational charter document",
    lead="The <b>social contract</b> is a model in moral and political philosophy: individuals in a 'state of nature' surrender some freedoms to a sovereign or society in exchange for security and rights, so that legitimate authority rests on consent. Hobbes's <i>Leviathan</i> (1651) made the contract nearly absolute to escape a life 'solitary, poor, nasty, brutish, and short'; " + L("John_Locke") + " made government conditional and revocable; Rousseau recast it as the general will.",
    sections=[("Modern forms", "<p>John Rawls's <i>A Theory of Justice</i> (1971) revived contract thinking with the 'original position' behind a veil of ignorance. Critics note historical contracts never happened and that actual societies' membership is unchosen; contractarians answer that the model is a device of representation, testing whether principles could be reasonably endorsed.</p>")],
    seealso=["John_Locke", "Liberalism", "Ethics"],
    outgoing=["John_Locke", "Liberalism", "Ethics", "Philosophy"],
    unsure=[])

add(slug="Enlightenment", title="Age of Enlightenment",
    infobox=[("Period", "17th–18th centuries"), ("Key figures", "Kant, Locke, Voltaire, Hume, Diderot, Montesquieu, Rousseau"), ("Motto (Kant)", "'Sapere aude' — dare to know")],
    img="An 18th-century Parisian salon where philosophers debate by candlelight",
    lead="The <b>Age of Enlightenment</b> was an intellectual and philosophical movement that dominated Europe in the 17th and 18th centuries, exalting reason, science, individual liberty and toleration against tradition and religious authority. " + L("Immanuel_Kant") + "'s 1784 essay defined it as humanity's emergence from self-imposed immaturity: <i>Sapere aude</i> — dare to use your own understanding. Its vehicles were salons, coffeehouses, academies and Diderot's great <i>Encyclopédie</i>.",
    sections=[("Legacy and critique", "<p>Enlightenment ideas undergird modern democracy, human rights, the separation of powers (Montesquieu) and scientific institutions; they also coexisted with, and were used to justify, colonialism and hierarchies of race and sex that its own universalism later helped to attack. Adorno and Horkheimer's <i>Dialectic of Enlightenment</i> (1944) indicted instrumental reason; postcolonial and feminist scholarship continues to contest and reclaim its promises.</p>")],
    seealso=["Immanuel_Kant", "John_Locke", "David_Hume", "Philosophy"],
    outgoing=["Immanuel_Kant", "John_Locke", "David_Hume", "Philosophy", "Rationalism", "Empiricism"],
    unsure=["Period boundaries conventional"])

print("w2 part2 loaded", len(PAGES))

# ---------------- BUILD (same as wave 1) ----------------
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
                        "unsure": ["Page already existed on disk when wave 2 ran"], "outgoing": [url_of(s) for s in p.get("outgoing", [])]})
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
