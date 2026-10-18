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

# ---------------- PHILOSOPHY: CORE BRANCHES ----------------
add(slug="Metaphysics", title="Metaphysics",
    infobox=[("Branch", "Philosophy"), ("Parent", "Philosophy"), ("Key topics", "Being, existence, causality, time, mind")],
    img="A diagram of Aristotle's categories and the branches of metaphysics (ontology, cosmology, theology)",
    lead="<b>Metaphysics</b> is the branch of " + L("Philosophy") + " that investigates the fundamental nature of reality, including the relationship between mind and matter, substance and attribute, and potentiality and actuality. Its name derives from the Greek <i>meta ta physika</i> ('after the Physics'), the title given to works of " + L("Aristotle") + " placed after his writings on physics. Central questions include what exists (ontology), what kinds of things exist, how objects persist through change, the nature of time and space, and whether the will is free.",
    sections=[
      ("History", "<p>Metaphysical speculation begins in the West with the Pre-Socratic philosophers, who sought the underlying <i>arche</i> (principle) of all things. " + L("Plato") + " located reality in eternal Forms, while Aristotle grounded it in substances and their forms and matter. Medieval thinkers such as " + L("Thomas_Aquinas") + " fused Aristotelian metaphysics with Christian theology. In the early modern period, " + L("René_Descartes", "Descartes") + " split reality into thinking and extended substance, " + L("Baruch_Spinoza", "Spinoza") + " argued for a single substance, and " + L("Immanuel_Kant") + " held that metaphysics must be limited by the conditions of possible experience.</p><p>In the 20th century, logical positivists dismissed much traditional metaphysics as meaningless, but the field revived in analytic philosophy through work by figures such as W. V. O. Quine and Saul Kripke on modality, identity and possible worlds.</p>"),
      ("Central problems", "<p>Core problems include the mind–body problem, free will, the nature of universals, causation, personal identity over time, and the existence and nature of God, treated by philosophical theology. Ontology, the sub-field concerned with what there is, asks whether abstract objects such as numbers exist and how categories of being are structured.</p>"),
    ],
    seealso=["Ontology", "Philosophy_of_mind", "Free_will", "Causality"],
    outgoing=["Philosophy", "Aristotle", "Plato", "Thomas_Aquinas", "René_Descartes", "Baruch_Spinoza", "Immanuel_Kant", "Ontology", "Philosophy_of_mind", "Free_will", "Causality"],
    unsure=["Exact etymology date of the term's editorial origin in Andronicus of Rhodes' edition is approximate"])

add(slug="Ontology", title="Ontology",
    infobox=[("Branch", "Metaphysics"), ("Key topics", "Being, existence, categories, universals")],
    img="A tree diagram of categories of being, from substance down to particular objects",
    lead="<b>Ontology</b> is the philosophical study of being — what exists, and how the things that exist can be grouped and related. It is traditionally listed as a part of the major branch of " + L("Philosophy") + " known as " + L("Metaphysics") + ". Ontologists ask whether entities such as properties, numbers, fictional characters and possible objects genuinely exist, and what the most fundamental categories of reality are.",
    sections=[
      ("History", "<p>The term was coined in the early 17th century from the Greek <i>on</i> (being) and <i>logos</i> (study). " + L("Aristotle") + " had already described the inquiry as the study of 'being qua being'. Medieval scholastics elaborated hierarchies of being, while " + L("René_Descartes", "Descartes") + " and later " + L("Immanuel_Kant") + " reframed the questions. In the 20th century W. V. O. Quine made ontological commitment — what a theory says exists — a standard analytic tool with his criterion 'to be is to be the value of a bound variable'.</p>"),
      ("Questions", "<p>Typical questions include: What is existence? Do abstract objects exist independently of minds (realism) or not (nominalism)? What is an object, and how do parts relate to wholes (mereology)? Debates also cover social ontology — the existence of groups, institutions and money — and applied ontology in information science, where the word names formal specifications of concepts in a domain.</p>"),
    ],
    seealso=["Metaphysics", "Nominalism", "Realism_(philosophy)", "Mereology"],
    outgoing=["Metaphysics", "Philosophy", "Aristotle", "René_Descartes", "Immanuel_Kant", "Nominalism", "Realism_(philosophy)", "Mereology"],
    unsure=["Year of coinage of 'ontologia' (Lorhard 1606 / Goclenius 1613) differs between sources"])

add(slug="Epistemology", title="Epistemology",
    infobox=[("Branch", "Philosophy"), ("Key topics", "Knowledge, belief, justification, scepticism")],
    img="A diagram contrasting rationalism and empiricism as sources of knowledge",
    lead="<b>Epistemology</b> is the branch of " + L("Philosophy") + " concerned with knowledge: its nature, sources, structure and limits. Epistemologists ask what knowledge is, how it differs from mere true belief, how beliefs are justified, and whether sceptical challenges — the possibility that we are deceived about everything — can be answered. The classical analysis defined knowledge as justified true belief, a definition famously challenged by Edmund Gettier in 1963.",
    sections=[
      ("Sources of knowledge", "<p>Perception, memory, introspection, testimony and reasoning are the standard candidate sources. Rationalists such as " + L("René_Descartes", "Descartes") + " and " + L("Gottfried_Wilhelm_Leibniz", "Leibniz") + " emphasised a priori reasoning independent of experience; empiricists such as " + L("John_Locke") + ", " + L("George_Berkeley") + " and " + L("David_Hume") + " held that knowledge derives ultimately from sense experience. " + L("Immanuel_Kant") + " sought a synthesis, arguing that the mind actively structures experience through innate categories.</p>"),
      ("Scepticism and the Gettier problem", "<p>Descartes' method of doubt imagined a deceiving demon to test which beliefs survive radical scepticism. Hume argued that induction — inference from past to future — cannot be rationally justified. In 1963 Gettier published counterexamples in which a belief is true and justified yet intuitively not knowledge, prompting decades of work on a fourth condition or alternative accounts such as reliabilism.</p>"),
    ],
    seealso=["Philosophy_of_science", "Scepticism", "Rationalism", "Empiricism", "Gettier_problem"],
    outgoing=["Philosophy", "René_Descartes", "Gottfried_Wilhelm_Leibniz", "John_Locke", "George_Berkeley", "David_Hume", "Immanuel_Kant", "Philosophy_of_science", "Scepticism", "Rationalism", "Empiricism", "Gettier_problem"],
    unsure=["Gettier paper details (Is Justified True Belief Knowledge?, Analysis 1963) recalled from memory"])

add(slug="Aesthetics", title="Aesthetics",
    infobox=[("Branch", "Philosophy"), ("Key topics", "Beauty, art, taste, the sublime")],
    img="Visitors contemplating paintings in a grand art gallery hall",
    lead="<b>Aesthetics</b> is the branch of " + L("Philosophy") + " that studies beauty, art, taste and aesthetic experience and judgement. The word derives from the Greek <i>aisthetikos</i> (of sense perception); the German philosopher Alexander Baumgarten gave it its modern philosophical use in the 18th century. Key questions include what makes something beautiful or sublime, whether aesthetic judgements are objective or subjective, and how art should be defined.",
    sections=[
      ("History", "<p>" + L("Plato") + " distrusted art as imitation at two removes from truth, while " + L("Aristotle") + " defended poetry and tragedy in the <i>Poetics</i>. " + L("Immanuel_Kant") + ", in the <i>Critique of Judgment</i> (1790), analysed judgements of beauty as 'disinterested' pleasure claiming universal assent, and distinguished the beautiful from the sublime. Later thinkers — from Arthur Schopenhauer to the pragmatists and analytic philosophers — debated expression, representation and the institutional definition of art.</p>"),
      ("Theories of art", "<p>Major approaches define art by representation (mimesis), by expression of emotion, by formal properties, or by the conventions of the 'artworld' (Arthur Danto, George Dickie). Aesthetics also covers everyday aesthetic experience, nature, design and the ethics of art.</p>"),
    ],
    seealso=["Beauty", "Philosophy_of_art", "Sublime_(philosophy)", "Taste_(sociology)"],
    outgoing=["Philosophy", "Plato", "Aristotle", "Immanuel_Kant", "Beauty", "Philosophy_of_art", "Sublime_(philosophy)"],
    unsure=["Baumgarten dates for Aesthetica (1750) recalled approximately"])

add(slug="Philosophy_of_mind", title="Philosophy of mind",
    infobox=[("Branch", "Philosophy"), ("Key topics", "Consciousness, qualia, intentionality, personal identity")],
    img="An illustration of a human head with gears and light, representing the mind-body problem",
    lead="<b>Philosophy of mind</b> is the branch of " + L("Philosophy") + " that studies the nature of the mind, mental events and functions, consciousness, and their relationship to the body and brain. Its central issue is the mind–body problem: how can subjective experience — the felt quality of seeing red or feeling pain, called qualia — arise from physical processes?",
    sections=[
      ("Major positions", "<p>" + L("René_Descartes", "Descartes") + " defended substance dualism, holding mind and body to be distinct kinds of substance. 20th-century behaviourism tried to define mental states by behaviour; identity theory identified them with brain states; functionalism, associated with Hilary Putnam, defines them by causal role and underlies much of cognitive science and thinking about artificial intelligence. Eliminative materialists argue folk psychology will be replaced by neuroscience.</p>"),
      ("Consciousness", "<p>Thomas Nagel's 'What is it like to be a bat?' (1974) and David Chalmers' 'hard problem of consciousness' press the difficulty of explaining subjective experience physically. Thought experiments such as the Chinese room (John Searle) and philosophical zombies structure ongoing debate.</p>"),
    ],
    seealso=["Metaphysics", "Consciousness", "Dualism", "Functionalism_(philosophy_of_mind)", "Artificial_intelligence"],
    outgoing=["Philosophy", "René_Descartes", "Metaphysics", "Consciousness", "Dualism", "Artificial_intelligence"],
    unsure=["Attribution details of identity theory (Place, Smart) from memory"])

add(slug="Philosophy_of_religion", title="Philosophy of religion",
    infobox=[("Branch", "Philosophy"), ("Key topics", "Existence of God, faith and reason, problem of evil")],
    img="Silhouettes of world religious symbols arranged in a circle",
    lead="<b>Philosophy of religion</b> is the branch of " + L("Philosophy") + " that examines religious concepts and claims: the existence and attributes of God, the relationship between faith and reason, religious experience, miracles, and the problem of evil. It is distinct from theology in that it approaches these questions with philosophical methods open to any tradition, or none.",
    sections=[
      ("Arguments for God's existence", "<p>Classical arguments include the ontological argument of Anselm of Canterbury, the cosmological and teleological arguments systematised by " + L("Thomas_Aquinas") + " in his 'Five Ways', and design arguments revived in modern fine-tuning debates. " + L("Immanuel_Kant") + " judged all purely speculative proofs inconclusive while defending a practical, moral faith.</p>"),
      ("The problem of evil", "<p>The existence of suffering is pressed against belief in an omnipotent, wholly good God — a puzzle already posed in antiquity and sharpened by " + L("David_Hume") + " in his <i>Dialogues Concerning Natural Religion</i>. Responses include free-will defences (Alvin Plantinga) and soul-making theodicies (John Hick). Other topics include religious language, pluralism, and whether religious belief can be properly basic.</p>"),
    ],
    seealso=["Theology", "Problem_of_evil", "Ontological_argument", "Atheism"],
    outgoing=["Philosophy", "Religion", "Thomas_Aquinas", "Immanuel_Kant", "David_Hume", "Theology", "Problem_of_evil", "Ontological_argument", "Atheism"],
    unsure=[])

add(slug="Free_will", title="Free will",
    infobox=[("Branch", "Metaphysics / Ethics"), ("Key topics", "Determinism, compatibilism, moral responsibility")],
    img="A fork in a forest path symbolising choice between futures",
    lead="<b>Free will</b> is the capacity of agents to choose between different possible courses of action, closely tied to moral responsibility, praise and blame. Philosophy asks whether free will is compatible with determinism — the thesis that every event is necessitated by prior causes — and what kind of control genuine choice requires.",
    sections=[
      ("Positions", "<p>Compatibilists, following " + L("David_Hume") + " and modern writers such as Daniel Dennett, hold that freedom means acting on one's own desires without coercion, whether or not determinism is true. Libertarians about free will (not the political label) argue it requires genuine alternative possibilities or agent-causation. Hard determinists, such as Derk Pereboom, deny free will but debate how practices of responsibility should change. Thought experiments like Harry Frankfurt's cases challenge the idea that responsibility requires the ability to do otherwise.</p>"),
    ],
    seealso=["Determinism", "Metaphysics", "Moral_responsibility", "Compatibilism"],
    outgoing=["Metaphysics", "Ethics", "David_Hume", "Determinism", "Compatibilism", "Moral_responsibility"],
    unsure=[])

print("part1 loaded", len(PAGES))

# ---------------- PHILOSOPHERS ----------------
add(slug="René_Descartes", title="René Descartes",
    infobox=[("Born", "31 March 1596, La Haye en Touraine, France"), ("Died", "11 February 1650, Stockholm, Sweden"), ("Era", "17th-century philosophy"), ("Main interests", "Epistemology, metaphysics, mathematics"), ("Notable ideas", "Cogito ergo sum; Cartesian dualism; coordinate geometry")],
    img="A portrait of René Descartes with long dark hair and a white collar, after Frans Hals",
    lead="<b>René Descartes</b> (1596–1650) was a French philosopher, scientist and mathematician, often called the father of modern Western philosophy. In the <i>Meditations on First Philosophy</i> (1641) he subjected all his beliefs to methodical doubt, arriving at the indubitable <i>cogito ergo sum</i> — 'I think, therefore I am' — and building knowledge anew on that foundation. He argued that mind and body are distinct substances, a view known as Cartesian dualism.",
    sections=[
      ("Life", "<p>Descartes was educated by Jesuits at La Flèche and studied law at Poitiers before travelling as a gentleman soldier. Settling in the Dutch Republic in 1628, he wrote his major works there, including the <i>Discourse on the Method</i> (1637), published in French with essays on optics, meteorology and geometry. Invited to Stockholm by Queen Christina of Sweden, he died of pneumonia in February 1650, reputedly worn down by lessons at five in the morning in a freezing library.</p>"),
      ("Thought", "<p>Descartes' rationalism held that knowledge can be founded on innate ideas grasped by reason, and he sought certainty through clear and distinct ideas guaranteed by a non-deceiving God. His metaphysics distinguished thinking substance (<i>res cogitans</i>) from extended substance (<i>res extensa</i>) and located their interaction problematically in the pineal gland. In mathematics he created analytic geometry by joining algebra to geometry — the origin of the Cartesian coordinate system — laying groundwork for calculus. His mechanistic physics was later superseded by Newtonian physics, but his framing of the mind–body problem still structures debate.</p>"),
    ],
    seealso=["Epistemology", "Rationalism", "Philosophy_of_mind", "Cogito_ergo_sum"],
    outgoing=["Philosophy", "Epistemology", "Metaphysics", "Philosophy_of_mind", "Rationalism", "Cogito_ergo_sum", "Immanuel_Kant", "Baruch_Spinoza", "Gottfried_Wilhelm_Leibniz"],
    unsure=["Circumstances of death (pneumonia) are traditional accounts; some dispute details"])

add(slug="Immanuel_Kant", title="Immanuel Kant",
    infobox=[("Born", "22 April 1724, Königsberg, Prussia"), ("Died", "12 February 1804, Königsberg"), ("Era", "18th-century philosophy"), ("Main interests", "Epistemology, metaphysics, ethics, aesthetics"), ("Notable works", "Critique of Pure Reason (1781); Groundwork (1785)"), ("Notable ideas", "Categorical imperative; transcendental idealism; synthetic a priori")],
    img="A portrait of Immanuel Kant in old age, thin-faced with white hair tied back",
    lead="<b>Immanuel Kant</b> (1724–1804) was a German philosopher from Königsberg in Prussia and a central figure of the Enlightenment. His <i>Critique of Pure Reason</i> (1781) argued that human knowledge arises from the cooperation of sense experience with concepts the mind itself supplies — a self-described 'Copernican revolution' in philosophy. In ethics he grounded morality in the categorical imperative: act only on maxims you can will as universal law, and treat humanity always also as an end.",
    sections=[
      ("Life", "<p>Kant spent his whole life in and around Königsberg, teaching at its university and becoming known for a routine so regular that neighbours reputedly set their watches by his afternoon walk. After a decade of silence, the first <i>Critique</i> appeared in 1781, followed by the <i>Groundwork of the Metaphysics of Morals</i> (1785), the <i>Critique of Practical Reason</i> (1788) and the <i>Critique of Judgment</i> (1790). He also wrote on perpetual peace, history, religion and anthropology.</p>"),
      ("Critical philosophy", "<p>Kant distinguished phenomena (things as they appear under the forms of space, time and the categories) from noumena (things in themselves), which we cannot know. Judgements can be analytic or synthetic, a priori or a posteriori; his great question was how synthetic a priori knowledge — as in mathematics and natural science — is possible. His ethics makes autonomy and duty the basis of moral worth, and his aesthetics analysed beauty and the sublime. Kant's influence runs through virtually all subsequent Western philosophy, from German idealism to contemporary analytic and continental thought.</p>"),
    ],
    seealso=["Epistemology", "Metaphysics", "Aesthetics", "Enlightenment", "Categorical_imperative"],
    outgoing=["Philosophy", "Epistemology", "Metaphysics", "Aesthetics", "René_Descartes", "David_Hume", "Enlightenment", "Categorical_imperative", "German_idealism"],
    unsure=["The watch-setting anecdote is famous but partly legendary"])

add(slug="Categorical_imperative", title="Categorical imperative",
    infobox=[("Field", "Ethics"), ("Formulated by", "Immanuel Kant"), ("First presented", "Groundwork of the Metaphysics of Morals (1785)")],
    img="The title page of the first edition of Kant's Groundwork, 1785",
    lead="The <b>categorical imperative</b> is the central concept of " + L("Immanuel_Kant") + "'s moral philosophy: an unconditional moral obligation that applies to all rational beings regardless of their desires or interests. It contrasts with hypothetical imperatives, which command actions as means to chosen ends ('if you want X, do Y').",
    sections=[
      ("Formulations", "<p>Kant gives several formulations he takes to be equivalent. The universal-law formula: 'Act only according to that maxim whereby you can at the same time will that it become a universal law.' The humanity formula: 'Act in such a way that you treat humanity, whether in your own person or in the person of any other, never merely as a means to an end, but always at the same time as an end.' A third formula invokes the idea of a 'kingdom of ends', a community of rational agents legislating universal law.</p><p>The imperative is the foundation of Kantian deontology and a major influence on later ethics and political philosophy, including John Rawls. Critics from Hegel onward have charged that the universal-law test is empty or generates false positives and negatives; defenders reply that it captures the impartiality at the heart of morality.</p>"),
    ],
    seealso=["Ethics", "Deontology", "Immanuel_Kant", "Utilitarianism"],
    outgoing=["Ethics", "Immanuel_Kant", "Utilitarianism", "Deontology", "Philosophy"],
    unsure=[])

add(slug="David_Hume", title="David Hume",
    infobox=[("Born", "7 May 1711, Edinburgh, Scotland"), ("Died", "25 August 1776, Edinburgh"), ("Era", "18th-century philosophy"), ("Main interests", "Epistemology, ethics, history, religion"), ("Notable works", "A Treatise of Human Nature (1739–40); An Enquiry Concerning Human Understanding (1748)")],
    img="A portrait of David Hume as a round-faced gentleman in 18th-century dress, by Allan Ramsay",
    lead="<b>David Hume</b> (1711–1776) was a Scottish Enlightenment philosopher, historian and essayist, regarded as one of the most important figures in Western philosophy. His empiricism and scepticism — about causation, induction, the self and religion — posed challenges philosophy still answers; " + L("Immanuel_Kant") + " credited Hume with awakening him from his 'dogmatic slumber'.",
    sections=[
      ("Thought", "<p>In <i>A Treatise of Human Nature</i> (1739–40), Hume argued that all ideas derive from impressions of sense or feeling, and that our belief in cause and effect rests not on reason but on custom: we observe constant conjunction, never necessary connection. His problem of induction asks how inference from observed to unobserved can be justified. He analysed the self as a 'bundle' of perceptions and argued, in a famous passage, that no 'ought' follows from an 'is'. His ethics grounds morality in sympathy and sentiment rather than reason.</p>"),
      ("Religion and later life", "<p>Hume's <i>Dialogues Concerning Natural Religion</i> (published posthumously, 1779) criticise arguments for God's existence, and his essay 'Of Miracles' argues testimony can never make a miracle probable enough to outweigh uniform experience. Barred from university posts by religious controversy, he found fame with his multi-volume <i>History of England</i>. Affable and sociable — 'le bon David' to Paris friends — he faced terminal illness with famous cheerfulness, documented by Adam Smith and James Boswell.</p>"),
    ],
    seealso=["Epistemology", "Empiricism", "Scepticism", "Problem_of_induction"],
    outgoing=["Philosophy", "Epistemology", "Immanuel_Kant", "Empiricism", "Scepticism", "Problem_of_induction", "Philosophy_of_religion", "John_Locke", "George_Berkeley"],
    unsure=[])

add(slug="John_Locke", title="John Locke",
    infobox=[("Born", "29 August 1632, Wrington, England"), ("Died", "28 October 1704, High Laver, England"), ("Era", "17th-century philosophy"), ("Main interests", "Epistemology, political philosophy"), ("Notable works", "An Essay Concerning Human Understanding (1689); Two Treatises of Government (1689)")],
    img="A portrait of John Locke with long grey hair, by Godfrey Kneller",
    lead="<b>John Locke</b> (1632–1704) was an English philosopher and physician, among the most influential thinkers of the Enlightenment. His <i>Essay Concerning Human Understanding</i> (1689) argued that the mind at birth is a blank slate (<i>tabula rasa</i>) written on by experience, founding British empiricism. His <i>Two Treatises of Government</i> defended natural rights to life, liberty and property and a social contract revocable when government breaks its trust — ideas foundational to liberalism and the American and French revolutions.",
    sections=[
      ("Epistemology", "<p>Against the doctrine of innate ideas, Locke held that all ideas come from sensation and reflection. He distinguished primary qualities (such as shape and motion, resembling qualities in objects) from secondary qualities (colour, taste, sound — powers to produce ideas in us). His account of personal identity, based on continuity of consciousness and memory, launched a debate continued by " + L("George_Berkeley") + ", " + L("David_Hume") + " and modern philosophers.</p>"),
      ("Political thought", "<p>The <i>First Treatise</i> refutes divine-right absolutism; the <i>Second</i> describes a state of nature governed by natural law, in which people form societies to secure their rights, retaining a right of resistance to tyranny. Locke's <i>Letter Concerning Toleration</i> (1689) argued for religious toleration (though with limits typical of his age). He was also involved in colonial administration and investment, a record modern scholars scrutinise alongside his philosophy.</p>"),
    ],
    seealso=["Empiricism", "Epistemology", "Social_contract", "Liberalism"],
    outgoing=["Philosophy", "Epistemology", "Empiricism", "George_Berkeley", "David_Hume", "Social_contract", "Liberalism", "Tabula_rasa"],
    unsure=["Degree of Locke's involvement in colonial ventures debated by scholars"])

add(slug="George_Berkeley", title="George Berkeley",
    infobox=[("Born", "12 March 1685, County Kilkenny, Ireland"), ("Died", "14 January 1753, Oxford, England"), ("Era", "18th-century philosophy"), ("Main interests", "Metaphysics, epistemology"), ("Notable ideas", "Subjective idealism: esse est percipi ('to be is to be perceived')")],
    img="A portrait of Bishop George Berkeley in clerical dress",
    lead="<b>George Berkeley</b> (1685–1753) was an Anglo-Irish philosopher and Anglican bishop whose theory of subjective idealism holds that material objects exist only as ideas in minds: <i>esse est percipi</i>, 'to be is to be perceived'. In the <i>Principles of Human Knowledge</i> (1710) and the <i>Three Dialogues</i> (1713) he argued that what we perceive are ideas, and that talk of unperceived matter is incoherent; the continued existence of the world is secured by God's perception of it.",
    sections=[
      ("Thought and life", "<p>Berkeley developed " + L("John_Locke") + "'s empiricism by attacking the primary/secondary quality distinction and abstract ideas. Samuel Johnson famously 'refuted' him by kicking a stone, but philosophers take Berkeley's arguments seriously as a challenge to materialism. He travelled in America planning a college in Bermuda (the city of Berkeley, California, is named for him) and later served as Bishop of Cloyne, writing on economics and public health — including a pamphlet promoting tar-water as a cure-all.</p>"),
    ],
    seealso=["Empiricism", "Idealism", "Epistemology", "Metaphysics"],
    outgoing=["John_Locke", "David_Hume", "Epistemology", "Metaphysics", "Empiricism", "Idealism"],
    unsure=[])

add(slug="Baruch_Spinoza", title="Baruch Spinoza",
    infobox=[("Born", "24 November 1632, Amsterdam, Dutch Republic"), ("Died", "21 February 1677, The Hague"), ("Era", "17th-century philosophy"), ("Main interests", "Metaphysics, ethics, biblical criticism"), ("Notable works", "Ethics (published 1677); Tractatus Theologico-Politicus (1670)")],
    img="A portrait of Baruch Spinoza, a young man with dark shoulder-length hair",
    lead="<b>Baruch Spinoza</b> (1632–1677) was a Dutch philosopher of Portuguese-Jewish origin, one of the great rationalists of the 17th century. His <i>Ethics</i>, written in geometrical form and published after his death, argues that there is only one substance — God or Nature (<i>Deus sive Natura</i>) — of which minds and bodies are modes. Excommunicated from Amsterdam's Jewish community in 1656 for his unorthodox views, he earned his living grinding lenses.",
    sections=[
      ("Thought", "<p>Spinoza's monism denies a transcendent creator: God is not a person who chooses, but the infinite substance of which everything is a necessary expression. Human bondage, in his ethics, is slavery to passive emotions caused by inadequate ideas; freedom comes through understanding necessity, culminating in the 'intellectual love of God'. His <i>Theological-Political Treatise</i> (1670) pioneered historical criticism of the Bible and defended freedom of thought and democratic government. Long reviled as an atheist, he was later celebrated by the German Romantics and remains central to debates on pantheism and determinism.</p>"),
    ],
    seealso=["Rationalism", "Pantheism", "Metaphysics", "René_Descartes"],
    outgoing=["René_Descartes", "Gottfried_Wilhelm_Leibniz", "Metaphysics", "Pantheism", "Rationalism", "Philosophy"],
    unsure=["Content of the 1656 cherem (excommunication) charges is not fully documented"])

add(slug="Friedrich_Nietzsche", title="Friedrich Nietzsche",
    infobox=[("Born", "15 October 1844, Röcken, Prussia"), ("Died", "25 August 1900, Weimar, Germany"), ("Era", "19th-century philosophy"), ("Main interests", "Ethics, aesthetics, religion, culture"), ("Notable works", "The Birth of Tragedy (1872); Thus Spoke Zarathustra (1883–85); Beyond Good and Evil (1886); On the Genealogy of Morality (1887)"), ("Notable ideas", "Death of God; Übermensch; eternal recurrence; master–slave morality; Apollonian and Dionysian")],
    img="A portrait photograph of Friedrich Nietzsche with his large walrus moustache, gazing intently",
    lead="<b>Friedrich Wilhelm Nietzsche</b> (1844–1900) was a German philosopher and classical philologist whose critiques of religion, morality and modern culture made him one of the most influential — and most contested — thinkers of the modern age. He proclaimed the 'death of God', dissected 'slave morality', and proposed ideals such as the Übermensch and eternal recurrence in aphoristic, poetic prose.",
    sections=[
      ("Life", "<p>Appointed a professor at Basel at only 24, Nietzsche published <i>The Birth of Tragedy</i> (1872), distinguishing the Apollonian (form, reason) from the Dionysian (ecstasy, instinct) in Greek culture. Ill health forced his resignation in 1879; a decade of itinerant writing in Switzerland and Italy produced <i>Thus Spoke Zarathustra</i>, <i>Beyond Good and Evil</i> and <i>On the Genealogy of Morality</i>. In January 1889 he suffered a mental collapse in Turin and lived in care, latterly of his sister Elisabeth, until his death in 1900.</p>"),
      ("Ideas and legacy", "<p>Nietzsche's genealogy traces Christian morality to <i>ressentiment</i> — the weak revaluing the values of the strong as 'evil'. His perspectivism denies view-from-nowhere truth, and his call to 'revalue all values' influenced existentialism, postmodernism and the arts. His sister's editing and Nazi appropriation long distorted his reputation; he in fact despised antisemitism and German nationalism, and post-war scholarship (notably Walter Kaufmann) restored a more accurate picture.</p>"),
    ],
    seealso=["Existentialism", "Nihilism", "Ethics", "Søren_Kierkegaard"],
    outgoing=["Philosophy", "Ethics", "Existentialism", "Nihilism", "Søren_Kierkegaard", "Arthur_Schopenhauer", "Atheism"],
    unsure=["Cause of the 1889 collapse (syphilis vs other diagnoses) is disputed"])

add(slug="Arthur_Schopenhauer", title="Arthur Schopenhauer",
    infobox=[("Born", "22 February 1788, Danzig"), ("Died", "21 September 1860, Frankfurt am Main"), ("Era", "19th-century philosophy"), ("Main interests", "Metaphysics, ethics, aesthetics"), ("Notable work", "The World as Will and Representation (1818/1844)")],
    img="A portrait of Arthur Schopenhauer in old age with wild white hair",
    lead="<b>Arthur Schopenhauer</b> (1788–1860) was a German philosopher best known for <i>The World as Will and Representation</i> (1818), which portrays the world as the objectification of a blind, striving Will. Influenced by " + L("Immanuel_Kant") + " and by Indian thought — the Upanishads and Buddhism — Schopenhauer concluded that desire is the root of suffering and that release lies in aesthetic contemplation, compassion and ascetic denial of the will.",
    sections=[
      ("Influence", "<p>Long ignored while Hegel dominated German universities, Schopenhauer found fame late, after his essay collection <i>Parerga and Paralipomena</i> (1851). His philosophy of music, pessimism and the will shaped Wagner, " + L("Friedrich_Nietzsche") + " (who later rebelled against it), Freud and much modernist literature. His thought is a major bridge between Western philosophy and Asian religions.</p>"),
    ],
    seealso=["Pessimism", "Immanuel_Kant", "Friedrich_Nietzsche", "Buddhism"],
    outgoing=["Immanuel_Kant", "Friedrich_Nietzsche", "Buddhism", "Upanishads", "Pessimism", "Philosophy"],
    unsure=[])

add(slug="Søren_Kierkegaard", title="Søren Kierkegaard",
    infobox=[("Born", "5 May 1813, Copenhagen, Denmark"), ("Died", "11 November 1855, Copenhagen"), ("Era", "19th-century philosophy"), ("Main interests", "Religion, ethics, existence"), ("Notable works", "Either/Or (1843); Fear and Trembling (1843); The Sickness unto Death (1849)"), ("Notable ideas", "Leap of faith; the three stages of life; anxiety; knight of faith")],
    img="An unfinished sketch portrait of Søren Kierkegaard by Niels Christian Kierkegaard",
    lead="<b>Søren Aabye Kierkegaard</b> (1813–1855) was a Danish philosopher and theologian widely regarded as the father of existentialism. Writing much of his work under pseudonyms, he explored how an individual becomes a self through choice, anxiety and faith, and attacked both Hegelian system-building and the comfortable state Christianity of his day, which he called 'Christendom'.",
    sections=[
      ("Thought", "<p>Kierkegaard distinguishes three spheres of existence: the aesthetic (pleasure), the ethical (duty and commitment), and the religious (faith). <i>Fear and Trembling</i> retells Abraham's binding of Isaac to show faith as a paradoxical 'teleological suspension of the ethical'. <i>The Concept of Anxiety</i> and <i>The Sickness unto Death</i> analyse despair as the self's refusal to be itself. His broken engagement to Regine Olsen haunted his life and writing. Rediscovered in the 20th century, he deeply influenced theology (Karl Barth), existentialism and psychology.</p>"),
    ],
    seealso=["Existentialism", "Philosophy_of_religion", "Abraham", "Faith"],
    outgoing=["Existentialism", "Philosophy_of_religion", "Abraham", "Faith", "Friedrich_Nietzsche", "Jean-Paul_Sartre"],
    unsure=["Pseudonym attribution details for minor works vary between editions"])

print("part2 loaded", len(PAGES))

add(slug="Thomas_Aquinas", title="Thomas Aquinas",
    infobox=[("Born", "1225, Roccasecca, Kingdom of Sicily"), ("Died", "7 March 1274, Fossanova Abbey"), ("Era", "Medieval philosophy"), ("Main interests", "Theology, metaphysics, ethics"), ("Notable works", "Summa Theologiae (unfinished); Summa contra Gentiles"), ("Notable ideas", "Five Ways; natural law; act and potency")],
    img="A medieval altarpiece painting of Saint Thomas Aquinas in Dominican habit holding a book",
    lead="<b>Thomas Aquinas</b> (1225–1274) was an Italian Dominican friar, philosopher and theologian, the foremost figure of scholasticism and a Doctor of the Catholic Church. His unfinished masterpiece, the <i>Summa Theologiae</i>, synthesises Aristotelian philosophy with Christian doctrine and sets out the 'Five Ways' — five arguments for the existence of God from motion, causation, contingency, degrees and purpose.",
    sections=[
      ("Life and work", "<p>Born to a noble family near Aquino, Thomas was educated at Monte Cassino and Naples, joined the Dominicans against his family's wishes (they detained him for a year), and studied under Albertus Magnus in Paris and Cologne. He taught in Paris, Rome and Naples, writing vast commentaries on " + L("Aristotle") + " and Scripture. After a mystical experience in December 1273 he stopped writing, calling his work 'so much straw'. He died travelling to the Council of Lyon in 1274 and was canonised in 1323.</p>"),
      ("Thought", "<p>Aquinas holds that faith and reason are harmonious: some truths (God's existence) are demonstrable, others (the Trinity) known only by revelation. His natural-law ethics grounds moral precepts in human nature's God-given ends. He distinguishes essence and existence, act and potency, and adopts Aristotle's four causes. Thomism became near-official Catholic philosophy after Leo XIII's <i>Aeterni Patris</i> (1879) and remains influential in analytic philosophy of religion and ethics.</p>"),
    ],
    seealso=["Scholasticism", "Philosophy_of_religion", "Natural_law", "Aristotle"],
    outgoing=["Aristotle", "Philosophy_of_religion", "Philosophy", "Scholasticism", "Natural_law", "Averroes", "Maimonides"],
    unsure=[])

add(slug="Augustine_of_Hippo", title="Augustine of Hippo",
    infobox=[("Born", "13 November 354, Thagaste, Numidia"), ("Died", "28 August 430, Hippo Regius"), ("Era", "Late antiquity / patristics"), ("Main interests", "Theology, philosophy of time, ethics"), ("Notable works", "Confessions (c. 397–400); The City of God (413–426)")],
    img="A fresco of Saint Augustine in his study, wearing bishop's robes",
    lead="<b>Augustine of Hippo</b> (354–430), also known as Saint Augustine, was a theologian and philosopher from Roman North Africa whose writings shaped Western Christianity and philosophy. His <i>Confessions</i> — a spiritual autobiography famous for the garden conversion scene ('take up and read') — and <i>The City of God</i>, written after the sack of Rome in 410, influenced doctrines of original sin, grace, just war and the philosophy of history.",
    sections=[
      ("Life and thought", "<p>Raised by a Christian mother, Monica, Augustine spent nine years as a Manichaean hearer before turning to Neoplatonism and, in Milan, to Christianity under Bishop Ambrose; he was baptised in 387. As Bishop of Hippo he fought Donatist and Pelagian controversies, arguing against Pelagius that the will is bound by sin and freedom comes by grace. His meditations on time in the <i>Confessions</i> ('What then is time? If no one asks me, I know...') remain a starting point of the subject. He died as the Vandals besieged Hippo.</p>"),
    ],
    seealso=["Plato", "Theology", "Philosophy_of_religion", "Original_sin"],
    outgoing=["Plato", "Philosophy", "Theology", "Philosophy_of_religion", "Thomas_Aquinas", "Original_sin"],
    unsure=[])

add(slug="Averroes", title="Averroes",
    infobox=[("Born", "14 April 1126, Córdoba, al-Andalus"), ("Died", "10 December 1198, Marrakesh"), ("Era", "Medieval Islamic philosophy"), ("Main interests", "Aristotelian commentaries, medicine, law"), ("Also known as", "Ibn Rushd; 'The Commentator'")],
    img="A detail from a Renaissance fresco showing Averroes in a turban among Greek philosophers",
    lead="<b>Averroes</b> (1126–1198), known in Arabic as <b>Ibn Rushd</b>, was an Andalusian Muslim polymath — philosopher, physician and judge — whose detailed commentaries on " + L("Aristotle") + " earned him the Latin title 'The Commentator'. Writing in Almohad Córdoba, he defended philosophy against " + L("Al-Ghazali") + "'s <i>Incoherence of the Philosophers</i> in his own <i>Incoherence of the Incoherence</i>, arguing that revelation and philosophy are compatible paths to truth.",
    sections=[
      ("Influence", "<p>Averroes' commentaries, translated into Latin and Hebrew, profoundly shaped scholasticism: " + L("Thomas_Aquinas") + " cites him constantly, and his doctrine of the unity of the intellect sparked the Latin Averroist controversies in Paris. His medical encyclopedia, the <i>Colliget</i>, was used in European universities for centuries. Briefly exiled in a political-religious backlash, he was restored before his death in Marrakesh.</p>"),
    ],
    seealso=["Aristotle", "Al-Ghazali", "Thomas_Aquinas", "Islamic_philosophy"],
    outgoing=["Aristotle", "Al-Ghazali", "Thomas_Aquinas", "Islamic_philosophy", "Philosophy", "Maimonides"],
    unsure=["Latin titles of works (Colliget = Kitab al-Kulliyat) recalled in common form"])

add(slug="Maimonides", title="Maimonides",
    infobox=[("Born", "1135 (or 1138), Córdoba, al-Andalus"), ("Died", "12 December 1204, Fustat, Egypt"), ("Era", "Medieval Jewish philosophy"), ("Main interests", "Theology, Jewish law, medicine"), ("Notable works", "Mishneh Torah (c. 1180); Guide for the Perplexed (c. 1190)"), ("Also known as", "Rambam; Moses ben Maimon")],
    img="A portrait engraving of Maimonides from a later edition of his works",
    lead="<b>Moses ben Maimon</b> (1135/1138–1204), commonly called <b>Maimonides</b> and in Jewish tradition the <b>Rambam</b>, was a Sephardic rabbi, philosopher and physician, the preeminent Jewish thinker of the Middle Ages. His fourteen-volume <i>Mishneh Torah</i> codified Jewish law, while the <i>Guide for the Perplexed</i>, written in Judeo-Arabic, reconciled Aristotelian philosophy with Jewish theology through allegorical reading and a rigorous negative theology — God can be described only by what He is not.",
    sections=[
      ("Life and influence", "<p>Fleeing Almohad persecution, his family wandered Spain and Morocco before settling in Egypt, where he became court physician and leader of the Jewish community. His Thirteen Principles of Faith became a standard creed. The <i>Guide</i> influenced " + L("Thomas_Aquinas") + ", the scholastics, and later " + L("Baruch_Spinoza", "Spinoza") + " and modern Jewish thought; controversy over his rationalism ('the Maimonidean controversy') split medieval Jewish communities.</p>"),
    ],
    seealso=["Judaism", "Aristotle", "Thomas_Aquinas", "Jewish_philosophy"],
    outgoing=["Judaism", "Aristotle", "Thomas_Aquinas", "Baruch_Spinoza", "Jewish_philosophy", "Philosophy"],
    unsure=["Birth year given variously as 1135 or 1138 in sources"])

add(slug="Al-Ghazali", title="Al-Ghazali",
    infobox=[("Born", "c. 1058, Tus, Persia"), ("Died", "19 December 1111, Tus"), ("Era", "Medieval Islamic philosophy / theology"), ("Main interests", "Theology, Sufism, philosophy"), ("Notable works", "The Incoherence of the Philosophers (c. 1095); The Revival of the Religious Sciences"), ("Also known as", "Algazel; Hujjat al-Islam ('Proof of Islam')")],
    img="A Persian manuscript illumination of a scholar writing, representing Al-Ghazali",
    lead="<b>Abū Ḥāmid al-Ghazālī</b> (c. 1058–1111) was a Persian theologian, philosopher, jurist and Sufi, one of the most influential thinkers in Islamic history. A brilliant professor at Baghdad's Nizamiyya, he suffered a spiritual crisis in 1095, abandoned his post, and wandered as a Sufi before writing his vast <i>Revival of the Religious Sciences</i> (<i>Ihya Ulum al-Din</i>), which integrated law, theology and mystical practice.",
    sections=[
      ("The Incoherence", "<p>In <i>The Incoherence of the Philosophers</i> (<i>Tahafut al-Falasifa</i>), Ghazali attacked the metaphysics of the Aristotelian philosophers al-Farabi and Avicenna on twenty problems, holding three of their positions (the eternity of the world, God's knowledge of universals only, denial of bodily resurrection) to be unbelief. His occasionalism — fire does not burn cotton; God creates the burning — anticipates Hume's problem of causation. " + L("Averroes") + " answered him a century later. Modern scholarship debates how far Ghazali opposed philosophy as such, since he himself introduced Aristotelian logic into Islamic theology.</p>"),
    ],
    seealso=["Islam", "Averroes", "Sufism", "Islamic_philosophy"],
    outgoing=["Islam", "Averroes", "Sufism", "Islamic_philosophy", "David_Hume", "Philosophy"],
    unsure=["Exact death date (19 Dec 1111) recalled; some sources give 14 Jamadi al-Akhirah 505 AH"])

add(slug="Laozi", title="Laozi",
    infobox=[("Born", "Traditionally 6th century BC, Chu, China"), ("Era", "Ancient Chinese philosophy"), ("Main interests", "Taoism"), ("Notable work", "Tao Te Ching (Daodejing)"), ("Also known as", "Lao Tzu; Lao Tan")],
    img="A Chinese painting of Laozi riding an ox, departing to the west",
    lead="<b>Laozi</b>, also romanised as <b>Lao Tzu</b>, is the traditional author of the <i>Tao Te Ching</i> and the legendary founder of " + L("Taoism") + ". Later tradition makes him an older contemporary of " + L("Confucius") + " and keeper of the Zhou archives who, disgusted with the court's decline, rode west on an ox, leaving the 5,000-character <i>Tao Te Ching</i> with a gatekeeper at the pass. Modern scholars debate whether he was a historical individual or a composite figure, and the text itself likely took shape over centuries.",
    sections=[
      ("Teaching", "<p>The <i>Tao Te Ching</i> teaches that the Tao ('Way') that can be named is not the eternal Tao. Its political and personal ideal is <i>wu wei</i> — effortless, non-forcing action aligned with the natural order — and it praises softness, humility and yielding ('the soft overcomes the hard'). Together with the <i>Zhuangzi</i>, it is the founding text of philosophical Taoism; in religious Taoism Laozi was deified as Lord Lao, one of the Three Pure Ones.</p>"),
    ],
    seealso=["Taoism", "Tao_Te_Ching", "Confucius", "Yin_and_yang"],
    outgoing=["Taoism", "Tao_Te_Ching", "Confucius", "Yin_and_yang", "Philosophy", "Religion"],
    unsure=["Historicity of Laozi is genuinely uncertain; dates legendary"])

add(slug="Jean-Paul_Sartre", title="Jean-Paul Sartre",
    infobox=[("Born", "21 June 1905, Paris, France"), ("Died", "15 April 1980, Paris"), ("Era", "20th-century philosophy"), ("Main interests", "Existentialism, phenomenology, Marxism, literature"), ("Notable works", "Nausea (1938); Being and Nothingness (1943); Existentialism Is a Humanism (1946)"), ("Notable ideas", "Existence precedes essence; bad faith; 'Hell is other people'")],
    img="A photograph of Jean-Paul Sartre smoking a pipe, wearing round glasses",
    lead="<b>Jean-Paul Charles Aymard Sartre</b> (1905–1980) was a French philosopher, playwright, novelist and political activist, the leading figure of existentialism. His slogan 'existence precedes essence' holds that human beings, unlike tools, have no pre-given nature: we are 'condemned to be free', making ourselves through choices for which we bear total responsibility — a burden Sartre calls anguish, and evasion of it 'bad faith'.",
    sections=[
      ("Life and work", "<p>Educated at the École Normale Supérieure, where he met " + L("Simone_de_Beauvoir") + ", his lifelong partner, Sartre taught philosophy, served in the war, and was a prisoner of war in 1940–41. <i>Being and Nothingness</i> (1943) and the novel <i>Nausea</i> made his name; after the war his public lecture <i>Existentialism Is a Humanism</i> made him an international celebrity. He founded the journal <i>Les Temps Modernes</i>, supported (and quarrelled with) communism, backed Algerian independence, and in <i>Critique of Dialectical Reason</i> (1960) tried to fuse existentialism with Marxism. He refused the Nobel Prize in Literature in 1964. His funeral in 1980 drew tens of thousands onto the streets of Paris.</p>"),
    ],
    seealso=["Existentialism", "Simone_de_Beauvoir", "Albert_Camus", "Phenomenology"],
    outgoing=["Existentialism", "Simone_de_Beauvoir", "Albert_Camus", "Karl_Marx", "Phenomenology", "Philosophy"],
    unsure=["Funeral crowd estimate (50,000) varies by source"])

add(slug="Simone_de_Beauvoir", title="Simone de Beauvoir",
    infobox=[("Born", "9 January 1908, Paris, France"), ("Died", "14 April 1986, Paris"), ("Era", "20th-century philosophy"), ("Main interests", "Existentialism, feminism, ethics"), ("Notable works", "The Ethics of Ambiguity (1947); The Second Sex (1949)"), ("Notable idea", "'One is not born, but rather becomes, a woman'")],
    img="A photograph of Simone de Beauvoir at her writing desk",
    lead="<b>Simone Lucie Ernestine Marie Bertrand de Beauvoir</b> (1908–1986) was a French existentialist philosopher, novelist and feminist thinker. Her <i>The Second Sex</i> (1949) — a vast philosophical, historical and literary analysis of women's oppression — founded modern feminism with its claim that woman is made, not born, and cast as man's 'Other'. With " + L("Jean-Paul_Sartre") + " she formed the most famous intellectual partnership of the century.",
    sections=[
      ("Thought", "<p>In <i>The Ethics of Ambiguity</i> (1947) Beauvoir developed an existentialist ethics of freedom that wills the freedom of others. <i>The Second Sex</i> applied existential categories — transcendence versus immanence — to women's situation across biology, history, myth and lived experience, arguing for women's economic independence and self-definition. Her novels, including <i>The Mandarins</i> (Prix Goncourt, 1954), and her memoirs document French intellectual life; she campaigned for abortion rights, signing the Manifesto of the 343 in 1971.</p>"),
    ],
    seealso=["Existentialism", "Feminism", "Jean-Paul_Sartre", "Ethics"],
    outgoing=["Existentialism", "Jean-Paul_Sartre", "Ethics", "Feminism", "Philosophy"],
    unsure=[])

add(slug="Karl_Marx", title="Karl Marx",
    infobox=[("Born", "5 May 1818, Trier, Prussia"), ("Died", "14 March 1883, London, England"), ("Era", "19th-century philosophy"), ("Main interests", "Political economy, history, sociology"), ("Notable works", "The Communist Manifesto (1848, with Engels); Das Kapital (1867)"), ("Notable ideas", "Historical materialism; class struggle; alienation; surplus value")],
    img="A photograph of Karl Marx in later life with his full grey beard",
    lead="<b>Karl Marx</b> (1818–1883) was a German philosopher, economist, historian and revolutionary socialist whose critique of capitalism — developed with Friedrich Engels — became the theoretical basis of Marxism and of socialist and communist movements worldwide. His analysis of history as class struggle, and of capital as accumulated alienated labour, reshaped the social sciences regardless of readers' politics.",
    sections=[
      ("Life and work", "<p>Born in Trier to a middle-class family of Jewish origin converted to Lutheranism, Marx studied law and philosophy, joining the Young Hegelians and taking a doctorate in 1841. Journalism radicalised him: he edited the <i>Rheinische Zeitung</i>, was expelled from Prussia, Paris and Brussels, and settled in London in 1849, researching in the British Museum Reading Room. With Engels he wrote <i>The Communist Manifesto</i> (1848) ('Working men of all countries, unite!'); his mature economics culminated in <i>Das Kapital</i> (1867), whose later volumes Engels edited posthumously. He helped found the International Workingmen's Association (First International) in 1864.</p>"),
      ("Ideas", "<p>Historical materialism holds that a society's economic base — forces and relations of production — shapes its laws, politics and ideas. Marx analysed commodity fetishism, surplus value extracted from labour, and capitalism's tendency to crisis and concentration. His early writings on alienation, published only in 1932, influenced existentialist and humanist readings; governments invoking his name in the 20th century made him among history's most consequential — and contested — thinkers.</p>"),
    ],
    seealso=["Communism", "Socialism", "Capitalism", "Historical_materialism"],
    outgoing=["Philosophy", "Communism", "Socialism", "Capitalism", "Historical_materialism", "Jean-Paul_Sartre", "Friedrich_Engels"],
    unsure=[])

add(slug="Ludwig_Wittgenstein", title="Ludwig Wittgenstein",
    infobox=[("Born", "26 April 1889, Vienna, Austria-Hungary"), ("Died", "29 April 1951, Cambridge, England"), ("Era", "20th-century philosophy"), ("Main interests", "Logic, language, mind"), ("Notable works", "Tractatus Logico-Philosophicus (1921); Philosophical Investigations (1953, posthumous)")],
    img="A photograph of Ludwig Wittgenstein in 1930, intense gaze, wearing a jacket",
    lead="<b>Ludwig Josef Johann Wittgenstein</b> (1889–1951) was an Austrian-British philosopher who worked primarily in logic, the philosophy of mathematics, the philosophy of mind and the philosophy of language. Uniquely, he produced two opposed masterpieces: the <i>Tractatus Logico-Philosophicus</i> (1921), which pictures language as mirroring facts and ends 'Whereof one cannot speak, thereof one must be silent', and the posthumous <i>Philosophical Investigations</i> (1953), which replaces that picture with language as a motley of 'language-games' embedded in forms of life.",
    sections=[
      ("Life", "<p>Born into one of Europe's richest families, Wittgenstein studied engineering in Berlin and Manchester, then philosophy at Cambridge under " + L("Bertrand_Russell") + ". He served in the First World War (writing the <i>Tractatus</i> in the trenches), gave away his fortune, and worked as a schoolteacher, gardener's assistant and architect before returning to Cambridge in 1929. His charismatic, austere teaching shaped a generation; he died in Cambridge in 1951, saying 'Tell them I've had a wonderful life.'</p>"),
    ],
    seealso=["Bertrand_Russell", "Logic", "Philosophy_of_language", "Analytic_philosophy"],
    outgoing=["Bertrand_Russell", "Logic", "Philosophy_of_language", "Analytic_philosophy", "Philosophy"],
    unsure=[])

add(slug="Jeremy_Bentham", title="Jeremy Bentham",
    infobox=[("Born", "15 February 1748, London, England"), ("Died", "6 June 1832, London"), ("Era", "18th–19th-century philosophy"), ("Main interests", "Ethics, law, political philosophy"), ("Notable work", "An Introduction to the Principles of Morals and Legislation (1789)"), ("Notable ideas", "Utilitarianism; greatest happiness principle; Panopticon")],
    img="A portrait of Jeremy Bentham with white hair, in dark coat",
    lead="<b>Jeremy Bentham</b> (1748–1832) was an English philosopher and legal reformer, the founder of modern " + L("Utilitarianism") + ". Opening his <i>Principles of Morals and Legislation</i> (1789) with the claim that nature has placed mankind under two sovereign masters, pain and pleasure, he proposed that laws and actions be judged solely by their tendency to maximise happiness — 'the greatest happiness of the greatest number'.",
    sections=[
      ("Reforms and legacy", "<p>Bentham attacked the chaos of English common law, designed the Panopticon prison, and campaigned — far ahead of his time — for universal (male) suffrage, decriminalisation of homosexuality, animal welfare ('The question is not, Can they reason? ... but, Can they suffer?') and abolition of the death penalty for most offences. His disciple " + L("John_Stuart_Mill") + " both spread and revised his philosophy. Bentham's preserved, clothed skeleton — the 'auto-icon' — is displayed at University College London, whose founding he inspired.</p>"),
    ],
    seealso=["Utilitarianism", "John_Stuart_Mill", "Ethics", "Liberalism"],
    outgoing=["Utilitarianism", "John_Stuart_Mill", "Ethics", "Liberalism", "Philosophy"],
    unsure=["Bentham's exact role in founding UCL is indirect (inspiration and support) rather than founder in the formal sense"])

add(slug="John_Stuart_Mill", title="John Stuart Mill",
    infobox=[("Born", "20 May 1806, London, England"), ("Died", "8 May 1873, Avignon, France"), ("Era", "19th-century philosophy"), ("Main interests", "Ethics, political philosophy, logic, economics"), ("Notable works", "On Liberty (1859); Utilitarianism (1863); The Subjection of Women (1869)")],
    img="A photograph of John Stuart Mill in old age with white side-whiskers",
    lead="<b>John Stuart Mill</b> (1806–1873) was an English philosopher, political economist and civil servant, the most influential English-speaking philosopher of the 19th century. <i>On Liberty</i> (1859) gives the classic defence of free expression and the harm principle — power may be exercised over someone against their will only to prevent harm to others. His <i>Utilitarianism</i> (1863) refined " + L("Jeremy_Bentham", "Bentham") + "'s doctrine, distinguishing higher and lower pleasures.",
    sections=[
      ("Life and thought", "<p>Raised as an educational experiment by his father James Mill, Mill learned Greek at three and suffered a mental crisis at twenty, from which Wordsworth's poetry helped recover him — convincing him that feeling must complement analysis. He worked for the East India Company, sat in Parliament (1865–68) and proposed women's suffrage; <i>The Subjection of Women</i> (1869), written with Harriet Taylor Mill, argues for the equality of the sexes. His <i>System of Logic</i> (1843) and <i>Principles of Political Economy</i> (1848) were standard texts for decades.</p>"),
    ],
    seealso=["Utilitarianism", "Jeremy_Bentham", "Liberalism", "Ethics"],
    outgoing=["Utilitarianism", "Jeremy_Bentham", "Liberalism", "Ethics", "Philosophy", "Feminism"],
    unsure=["Extent of Harriet Taylor Mill's co-authorship debated by scholars"])

# ---------------- SCHOOLS ----------------
add(slug="Stoicism", title="Stoicism",
    infobox=[("Founder", "Zeno of Citium"), ("Founded", "c. 300 BC, Athens"), ("Key figures", "Seneca, Epictetus, Marcus Aurelius, Chrysippus"), ("Main ideas", "Virtue as the only good; dichotomy of control; living according to nature")],
    img="A marble bust of the Roman emperor Marcus Aurelius, author of Meditations",
    lead="<b>Stoicism</b> is a school of Hellenistic philosophy founded by Zeno of Citium in Athens around 300 BC, named for the Painted Porch (<i>Stoa Poikile</i>) where he taught. It teaches that virtue — wisdom, courage, justice and temperance — is the only true good, that destructive emotions result from errors of judgement, and that happiness (<i>eudaimonia</i>) comes from accepting what cannot be controlled while acting rightly on what can.",
    sections=[
      ("History", "<p>After Zeno, the school was systematised by Chrysippus and spread through the Roman world: the statesman Seneca, the freed slave Epictetus, whose <i>Discourses</i> and <i>Enchiridion</i> survive, and the emperor Marcus Aurelius, whose private notebooks became the <i>Meditations</i>. Stoic physics pictured a rational, providential cosmos (the <i>logos</i>) pervaded by divine reason; its logic and ethics shaped early Christian thought and later resurfaced in Spinoza, the Enlightenment and modern cognitive therapy.</p>"),
      ("Practices and modern revival", "<p>Stoic exercises include negative visualisation (imagining loss), journaling, distinguishing what is 'up to us' from what is not, and viewing events from the perspective of the whole. A popular revival since the 2000s has drawn on Stoicism for resilience and self-help, sometimes criticised for trimming its physics and communal ethics.</p>"),
    ],
    seealso=["Zeno_of_Citium", "Marcus_Aurelius", "Epictetus", "Seneca", "Ethics"],
    outgoing=["Philosophy", "Ethics", "Zeno_of_Citium", "Marcus_Aurelius", "Epictetus", "Seneca", "Baruch_Spinoza"],
    unsure=["Foundation date c. 301/300 BC approximate"])

add(slug="Marcus_Aurelius", title="Marcus Aurelius",
    infobox=[("Born", "26 April 121, Rome"), ("Died", "17 March 180, Vindobona (Vienna) or Sirmium"), ("Reigned", "161–180 AD"), ("Known for", "Roman emperor; Meditations; last of the 'Five Good Emperors'")],
    img="The bronze equestrian statue of Marcus Aurelius on the Capitoline Hill, Rome",
    lead="<b>Marcus Aurelius Antoninus</b> (121–180) was Roman emperor from 161 to 180 and a Stoic philosopher, the last of the rulers traditionally grouped as the Five Good Emperors. His <i>Meditations</i> — private notebooks in Greek, written on campaign along the Danube — urge self-discipline, humility and acceptance of fate, and are among the most read works of " + L("Stoicism") + ".",
    sections=[
      ("Reign", "<p>Adopted by Antoninus Pius as heir, Marcus ruled jointly with Lucius Verus until 169. His reign faced the Parthian and Marcomannic wars, plague (the Antonine Plague), and rising pressure on the northern frontiers. Though persecutions of Christians occurred under his rule, his personal involvement is debated. Breaking the adoptive succession, he named his son Commodus heir — a choice historians count among his few great errors. The <i>Meditations</i> were never intended for publication; their survival is one of literature's accidents.</p>"),
    ],
    seealso=["Stoicism", "Roman_Empire", "Epictetus", "Seneca"],
    outgoing=["Stoicism", "Roman_Empire", "Epictetus", "Seneca", "Philosophy"],
    unsure=["Place of death (Vienna vs Sirmium) uncertain in sources"])

add(slug="Epictetus", title="Epictetus",
    infobox=[("Born", "c. 50 AD, Hierapolis, Phrygia"), ("Died", "c. 135 AD, Nicopolis, Greece"), ("School", "Stoicism"), ("Notable works", "Discourses; Enchiridion (recorded by Arrian)")],
    img="An imagined engraving of Epictetus, the lame slave-philosopher, teaching students",
    lead="<b>Epictetus</b> (c. 50 – c. 135 AD) was a Greek Stoic philosopher born into slavery in Phrygia, who served in Rome as secretary to Epaphroditus, a wealthy freedman of Nero. Freed after Nero's death, he taught philosophy in Rome until Domitian banished the philosophers in 93 AD, then founded a school at Nicopolis. His pupil Arrian recorded the <i>Discourses</i> and condensed them into the <i>Enchiridion</i> ('Handbook').",
    sections=[
      ("Teaching", "<p>Epictetus' core doctrine is the dichotomy of control: some things are up to us — our judgements, impulses and desires — and others (body, property, reputation) are not; freedom and tranquillity consist in wanting what depends on us rightly and accepting the rest. His lame leg (injured, tradition says, by his master) and slave's perspective give his teaching its distinctive insistence that no external power can harm the true self.</p>"),
    ],
    seealso=["Stoicism", "Marcus_Aurelius", "Seneca"],
    outgoing=["Stoicism", "Marcus_Aurelius", "Seneca", "Philosophy"],
    unsure=["Birth/death years approximate; dates c. 50–135 are conventional"])

add(slug="Existentialism", title="Existentialism",
    infobox=[("Key figures", "Søren Kierkegaard, Friedrich Nietzsche, Jean-Paul Sartre, Simone de Beauvoir, Albert Camus, Martin Heidegger"), ("Key ideas", "Existence precedes essence; freedom and responsibility; anxiety; authenticity; the absurd")],
    img="A café in Paris's Saint-Germain-des-Prés, haunt of the post-war existentialists",
    lead="<b>Existentialism</b> is a family of philosophical views, prominent in 19th- and 20th-century Europe, holding that thinking begins with the experiencing individual: each person, thrown into a world without built-in meaning, defines themselves through free choices. The label was embraced by " + L("Jean-Paul_Sartre") + " in the 1940s and applied retrospectively to " + L("Søren_Kierkegaard") + " and " + L("Friedrich_Nietzsche") + "; some associated thinkers, such as Martin Heidegger and " + L("Albert_Camus") + ", rejected the term.",
    sections=[
      ("Themes", "<p>Sartre's formula 'existence precedes essence' denies a fixed human nature; with radical freedom come anguish, responsibility and the temptation of 'bad faith'. Camus explored the absurd — the clash between our demand for meaning and the world's silence — in <i>The Myth of Sisyphus</i>. Religious existentialists (Kierkegaard, Karl Jaspers, Gabriel Marcel) made faith central; atheistic existentialists drew opposite conclusions. The movement shaped post-war literature, theatre, psychology (Viktor Frankl, Rollo May) and theology.</p>"),
    ],
    seealso=["Søren_Kierkegaard", "Jean-Paul_Sartre", "Simone_de_Beauvoir", "Albert_Camus", "Nihilism"],
    outgoing=["Søren_Kierkegaard", "Friedrich_Nietzsche", "Jean-Paul_Sartre", "Simone_de_Beauvoir", "Albert_Camus", "Nihilism", "Philosophy", "Atheism"],
    unsure=[])

add(slug="Utilitarianism", title="Utilitarianism",
    infobox=[("Founders", "Jeremy Bentham; John Stuart Mill"), ("Class", "Consequentialism / normative ethics"), ("Core principle", "Actions are right insofar as they maximise overall well-being ('the greatest happiness principle')")],
    img="Title page of John Stuart Mill's Utilitarianism, first published in Fraser's Magazine, 1861",
    lead="<b>Utilitarianism</b> is a family of normative ethical theories holding that the morally best action is the one that maximises utility — usually understood as overall well-being or happiness minus suffering, for everyone affected. Systematised by " + L("Jeremy_Bentham") + " and " + L("John_Stuart_Mill") + ", it is the best-known form of consequentialism and a major influence on economics, public policy, animal ethics and effective altruism.",
    sections=[
      ("Variants and debates", "<p>Act utilitarians judge each act by its consequences; rule utilitarians judge rules whose general acceptance does best. Mill distinguished higher (intellectual) from lower pleasures to answer charges that utilitarianism is a 'doctrine worthy only of swine'. Critics object that it can licence injustice (punishing the innocent, violating rights) or demand superhuman self-sacrifice; defenders reply with two-level thinking and rights-protecting rules. Peter Singer's work on global poverty and animal liberation is its best-known modern continuation.</p>"),
    ],
    seealso=["Ethics", "Jeremy_Bentham", "John_Stuart_Mill", "Consequentialism", "Categorical_imperative"],
    outgoing=["Ethics", "Jeremy_Bentham", "John_Stuart_Mill", "Categorical_imperative", "Consequentialism", "Philosophy"],
    unsure=[])

print("part3 loaded", len(PAGES))

# ---------------- RELIGIONS ----------------
add(slug="Taoism", title="Taoism",
    infobox=[("Type", "Philosophy and religion"), ("Origin", "China, 4th century BC (textual tradition)"), ("Key texts", "Tao Te Ching; Zhuangzi; Daozang"), ("Key figures", "Laozi, Zhuangzi, Zhang Daoling"), ("Adherents", "Concentrated in China and the Chinese diaspora; diffuse worldwide influence")],
    img="A yin-yang symbol (taijitu) painted within a circle, surrounded by trigrams",
    lead="<b>Taoism</b> or <b>Daoism</b> is a family of Chinese philosophical and religious traditions centred on living in harmony with the <b>Tao</b> (Dao, 'the Way'), the source and pattern of the universe. Philosophical Taoism grows from the <i>Tao Te Ching</i>, attributed to " + L("Laozi") + ", and the <i>Zhuangzi</i>; religious Taoism, organised from the 2nd century AD, adds gods, rituals, alchemy, temples and priesthoods, and is one of China's five officially recognised religions.",
    sections=[
      ("Beliefs and practice", "<p>Core concepts include <i>wu wei</i> (effortless action), naturalness (<i>ziran</i>), simplicity, compassion, moderation and humility — the 'Three Treasures' — and balance symbolised by " + L("Yin_and_yang", "yin and yang") + ". Practices range from meditation and qigong to feng shui, Chinese medicine, ancestor rites and communal festivals; Taoist priests conduct funerals and exorcisms, and lineages such as Zhengyi and Quanzhen remain active. Taoist ideas profoundly influenced Buddhism's Chinese forms (especially Chan/Zen), Chinese art and literature, and modern Western spirituality.</p>"),
    ],
    seealso=["Laozi", "Tao_Te_Ching", "Yin_and_yang", "Confucianism", "Zen"],
    outgoing=["Laozi", "Tao_Te_Ching", "Yin_and_yang", "Confucianism", "Zen", "Buddhism", "Religion", "Philosophy"],
    unsure=["Adherent counts are notoriously hard to define for Taoism; no figure asserted"])

add(slug="Tao_Te_Ching", title="Tao Te Ching",
    infobox=[("Author", "Attributed to Laozi"), ("Language", "Classical Chinese"), ("Date", "Compiled c. 4th–3rd century BC"), ("Chapters", "81 (37 Tao, 44 Te in standard arrangement)"), ("Genre", "Philosophical / religious classic")],
    img="A bamboo-strip manuscript of the Tao Te Ching excavated at Mawangdui",
    lead="The <i><b>Tao Te Ching</b></i> (also <i>Daodejing</i>) is a Chinese classic and the foundational text of " + L("Taoism") + ", traditionally credited to the sage " + L("Laozi") + ". Its 81 short chapters of verse and paradox — opening 'The Tao that can be told is not the eternal Tao' — offer guidance on ruling, living and yielding that has made it one of the most translated works in world literature.",
    sections=[
      ("Content and transmission", "<p>The text's first part treats the Tao — ineffable source of all things — and the second <i>Te</i> (virtue/power), praising water-like softness, the usefulness of emptiness (a wheel's hub, a room's space), and government by non-action so that people 'transform themselves'. Silk manuscripts from Mawangdui (buried 168 BC) and bamboo slips from Guodian (c. 300 BC) are the earliest witnesses and differ in arrangement from the received Wang Bi edition. Commentaries by Heshang Gong and Wang Bi shaped its two-thousand-year reception.</p>"),
    ],
    seealso=["Laozi", "Taoism", "Zhuangzi", "Confucianism"],
    outgoing=["Laozi", "Taoism", "Zhuangzi", "Confucianism", "Yin_and_yang"],
    unsure=["Dating and stratigraphy of the text are scholarly reconstructions"])

add(slug="Yin_and_yang", title="Yin and yang",
    infobox=[("Tradition", "Chinese philosophy"), ("Concept", "Complementary interdependence of opposites"), ("Symbol", "Taijitu (yin-yang symbol)")],
    img="The taijitu: a circle divided by an S-curve into black and white halves, each containing a dot of the other",
    lead="<b>Yin and yang</b> is a concept in Chinese philosophy describing how opposite or contrary forces are complementary, interconnected and interdependent: dark and light, receptive and active, female and male, moon and sun. Neither pole is superior; each contains the seed of the other (shown by the dots in the taijitu symbol), and imbalance between them is the root of disharmony in the body, society and cosmos.",
    sections=[
      ("Applications", "<p>The idea, systematised in the <i>I Ching</i> tradition and correlative cosmology of the Han dynasty, underlies traditional Chinese medicine (health as balanced qi), feng shui, martial arts and " + L("Taoism") + " and " + L("Confucianism") + " alike. In the West it has become a popular emblem of balance and holistic thinking.</p>"),
    ],
    seealso=["Taoism", "Laozi", "Confucianism", "I_Ching"],
    outgoing=["Taoism", "Laozi", "Confucianism", "I_Ching", "Philosophy"],
    unsure=[])

add(slug="Confucianism", title="Confucianism",
    infobox=[("Type", "Philosophy / ethical tradition, sometimes classed as religion"), ("Founder", "Confucius (551–479 BC)"), ("Key texts", "Analects; the Five Classics; Mencius; Xunzi"), ("Key concepts", "Ren (benevolence), li (ritual propriety), filial piety, the junzi (exemplary person)")],
    img="A statue of Confucius in a temple courtyard in China",
    lead="<b>Confucianism</b> is an ethical and philosophical tradition originating with " + L("Confucius") + " (551–479 BC) that shaped the cultures of China, Korea, Japan and Vietnam for two millennia. It teaches that social harmony flows from cultivated character: benevolence (<i>ren</i>), ritual propriety (<i>li</i>), filial piety toward parents and ancestors, and rulers who govern by moral example rather than force.",
    sections=[
      ("Development", "<p>Mencius (4th century BC) argued human nature is innately good; Xunzi held it needs shaping by ritual. Under the Han dynasty Confucianism became state orthodoxy, with civil-service examinations on its classics lasting into 1905. Neo-Confucianism (Zhu Xi, 12th century) absorbed Buddhist and Taoist metaphysics and dominated East Asian thought until modern reforms — and the Cultural Revolution's campaigns — displaced it; interest has revived since the 1980s. Whether Confucianism is a religion (it includes ancestor veneration and state rites to Heaven) is long debated.</p>"),
    ],
    seealso=["Confucius", "Analects", "Taoism", "Chinese_philosophy"],
    outgoing=["Confucius", "Analects", "Taoism", "Religion", "Philosophy", "Mencius"],
    unsure=[])

add(slug="Analects", title="Analects",
    infobox=[("Author", "Compiled by disciples of Confucius"), ("Language", "Classical Chinese"), ("Date", "Compiled over the Warring States period; received form Han dynasty"), ("Structure", "20 books (chapters) of sayings and dialogues")],
    img="A woodblock-printed page of the Analects with commentary",
    lead="The <i><b>Analects</b></i> (Chinese: <i>Lunyu</i>, 'Selected Sayings') is a collection of sayings and ideas attributed to " + L("Confucius") + " and his contemporaries, compiled and edited by his followers over succeeding generations. It is the most revered text of " + L("Confucianism") + " and one of the Four Books canonised by Zhu Xi: for two thousand years its short dialogues and aphorisms ('Learning without thought is labour lost; thought without learning is perilous') were memorised by every literate East Asian schoolchild.",
    sections=[
      ("Content", "<p>The <i>Analects</i> present the Master teaching benevolence, ritual, filial piety and the rectification of names — let a ruler be a ruler, a father a father — through concrete exchanges rather than systematic treatise. Its portrait of Confucius (delighted in learning, grief-stricken for his favourite disciple Yan Hui, wryly aware of his political failure) shaped the ideal of the junzi, the exemplary person.</p>"),
    ],
    seealso=["Confucius", "Confucianism", "Tao_Te_Ching"],
    outgoing=["Confucius", "Confucianism", "Tao_Te_Ching", "Philosophy"],
    unsure=["Compilation history layered and disputed in detail"])

add(slug="Sikhism", title="Sikhism",
    infobox=[("Founder", "Guru Nanak (1469–1539)"), ("Origin", "Punjab, late 15th century"), ("Scripture", "Guru Granth Sahib"), ("Place of worship", "Gurdwara"), ("Holiest site", "Golden Temple (Harmandir Sahib), Amritsar"), ("Adherents", "c. 25–30 million worldwide")],
    img="The Golden Temple at Amritsar at dawn, its gilded facade reflected in the surrounding pool",
    lead="<b>Sikhism</b> is a monotheistic religion founded by Guru Nanak in the Punjab region of South Asia in the late 15th century. Sikhs believe in one God (<i>Ik Onkar</i>), the equality of all people, honest work, sharing with others (<i>vand chakko</i>) and selfless service (<i>seva</i>). Authority passed through ten human Gurus; the tenth, Guru Gobind Singh, vested it permanently in the scripture, the <i>Guru Granth Sahib</i>, and founded the Khalsa order in 1699. With roughly 25–30 million adherents, Sikhism is among the world's youngest major religions.",
    sections=[
      ("Beliefs and practice", "<p>Sikhs reject caste by birth, ritualism and ascetic withdrawal, aiming instead for a householder's life of devotion and action, overcoming the five vices (lust, anger, greed, attachment, pride). Worship centres on the gurdwara, where the <i>Guru Granth Sahib</i> is enthroned and the <i>langar</i> — a free vegetarian kitchen open to all — embodies equality. Initiated Khalsa Sikhs keep the Five Ks, including uncut hair (<i>kesh</i>) under a turban and a steel bracelet (<i>kara</i>). The Golden Temple in Amritsar, rebuilt in marble and gold in the early 19th century, is the faith's holiest shrine.</p>"),
      ("History", "<p>The Gurus led a community that, under Mughal persecution (two Gurus were martyred), became militarised in defence; Banda Singh Bahadur and later the Sikh Empire of Maharaja Ranjit Singh (1799–1849) ruled Punjab before British annexation. Partition in 1947 split Punjab between India and Pakistan; a large diaspora now lives in Canada, Britain and elsewhere. The 1984 storming of the Golden Temple by Indian troops and the anti-Sikh violence that followed remain defining traumas.</p>"),
    ],
    seealso=["Guru_Nanak", "Guru_Granth_Sahib", "Golden_Temple", "Punjab", "Hinduism"],
    outgoing=["Religion", "Guru_Nanak", "Guru_Granth_Sahib", "Golden_Temple", "Hinduism", "Islam"],
    unsure=["Adherent figures vary by source (25–30 million)"])

add(slug="Guru_Nanak", title="Guru Nanak",
    infobox=[("Born", "15 April 1469, Rai Bhoi di Talwandi (now Nankana Sahib, Pakistan)"), ("Died", "22 September 1539, Kartarpur"), ("Known for", "Founder of Sikhism; first of the ten Sikh Gurus"), ("Resting place", "Gurdwara Darbar Sahib, Kartarpur")],
    img="A traditional painting of Guru Nanak seated under a tree, with his companions Bhai Bala and Bhai Mardana",
    lead="<b>Guru Nanak</b> (1469–1539) was an Indian spiritual teacher who founded " + L("Sikhism") + " and is its first Guru. After a transformative experience around 1499 — tradition says he disappeared in a river for three days and emerged declaring 'There is no Hindu, there is no Muslim' — he spent decades travelling across Asia teaching, through poetry and song, devotion to one God, honest labour, and the equality of all people regardless of caste or creed.",
    sections=[
      ("Life and teaching", "<p>Born in the village of Talwandi (now Nankana Sahib in Pakistan), Nanak worked in a granary store before his calling. His four great journeys (<i>udasis</i>) took him, by tradition, across India and to Mecca, Baghdad and Tibet; historical scrutiny finds firm ground mainly in Punjab, but the travels became foundational legend. He settled at Kartarpur on the Ravi, farming with a community that sang his hymns — some 974 of which are in the <i>Guru Granth Sahib</i>. Before dying he named a disciple, Guru Angad, as successor, beginning the line of ten Gurus.</p>"),
    ],
    seealso=["Sikhism", "Guru_Granth_Sahib", "Golden_Temple"],
    outgoing=["Sikhism", "Guru_Granth_Sahib", "Golden_Temple", "Religion"],
    unsure=["Birth date also celebrated as Kartik Purnima; travel itineraries are partly traditional (janamsakhi) accounts"])

add(slug="Guru_Granth_Sahib", title="Guru Granth Sahib",
    infobox=[("Religion", "Sikhism"), ("Language", "Punjabi and other languages, in Gurmukhi script"), ("Compiled", "First version 1604 (Guru Arjan); final version 1705–06 (Guru Gobind Singh)"), ("Pages", "1,430 (standard printed edition)")],
    img="The Guru Granth Sahib enthroned under a canopy in a gurdwara, attended by a granthi with a fly-whisk",
    lead="The <i><b>Guru Granth Sahib</b></i> is the central scripture of " + L("Sikhism") + ", treated by Sikhs not merely as a book but as the eternal living Guru: it is enthroned in every gurdwara, fanned and attended, and put to rest at night. Compiled by Guru Arjan in 1604 and given final form by Guru Gobind Singh, its 1,430 pages contain hymns by six Sikh Gurus and by Hindu and Muslim saints including Kabir and Sheikh Farid, set to ragas and arranged by musical mode.",
    sections=[
      ("Status and use", "<p>Guru Gobind Singh ended the line of human Gurus in 1708, declaring the Granth and the community (Panth) his successors. A random opening reading (<i>hukamnama</i>) provides daily guidance, and continuous readings (<i>akhand path</i>) take about 48 hours. Its theology centres on remembrance of God's name (<i>nam simran</i>), the unity of God and the rejection of caste — radical inclusions for its time, since low-caste and Muslim voices share its sanctity.</p>"),
    ],
    seealso=["Sikhism", "Guru_Nanak", "Golden_Temple"],
    outgoing=["Sikhism", "Guru_Nanak", "Golden_Temple", "Religion"],
    unsure=[])

add(slug="Golden_Temple", title="Golden Temple",
    infobox=[("Location", "Amritsar, Punjab, India"), ("Religion", "Sikhism"), ("Founder", "Guru Ram Das (city, 1577); temple by Guru Arjan (1589–1604)"), ("Style", "Sikh architecture with Hindu and Islamic influences")],
    img="The Golden Temple (Harmandir Sahib) glowing at night, reflected in the Amrit Sarovar pool",
    lead="The <b>Golden Temple</b>, formally <b>Sri Harmandir Sahib</b> ('Abode of God'), is the holiest shrine of " + L("Sikhism") + ", standing on an island in the Amrit Sarovar ('Pool of Nectar') at Amritsar. Built by Guru Arjan — who deliberately set it lower than the surrounding city so visitors descend in humility, and open on four sides to welcome all — the present marble-and-gold structure dates largely from the era of Maharaja Ranjit Singh, who covered its upper floors in gilded copper in the 1830s.",
    sections=[
      ("Significance and history", "<p>The temple houses the <i>Guru Granth Sahib</i> by day and runs the world's largest free kitchen, serving tens of thousands of meals daily. Destroyed repeatedly by Afghan invaders in the 18th century, it was rebuilt each time. In June 1984 Indian Army troops stormed the complex to dislodge militants (Operation Blue Star), killing many and severely damaging the Akal Takht — an event that led to Indira Gandhi's assassination by her Sikh bodyguards and anti-Sikh pogroms, and still shapes Sikh politics.</p>"),
    ],
    seealso=["Sikhism", "Guru_Granth_Sahib", "Amritsar"],
    outgoing=["Sikhism", "Guru_Granth_Sahib", "Amritsar", "Religion"],
    unsure=["Daily langar meal counts vary widely in reports (50,000–100,000)"])

add(slug="Shinto", title="Shinto",
    infobox=[("Type", "Indigenous religion of Japan"), ("Key concept", "Kami (spirits/deities inhabiting places, phenomena, ancestors)"), ("Major shrines", "Ise Grand Shrine; Itsukushima Shrine; Fushimi Inari"), ("Texts", "Kojiki (712); Nihon Shoki (720) — mytho-historical chronicles")],
    img="A vermilion torii gate standing in the sea at Itsukushima Shrine, Miyajima",
    lead="<b>Shinto</b> ('the way of the kami') is the indigenous spiritual tradition of Japan, centred on ritual devotion to <i>kami</i> — sacred spirits associated with natural features, phenomena, places, ancestors and deities such as the sun goddess Amaterasu. It has no formal dogma or single scripture, emphasising ritual purity, festivals (<i>matsuri</i>) and harmony with the natural world, and it coexists syncretically with Buddhism in the lives of most adherents.",
    sections=[
      ("Practice and history", "<p>Worship takes place at tens of thousands of shrines (<i>jinja</i>), entered through torii gates and marked by sacred ropes (<i>shimenawa</i>); visitors wash for purification, offer coins, bow and clap to summon the kami. The imperial house claims descent from Amaterasu, and the Ise Grand Shrine is ritually rebuilt every twenty years. From 1868 to 1945 'State Shinto' made shrine observance a civic duty tied to emperor worship; after 1945 it was disestablished, while folk practice, New Year visits, weddings and festivals continue to structure Japanese life.</p>"),
    ],
    seealso=["Japan", "Buddhism", "Kami", "Animism"],
    outgoing=["Religion", "Buddhism", "Japan", "Kami", "Animism", "Taoism"],
    unsure=["Shrine counts (c. 80,000 affiliated) approximate"])

add(slug="Jainism", title="Jainism",
    infobox=[("Type", "Indian (dharmic) religion"), ("Key figure", "Mahavira (6th–5th century BC), 24th Tirthankara"), ("Core principles", "Ahimsa (non-violence), anekantavada (many-sidedness), aparigraha (non-possession)"), ("Scriptures", "Agamas"), ("Adherents", "c. 4–5 million, mainly in India")],
    img="A white marble Jain temple with intricate carved pillars at Ranakpur",
    lead="<b>Jainism</b> is an ancient Indian religion teaching a path to liberation through non-violence toward all living beings. Its followers revere 24 enlightened teachers (<i>Tirthankaras</i>), the last being Mahavira, a contemporary of the Buddha. Jains hold that the universe is eternal and uncreated, that every soul is potentially divine but weighed down by karma — conceived as a subtle material — and that liberation comes by shedding karma through asceticism and the 'three jewels': right faith, right knowledge, right conduct.",
    sections=[
      ("Practice", "<p>The supreme vow is <i>ahimsa</i>: Jains are strict vegetarians, avoid harming even insects (monks may wear mouth-cloths and sweep their path), and have excelled in commerce and scholarship partly through avoiding violent trades. The doctrine of <i>anekantavada</i> ('many-sidedness') holds that truth is too complex for any single viewpoint — the parable of the blind men and an elephant is Jain in origin. The faith split into two main sects, Digambara ('sky-clad', whose monks own nothing, not even robes) and Svetambara ('white-clad'), and its temples at Mount Abu and Ranakpur are masterpieces of marble carving.</p>"),
    ],
    seealso=["Mahavira", "Hinduism", "Buddhism", "Ahimsa", "Karma"],
    outgoing=["Religion", "Mahavira", "Hinduism", "Buddhism", "Karma", "India"],
    unsure=["Mahavira's dates (trad. 599–527 BC; scholarly c. 540–468 BC) vary"])

add(slug="Mahavira", title="Mahavira",
    infobox=[("Born", "Traditionally 599 BC, Kundagrama, near Vaishali (Bihar)"), ("Died", "Traditionally 527 BC, Pavapuri"), ("Known for", "24th and last Tirthankara of Jainism")],
    img="A serene seated statue of Mahavira in meditation posture, in white marble",
    lead="<b>Mahavira</b> ('Great Hero'), born Vardhamana, was an Indian ascetic teacher of the 6th–5th century BC, regarded by Jains as the 24th and last <i>Tirthankara</i> ('ford-maker') of the present age. A contemporary of the Buddha from the same region and milieu, he systematised the doctrines of " + L("Jainism") + " — above all absolute non-violence (<i>ahimsa</i>) — and organised a fourfold community of monks, nuns, laymen and laywomen that survives today.",
    sections=[
      ("Life", "<p>Tradition holds that Vardhamana, son of a local chief, renounced wealth at thirty, wandered naked for twelve years of harsh asceticism, and attained omniscience (<i>kevala jnana</i>) seated under a sal tree, after which he preached for thirty years and died at Pavapuri — where Diwali, for Jains, marks his liberation. Some scholars date him slightly later than tradition and regard the 23rd Tirthankara, Parshvanatha, as an earlier historical forerunner whose teachings Mahavira reformed.</p>"),
    ],
    seealso=["Jainism", "Buddhism", "Ahimsa", "Gautama_Buddha"],
    outgoing=["Jainism", "Buddhism", "Karma", "Religion"],
    unsure=["Dates follow Svetambara tradition; Digambara and scholarly datings differ"])

add(slug="Zoroastrianism", title="Zoroastrianism",
    infobox=[("Founder", "Prophet Zoroaster (Zarathustra)"), ("Origin", "Ancient Iran, possibly c. 1200–1000 BC"), ("God", "Ahura Mazda"), ("Scripture", "Avesta (including the Gathas)"), ("Key concepts", "Asha (truth/order) vs druj (lie); good thoughts, good words, good deeds; sacred fire")],
    img="A Zoroastrian fire temple flame burning in a silver urn, tended by a priest in white",
    lead="<b>Zoroastrianism</b> is one of the world's oldest monotheistic religions, founded by the prophet Zoroaster (Zarathustra) in ancient Iran. It worships Ahura Mazda, the Wise Lord, as the uncreated creator, and frames existence as a cosmic struggle between <i>asha</i> (truth, order) and <i>druj</i> (the lie), in which every person freely chooses a side — summed up in the maxim 'good thoughts, good words, good deeds'. It was the state religion of successive Persian empires for over a millennium.",
    sections=[
      ("History and influence", "<p>Zoroaster's hymns, the Gathas, are the oldest layer of the Avesta. Under the Achaemenid, Parthian and especially Sasanian empires the faith spread across the Iranian world; the Arab conquest of the 7th century AD reduced it, and refugees (the Parsis) carried it to Gujarat in India, where the community became prominent in trade, industry and science. Zoroastrian ideas — heaven and hell, final judgement, resurrection, a saviour, angels and a devil figure — plausibly influenced Second Temple Judaism and through it Christianity and Islam. Today perhaps 100,000–200,000 adherents remain, mainly Parsi and Iranian, facing demographic decline debated within the community.</p>"),
      ("Practice", "<p>Worship centres on fire temples, where a consecrated flame symbolises truth and purity; priests tend it in white garments with covered mouths. Traditional funerary practice exposed the dead in 'towers of silence' to vultures, avoiding pollution of earth, fire and water — a rite now restricted by law and by the collapse of vulture populations in India. Navroz, the spring new year, is the best-known festival.</p>"),
    ],
    seealso=["Zoroaster", "Iran", "Parsis", "Ahura_Mazda"],
    outgoing=["Religion", "Zoroaster", "Iran", "Parsis", "Ahura_Mazda", "Judaism", "Christianity", "Islam"],
    unsure=["Zoroaster's dates are highly uncertain (proposals range 1500–600 BC); adherent estimates vary"])

add(slug="Zoroaster", title="Zoroaster",
    infobox=[("Born", "Unknown; possibly c. 1200–1000 BC, eastern Iran/Central Asia"), ("Also known as", "Zarathustra; Zartosht"), ("Known for", "Prophet and founder of Zoroastrianism; author of the Gathas")],
    img="A traditional portrait of Zoroaster in white robes and turban, holding a staff, from a fire temple",
    lead="<b>Zoroaster</b>, also known as <b>Zarathustra</b>, was an Iranian religious reformer and prophet who founded " + L("Zoroastrianism") + ", among the earliest known monotheistic faiths. A priest (<i>zaotar</i>) by training, he proclaimed Ahura Mazda — the 'Wise Lord' — as the one uncreated God, rejecting the old gods (daevas) as demons, and taught that humans must actively choose truth over the lie. His hymns, the Gathas, composed in an archaic Avestan closely related to Vedic Sanskrit, are the only texts attributed directly to him.",
    sections=[
      ("Life and dating", "<p>Almost everything about Zoroaster's life is uncertain. Greek sources placed him absurdly early; Zoroastrian tradition dates him to '258 years before Alexander', suggesting the 7th–6th century BC, while linguistic evidence for the Gathas points several centuries earlier, perhaps 1200–1000 BC, in the steppes of Central Asia. Tradition tells of his laughing at birth, his revelation at thirty on a riverbank, persecution, and eventual conversion of King Vishtaspa. " + L("Friedrich_Nietzsche", "Nietzsche") + " borrowed his name for the prophet of <i>Thus Spoke Zarathustra</i> precisely because, as he saw it, the inventor of good-and-evil dualism should be the first to unmask it.</p>"),
    ],
    seealso=["Zoroastrianism", "Ahura_Mazda", "Friedrich_Nietzsche", "Avesta"],
    outgoing=["Zoroastrianism", "Ahura_Mazda", "Friedrich_Nietzsche", "Religion"],
    unsure=["Dates and homeland are among the most uncertain in religious history"])

add(slug="Baháʼí_Faith", title="Baháʼí Faith",
    infobox=[("Founder", "Baháʼu'lláh (1817–1892)"), ("Origin", "Persia (Iran), 19th century"), ("Scripture", "Kitáb-i-Aqdas; writings of Baháʼu'lláh, the Báb and ʻAbdu'l-Bahá"), ("Headquarters", "Baháʼí World Centre, Haifa, Israel"), ("Adherents", "Several million in over 200 countries")],
    img="The Shrine of the Báb on Mount Carmel, Haifa, with its golden dome and terraced gardens",
    lead="The <b>Baháʼí Faith</b> is a monotheistic religion founded by Baháʼu'lláh in 19th-century Persia, teaching the essential worth of all religions and the unity of all humanity. Baháʼís believe God progressively reveals His will through Manifestations — including Abraham, Moses, Jesus, Muhammad, the Buddha and Baháʼu'lláh — and that humanity is reaching maturity, called to abolish extremes of wealth and poverty, establish world peace, universal education and equality of the sexes.",
    sections=[
      ("History", "<p>The faith grew from the Bábí movement: in 1844 the Báb declared himself a herald of 'Him whom God shall make manifest', identified by Baháʼís as Baháʼu'lláh, who announced his own mission in Baghdad in 1863. Persecuted in Persia and exiled by the Ottomans to Acre, Baháʼu'lláh wrote the <i>Kitáb-i-Aqdas</i> (Book of Laws) and letters to the world's rulers. His son ʻAbdu'l-Bahá led the faith's spread to the West; the administrative order — elected local and national Spiritual Assemblies and the Universal House of Justice in Haifa — has no clergy. Baháʼís in Iran remain subject to severe persecution.</p>"),
    ],
    seealso=["Baháʼu'lláh", "Haifa", "Religion", "Iran"],
    outgoing=["Religion", "Iran", "Abraham", "Moses", "Jesus", "Muhammad"],
    unsure=["Adherent counts contested (estimates roughly 5–8 million); persecution toll figures from memory"])

print("part4 loaded", len(PAGES))

# ---------------- FIGURES, PLACES, CONCEPTS ----------------
add(slug="Abraham", title="Abraham",
    infobox=[("Known for", "Patriarch of Judaism, Christianity and Islam ('Abrahamic religions')"), ("Spouse", "Sarah (Sarai)"), ("Children", "Isaac and Ishmael (among others)"), ("Birthplace (tradition)", "Ur of the Chaldees")],
    img="A Baroque painting of the Binding of Isaac: Abraham raising the knife as the angel intervenes",
    lead="<b>Abraham</b> (originally <b>Abram</b>) is the common patriarch of the Abrahamic religions — Judaism, Christianity and Islam. In the Book of Genesis he is called by God to leave Mesopotamia for Canaan, receives the covenant marked by circumcision and the promise of descendants 'as the stars', and proves his faith by his willingness, in the Binding of Isaac, to sacrifice his son before God provides a ram instead. Jews trace descent through his son Isaac, Arabs and Islam through his son Ishmael; Muhammad is remembered as restoring Abraham's pure monotheism at the Kaaba in Mecca.",
    sections=[
      ("In the three traditions", "<p>For Judaism, Abraham is the first patriarch and model of faith and hospitality. Christianity, following Paul, makes him the exemplar of justification by faith. In Islam, Ibrahim is a prophet and 'friend of God', builder with Ishmael of the " + L("Kaaba") + " and archetypal <i>hanif</i> (pure monotheist); the festival Eid al-Adha commemorates his willingness to sacrifice. Historicity is debated: the narratives are usually dated as literary compositions of the first millennium BC, and no extra-biblical evidence for Abraham himself exists, though the world they describe fits the early second millennium BC in many details.</p>"),
    ],
    seealso=["Judaism", "Christianity", "Islam", "Moses", "Kaaba", "Søren_Kierkegaard"],
    outgoing=["Judaism", "Christianity", "Islam", "Moses", "Kaaba", "Søren_Kierkegaard", "Bible", "Quran"],
    unsure=["Historicity widely debated; framing here follows mainstream scholarship from memory"])

add(slug="Temple_Mount", title="Temple Mount",
    infobox=[("Location", "Old City of Jerusalem"), ("Religions", "Judaism, Islam, Christianity"), ("Key structures", "Dome of the Rock; Al-Aqsa Mosque; Western Wall (retaining wall)")],
    img="Aerial view of the Temple Mount with the golden Dome of the Rock and Al-Aqsa Mosque",
    lead="The <b>Temple Mount</b> (Hebrew: <i>Har haBayit</i>; Arabic: <i>al-Haram al-Sharif</i>, 'the Noble Sanctuary') is a walled hilltop compound in the Old City of Jerusalem, among the most sacred and contested religious sites on earth. For Judaism it is the site of the First and Second Temples and, in tradition, of the binding of Isaac; for Islam it is the place of Muhammad's Night Journey and ascension, crowned by the Dome of the Rock (built 691–92 AD) and Al-Aqsa Mosque.",
    sections=[
      ("History and status quo", "<p>Herod the Great massively expanded the platform in the 1st century BC; Rome destroyed the Second Temple in 70 AD, leaving the " + L("Western_Wall") + " as its surviving retaining wall. Muslim rule from the 7th century built the shrines; Crusaders, Ayyubids, Mamluks and Ottomans succeeded one another. Since 1967 Israel controls security while the Jordanian-linked Waqf administers the compound; under the 'Status Quo', non-Muslims may visit but not pray there — rules whose every breach risks violence, making the Mount a perennial flashpoint of the Israeli–Palestinian conflict.</p>"),
    ],
    seealso=["Western_Wall", "Jerusalem", "Dome_of_the_Rock", "Al-Aqsa_Mosque"],
    outgoing=["Western_Wall", "Jerusalem", "Judaism", "Islam", "Church_of_the_Holy_Sepulchre"],
    unsure=["Some architectural dates (Al-Aqsa rebuilding phases) condensed"])

add(slug="Western_Wall", title="Western Wall",
    infobox=[("Location", "Old City of Jerusalem"), ("Religion", "Judaism"), ("Also known as", "Kotel; Wailing Wall; al-Buraq Wall in Islamic tradition"), ("Constructed", "c. 19 BC (Herod the Great)")],
    img="Jewish worshippers praying at the Western Wall, notes pressed into the cracks between its stones",
    lead="The <b>Western Wall</b> (the <b>Kotel</b>) is an ancient limestone wall in the Old City of Jerusalem and one of the holiest sites in Judaism. It is not part of the Temple itself but a retaining wall of Herod the Great's vast expansion of the " + L("Temple_Mount") + " plaza around 19 BC — the closest place to the site of the destroyed Temples where Jewish prayer has traditionally been permitted, facing the Holy of Holies.",
    sections=[
      ("Practice and history", "<p>Worshippers pray in a plaza divided by gender according to Orthodox custom, and press written prayers into the wall's cracks (periodically removed and buried on the Mount of Olives). The visible section is about 57 metres long; the wall continues underground and along a tunnel northward. Under the name al-Buraq Wall, the site is also significant in Islam as where Muhammad tethered his steed al-Buraq. Control of the wall was a focus of conflict in 1929, and its capture in 1967 — paratroopers at the Wall — is an iconic moment in Israeli history.</p>"),
    ],
    seealso=["Temple_Mount", "Jerusalem", "Judaism", "Second_Temple"],
    outgoing=["Temple_Mount", "Jerusalem", "Judaism", "Islam"],
    unsure=["Exposed length figure (~57 m) from memory; total wall length c. 488 m"])

add(slug="Church_of_the_Holy_Sepulchre", title="Church of the Holy Sepulchre",
    infobox=[("Location", "Christian Quarter, Old City of Jerusalem"), ("Religion", "Christianity"), ("Consecrated", "335 AD (original church of Constantine)"), ("Custodians", "Greek Orthodox, Armenian Apostolic, Roman Catholic (Franciscan) and others under the Status Quo")],
    img="The stone facade and bell tower of the Church of the Holy Sepulchre, Jerusalem",
    lead="The <b>Church of the Holy Sepulchre</b> is a church in the Christian Quarter of Jerusalem's Old City, venerated by most Christians as the site of Jesus's crucifixion (Calvary/Golgotha), burial and resurrection. First built under Emperor Constantine and consecrated in 335 AD on a site identified by his mother Helena, it encloses the last stations of the Via Dolorosa and the empty tomb (the Aedicule), and has been a supreme goal of pilgrimage for seventeen centuries.",
    sections=[
      ("History and the Status Quo", "<p>The church was destroyed by the Fatimid caliph al-Hakim in 1009, rebuilt with Byzantine help, and taken over and enlarged by the Crusaders (the present building is substantially theirs, rededicated 1149). Six Christian communities share it under a fragile 'Status Quo' codified in Ottoman decrees (1757, 1852s): rights over every stone, lamp and cleaning duty are specified to the centimetre — a ladder left on a ledge since the 18th century, the famous 'immovable ladder', symbolises the arrangement. Two Muslim families have held the key and opened the door daily since the time of Saladin, by tradition.</p>"),
    ],
    seealso=["Jesus", "Jerusalem", "Crusades", "Eastern_Orthodox_Church"],
    outgoing=["Jesus", "Jerusalem", "Christianity", "Temple_Mount"],
    unsure=["Dating of the Status Quo firman (1757 / 1852) and ladder's first record are commonly cited figures"])

add(slug="Mythology", title="Mythology",
    infobox=[("Field", "Folklore, religious studies, anthropology"), ("Key traditions", "Greek, Norse, Egyptian, Hindu, Mesopotamian, Japanese, Indigenous traditions worldwide")],
    img="Illustration of Zeus hurling a thunderbolt from Mount Olympus",
    lead="<b>Mythology</b> is both the body of myths belonging to a culture or religion — traditional stories involving gods, heroes and the origins of the world and customs — and the scholarly study of such stories. Myths explain creation, natural phenomena, death and social norms; their interpretation has been pursued through comparative mythology, ritual theory, psychology (Freud, Jung) and structuralism (Claude Lévi-Strauss).",
    sections=[
      ("Functions and study", "<p>Bronisław Malinowski argued myth is a 'charter' validating institutions; Mircea Eliade stressed myths of origin re-enacted in ritual; Joseph Campbell's 'monomyth' or hero's journey (1949) claimed a universal pattern, hugely influential on storytelling though criticised by folklorists. Modern scholarship generally treats myth as a genre of traditional narrative whose truth-status within its culture is more complex than 'false story', and compares motifs — flood myths, dying-and-rising gods, world trees — across traditions.</p>"),
    ],
    seealso=["Greek_mythology", "Norse_mythology", "Religion", "Folklore"],
    outgoing=["Greek_mythology", "Norse_mythology", "Religion", "Folklore", "Zeus", "Odin"],
    unsure=[])

add(slug="Greek_mythology", title="Greek mythology",
    infobox=[("Origin", "Ancient Greece; sources include Hesiod's Theogony, Homer, Apollodorus"), ("Principal deities", "The twelve Olympians, led by Zeus"), ("Sacred centre", "Mount Olympus")],
    img="A classical painting of the gods feasting on Mount Olympus",
    lead="<b>Greek mythology</b> is the body of myths and legends of the ancient Greeks concerning their gods and heroes, the nature of the world, and the origin and meaning of their rituals. From Hesiod's <i>Theogony</i> (c. 700 BC), which orders the generations of gods from Chaos and Gaia to the Olympians, through Homer's <i>Iliad</i> and <i>Odyssey</i>, the myths formed the shared imaginative world of Greek culture and, through Rome, of the Western tradition.",
    sections=[
      ("The Olympians and heroes", "<p>Twelve gods dwell on Mount Olympus under Zeus, hurler of thunderbolts: Hera, Poseidon, Demeter, Athena, Apollo, Artemis, Ares, Aphrodite, Hephaestus and Hermes, with Dionysus or Hestia completing the count and Hades ruling the underworld below. Around them cluster myths of heroes — Heracles and his twelve labours, Perseus and Medusa, Theseus and the Minotaur, Jason and the Argonauts, Achilles and Odysseus — and of mortals punished for hubris, from Prometheus (who stole fire for mankind) to Icarus and Narcissus. Greek myth remains endlessly retold in literature, art, psychology (Oedipus, narcissism) and popular culture.</p>"),
    ],
    seealso=["Mythology", "Zeus", "Ancient_Greece", "Norse_mythology"],
    outgoing=["Mythology", "Zeus", "Ancient_Greece", "Norse_mythology", "Heracles", "Odysseus"],
    unsure=["Twelve-Olympian roster varies by source (Hestia/Dionysus) — standard note"])

add(slug="Norse_mythology", title="Norse mythology",
    infobox=[("Origin", "Scandinavia and the Norse world; sources: Poetic Edda, Prose Edda (Snorri Sturluson, c. 1220)"), ("Principal deities", "Odin, Thor, Freyr, Freyja, Loki"), ("Cosmology", "Yggdrasil, the world tree; Ragnarök, the prophesied end")],
    img="Thor wielding his hammer Mjölnir against the giants, lightning in a stormy sky",
    lead="<b>Norse mythology</b> is the body of myths of the North Germanic peoples, drawn chiefly from Old Norse texts of medieval Iceland — the anonymous poems of the <i>Poetic Edda</i> and Snorri Sturluson's <i>Prose Edda</i> (c. 1220). It tells of Odin, one-eyed seeker of wisdom; Thor, defender of gods and men; the trickster Loki; and a cosmos held in the branches of the world tree Yggdrasil, doomed to end in fire and flood at Ragnarök — after which a renewed world rises from the sea.",
    sections=[
      ("Myths and legacy", "<p>Creation begins with ice and fire meeting in the void Ginnungagap; the first gods dismember the giant Ymir to build earth, sea and sky. Tales include Odin hanging on the tree to win the runes, Thor fishing for the World Serpent, and Baldr's death through Loki's malice — the first link in the chain to Ragnarök. Christianisation ended cult practice, but the myths survived in Icelandic manuscripts and now permeate modern fantasy, from Wagner's <i>Ring</i> to Tolkien and Marvel's Thor.</p>"),
    ],
    seealso=["Mythology", "Odin", "Thor", "Vikings", "Greek_mythology"],
    outgoing=["Mythology", "Odin", "Thor", "Greek_mythology", "Religion"],
    unsure=[])

add(slug="Sufism", title="Sufism",
    infobox=[("Religion", "Islam"), ("Focus", "Inward, mystical dimension of Islam; direct experience of God"), ("Key figures", "Rumi, Ibn Arabi, Al-Ghazali, Rabia al-Adawiyya"), ("Practices", "Dhikr (remembrance), sama (music/whirling), master–disciple guidance (tariqa)")],
    img="Whirling dervishes of the Mevlevi order performing the sema ceremony in white robes",
    lead="<b>Sufism</b> (Arabic: <i>Tasawwuf</i>) is the mystical tradition of " + L("Islam") + ", emphasising the inward search for God and purification of the heart from ego. Sufis seek experiential knowledge of the divine through remembrance (<i>dhikr</i>), meditation, music and poetry, usually within an order (<i>tariqa</i>) tracing a chain of teachers back to the Prophet Muhammad.",
    sections=[
      ("History and influence", "<p>Early ascetics such as Rabia of Basra (8th century) taught disinterested love of God; " + L("Al-Ghazali") + " reconciled Sufism with orthodox theology. The great orders — Qadiriyya, Naqshbandiyya, Chishtiyya, Mevleviyye (the 'whirling dervishes' founded around Rumi) — spread Islam across Africa and Asia. Sufi poets — Rumi, Hafez, Attar, Kabir — produced some of the world's most beloved religious literature; Rumi's <i>Masnavi</i> is often called 'the Quran in Persian'. Modern reformist movements sometimes condemn Sufi shrine practices, yet Sufism remains a major, often moderate, force in Muslim life.</p>"),
    ],
    seealso=["Islam", "Al-Ghazali", "Rumi", "Mysticism"],
    outgoing=["Islam", "Al-Ghazali", "Rumi", "Mysticism", "Religion"],
    unsure=[])

add(slug="Karma", title="Karma",
    infobox=[("Traditions", "Hinduism, Buddhism, Jainism, Sikhism"), ("Concept", "Moral law of cause and effect governing rebirth (samsara)"), ("Goal", "Liberation (moksha/nirvana) from the karma-driven cycle")],
    img="A stylised wheel symbolising samsara, the cycle of birth and rebirth",
    lead="<b>Karma</b> (Sanskrit: 'action, deed') is the spiritual principle of cause and effect in Indian religions: the moral quality of a person's intentional actions shapes their future experiences and the circumstances of their rebirth within <i>samsara</i>, the cycle of birth, death and rebirth. Liberation from the cycle — <i>moksha</i> or <i>nirvana</i> — is the soteriological goal of " + L("Hinduism") + ", " + L("Buddhism") + ", " + L("Jainism") + " and " + L("Sikhism") + ", each interpreting karma's mechanics differently.",
    sections=[
      ("Interpretations", "<p>In Hindu thought karma operates under divine order and devotion can mitigate it; in Jainism karma is a fine material substance that literally sticks to the soul and is burnt off by asceticism; Buddhism, denying a permanent soul, treats karma as intention (<i>cetana</i>) whose ripening conditions rebirth without a transmigrating self. In the modern West 'karma' has entered popular speech as a loose idea of cosmic payback — a simplification scholars contrast with the traditions' subtler accounts.</p>"),
    ],
    seealso=["Reincarnation", "Samsara", "Moksha", "Nirvana", "Dharma"],
    outgoing=["Hinduism", "Buddhism", "Jainism", "Sikhism", "Reincarnation", "Moksha", "Nirvana"],
    unsure=["Popular formulations vary; section reflects common scholarly summaries"])

add(slug="Zen", title="Zen",
    infobox=[("Tradition", "Mahayana Buddhism"), ("Origin", "China (as Chan), transmitted to Japan from the 12th century"), ("Key practices", "Zazen (seated meditation), koans, mondo"), ("Major schools", "Soto, Rinzai (Japan); Chan (China); Seon (Korea); Thiền (Vietnam)")],
    img="A Zen rock garden of raked gravel and stones at Ryōan-ji temple, Kyoto",
    lead="<b>Zen</b> is a school of Mahayana " + L("Buddhism") + " that originated in China as Chan during the Tang dynasty and spread to Vietnam, Korea and Japan, where as Zen it took its best-known forms. It emphasises direct experience over scripture and doctrine: awakening (<i>satori</i>, <i>kensho</i>) is pursued through seated meditation (<i>zazen</i>), paradoxical koan stories ('What is the sound of one hand clapping?'), and the guidance of a master, aiming at seeing one's true nature.",
    sections=[
      ("History and influence", "<p>Legend traces Zen to the Buddha's silent 'flower sermon' and to Bodhidharma, who brought it to China. In Japan, Eisai founded the Rinzai school (koan-centred) and Dogen the Soto school ('just sitting', <i>shikantaza</i>), whose writings are philosophical classics. Zen deeply marked Japanese arts — ink painting, tea ceremony, gardens, haiku, martial arts — and, from the writings of D. T. Suzuki and the Beats onward, Western art, literature and psychology; secular mindfulness derives in part from it.</p>"),
    ],
    seealso=["Buddhism", "Meditation", "Taoism", "Dogen"],
    outgoing=["Buddhism", "Taoism", "Meditation", "Religion", "Japan"],
    unsure=[])

add(slug="Atheism", title="Atheism",
    infobox=[("Position", "Absence of belief in the existence of gods"), ("Related terms", "Agnosticism, humanism, 'new atheism'")],
    img="The 'atomic whirl' symbol of atheism, an atom with an A at its centre",
    lead="<b>Atheism</b>, in its broadest sense, is an absence of belief in the existence of deities; more narrowly it is the position that there are no gods. Atheistic arguments and traditions are ancient — present in Indian materialism (Charvaka), Greek thought (the atomists, Euhemerus) and Chinese philosophy — but the identity 'atheist' became publicly assertable mainly in the Enlightenment and after. Modern surveys vary widely by country, and definitions (belief versus knowledge, hence the atheism/agnosticism distinction) matter to the counts.",
    sections=[
      ("Arguments and movements", "<p>Standard atheological arguments include the problem of evil, inconsistencies among divine attributes, the lack of empirical evidence ('extraordinary claims'), and naturalistic explanations of religion's origins. The 2000s 'New Atheism' of Richard Dawkins, Christopher Hitchens, Sam Harris and Daniel Dennett popularised assertive critique of religion; critics within and beyond atheism debate its tones and politics. Atheists remain a persecuted minority in some states (apostasy laws) while forming large minorities or pluralities in much of Europe and East Asia.</p>"),
    ],
    seealso=["Agnosticism", "Humanism", "Philosophy_of_religion", "Secularism", "Problem_of_evil"],
    outgoing=["Philosophy_of_religion", "Humanism", "Secularism", "Problem_of_evil", "Religion", "Agnosticism"],
    unsure=["Global adherence percentages intentionally not asserted (methodologies differ)"])

add(slug="Nihilism", title="Nihilism",
    infobox=[("Field", "Philosophy"), ("Core claim", "Life/world lacks inherent meaning, value or truth (forms vary)"), ("Key figures", "Friedrich Nietzsche (diagnostician and critic), Ivan Turgenev (popularised term)")],
    img="A dark abstract painting of a void, evoking the nihilist abyss",
    lead="<b>Nihilism</b> (from Latin <i>nihil</i>, 'nothing') is a family of views that the world, or aspects of it, lacks inherent meaning, purpose, truth or value. Existential nihilism denies life's intrinsic meaning; moral nihilism denies objective morality; epistemological nihilism denies knowledge. The term was popularised by Turgenev's novel <i>Fathers and Sons</i> (1862) for Russian radicals, and philosophically deepened by " + L("Friedrich_Nietzsche") + ", who treated nihilism as the defining danger of the modern age — the collapse of the highest values after the 'death of God' — to be overcome, not celebrated.",
    sections=[
      ("Responses", "<p>Thinkers respond differently: existentialists urge creating meaning through commitment; " + L("Albert_Camus") + " prescribed revolt in lucid defiance of the absurd; religious thinkers see nihilism as the consequence of abandoning transcendence. Nietzsche's own answer — amor fati, the Übermensch, eternal recurrence willed as affirmation — remains disputed.</p>"),
    ],
    seealso=["Existentialism", "Friedrich_Nietzsche", "Albert_Camus", "Absurdism"],
    outgoing=["Friedrich_Nietzsche", "Albert_Camus", "Existentialism", "Philosophy"],
    unsure=[])

add(slug="Pantheism", title="Pantheism",
    infobox=[("Position", "God is identical with the universe / nature"), ("Key figures", "Baruch Spinoza; echoes in Stoicism, Advaita Vedanta, some modern thought")],
    img="Sunlight streaming through an ancient forest canopy, suggesting divinity in nature",
    lead="<b>Pantheism</b> is the belief that reality and divinity are identical — that God is the universe itself, or that everything composes an all-encompassing God. Its classic philosophical statement is " + L("Baruch_Spinoza") + "'s <i>Deus sive Natura</i> ('God or Nature'), for which he was long branded an atheist and later hailed as 'the God-intoxicated man'. Kindred ideas appear in " + L("Stoicism") + "'s divine logos pervading the cosmos and in aspects of Hindu thought; Albert Einstein invoked Spinoza's God as the object of his 'cosmic religion'.",
    sections=[
      ("Variants and debates", "<p>Deterministic pantheism (Spinoza) contrasts with panentheism, which holds the universe is in God but God exceeds it. Critics ask whether pantheism adds anything to naturalism beyond reverent vocabulary; defenders answer that it names a religious attitude toward nature with real ethical consequences for ecology.</p>"),
    ],
    seealso=["Baruch_Spinoza", "Stoicism", "Monism", "Philosophy_of_religion"],
    outgoing=["Baruch_Spinoza", "Stoicism", "Philosophy_of_religion", "Religion"],
    unsure=[])

print("part5 loaded", len(PAGES))

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
                        "depth": 7, "status": "skipped-duplicate", "crawler": "AD", "built_at": None,
                        "unsure": ["Page already existed on disk at Crawler AD start"], "outgoing": [url_of(s) for s in p.get("outgoing", [])]})
        skipped.append(url)
        continue
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page_html(p))
    records.append({"url": url, "local_path": local, "source_url": "https://en.wikipedia.org/wiki/Philosophy",
                    "depth": 7, "status": "built", "crawler": "AD", "built_at": NOW,
                    "unsure": p.get("unsure", []), "outgoing": [url_of(s) for s in p.get("outgoing", [])]})
    built.append(url)

built_set = set(built)
for target, source in sorted(all_outgoing.items()):
    if target in built_set:
        continue
    slug = target.split("/wiki/")[-1]
    path = os.path.join(WIKI, urllib.parse.unquote(slug), "index.html")
    if os.path.exists(path):
        continue
    records.append({"url": target, "local_path": "web/en.wikipedia.org/wiki/%s/index.html" % slug,
                    "source_url": source, "depth": 8, "status": "queued", "crawler": "AD", "built_at": None,
                    "unsure": [], "outgoing": []})

with open(LEDGER, "a", encoding="utf-8") as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("BUILT:", len(built))
for u in built: print("  ", u)
print("SKIPPED-DUP:", len(skipped), skipped)
print("QUEUED records:", sum(1 for r in records if r["status"] == "queued"))
