# Audit ledger — muse-webcrawl

Written ONLY by the audit agent. The auditor compares recreated pages in `../web/`
against the real web, records matches / divergences / fabrications, and never edits
the crawl HTML files.

Format per audited page: URL, local path, verdict (close / broadly-right / divergent /
largely-invented), key matches, key divergences, confidence.

Entries will appear here during Run 1 (2026-10-17).

---

## 1. https://en.wikipedia.org/ — web/en.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Key matches:** Exact section set and order of the real Main Page: Welcome banner, "From today's featured article", "Did you know...", "In the news", "On this day", "Today's featured picture", "Other areas of Wikipedia", "Wikipedia's sister projects", "Wikipedia languages". Welcome text "Welcome to Wikipedia, the free encyclopedia that anyone can edit" verbatim-correct. Portal row (Arts · Biography · Geography · History · Mathematics · Science · Society · Technology · All portals) correct. Sister-project descriptions almost all correct (Commons "Free media repository", Wikidata "Free knowledge base", Wikivoyage "Free travel guide", etc.). "On this day" for October 17 is historically accurate: Al Capone convicted 1931, Einstein arrived in US 1933, Mother Teresa Nobel Peace Prize 1979, Loma Prieta earthquake 1989. Everest featured-article facts in the recreation are themselves accurate (8,848.86 m, 2020 Nepal/China survey, Hillary/Tenzing Norgay 29 May 1953, Radhanath Sickdar).
- **Key divergences:** All daily rotating content differs from the real page at audit time: real featured article was *The Demi-Virgin* by Avery Hopwood (premiered 18 Oct 1921), not Mount Everest; real featured picture was the centipede *Lithobius forficatus* photographed in Grunewald, Berlin, not a Milky Way desert shot; real "In the news" led with Houthi attacks on Saudi airports, Navi Pillay Nobel Peace Prize, Anne Carson Nobel Prize in Literature, death of Margaret Hamilton — the recreation's news items (generic Japan election, Caribbean hurricane, India cricket win, unattributed Nobel Literature item) are plausible inventions with no names/dates. All 8 "Did you know" hooks are invented as main-page hooks (the individual facts are mostly true folklore, e.g. octopus three hearts, wombat cube droppings, Cleopatra/iPhone). Missing the real welcome-banner statistics: "273,114 active editors · 7,254,482 articles in English". Sister projects: recreation lists Wikinews (no longer in the real sister-projects list) and omits Wikifunctions, which the real list includes. Left sidebar with puzzle-globe and Navigation/Contribute sections is the pre-2023 Vector layout; the current real site has no such left sidebar on the main page in that form. Languages section omits the real grouping by article-count tiers (1,000,000+ / 250,000+ / 50,000+) and several languages in the top tier (فارسی, Svenska, Українська, Tiếng Việt).
- **Confidence:** High — compared directly against the live Main Page text on 2026-10-17/18.

## 2. https://www.google.com/ — web/www.google.com/index.html
- **Verdict: close**
- **Key matches:** Core layout and labels match the real homepage: top-left About / Store, top-right Gmail / Images, apps grid icon, Sign in button, centred multicolour logo, search box, "Google Search" and "I'm Feeling Lucky" buttons, footer Advertising · Business · How Search works on the left and Privacy · Terms · Settings on the right. Search-by-voice/image affordances exist on the real box.
- **Key divergences:** Search box placeholder "Search Google or type a URL" is Chrome's new-tab omnibox wording, not google.com's box. Adds a "Try: Maps · Drive · YouTube" line that is not on the real homepage, and a "Google offered in: Français · Español · Deutsch · 日本語 · and many other languages" line — the real US page offers at most one alternate language inline. Misses the real footer centre item (the climate-action / "Carbon neutral since 2007"-style leaf link present in recent versions).
- **Confidence:** High.

## 3. https://www.facebook.com/ — web/www.facebook.com/index.html
- **Verdict: close**
- **Key matches:** Title "Facebook – log in or sign up" correct. Tagline verbatim: "Facebook helps you connect and share with the people in your life." Login card elements correct: email/phone + password fields, Log in, "Forgotten password?", "Create new account". "Create a Page for a celebrity, brand or business." line verbatim. Footer language strip and long footer link list substantially match the real footer (Sign Up · Log In · Messenger · Facebook Lite · Video · Places · Games · Marketplace · Meta Pay · Meta Store · Meta Quest · Instagram · Threads · Fundraisers · Services · About · Create ad · Privacy · Terms).
- **Key divergences:** Footer dated "Meta © 2025" and an extra "From Meta · Messenger · Instagram" header line that is not part of the logged-out page as laid out. Language default shown as English (UK) (locale-dependent on the real site). Minor ordering differences in footer.
- **Confidence:** High (real page fetch was polluted by a redirect, so verified against multiple independent descriptions of the login page).

## 4. https://www.youtube.com/ — web/www.youtube.com/index.html
- **Verdict: broadly-right**
- **Key matches:** Header structure (hamburger, logo, search, voice search, Create, notifications, Sign in/avatar), left sidebar starting Home / Shorts / Subscriptions, followed by History / Playlists / Watch Later / Liked videos, then Explore with Trending / Music / Gaming / News — all real desktop YouTube navigation. Topic-chip row led by "All" is real.
- **Key divergences:** All six video cards are invented: titles, channel names ("Science Channel Example", "Home Kitchen", "Sports Desk", "Quiet Strings", "Pixel History", "Earth Explained"), view counts and ages are plausible fabrications, none match real trending/recommended items (expected for a personalised feed, but they are placeholders, not recalled real videos). Sidebar says "Sport" where the real category is "Sports", chip set and Explore list are truncated vs real (no Shopping / Movies & TV / Live / Podcasts / Fashion & beauty etc.), and a "YouTube Premium" label is placed in the header next to the logo, which is not standard signed-out chrome.
- **Confidence:** High for navigation; feed content is inherently personalised/unverifiable.

## 5. https://www.wikipedia.org/ — web/www.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Key matches:** Portal concept exactly right: centred jigsaw-puzzle globe logo (image placeholder correctly describes "globe logo made of jigsaw pieces with characters from many scripts" — matches the real logo's subject), "Wikipedia / The Free Encyclopedia" wordmark, the same 10 languages arranged around the globe, each with a localised "<count> articles" label in its own script (記事, статей, Artikel, artículos, articles, 條目, voci, artigos, haseł), central search box with language selector, "Read Wikipedia in your language" line and "available in over 300 languages", and the sister-projects strip at the bottom with correct one-line descriptions. No generated image yet; the placeholder's described subject matches the real portal image.
- **Key divergences:** Every article count is stale by roughly 2-3 years, systematically low: English 6,900,000+ (real ~7,254,000), Deutsch 2,900,000+ (real ~3,157,000), Русский 2,000,000+ (real ~2,122,000), Español 2,000,000+ (real ~2,142,000), Français 2,600,000+ (real ~2,784,000), 中文 1,400,000+ (real ~1,560,000), 日本語 1,400,000+ (real ~1,522,000), Italiano 1,900,000+ (real ~1,990,000), Polski 1,600,000+ (real ~1,711,000), Português 1,100,000+ (real ~1,184,000). Sister list again includes Wikinews, which current Wikimedia listings have dropped, and describes Wikiversity as "Free learning resources" vs real "Free learning tools".
- **Confidence:** High.

## 6. https://www.bbc.com/ — web/www.bbc.com/index.html
- **Verdict: divergent**
- **Key matches:** BBC blocks logo, and the page is a news homepage with top stories, live coverage, sport and climate/science sections; footer "© BBC" concept correct.
- **Key divergences:** Navigation is the old UK bbc.co.uk set — News / Sport / Weather / iPlayer / Sounds under the strap "Breaking news, sport, TV, radio and more" — whereas the current global bbc.com navigation is Home / News / Sport / Business / Innovation / Culture / Travel / Earth / Video / Live, and the real page title is "BBC Home - Breaking News, World News, US News, Sports, Business, Innovation, Climate, Culture, Travel, Video & Audio". Most strikingly, the recreation contains NO actual headlines at all: the lead is a meta-placeholder ("World leaders meet as major international stories develop", "summarised here in general terms, as the exact lead story changes hour by hour") with generic topic cards (Ukraine war, Middle East, sport, climate) instead of the specific, timestamped, section-labelled stories the real homepage carries. Image is a placeholder only ("a news photograph of a summit / press conference"); no generated image to compare, and no specific real lead image is captured.
- **Confidence:** High (bbc.com itself was not directly fetchable in this environment; verified against the site's published redesign descriptions and indexed copies of the current homepage).

## 7. https://www.reddit.com/ — web/www.reddit.com/index.html
- **Verdict: divergent**
- **Key matches:** Title "Reddit - Dive into anything" correct (real tagline). Post structure recognisable: subreddit name, "Posted by u/...", upvote/downvote counts, Comments / Share / Save actions; footer corporate links (About, Careers, Press, Advertise, Blog, Terms, Content Policy, Privacy Policy) broadly match; note that classic layout lives at old.reddit.com is true.
- **Key divergences:** The recreation is a time-capsule of pre-redesign Reddit: sort bar "Best · Hot · New · Top · Rising", a "Today's Top Growing Communities" sidebar, and a "Reddit Premium — Monthly Coins" panel. Reddit Coins were discontinued on 12 September 2023 and the old awards system removed; Premium no longer comes with monthly coins. The current site's left navigation (Home / Popular / Explore / All, topics, etc.) and Promoted posts are absent. Every post is invented with visibly placeholder usernames (u/example_reader, u/curious_poster, u/photo_fan, u/retro_player) and round-number scores (24.6k, 18.2k, 41.0k). Dated "Reddit, Inc. © 2025".
- **Confidence:** High.

## 8. https://www.instagram.com/ — web/www.instagram.com/index.html
- **Verdict: broadly-right**
- **Key matches:** Desktop logged-in layout structure is right: left sidebar Home / Search / Explore / Reels / Messages / Notifications / Create / Profile, Threads entry, story rings at top labelled "Your story", post action row (like / comment / share / save), like counts and "View all N comments" pattern, right-hand current-account + "Switch" + "Suggested for you" panel with Follow buttons, footer links (About · Help · Press · API · Jobs · Privacy · Terms · Locations) and "From Meta" branding.
- **Key divergences:** All content is invented by design (usernames maya.k, jon.trails, sofia.eats, north.peak and posts about sunrise hikes, pasta and northern lights are fictional, with placeholder photo descriptions instead of generated images — no image files present yet). Like counts (1,248 / 3,902 / 8,411) are plausible fabrications. Footer omits Language / Meta Verified-type items and is dated 2025. Story-ring usernames are truncated in a slightly un-Instagram way ("maya.k", "jon.t").
- **Confidence:** Medium-high — structure verifiable from the public product; a real logged-in feed is personalised and not directly fetchable.

## 9. https://en.wikipedia.org/wiki/Albert_Einstein — web/en.wikipedia.org/wiki/Albert_Einstein/index.html
- **Verdict: broadly-right**
- **Images at audit time: partial** — a generated portrait exists in the page's images/ folder but was not yet embedded in the HTML (still a text placeholder in the page).
- **Key matches:** Infobox facts all correct: born 14 March 1879 Ulm, German Empire; died 18 April 1955 (aged 76), Princeton; Nobel Prize in Physics 1921; known for relativity, E = mc², photoelectric effect. Body facts correct: 1905 annus mirabilis as a Bern patent clerk, four papers, 1915 general relativity confirmed by 1919 eclipse observations, emigrated to the US in 1933 as a refugee from Nazi Germany (his 17 October 1933 arrival date is correct), US citizen 1940, signed the 1939 letter to Roosevelt, later unified-field-theory work, civil-rights/pacifism advocacy. **Generated image:** striking match in subject and composition to the real article's famous lead portrait (the 1947 Oren Jack Turner photograph): black-and-white, older Einstein in three-quarter profile looking to his left, wild white hair, moustache, dark knitted sweater against a plain grey backdrop.
- **Key divergences:** The recreation is a ~3-section stub vs the real article's very long multi-section biography with a large infobox (education, spouses, children, scientific career fields/institutions, full awards list) — everything present is right, most of the real page is absent. Generated portrait's face is more gaunt/ deeply lined than the real 1947 photograph and the hair is wispier — recognisably "Einstein" but not the same face.
- **Confidence:** High.

## 10. https://en.wikipedia.org/wiki/Mona_Lisa — web/en.wikipedia.org/wiki/Mona_Lisa/index.html
- **Verdict: broadly-right**
- **Images at audit time: partial** — generated painting exists in images/ but was not yet embedded; page still showed the placeholder.
- **Key matches:** Infobox: artist Leonardo da Vinci, medium "Oil on poplar panel", location Louvre, Paris — all correct. Sitter identified as Lisa del Giocondo, wife of a Florentine merchant — correct. Sfumato and enigmatic expression, taken to France and acquired by Francis I, theft in 1911 by Vincenzo Peruggia and recovery two years later, bulletproof glass, "best known / most visited / most parodied" characterisation — all match the real article. **Generated image:** overall composition matches the real painting: half-length seated woman, hands folded right-over-left in the lap, winding road on the left background, small bridge over a river on the right, hazy mountainous landscape.
- **Key divergences:** Date given as "c. 1503–1519"; the real infobox dates it 1503–1506, perhaps continuing until 1517 (1519 is Leonardo's death year). "Displayed in Paris since the late 18th century" is loose (Louvre from 1797, after periods at Fontainebleau/Versailles/Tuileries). **Generated image:** the face diverges noticeably — a broader, more modern smile and different features than Lisa del Giocondo's likeness; the sitter occupies less of the frame, the landscape is far more expansive and colourful than the real painting's tighter crop with dark loggia edges, and proportions read as an AI homage rather than the painting itself.
- **Confidence:** High.

## 11. https://en.wikipedia.org/wiki/Chicago — web/en.wikipedia.org/wiki/Chicago/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — one generated image, embedded in the page.
- **Key matches:** Lead facts correct: most populous city in Illinois, third-most populous in the US, on the southwestern shore of Lake Michigan; population "about 2.7 million city / 9.5 million metro" matches current figures; nickname "The Windy City"; incorporated 1837; Great Chicago Fire 1871 and rebuilding/skyscraper history; Prohibition-era organised crime / Al Capone association; the Loop, elevated rail, Chicago River, deep-dish pizza, blues/jazz — all accurate. **Generated image:** skyline from across Lake Michigan at sunset is recognisably Chicago — the black stepped Willis (Sears) Tower with twin antennae dominates the left, the tall white Aon Center stands right of centre, and the diamond-topped Smurfit-Stone/Crain building appears mid-frame; subject and composition match the kind of lakefront skyline photograph the real article uses.
- **Key divergences:** Real article's lead visual is a multi-image montage infobox (skyline, Cloud Gate, theatre, etc.) plus a detailed infobox (mayor, area, elevation, ZIP codes, area codes, time zones) — the recreation has a single skyline image and a 4-line summary infobox, and the body is a short stub (History / Geography and culture only). The generated skyline rearranges/invents some mid-frame towers and the sunset lighting is more dramatic than the real article's daytime montage shot.
- **Confidence:** High.

## 12. https://www.facebook.com/feed (invented logged-in view) — web/www.facebook.com/feed/index.html
- **Verdict: broadly-right**
- **Images at audit time: partial** — the lead post's generated image is embedded; other posts still have text placeholders.
- **Key matches:** Logged-in Facebook chrome is faithfully structured: top bar with Search Facebook, centre tabs Home / Watch / Marketplace / Groups / Gaming, right-side Menu / Messenger / Notifications / profile; left shortcuts (profile, Friends, Memories, Saved, Groups, Marketplace, Feeds, Events) match the real shortcut list; Stories row, "What's on your mind, Alex?" composer, post format with poster/timestamp/audience icon, reaction counts in the real "48 · 12 comments · 3 shares" style, right-hand Contacts with green presence dots and Group conversations. **Generated image:** the garden-beds photograph embedded in the first post matches that (invented) post's described photo very well: raised wooden beds with staked tomato plants bearing red tomatoes, a basil bed beside it, watering can, morning sun — subject and composition exactly as the page describes.
- **Key divergences:** By design there is no real counterpart to compare content against — the entire feed is invented (people, groups, posts, counts). One wrinkle: the invented account holder is named "Alex Morgan", which collides with a real public figure (the US footballer), contrary to the project's invented-people rule. A Page post is self-labelled "Sponsored-ish typical post", which no real post would say.
- **Confidence:** Medium — layout verifiable from the public product; a private feed has no real reference version.

## 13. https://de.wikipedia.org/ — web/de.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (logo described in a placeholder; no generated image embedded).
- **Key matches:** Section set matches the real Hauptseite exactly: Artikel des Tages, Was geschah am …?, In den Nachrichten, Verstorben (recreation: "Kürzlich Verstorbene"), Schon gewusst?, Schwesterprojekte. The welcome text's wording closely tracks the real text: "Wikipedia ist ein Projekt zum Aufbau einer Enzyklopädie aus freien Inhalten, zu denen du sehr gern beitragen kannst. Seit März 2001 sind … Artikel in deutscher Sprache entstanden" — March 2001 founding is correct. Title "Wikipedia – Die freie Enzyklopädie" correct.
- **Key divergences:** Article count given as "rund 2,9 Millionen" — the real count is 3,154,416+ (3 million was passed in March 2025), so the figure is ~1.5 years stale. As with the news sites, the sections contain descriptions of what the section is rather than its actual daily content (no real Artikel des Tages, no real news items or obituaries). Topic-portal list (Geographie, Geschichte, Gesellschaft, Kunst und Kultur, Religion, Sport, Technik, Wissenschaft) and the "Wikipedia aktuell" notices are missing.
- **Confidence:** High.

## 14. https://www.nytimes.com/ — web/www.nytimes.com/index.html
- **Verdict: divergent**
- **Images at audit time: placeholder-only.**
- **Key matches:** Nameplate and section taxonomy correct: World, U.S., Politics, Business, Technology, Sports, Arts, Opinion are real NYT sections; the general concept of a multi-column homepage with a central lead, live coverage and a subscription paywall is right.
- **Key divergences:** No actual journalism is recreated at all — the "lead story" is a meta-placeholder ("Lead report from correspondents around the world", "The Times homepage opens in a multi-column newspaper layout…") and every other item is a generic topic card. The real homepage carries dozens of specific headlines with photographs, bylines and timestamps, plus the date line, "The Morning"-style entry points, Games / Cooking / Wirecutter / The Athletic cross-promotion — none of which appear. Nothing falsifiable was even attempted, which for a "recreate from memory" test is itself the finding: for fast-moving news homepages the crawler fell back to describing the genre.
- **Confidence:** High.

## 15. https://www.reuters.com/ — web/www.reuters.com/index.html
- **Verdict: divergent**
- **Images at audit time: placeholder-only.**
- **Key matches:** Section set World / Business / Markets / Technology / Sports matches real Reuters top sections; the characterisation (concise factual wire copy, timestamps and datelines, registration/subscription wall, markets data with indices/currencies/commodities) is an accurate description of the product.
- **Key divergences:** Same failure mode as NYT/BBC: zero specific stories — the top-stories box is a genre description ("Top world news, reported factually and fast"), not a recreated headline. Real Reuters leads with concrete, timestamped headlines and live market figures. Missing real elements include the markets ticker values, "Live" coverage markers and section breadth (Legal, Breakingviews, Investigations, pictures/video verticals).
- **Confidence:** High.

## 16. https://commons.wikimedia.org/ — web/commons.wikimedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — the Picture of the Day slot has a generated image embedded.
- **Key matches:** Main Page structure matches the real Commons main page: welcome banner with the tagline "a collection of freely usable media files to which anyone can contribute", Picture of the Day and Media of the Day boxes, browse-by-topic categories (Nature, Animals, Plants, Architecture, Art, Maps, Science, Technology, Food and drink, People, Sound — matching the real "Content by topic: Nature…" list), Participate section, Highlights naming Featured / Quality / Valued images and the Featured Pictures / Picture of the Year processes, sister-project footer. **Generated image:** an alpine lake at sunset reflecting jagged snow-dusted peaks — exactly the genre of a Commons Featured Picture / Picture of the Day landscape photograph, matching the page's own description of "a landscape / nature photograph".
- **Key divergences:** File count is understated: "well over one hundred million files" vs the real banner's ~147.8 million. The real Picture of the Day is a specific captioned file (recent examples: street lights on the Norderney promenade; a hyacinth macaw in flight) — the generated alpine-lake image matches no real POTD, only the genre. The recreation omits the real page's Participating help text ("Browsing? / Using? / Identifying? / Creating? / Discussion?") and the Monthly photo challenge box.
- **Confidence:** High.

## 17. https://en.wikipedia.org/wiki/Mount_Everest — web/en.wikipedia.org/wiki/Mount_Everest/index.html
- **Verdict: close**
- **Images at audit time: partial** — generated north-face image exists in images/ but the HTML still carried the text placeholder at audit time.
- **Key matches:** Infobox data essentially perfect: elevation 8,848.86 m (29,031.7 ft), prominence equal to elevation, coordinates 27°59′17″N 86°55′31″E, Mahalangur Himal, first ascent 29 May 1953 Hillary/Norgay, easiest route Southeast ridge, Seven Summits / eight-thousander listings. Survey history is accurate including the famous detail that Sickdar computed 29,000 ft in 1852 and the survey published 29,002 ft so it would not look like a rounded estimate; 2020 joint Nepal–China survey using summit GPS and ground-penetrating radar; name honouring George Everest (Surveyor General 1830–1843) despite his objections; death-zone, crowding, permit-cost and waste criticism all real themes of the article. **Generated image:** Everest's north face from the Tibetan/Rongbuk side — snow pyramid above a brown rocky valley under deep blue sky — matches the subject and composition of the real article's well-known lead photograph very closely.
- **Key divergences:** Compressed vs the real article (no detailed climbing-history, geology or flora/fauna sections beyond stubs). "Sagarmatha coined in the 1960s" is loose — the name was coined by Baburam Acharya in 1938 and officially adopted later. Chomolungma glossed "Holy Mother or Goddess Mother of the World" vs the common "Mother Goddess of the World" — close enough.
- **Confidence:** High.

## 18. https://www.wikidata.org/ — web/www.wikidata.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (logo described, not generated/embedded).
- **Key matches:** Tagline "The free knowledge base that anyone can edit" and the welcome text "a free and open knowledge base that can be read and edited by both humans and machines" track the real main page. The canonical example is exactly right: Douglas Adams is item Q42 — the same example the real project uses everywhere. Statements/labels/descriptions/aliases/references/qualifiers model, SPARQL Query Service with list/map/chart/timeline visualisations, CC0 licence for the data, dumps and API access — all correct.
- **Key divergences:** Simplified vs the real main page (which carries community portal / help / chat entry points and project statistics — e.g. the item count, now well past 100 million items — none given here). The logo placeholder describes "vertical bars forming a stylised W", missing that the real bars are red/green/blue and encode "WIKI" in Morse-like form.
- **Confidence:** High.

## 19. https://en.wiktionary.org/ — web/en.wiktionary.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** "The free dictionary" branding; the real main page's twin features Word of the Day and Foreign Word of the Day are both present; entry anatomy (IPA pronunciation, etymology, ordered senses, examples, synonyms/antonyms, derived terms, translations) is accurate; and two genuinely insider details are right — the community pages really are called the Beer Parlour and the Tea Room.
- **Key divergences:** No actual Word of the Day is given (the feature is described, not populated), unlike the real page which shows today's word with definition and example. "Well over 150 languages" is in the right ballpark but vague vs. the real site's edition list. Overall a faithful skeleton with the daily content left blank.
- **Confidence:** High.

## 20. https://www.theguardian.com/ — web/www.theguardian.com/index.html
- **Verdict: divergent**
- **Images at audit time: complete** — one generated image embedded, but see below: it is the wrong kind of image entirely.
- **Key matches:** Masthead/nav recall is good: sections News / Opinion / Sport / Culture / Lifestyle are the real Guardian top sections, and two distinctive real features are correctly remembered — story "containers" ordered by section, and the supporter appeals asking readers to fund open independent journalism (very Guardian-specific). "Comment is Free" as the opinion brand is correct.
- **Key divergences:** Again zero real headlines — top stories are genre descriptions. **Generated image:** instead of a web lead photograph, the generator produced a fake *print newspaper front page*: a convincing Guardian-serif "The Guardian" masthead, dateline "Saturday 12 October 2024" (over a year stale), a generic British high-street photograph and a caption about "daily life on the high street". The Guardian website's masthead is white-on-deep-blue, not black-on-white print; the image matches neither the real homepage's lead story nor its format. A plausible newspaper, a wrong website image.
- **Confidence:** High.

## 21. https://apnews.com/ — web/apnews.com/index.html
- **Verdict: divergent**
- **Images at audit time: complete** — one generated lead photo embedded (generic wire-style photograph; no specific real story to match).
- **Key matches:** Full name "Associated Press News: Breaking News" and sections World / U.S. / Politics / Sports / Entertainment / Business / Science match AP's real section taxonomy; the characterisation of AP style (factual, attributed, concise, cooperative wire) is accurate; hub structure (Top stories, US news, Politics, AP Sports, Science) is plausible AP.
- **Key divergences:** The page itself admits the failure mode in-line: "Summarised generically here." No specific top stories, no timestamps, none of the real homepage's dense headline grid. As with the other news homepages, only the genre was recreated.
- **Confidence:** High.

## 22. https://www.cnn.com/ — web/www.cnn.com/index.html
- **Verdict: divergent**
- **Images at audit time: complete** — one generated image embedded, and it is strikingly wrong.
- **Key matches:** Title "CNN – Breaking News, Latest News and Videos" correct; section set World / US / Politics / Business / Health / Entertainment / Sport matches CNN's; the observation that CNN digital is built around a big lead with red breaking-news treatment and live-update pages is accurate.
- **Key divergences:** No real headlines (genre summary again). **Generated image:** a generic *local TV* news-studio graphic — an anchor desk branded "NEWS 24 • LIVE", a "BREAKING NEWS: City Council proposes new infrastructure plan" screen, a weather radar marked 72°F and a ticker about "storm conditions developing downtown". There is no CNN logo or CNN branding anywhere in it, and its content is invented local-news filler; it resembles a US local-station promo, not CNN.com's lead imagery in subject, branding or composition.
- **Confidence:** High.

## 23. https://www.nasa.gov/ — web/nasa.gov/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (Artemis/Moon hero, ISS, Webb galaxy and Mars rover images all described as placeholders at audit time).
- **Key matches:** Top navigation matches the real nasa.gov: Missions, Humans in Space, Earth, The Solar System, The Universe, Science, Aeronautics, Technology, Learning Resources, plus LIVE and NASA+. Artemis copy tracks NASA's real messaging: returning humans to the Moon, landing near the lunar South Pole on Artemis III, Artemis II crewed lunar flyby, preparing for Mars; Perseverance caching samples in Jezero Crater and Ingenuity's powered-flight demonstration are correct; "min read" story labels, Image of the Day and Podcasts entry points, and the official footer (Page Editor, FOIA, Privacy, Accessibility, No Fear Act, USA.gov) are all real NASA site furniture. The placeholder descriptions (Moon surface with Earth crescent; ISS with arrays spread; Webb spiral galaxy; rusty Mars terrain with six-wheeled rover) match the subjects of the real imagery used in those slots.
- **Key divergences:** The Artemis strap uses British spelling "first person of colour" where NASA's actual copy is "first person of color". Featured-news headlines are generic inventions ("Station Crew Continues Research Aboard the International Space Station") rather than the real dated headlines. Founded-1958 and agency description are correct but buried in an "About" block that doesn't mirror the real homepage's layout.
- **Confidence:** High.

## 24. https://x.com/ — web/x.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only / logo-as-text** (the 𝕏 mark is rendered as a character, which is effectively what the real page shows).
- **Key matches:** The logged-out landing page is reproduced almost exactly: giant 𝕏, "Happening now" headline, "Join today." subhead, "Sign up with Apple" and "Sign up with Google" buttons, "or" divider, "Create account", the legal sentence "By signing up, you agree to the Terms of Service and Privacy Policy, including Cookie Use.", "Already have an account?" + "Sign in", and the long footer link row ending "© 2025 X Corp." — all matching the real x.com landing page, including British-spelled "Help Centre" in the footer as the real footer renders in some locales.
- **Key divergences:** Minor: footer ordering/completeness slightly trimmed vs. the real two-row footer; nothing of substance missing.
- **Confidence:** High.

## 25. https://www.tiktok.com/ — web/www.tiktok.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: partial** — first video has a generated still embedded; the second is still a placeholder.
- **Key matches:** Title tagline "TikTok - Make Your Day" correct. Left rail For You / Explore / Upload / LIVE / Profile with Log in button matches the real desktop layout; video card anatomy (username, caption, hashtags, "original sound — <user>" music line, heart/comment/share counts down the right) is faithful. **Generated image:** the flatbread-kitchen still matches its video's described content (a 3-ingredient flatbread kitchen hack by the invented @home.with.ana).
- **Key divergences:** All videos, creators and counts are invented (84.2K / 412K likes etc.) — unavoidable for the For You feed, but none correspond to real trending content. The "Discover / Following accounts appear here when logged in" panel is a summarised stand-in for the real Discover hashtag list and suggested accounts.
- **Confidence:** Medium-high.

## 26. https://www.linkedin.com/ — web/www.linkedin.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only.**
- **Key matches:** Title "LinkedIn: Log In or Sign Up" correct; headline "Welcome to your professional community" verbatim from the real logged-out page; top-right Articles / People / Learning / Jobs discovery icons with Join now / Sign in; "Continue with Google", email/password form, "Forgot password?", and the "By clicking Continue, you agree to LinkedIn's User Agreement, Privacy Policy and Cookie Policy" sentence — all real. The explore-by-topic and find-the-right-job link blocks mirror the real page's SEO link sections, and the footer policy list (About, Accessibility, User Agreement, Privacy Policy, Cookie Policy, Copyright Policy, Brand Policy, Community Guidelines) with "LinkedIn Corporation © 2025" matches.
- **Key divergences:** The hero image is a placeholder description; the real page's large photo of professionals is not yet generated. Minor section ordering differences.
- **Confidence:** High.

## 27. https://mail.google.com/ (invented inbox) — web/mail.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only / none needed** (Gmail UI is icon-driven; rendered with emoji-style glyphs).
- **Key matches:** Gmail chrome is faithfully reproduced: Compose button, left labels Inbox / Starred / Snoozed / Sent / Drafts, category tabs Primary | Promotions | Social, search bar, settings/apps/account icons, message rows with checkbox, star, sender, subject + snippet, and time ("09:12", "Yesterday", "Mon"), and the storage footer format "4.1 GB of 15 GB used · Google Drive" — 15 GB is the correct free-tier quota.
- **Key divergences:** The inbox content is invented by design (Harbour Library, "North Peak Airlines" flight NP214, Garden Club) — no real counterpart exists. Small internal inconsistency: the title says "Inbox (3)" while five messages are listed. Custom labels (Work / Receipts / Travel) are plausible but invented.
- **Confidence:** Medium-high — UI verifiable, mailbox content private by nature.

## 28. https://en.wikipedia.org/wiki/Marie_Curie — web/en.wikipedia.org/wiki/Marie_Curie/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated portrait embedded.
- **Key matches:** Every stated fact checks out: born Maria Salomea Skłodowska, 7 November 1867 Warsaw; died 4 July 1934 (aged 66); Nobel Physics 1903 (shared) and Chemistry 1911; first woman Nobel laureate and only person to win in two different scientific fields (the real lead's exact framing); polonium named for Poland; death from aplastic anaemia attributed to radiation exposure; institutes founded in Paris and Warsaw; 1995 Panthéon interment as first woman honoured on her own merits.
- **Key divergences:** Greatly compressed vs. the real biography. **Generated image:** a black-and-white "in her laboratory" portrait with bottles helpfully labelled RADIUM and POLONIUM and a chalkboard reading "Ra 226 / ionization" — thematically apt but a staged composite: the real article's lead portrait is a plain c.1920 studio portrait with no lab props, and the generated face is of an older Curie than the c.1920 photograph.
- **Confidence:** High.

## 29. https://en.wikipedia.org/wiki/Earth — web/en.wikipedia.org/wiki/Earth/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Blue Marble embedded.
- **Key matches:** Facts all correct: third planet, mean diameter ~12,742 km, orbital period ~365.25 days, one moon, oceans ~71% of surface, nitrogen/oxygen atmosphere, formation ~4.54 billion years ago, crust/mantle/core and plate tectonics. **Generated image:** an Africa-centred Blue Marble — Sahara and Arabian Peninsula upper centre, Madagascar lower right, ice cap at the bottom, a sliver of South America at the left edge, swirling Southern Ocean cloud — matching the subject and composition of the real article's Blue Marble lead image very closely.
- **Key divergences:** Stub-length vs. the real article's extensive physical/orbital/life sections and full planetary infobox. Coastline detail in the generated globe is painterly on close inspection, though geography is recognisably correct.
- **Confidence:** High.

## 30. https://en.wikipedia.org/wiki/Al_Capone — web/en.wikipedia.org/wiki/Al_Capone/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (1931 mugshot described; no generated image embedded yet).
- **Key matches:** A clean factual sweep: Alphonse Gabriel Capone, born 17 January 1899 Brooklyn to Neapolitan immigrant parents, died 25 January 1947 (aged 48) Palm Island, Florida; "Scarface"; Frankie Yale then Johnny Torrio; Torrio's retirement after the mid-1920s assassination attempt; Saint Valentine's Day Massacre 1929 (seven victims, never charged); convicted of tax evasion on 17 October 1931; 11-year sentence including Alcatraz; neurosyphilis, released 1939, died after stroke/pneumonia/cardiac arrest. The placeholder description of the 1931 mugshot (heavy-set man in suit and fedora) matches the famous real photograph's subject.
- **Key divergences:** Compressed (no detailed Outfit wars, no soup-kitchen / public-image material); nothing found to be wrong.
- **Confidence:** High.

## 31. https://fr.wikipedia.org/ — web/fr.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Title "Wikipédia, l'encyclopédie libre" correct; main-page section names are the real French ones: "Lumière sur…", "Actualités", "Le saviez-vous ?", "Image du jour", plus Présentation and Comment contribuer blocks; sister projects correctly named in French (Wiktionnaire etc.); the welcome description of Wikipedia as a "projet d'encyclopédie collective en ligne, universelle, multilingue et fonctionnant sur le principe du wiki" tracks the project's standard French self-description.
- **Key divergences:** Article count "environ 2,6 millions" is stale vs. the real ~2,78 million. As with the English/German homepages, the daily sections are described rather than populated — no real featured article, news or anecdotes.
- **Confidence:** High.

## 32. https://old.reddit.com/ — web/old.reddit.com/index.html
- **Verdict: close** (as a historical recreation)
- **Images at audit time: placeholder-only / none** (the old design is text-led).
- **Key matches:** The pre-2018 Reddit interface is recreated with real insider fidelity: "reddit: the front page of the internet" strapline, MY SUBREDDITS bar with POPULAR – ALL – RANDOM and the default subreddit list (AskReddit, pics, science, gaming, worldnews, videos, todayilearned, aww, news, technology), sort tabs hot / new / rising / controversial / top / gilded / wiki, user karma in parentheses with mail / preferences / logout, "Submit a new link / text post", and even the "Daily Reddit Gold goal" progress bar (62%) — a real old-reddit sidebar feature. Footer link set (about, blog, careers, press, apps, source code, advertise, help, wiki, FAQ…) matches the old site. The page correctly notes this layout was largely replaced by the 2018 redesign while remaining live at old.reddit.com.
- **Key divergences:** The three posts are the same invented items used on the modern reddit.com recreation, with placeholder usernames — old Reddit's real front page content is unknowable now, so this is expected; scores differ slightly between the two recreations of the "same" posts (31.2k/18.9k/44.1k here vs 24.6k/18.2k/41.0k there), showing the numbers are improvised each time.
- **Confidence:** High for the interface; content inherently invented.

## 33. https://en.wikipedia.org/wiki/Wikipedia — web/en.wikipedia.org/wiki/Wikipedia/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only.**
- **Key matches:** Lead facts mirror the real article: free online encyclopedia written by a volunteer community ("Wikipedians"), founded 15 January 2001 by Jimmy Wales and Larry Sanger, originating alongside Nupedia, hosted by the San Francisco-based Wikimedia Foundation, "largest and most-read reference work in history" (the real lead's own superlative), 300+ language editions, English edition passing one million articles in 2006. NPOV/verifiability, summary style, public edit histories, rapid vandalism reversion, consensus dispute resolution, and the reception summary (comparable scientific accuracy in studies; criticism over systemic bias and uneven quality) all faithfully track the real article's content and balance.
- **Key divergences:** Compressed to four sections vs. the real article's long history/governance/operations treatment; no statistics (editor counts, article totals across editions).
- **Confidence:** High.

## 34. https://www.whatsapp.com/ — web/www.whatsapp.com/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated phone-chat image embedded.
- **Key matches:** Hero copy is verbatim from the real site: "Message privately" over "Simple, reliable, private messaging and calling for free*, available all over the world." with Download button and the real "*Data charges may apply" footnote. Top navigation (Features, Privacy, Help Center, Blog, For Business, Apps, Download) matches whatsapp.com. Feature blurbs (voice/video calls, groups and Communities, stickers/GIFs/Status) are real WhatsApp features in the site's own terms. **Generated image:** a phone showing a chat with green outgoing / white incoming bubbles matches both the page's description and the real product's signature look.
- **Key divergences:** Footer legal line mixes "WhatsApp LLC" and "© 2025 Meta" (the real footer is Meta-branded); page is a compact summary of a longer marketing page (no QR-code WhatsApp Web panel beyond a mention, no detailed feature sections).
- **Confidence:** High.

## 35. https://www.threads.net/ — web/www.threads.net/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only / none** (text-led feed).
- **Key matches:** Threads web chrome is right: top icon bar (home, search, new post, likes, profile) with the Threads swirl logo, "For you | Following" feed tabs, post anatomy (avatar, username, time, text, heart/comment/repost/share counts), and the login framing "Log in with Instagram" / "Threads by Instagram" / Meta footer — all matching the real product.
- **Key divergences:** Feed content is invented, though notably it reuses the same invented personas as this crawl's Instagram page (maya.k, jon.trails, north.peak), so the invented universe is at least self-consistent across the two Meta properties. Counts and posts correspond to nothing real.
- **Confidence:** Medium-high.

## 36. https://drive.google.com/ (invented My Drive) — web/drive.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only / icon-based UI.**
- **Key matches:** Drive web UI is faithfully structured: "+ New" button, left nav Home / My Drive / Computers / Shared with me / Recent / Starred / Bin, "Search in Drive", file list with Name / Owner / Last modified / Size columns, file-type icons (folder, Sheet, Doc, PDF, PNG), sharing shown via owner values ("me", "shared"), and storage meter "8.2 GB of 15 GB used" with the correct 15 GB free quota.
- **Key divergences:** All files are invented user content (Holiday photos 2025, a Lisbon trip itinerary, a lease PDF) — by design for a private drive. "Bin" is the en-GB label (US Drive says "Trash"); file sizes are given for folders as "—" which the real UI also does, but dates are vaguer than the real exact timestamps.
- **Confidence:** Medium-high.

## 37. https://www.aljazeera.com/ — web/www.aljazeera.com/index.html
- **Verdict: divergent**
- **Images at audit time: complete** — one generated "photojournalism" lead image embedded (generic regional news photograph, matching no specific real story).
- **Key matches:** Title "Breaking News, World News and Video from Al Jazeera" correct; sections News / Middle East / Features / Opinion / Video / Sport are AJE's real sections; the editorial characterisation (Doha-based, Middle East and Global South emphasis, Gaza/Israel lead coverage, live blogs) is accurate, including the network's stated aim of giving "a voice to the voiceless".
- **Key divergences:** Same news-homepage pattern as BBC/NYT/Reuters/CNN/AP: no specific headlines at all — the top story is a description of the coverage focus, and all other items are topic cards. The real site leads with concrete timestamped stories.
- **Confidence:** High.

## 38. https://es.wikipedia.org/ — web/es.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Title "Wikipedia, la enciclopedia libre" correct; section names are the real Spanish main-page set: Artículo destacado, Actualidad, ¿Sabías que…, Imagen del día, Efemérides, Proyectos hermanos (with correct Spanish sister names: Wikcionario, Wikilibros, Wikinoticias, Wikiviajes, Wikiversidad, Wikidata). Welcome formula "la enciclopedia de contenido libre que todos pueden editar" tracks the real text.
- **Key divergences:** "Unos dos millones de artículos" is now an under-rounding (real ~2,14 millones). Daily sections described rather than populated, as with the other language homepages.
- **Confidence:** High.

## 39. https://ja.wikipedia.org/ — web/ja.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Japanese main-page component names are correctly recalled in Japanese: 秀逸な記事 (featured articles), 良質な記事 (good articles), 新しいページ, 強化記事, 季節の画像・特集, 姉妹プロジェクト with correct Japanese sister-project names (ウィクショナリー, ウィキブックス, ウィキソース, ウィキクォート, ウィキデータ, ウィキメディア・コモンズ). Welcome framing (free multilingual encyclopedia anyone can edit) correct.
- **Key divergences:** Article count "約140万本以上" is technically true but stale-leaning (real count ~152万). Daily content described rather than populated; the real Japanese main page's layout (with its distinctive date/weather-style boxes and portal links) is only sketched.
- **Confidence:** Medium-high.

## 40. https://en.wikipedia.org/wiki/Leonardo_da_Vinci — web/en.wikipedia.org/wiki/Leonardo_da_Vinci/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated self-portrait embedded.
- **Key matches:** Full name Leonardo di ser Piero da Vinci, born 15 April 1452 Vinci, Republic of Florence; died 2 May 1519 (aged 67) Amboise; trained under Verrocchio; Mona Lisa and The Last Supper as notable works; chiaroscuro/sfumato, anatomy dissections, flying machines, mirror-script notebooks, "Renaissance man" archetype — all correct. **Generated image:** the red-chalk self-portrait is a strong match to the real article's lead image (the Turin red chalk drawing): elderly bearded man in three-quarter view facing right, long flowing hair and beard, red chalk on aged, foxed paper — subject, medium and composition all right.
- **Key divergences:** Compressed (real article is very long with detailed painting lists, science and legacy sections). Generated face is a little coarser/more heavily lined than the Turin drawing.
- **Confidence:** High.

## 41. https://en.wikipedia.org/wiki/Jimmy_Wales — web/en.wikipedia.org/wiki/Jimmy_Wales/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only.**
- **Key matches:** Born Jimmy Donal Wales, 7 August 1966, Huntsville, Alabama — correct. Finance studies at Auburn and the University of Alabama, Chicago finance career, Bomis in the 1990s, Nupedia launched 2000, Wikipedia January 2001 with Larry Sanger, co-founder of for-profit Fandom, Wikimedia Foundation trustee, "Jimbo Wales" username, WikiTribune later relaunched as WT.Social — every checkable claim verified correct.
- **Key divergences:** Compressed vs. the real article (no later ventures/controversies detail); nothing found to be wrong.
- **Confidence:** High.

## 42. https://maps.google.com/ — web/maps.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (the map itself is a stylised placeholder, as the page itself notes).
- **Key matches:** Maps UI furniture is right: search box "Search Google Maps", category chips (Restaurants, Hotels, Parking, ATMs), Directions button, place-card format (name, star rating "★★★★☆ 4.6 (1,204)", category, closing time "Closes 18:00"), transit entry, Satellite/Map layers toggle, zoom +/− and target controls, "Map data ©2025 Google" attribution in the real format.
- **Key divergences:** The locality is entirely invented (Harbour Coffee House, Central Station, Riverside Park in an unnamed coastal city) — real Maps opens on the user's actual location. Chip set uses British "Petrol" where the US product says "Gas" and omits the prominent "Coffee" chip. No real cartography is (or could be) reproduced.
- **Confidence:** Medium-high.

## 43. https://en.wikipedia.org/wiki/October_17 — web/en.wikipedia.org/wiki/October_17/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only / none.**
- **Key matches:** An unusually verifiable page, and it passes almost everything: "290th day of the year (291st in leap years); 75 days remain" is arithmetically correct. Events all check out against the real date article — 1604 Kepler's Supernova first sighted (17 Oct), 1814 London Beer Flood (eight deaths), 1931 Capone convicted, 1933 Einstein arrived in the US, 1979 Mother Teresa Nobel Peace Prize, 1989 Loma Prieta earthquake (6.9, 63 deaths, during the World Series), 2003 Taipei 101 topped out. Births correct: Arthur Miller 1915, Rita Hayworth 1918, Eminem 1972. Deaths correct: Chopin 1849, Puyi 1967. Holiday correct: International Day for the Eradication of Poverty.
- **Key divergences:** Only that it is a selection (the real article lists many more events/births/deaths) — everything included is right.
- **Confidence:** High.

## 44. https://wikimediafoundation.org/ — web/wikimediafoundation.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Identity and role correctly stated (the non-profit hosting Wikipedia, Wiktionary, Commons, Wikidata etc.); the mission is paraphrased closely from the real one ("empower people around the world to collect and develop educational content under a free licence and to disseminate it effectively and globally"); funding model (mostly small reader donations), transparency content (finances, annual reports, policies), San Francisco base — all accurate.
- **Key divergences:** A summary of the site rather than a recreation of its actual homepage layout/campaign content; mission paraphrase omits "or in the public domain" and "engage".
- **Confidence:** High.

## 45. https://en.wikivoyage.org/ — web/en.wikivoyage.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Tagline "The free worldwide travel guide that anyone can edit" correct; front-page features Destination of the Month, a previous winner, Off the Beaten Path, and a rotating "Discover" fact box are the real Wikivoyage main-page components; the guide anatomy it cites (getting in / around, see, do, buy, eat, drink, sleep) is the real Wikivoyage article template; continent entry points and phrasebooks are real.
- **Key divergences:** No actual destination content populated; logo placeholder ("globe formed of arrows pointing outwards") is approximately the real mark (a globe with opposed arrows) but loosely described.
- **Confidence:** High.

## 46. https://en.wikiquote.org/ — web/en.wikiquote.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Self-description ("a free online compendium of quotations from notable people and creative works, with sources where known") matches the project's real description; Quote of the Day is the real daily feature; organisation by person / work / theme / proverbs and the editorial concern about misattributed quotes are all true to the project.
- **Key divergences:** No actual quote of the day populated; structure only.
- **Confidence:** High.

## 47. https://en.wikipedia.org/wiki/Internet — web/en.wikipedia.org/wiki/Internet/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only.**
- **Key matches:** Lead definition faithfully paraphrases the real article ("global system of interconnected computer networks that links billions of devices worldwide, using the Internet protocol suite (TCP/IP)"); history is correct in sequence and attribution — ARPANET first demonstrated 1969, TCP/IP developed in the 1970s by Vint Cerf and Robert Kahn, the Web invented by Tim Berners-Lee at CERN in 1989–91, followed by browsers, search, social and mobile; governance section (no single owner; standards bodies; names-and-numbers coordination) matches the real article's account.
- **Key divergences:** Heavily compressed vs. the real article's extensive sections and diagrams (the real lead also carries the famous optical-map/opte.org image, not yet generated here).
- **Confidence:** High.

## 48. https://en.wikipedia.org/wiki/Portal:Current_events — web/en.wikipedia.org/wiki/Portal:Current_events/index.html
- **Verdict: divergent**
- **Images at audit time: placeholder-only.**
- **Key matches:** Portal furniture is right (Topics in the news header, ongoing-events sidebar concept, recent-deaths and by-month navigation exist on the real portal); the two lead ongoing conflicts named (Russo-Ukrainian War, war in Gaza) are indeed major ongoing stories.
- **Key divergences:** Content is again generic summary rather than the real portal's dated, linked daily entries — and it is time-stamped wrongly: "Current events by month" tops out at **October 2025**, a full year stale against the real portal (October 2026). The crawl's internal "present" is consistently ~Oct 2025 on several pages (cf. © 2025 footers on Facebook/Reddit/LinkedIn recreations), even though the run is in Oct 2026.
- **Confidence:** High.

## 49. https://en.wikipedia.org/wiki/Climate_change — web/en.wikipedia.org/wiki/Climate_change/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — generated melting-glacier image embedded; it matches the page's own described subject, though the real article's lead visuals are data graphics (temperature records, attribution charts) alongside photography, so a lone glacier photo is a glossier stand-in than the real lead.
- **Key matches:** Definition and causal account correct (long-term shifts, primarily human-driven via fossil-fuel burning raising greenhouse-gas concentrations); effects list (sea-level rise, ocean acidification, intensifying heatwaves, precipitation change) matches the real article; Paris Agreement 2015 goal correctly stated as "well below 2 °C, preferably 1.5 °C" above pre-industrial levels; UNFCCC centrality correct.
- **Key divergences:** Extremely compressed vs. one of Wikipedia's longest articles (no observed-temperature numbers, no attribution percentages, no scenarios/economics); nothing included is wrong.
- **Confidence:** High.

## 50. https://en.wikipedia.org/wiki/Citizendium — web/en.wikipedia.org/wiki/Citizendium/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only.**
- **Key matches:** All facts verified: English-language wiki encyclopedia founded by Wikipedia co-founder Larry Sanger; announced 2006, piloted, launched publicly in 2007; model differences correctly identified — real names required and expert editors guiding/approving articles; subsequent sharp decline in activity while remaining online as a small project; its role in debates over expert-guided alternatives is accurately characterised.
- **Key divergences:** Compressed; nothing found wrong.
- **Confidence:** High.

## 51. https://www.mediawiki.org/ — web/www.mediawiki.org/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated logo embedded, and it is one of the best image matches of the run.
- **Key matches:** Site purpose and structure correct (documentation home for users/sysadmins/developers; download + installation guide; manuals for use, administration and development; extensions/skins incl. VisualEditor; support desk, IRC, mailing lists, Phabricator for bugs). Technical facts correct: written in PHP; runs on MariaDB/MySQL, PostgreSQL or SQLite. **Generated logo:** double square brackets [[ ]] in dark grey flanking a ring of overlapping gradient petals (red → orange → purple) — this is a strikingly close regeneration of the real (2021) MediaWiki logo in composition, colours and proportions, matching the page's own description ("square brackets around a sunflower-like emblem").
- **Key divergences:** Homepage content is summarised rather than reproducing the real page's exact welcome-box layout and links; no version number for the "current stable release" is given (the real site names it).
- **Confidence:** High.

## 52. https://species.wikimedia.org/ — web/species.wikimedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Tagline "The free species directory that anyone can edit" correct; scope (animals, plants, fungi, bacteria, archaea, protists, viruses) and page anatomy (classification, taxon authority, synonyms, distribution, references, vernacular names) accurately describe real Wikispecies pages; top-level taxonomy browsing (Archaea / Bacteria / Eukaryota → Animalia, Fungi, Plantae…) is correct.
- **Key divergences:** Summary-level; the placeholder's logo description (leaf/tree-of-life motif) is looser than the real spherical "species" mark. No taxon counts given.
- **Confidence:** Medium-high.

## 53. https://en.wikibooks.org/ — web/en.wikibooks.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Tagline "Open books for an open world" is Wikibooks' real tagline. Featured Book is the real main-page feature; Wikijunior as the children's-books sister project is correct; department/shelf structure (Computing, Engineering, Health, Humanities, Languages, Mathematics, Science, Social Sciences, Miscellaneous, plus the Cookbook) closely matches the real shelving system.
- **Key divergences:** Featured Book not actually populated with a title; structure faithful, content blank.
- **Confidence:** High.

## 54. https://en.wikisource.org/ — web/en.wikisource.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Two insider details are exactly right: the logo placeholder correctly identifies the Wikisource logo as **an iceberg** ("most knowledge lies beneath the surface"), and **Proofread of the Month** is the project's real monthly collaboration, correctly described (checking transcriptions against scans, plus validation by others). Featured Text is the real main-page feature; the public-domain/freely-licensed scope statement is accurate.
- **Key divergences:** Tagline rendered "The free content library" vs. the project's usual "the free library"; no featured text actually populated.
- **Confidence:** High.

## 55. https://meta.wikimedia.org/ — web/meta.wikimedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Function list is an accurate map of what Meta-Wiki actually hosts: requests for comment, steward and global-admin coordination, spam/vandalism blacklists, translation coordination, grants, elections, movement strategy, and the Babel language forum. Welcome framing ("global community site for the Wikimedia projects and the movement") matches the real site.
- **Key divergences:** Summary-level; no specific live processes (current RFCs, elections) represented, as expected.
- **Confidence:** Medium-high.

## 56. https://www.messenger.com/ — web/www.messenger.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — a generated chat-window visual is embedded; it matches the page's described content (colourful message bubbles, call thumbnails) and the product's look in general terms.
- **Key matches:** Headline "Hang out anytime, anywhere" is Messenger.com's real headline, and the sub-line ("Messenger makes it easy and fun to stay close to your favourite people") tracks the real "…stay close to your favorite people" copy. Nav (Features · Privacy & safety · For developers), login card with "Forgotten your password?" and "Keep me signed in", and app-store badges all match the real landing page.
- **Key divergences:** British "favourite" vs. the US site's "favorite"; footer "© Meta 2025" repeats the crawl's year-staleness; page is much shorter than the real feature-scrolling landing page.
- **Confidence:** Medium-high.

## 57. https://en.wikipedia.org/wiki/Kolkata — web/en.wikipedia.org/wiki/Kolkata/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Howrah Bridge image embedded.
- **Key matches:** Facts all correct: capital of West Bengal on the eastern bank of the Hooghly; capital of British India until 1911; Tagore association; Mother Teresa founded the Missionaries of Charity there in 1950; trams, Durga Puja, Victoria Memorial and Indian Museum are the city's signature institutions. **Generated image:** the Howrah Bridge at dusk — a steel cantilever truss bridge lit against a blue evening sky over the wide Hooghly — matches the real bridge's unmistakable silhouette and the dusk-over-the-river composition typical of the real article's imagery.
- **Key divergences:** No infobox data (population, area, elevation) and no mention of the 2001 renaming date from Calcutta; compressed to two sections.
- **Confidence:** High.

## 58. https://en.wikinews.org/ — web/en.wikinews.org/index.html
- **Verdict: divergent**
- **Images at audit time: placeholder-only.**
- **Key matches:** As a portrait of Wikinews as it existed for most of its life, this is accurate: tagline "The free-content news source that you can write!", collaborative volunteer news with NPOV aims, lead stories / latest news / developing stories structure, review-before-publication workflow, region and topic categories — all genuine Wikinews.
- **Key divergences:** **The project no longer exists as a writable site.** Following a June 2025 closure proposal, the WMF Board decided in March 2026 to close Wikinews, and all 31 language editions went **read-only on 4 May 2026**; Wikipedia's article now describes it in the past tense as "a discontinued free-content news wiki". The recreation invites readers to "Write a story… anyone can start a story" as if it were live. This also explains the seed-page divergence noted in entry 1: the real Wikipedia sister-projects list has dropped Wikinews (and added Wikifunctions), while every recreation in this crawl still lists Wikinews as a current sister project.
- **Confidence:** High.

## 59. https://en.wikiversity.org/ — web/en.wikiversity.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Slogan "Set learning free" is Wikiversity's real motto. Featured Project on the main page, schools/portals organisation, learning levels from pre-school to tertiary and non-formal, and the distinctive correct point that Wikiversity uniquely welcomes original research alongside teaching materials — all accurate.
- **Key divergences:** Summary-level; no featured project actually named.
- **Confidence:** Medium-high.

## 60. https://query.wikidata.org/ — web/query.wikidata.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (editor screenshot described).
- **Key matches:** The service is described with unusual precision: SPARQL over all Wikidata, result visualisations as tables, images, maps, bubble charts, timelines and graphs; the blue run button; the query-helper (pencil) tool for non-programmers; downloadable JSON/CSV results via the public endpoint. The example queries named are the real canonical ones — "Cats" (with pictures) is the service's signature beginner example, and hospitals / largest cities are genuine example-set staples.
- **Key divergences:** Landing summary only — the real page is the editor itself; no actual example list beyond the (correct) headline examples.
- **Confidence:** High.

## 61. https://music.youtube.com/ — web/music.youtube.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — four generated album-art images embedded (a good multi-image page under the dropped 1-image cap).
- **Key matches:** YouTube Music layout is faithfully captured: Home / Explore / Library rail, "Search songs, albums, artists…" prompt, Cast and Sign in, "Listen again" and "Quick picks" shelves, album cards labelled Playlist · N songs / Artist · Album, and a bottom player bar with skip controls, volume and a live progress position (1:12 / 3:48). The four generated artworks match their described subjects (purple abstract mix art, red desert album cover, green forest playlist art, blue night-city jazz cover).
- **Key divergences:** All music content is invented with openly placeholder names — "The Example Band", "Sample Quartet", "Sample Singer", "Example Trio" and a band literally called "The Placeholders" — none of it corresponds to real charts or releases.
- **Confidence:** Medium-high.

## 62. https://about.meta.com/ — web/about.meta.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — three generated images embedded (Quest VR user, family video call, Meta AI chat), each matching its section.
- **Key matches:** Meta's current strapline is reproduced verbatim: "Build the future of human connection and the technology that makes it possible". Facts correct: founded 2004 as Facebook, renamed Meta in October 2021, HQ Menlo Park; Family of Apps list (Facebook, Instagram, Messenger, Threads, WhatsApp) and Reality Labs / Quest / Horizon / Meta AI coverage all match the real site's structure; nav (Who we are, Our technologies, The metaverse, News, Careers) closely tracks the real about site.
- **Key divergences:** Condensed marketing summary vs. the real site's long product/news pages; generated imagery is generic stock-style rather than Meta's actual product photography.
- **Confidence:** High.

## 63. https://en.wikipedia.org/wiki/Nobel_Peace_Prize — web/en.wikipedia.org/wiki/Nobel_Peace_Prize/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (medal described: Alfred Nobel profile — correct subject for the prize medal image).
- **Key matches:** Award criteria paraphrase Nobel's will correctly (fraternity between nations, abolition/reduction of standing armies, peace congresses); uniquely selected by the Norwegian Nobel Committee and presented in Oslo on 10 December (anniversary of Nobel's death) while other prizes are presented in Stockholm — correct. Laureate spot-checks all correct: Martin Luther King Jr. 1964, Mandela & de Klerk 1993, Malala Yousafzai 2014 as youngest laureate, the ICRC as a three-time recipient, Mother Teresa 1979.
- **Key divergences:** Compressed; no prize-amount or full laureate machinery. Nothing wrong found.
- **Confidence:** High.

## 64. https://en.wikipedia.org/wiki/Mother_Teresa — web/en.wikipedia.org/wiki/Mother_Teresa/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (blue-bordered white sari portrait described — the correct iconic image).
- **Key matches:** Infobox and body facts verified across the board: born Anjezë Gonxhe Bojaxhiu, 26 August 1910 Skopje; died 5 September 1997 (aged 87) Calcutta; Sisters of Loreto in Ireland at 18, arrived India 1929; the 1946 calling; Indian citizenship and founding the Missionaries of Charity in 1950; hospices for HIV/AIDS, leprosy and tuberculosis; Nobel Peace Prize 1979; beatified by John Paul II 2003; canonised by Pope Francis on 4 September 2016. The criticism section (standards of care, abortion/contraception views, donation sources) fairly mirrors the real article's controversies.
- **Key divergences:** Compressed vs. the long real biography; nothing wrong found.
- **Confidence:** High.

## 65. https://en.wikipedia.org/wiki/Encyclopaedia_Britannica — web/en.wikipedia.org/wiki/Encyclopaedia_Britannica/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only.**
- **Key matches:** First published in Edinburgh in instalments 1768–1771; fifteen official print editions; print ended with the 2010 edition; digital-only from 2012; later US-based publication — all correct, including the standard framing of the transition as emblematic of print encyclopedias' displacement (partly by Wikipedia).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 66. https://en.wikipedia.org/wiki/Ada_Lovelace — web/en.wikipedia.org/wiki/Ada_Lovelace/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only.**
- **Key matches:** Augusta Ada King, Countess of Lovelace (born Byron), 10 December 1815 – 27 November 1852 (aged 36) — correct. Only legitimate child of Lord Byron; mathematical education at her mother's insistence; the translated article with appended Notes A–G longer than the article itself, containing the Bernoulli-numbers algorithm recognised as the first intended for a machine, and her speculation about the Engine composing music — all faithfully match the real article.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 67. https://en.wikipedia.org/wiki/Isaac_Newton — web/en.wikipedia.org/wiki/Isaac_Newton/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Kneller portrait described — the real article's lead portrait type).
- **Key matches:** Born 4 January 1643 (New Style) Woolsthorpe; died 31 March 1727 (aged 84) — matching the real infobox's dual-dating. Principia (1687), Opticks (1704), plague-closure "years of wonder" 1665–67 at home, fluxions, Halley's prompting question, Moon/apple same-gravity derivation of Kepler's laws, first practical reflecting telescope 1668, Trinity College / Lucasian Professor / Royal Society president / Warden and Master of the Mint — a full sweep of correct facts, including the careful note that the apple story comes from Newton's own later telling.
- **Key divergences:** Compressed relative to the real article; nothing wrong found.
- **Confidence:** High.

## 68. https://en.wikipedia.org/wiki/Charles_Darwin — web/en.wikipedia.org/wiki/Charles_Darwin/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — and the placeholder's description (Darwin c.1854, balding, beard developing, dark jacket) matches the real article's actual lead photograph (the c.1854 portrait).
- **Key matches:** Dates (12 Feb 1809 Shrewsbury – 19 Apr 1882 Downe, aged 73), Edinburgh and Christ's College, Emma Wedgwood; Beagle second survey 1831–36 aged 22; Galápagos mockingbirds/finches and South American fossils; Malthus read in 1838; twenty years of evidence (pigeons, barnacles, seeds); Wallace prompting the 1858 joint presentation; Origin (1859) avoiding human origins, Descent of Man (1871) adding sexual selection — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 69. https://en.wikipedia.org/wiki/Periodic_table — web/en.wikipedia.org/wiki/Periodic_table/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (the full 18-column colour-coded table described, not rendered).
- **Key matches:** The text-rendered element sequence for periods 1–4 (H 1 through Kr 36) is in the correct order with correct atomic numbers throughout. History correct: Mendeleev 1869 with successful gap predictions (gallium, germanium), Lothar Meyer's independent table, Moseley 1913 re-basing on atomic number, 118 confirmed elements ending at oganesson completing period 7. Group/trend statements (group 1 reactivity, group 17 halogens, group 18 inertness, radius/electronegativity trends) all correct.
- **Key divergences:** Only the first four periods are tabulated in text (the page itself says so); the real article's full interactive table is described, not reproduced. Nothing wrong found.
- **Confidence:** High.

## 70. https://www.esa.int/ — web/www.esa.int/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (ISS Earth view, Juice artist's impression, Copernicus map, Gaia star map — all plausible ESA homepage imagery subjects).
- **Key matches:** ESA's mission sentence is quoted essentially verbatim from the real site ("shape the development of Europe's space capability and ensure that investment in space continues to deliver benefits to the citizens of Europe and the world"). Top sections (About ESA, Science & Exploration, Space Applications, Space Safety, Enabling & Support, Media, Careers) match esa.int. Programme facts correct: Juice launched 2023 to Ganymede/Europa/Callisto; Copernicus Sentinels with free/full/open data; Gaia's billion-plus stars; European Service Module for Orion/Artemis; Kourou spaceport with Ariane and Vega.
- **Key divergences:** "22 Member States" is one stale — Slovenia became the 23rd full Member State on 1 January 2025, and ESA now describes itself as having 23 Member States. Highlight stories are summarised rather than the real dated items.
- **Confidence:** High.

## 71. https://en.wikipedia.org/wiki/World_War_II — web/en.wikipedia.org/wiki/World_War_II/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (montage described — Normandy landing craft, Soviet flag over the Reichstag, Pacific aircraft — matching the real infobox montage's components).
- **Key matches:** Infobox essentials correct: 1 September 1939 – 2 September 1945 (with the 1937 Asia start noted), Allied victory, 70–85 million deaths (the real article's casualty range) including the Holocaust's ~six million Jewish victims. Narrative sequence correct: Poland invasion, Barbarossa June 1941, Pearl Harbor 7 December 1941, El Alamein/Stalingrad turning points, D-Day 6 June 1944, German surrender May 1945, Japanese surrender 2 September 1945 after the atomic bombings and Soviet invasion of Manchuria.
- **Key divergences:** Necessarily a summary of one of Wikipedia's longest articles; nothing wrong found in the sampled text.
- **Confidence:** High.

## 72. https://en.wikipedia.org/wiki/Abraham_Lincoln — web/en.wikipedia.org/wiki/Abraham_Lincoln/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — the placeholder specifies the 1863 Alexander Gardner portrait, which is indeed the real article's famous lead photograph type.
- **Key matches:** Dates (12 Feb 1809 Hodgenville – 15 Apr 1865 Washington, aged 56), 16th president, single House term, 1858 Douglas debates, seven states seceding after the 1860 election, Fort Sumter April 1861, Emancipation Proclamation 1 January 1863 including Black enlistment, Gettysburg Address November 1863, habeas corpus suspension noted as controversial, shot by Booth at Ford's Theatre on 14 April 1865, five days after Appomattox — every sampled fact correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 73. https://en.wikipedia.org/wiki/Saturn — web/en.wikipedia.org/wiki/Saturn/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (Cassini-style ringed view described — the right lead-image subject).
- **Key matches:** Orbital period 29.4 years, 9.5 AU, diameter 116,460 km, density 0.687 g/cm³ (least dense planet), rings ~280,000 km wide and ~10 m thick in places; Galileo's 1610 "handles", Huygens' ring description and Titan; Titan larger than Mercury with nitrogen atmosphere and methane lakes; Enceladus plumes feeding the E ring; Pioneer 11 (1979), Voyagers (1980–81), Cassini–Huygens 2004–2017 with the Grand Finale plunge — all correct.
- **Key divergences:** Moon count given as 146 with the page's own hedge "(2023 count as remembered)" — that was right in 2023, but 128 further moons were recognised in March 2025, making the current official count **274**. A clean example of the crawl's knowledge being a couple of years behind the real article.
- **Confidence:** High.

## 74. https://en.wikipedia.org/wiki/ARPANET — web/en.wikipedia.org/wiki/ARPANET/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (1969 four-node map described — a real, iconic image in the article).
- **Key matches:** Launched 1969, decommissioned 1990; first four nodes UCLA / Stanford Research Institute / UC Santa Barbara / Utah in late 1969; the first host-to-host message on 29 October 1969 crashing after the first two letters of LOGIN ("LO") — the famous detail, correct; Baran and Davies packet switching, Licklider's "Intergalactic Computer Network", BBN's IMPs; Tomlinson's 1971 email and @ choice; TCP/IP flag day 1 January 1983. All verified.
- **Key divergences:** Compressed; the infobox writes successor as a raw "[[Internet]] / NSFNET" wikilink artefact, a formatting blemish not a factual one.
- **Confidence:** High.

## 75. https://en.wikipedia.org/wiki/Alphabet_Inc. — web/en.wikipedia.org/wiki/Alphabet_Inc./index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Googleplex described).
- **Key matches:** Created 2 October 2015 by restructuring Google; Page/Brin founders; Mountain View HQ; Pichai Google CEO 2015 then Alphabet CEO December 2019 on the founders' step-back, with founder voting control via special share classes; "cleaner and more accountable" rationale and Other Bets reporting; the August 2024 US ruling that Google illegally maintained a search monopoly — all correct.
- **Key divergences:** DeepMind is listed among the Other Bets subsidiaries; since the April 2023 merger forming Google DeepMind it sits inside Google rather than as a standalone Alphabet bet — a small structural staleness. Compressed otherwise.
- **Confidence:** High.

## 76. https://www.nasa.gov/missions/artemis — web/www.nasa.gov/missions/artemis/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated SLS-on-pad image embedded (the right subject: SLS stack on a launch pad; the recreation captions it Pad 39B, where Artemis I indeed launched).
- **Key matches:** The lead paragraph is NASA's real Artemis copy: "land the first woman and the first person of color on the lunar surface… and then take the next giant leap: sending the first astronauts to Mars." Mission facts correct: Artemis I uncrewed Nov–Dec 2022; Artemis II crew as announced in 2023 (Wiseman, Glover, Koch, and CSA's Jeremy Hansen) on a free-return lunar loop; Artemis III South Pole landing via a commercial Human Landing System; Starship HLS and Blue Origin Blue Moon named correctly; South Pole water-ice rationale correct.
- **Key divergences:** "The planned Gateway station serves as an outpost" — stated flatly; its status has been under active budget threat, so the certainty is a touch behind the debate (though not yet wrong). The page also carries an on-page footer credit ("a from-memory recreation for the muse-webcrawl experiment"), which of course the real NASA page does not.
- **Confidence:** High.

## 77. https://www.nasa.gov/image-of-the-day — web/www.nasa.gov/image-of-the-day/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (no actual image of the day — the point of the page — is shown).
- **Key matches:** NASA does run an Image of the Day gallery, and the archive/search framing and the pointer to the NASA Image and Video Library at images.nasa.gov are correct; the image categories listed (Webb/Hubble, ISS photography, launches, planetary missions, auroras/eclipses) match the gallery's content.
- **Key divergences:** The defining sentence ("Every day, NASA features a new image… along with a brief explanation written by a professional astronomer") is the description of **Astronomy Picture of the Day (APOD)**, a different (NASA-hosted but separately run) institution; the recreation half-notices this by calling the gallery "adapted from" APOD, conflating the two. And as a gallery page with no daily image populated, it misses its own purpose.
- **Confidence:** High.

## 78. https://en.wikipedia.org/wiki/Euclid — web/en.wikipedia.org/wiki/Euclid/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated "imagined bust" embedded; the page itself (like the real article, which uses an artist's impression since no likeness survives) labels the portrait imagined, which is honest and matches the real article's approach.
- **Key matches:** Active at Alexandria c.300 BC under Ptolemy I; "father of geometry"; Elements in thirteen books with the contents correctly summarised (proportion, number theory incl. Euclidean algorithm and infinitude of primes, incommensurables, solid geometry ending at the five Platonic solids); its two-millennia textbook reign and Bible-comparable print history; Lincoln studying Euclid to learn "demonstrate" — a true anecdote the real article also tells; surviving works list (Data, On Divisions of Figures, Catoptrics, Phaenomena, Optics); parallel-postulate → non-Euclidean geometry → general relativity lineage; ESA's Euclid telescope launched 2023 — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 79. https://en.wikipedia.org/wiki/Afghanistan — web/en.wikipedia.org/wiki/Afghanistan/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Hindu Kush scene described).
- **Key matches:** Current official name Islamic Emirate of Afghanistan; Kabul; all six neighbours correct including the Wakhan Corridor link to China; independence 1919; Great Game buffer history; Soviet–Afghan War 1979–89; first Taliban government 1996–2001; 2001 US-led invasion; Republic for twenty years; Taliban retaking Kabul August 2021 with non-recognition and women's-rights restrictions noted; ethnic groups and Pashto/Dari languages; pomegranates/nuts/saffron agriculture — all accurate. Population "around 40 million (estimate)" is within the range of current estimates.
- **Key divergences:** Compressed country profile without the real article's detailed infobox; nothing wrong found.
- **Confidence:** High.

## 80. https://www.apple.com/ — web/www.apple.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — one generated iPhone hero image embedded (clean product shot matching its description; plausible Apple-style hero, though not a specific current model's exact shot).
- **Key matches:** Product universe and services correctly mapped (iPhone standard/Pro with titanium finishes and Apple Intelligence, MacBook Air/Pro, iMac, Mac mini, Mac Studio on M-series silicon, iPad Pro/Air/mini, Watch, AirPods; Music, TV+, Arcade, iCloud+, Pay, App Store, Apple Card, trade-in/financing). Apple Intelligence description is accurate: rolled out from late 2024 with iOS 18, writing tools, notification summaries, redesigned Siri, image generation, on-device processing plus Private Cloud Compute.
- **Key divergences:** Like the news sites, the homepage narrates itself ("The homepage leads with the newest products…") instead of reproducing the real current hero copy for specific products. Nav order is slightly off (iPhone before iPad; the real order is Store, Mac, iPad, iPhone, Watch, Vision, AirPods…) and the Vision / TV & Home entries are missing.
- **Confidence:** High.

## 81. https://www.amazon.com/ — web/www.amazon.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — four generated product-card images embedded (vacuum, headphones, e-reader, board game), each matching its card.
- **Key matches:** Header anatomy is right: logo, "Deliver to" location slot, Search Amazon bar, language selector, "Hello, sign in / Account & Lists", "Returns & Orders", cart; hamburger "All" menu followed by Today's Deals, Prime Video, Buy Again, Customer Service, Registry, Gift Cards, Sell — real Amazon nav items. Card grid with "Shop now", "Back to top" band, the four footer link columns (Get to Know Us / Make Money with Us / Amazon Payment Products / Let Us Help You) and Conditions of Use / Privacy Notice / Interest-Based Ads legal row all match the real homepage.
- **Key divergences:** All merchandise and the seasonal promotion are invented (the page labels the promo invented); the "Deliver to Seattle 98101" location is a made-up default; legal line dated "© 1996-2025" — the crawl's recurring stale year.
- **Confidence:** High.

## 82. https://www.netflix.com/ — web/www.netflix.com/index.html
- **Verdict: close**
- **Images at audit time: complete** — four generated poster images embedded in the Trending Now row, matching their (invented) title descriptions.
- **Key matches:** The logged-out landing copy is verbatim: title "Netflix - Watch TV Shows Online, Watch Movies Online", "Unlimited movies, TV shows, and more", "Watch anywhere. Cancel anytime.", "Ready to watch? Enter your email to create or restart your membership.", "Get Started >", language selector and Sign In in the header, "Questions? Contact us." and the footer set (Netflix USA, Terms of Use, Privacy, Cookie Preferences, Corporate Information). "Trending Now" is the real current landing-page row.
- **Key divergences:** The trending titles themselves are invented genre posters ("Invented Drama Series", "Invented Space Saga"…) rather than the real current top-10 titles — honestly labelled as invented on the page, but not a memory test of actual trending content.
- **Confidence:** High.

## 83. https://home.cern/ — web/home.cern/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated LHC tunnel image embedded; its subject (blue dipole magnets curving away down the tunnel) matches CERN's iconic real tunnel photography.
- **Key matches:** "CERN — Accelerating science" is the real branding/title. Facts all correct: founded 1954 on the Franco-Swiss border near Geneva; LHC a 27-kilometre ring; experiments ATLAS, CMS, ALICE, LHCb; Higgs boson discovery 2012; Berners-Lee inventing the Web at CERN in 1989; the Science Gateway opened in 2023 as the public/education anchor.
- **Key divergences:** Homepage highlights are summarised in general terms rather than the real dated news items; the header cross-links to LIGO / Royal Society look like crawler cross-references rather than CERN's own navigation wording.
- **Confidence:** High.

## 84. https://open.spotify.com/ — web/open.spotify.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — four generated playlist-cover images embedded, each matching its playlist's described artwork.
- **Key matches:** Title "Spotify - Web Player: Music for everyone" correct. Sidebar (Home, Search, Your Library, Create Playlist, Liked Songs) matches the web player; time-of-day greeting ("Good evening") is a genuine Spotify home behaviour; the "Made For You" family named is the real one: Discover Weekly, Release Radar, Daily Mix 1/2, On Repeat; bottom player bar with progress is faithful.
- **Key divergences:** All playlists and the now-playing track are invented ("Evening Song — Sample Artist"; mixes with round song counts 50/38/44/61). Real home content is personalised, so this is invention in the expected place — but playlist cover art, while plausible, matches no real editorial playlists.
- **Confidence:** Medium-high.

## 85. https://www.microsoft.com/ — web/www.microsoft.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — one generated Surface-style laptop hero image embedded, matching its description.
- **Key matches:** Title "Microsoft — Cloud, Computers, Apps & Gaming" is the real homepage title. The product map is accurate: Microsoft 365 (Word, Excel, PowerPoint, Outlook, OneDrive), Windows 11 and Copilot+ PCs, Surface Pro/Laptop, Xbox and Game Pass for home; Azure, Microsoft 365 for business, Teams, Dynamics 365 and security for business. The central claim — that since 2023 Microsoft's marketing centres on Copilot woven into Windows, 365, Edge and Bing — is true.
- **Key divergences:** The page narrates itself ("Microsoft's homepage leads with hero campaigns…") rather than reproducing the actual current hero slides/copy. The top nav omits the real "All Microsoft" mega-menu framing and small-business entries.
- **Confidence:** High.

## 86. https://www.nature.com/ — web/www.nature.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — one generated false-colour microscopy hero image embedded, a genuinely typical Nature homepage research visual.
- **Key matches:** Journal identity fully correct: British weekly, founded 1869, among the most cited/prestigious, published by Springer Nature, Nature Portfolio family; its pages carried the 1953 DNA-structure papers; section mix (News, research articles, Careers, Podcast, Books & Arts, Collections, Comment/World View on funding) matches the real site's departments.
- **Key divergences:** All specific headlines are invented — though one is candidly labelled "A plausible feature in the journal's current style; specific headlines rotate daily". The chrome is thinner than the real nature.com (no journal-navigation strip, metrics, or sign-in flows beyond labels).
- **Confidence:** High.

## 87. https://www.snapchat.com/ — web/www.snapchat.com/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated AR-lens selfie image embedded, matching the page's "friends using a playful dog-ear AR lens" description and Snapchat's Lens-centred marketing.
- **Key matches:** Hero copy is near-verbatim from the real site: "Snapchat is a fast and fun way to share the moment with your friends and family. Snapchat opens straight to the camera — just tap to capture a photo or press and hold for video. Add a Lens, doodle or caption, send it to friends, and it disappears after it's seen." Top nav (Ads · Spectacles · Filters & Lenses · Download · Stories · Spotlight) matches snapchat.com's real sections; ghost mark and yellow branding; "Log in to chat, snap and enjoy stories on the web" reflects Snapchat for Web.
- **Key divergences:** Footer is abbreviated (Support / Community Guidelines / Privacy / Terms are real, but the real footer is far longer with company/careers/legal groups).
- **Confidence:** High.

## 88. https://scholar.google.com/ — web/scholar.google.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none needed — Scholar's real page is famously bare: logo, search box, links).
- **Key matches:** The About paragraph is a faithful paraphrase of Google's own Scholar description ("provides a simple way to broadly search for scholarly literature… articles, theses, books, abstracts and court opinions, from academic publishers, professional societies, online repositories, universities and other web sites"). Feature list correct: relevance ranking with citation counts and "Cited by" links, author profiles with h-index, library links, alerts — and the Newton-play tagline "Stand on the shoulders of giants" is Scholar's real motto, correctly attributed as a play on Newton.
- **Key divergences:** The page adds an explanatory "Features" section where the real scholar.google.com shows only the search box with links (About, and profile/library links when signed in) — accurate content, richer chrome than reality.
- **Confidence:** High.

## 89. https://www.khanacademy.org/ — web/www.khanacademy.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded at audit time).
- **Key matches:** Title and mission line are right ("provide a free, world-class education to anyone, anywhere" — the real wording is "for anyone, anywhere"); subject structure correct (maths by grade through calculus/statistics/linear algebra, science incl. AP courses, humanities, personal finance, test prep); pedagogy accurately described (short videos, practice with instant feedback, mastery-based progress, teacher dashboards); Khanmigo correctly identified as its AI tutor; Sal Khan founding story (tutoring cousins remotely in the mid-2000s) correct.
- **Key divergences:** The "official SAT prep built with the College Board" is presented in past-ish hedged form ("as long offered") — that partnership-era offering has been wound down/replaced since the digital SAT transition, so it is (appropriately hedged) history rather than a current homepage feature.
- **Confidence:** High.

## 90. https://www.nhm.ac.uk/ — web/www.nhm.ac.uk/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Hintze Hall image embedded, showing the suspended blue whale skeleton, matching the hall's real appearance since 2017.
- **Key matches:** Every fact checks out: ~80 million items across the five collections (botany, entomology, mineralogy, palaeontology, zoology); Waterhouse's Romanesque "cathedral to nature" opened 1881; the blue whale "Hope" has hung in Hintze Hall since 2017, succeeding Dippy the Diplodocus; the Darwin Centre cocoon; free entry to permanent galleries; Wildlife Photographer of the Year as the museum's famous competition/exhibition.
- **Key divergences:** "Dippy… now tours" is a little dated (the tour era ended; Dippy has since been on long-term display in Coventry) — a minor staleness, not a fabrication.
- **Confidence:** High.

## 91. https://www.royalsociety.org/ — web/www.royalsociety.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Founded 1660 and "the oldest scientific academy in continuous existence" — the Society's own self-description; motto Nullius in verba, "take nobody's word for it"; Philosophical Transactions began 1665 as the world's first science journal; Copley Medal correctly flagged as the oldest surviving scientific award; Summer Science Exhibition each July; fellowship scale (~1,700 Fellows and Foreign Members, hedged "as recalled") is in the right range.
- **Key divergences:** Summary-level only; no specific current content. Nothing wrong found.
- **Confidence:** High.

## 92. https://www.ligo.org/ — web/www.ligo.org/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated aerial of the L-shaped detector embedded; it matches the iconic real aerial photographs of the Hanford/Livingston corner stations with their two 4-km arms.
- **Key matches:** Operated by Caltech and MIT; twin detectors at Hanford, Washington and Livingston, Louisiana; 4-km arms sensing displacements far below a proton's width; GW150914 announced February 2016; 2017 Nobel to Weiss, Barish and Thorne; observing runs O1–O4 with Virgo and KAGRA; open data and public alerts; LSC membership "more than a thousand" — all correct.
- **Key divergences:** Catalogue size kept vague ("hundreds of candidate and confirmed events, as recalled") rather than a specific number; a fair hedge, consistent with the real growth of the GraceDB catalogue.
- **Confidence:** High.

## 93. https://www.ams.org/ — web/www.ams.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded; the real AMS homepage is likewise mostly text/links).
- **Key matches:** Founded 1888; journals correctly named (Journal of the AMS, Transactions, Notices as the membership magazine); MathSciNet described correctly with its lineage to Mathematical Reviews (begun 1940); Joint Mathematics Meetings each January as one of the world's largest maths gatherings; Cole and Steele Prizes real AMS prizes.
- **Key divergences:** Summary-level; nothing wrong found.
- **Confidence:** High.

## 94. https://www.rsc.org/ — web/www.rsc.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded at audit time).
- **Key matches:** Identity and publishing stable correct: Chemical Science as the gold open-access flagship, Chemical Communications, Chemical Society Reviews, the Journal of Materials Chemistry family, RSC Education for teachers; membership grades up to Fellow (FRSC); degree accreditation; roots in the Chemical Society founded 1841. The quoted mission line closely tracks the RSC's real wording about connecting the world with the chemical sciences and investing in chemistry's future.
- **Key divergences:** Summary-level homepage only; nothing wrong found.
- **Confidence:** High.

## 95. https://pubmed.ncbi.nlm.nih.gov/ — web/pubmed.ncbi.nlm.nih.gov/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none needed; the real page is a search box).
- **Key matches:** The lead paragraph reproduces the real NCBI/PubMed blurb and the feature set is exactly right: advanced-search builder, filters by type/date/language/free full text, MeSH vocabulary searching, My NCBI saved searches/alerts, citation export and clipboard.
- **Key divergences:** The blurb's count is stale: "more than 35 million citations" was true around 2022; the real blurb now reads over 39–40 million. Same systemic ~2025-knowledge lag seen in Wikipedia counts and © years.
- **Confidence:** High.

## 96. https://www.ncbi.nlm.nih.gov/ — web/www.ncbi.nlm.nih.gov/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** NCBI's identity (part of the US National Library of Medicine at NIH) and the flagship resources are all described correctly: PubMed, GenBank as "the annotated collection of all publicly available DNA sequences", BLAST's full name and purpose, plus Bookshelf, ClinVar, dbSNP, GEO and Taxonomy; the cross-database search box and resource categories (Literature, Genes, Proteins, Genomes, Clinical…) match the real homepage's organisation and its familiar blue NIH design.
- **Key divergences:** Summary-level; nothing wrong found.
- **Confidence:** High.

## 97. https://news.google.com/ — web/news.google.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (story thumbnails not generated at audit time).
- **Key matches:** The product model is exactly right: aggregated personalised front page, "Your briefing", Top stories as clusters with multiple publishers side-by-side and "Full coverage" views, followed/local stories, a Fact Check section, and the standing topic tabs (World · U.S. · Business · Technology · Entertainment · Sports · Science · Health) — the correct post-2018 Google News design vocabulary.
- **Key divergences:** No actual headlines (necessarily user/time-specific), so the page describes the machine rather than showing output — the same genre-summary fallback as other aggregators, but here it costs less because the real page is un-reproducible for anyone else anyway.
- **Confidence:** High.

## 98. https://about.google/ — web/about.google/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded at audit time).
- **Key matches:** Mission statement verbatim ("organize the world's information and make it universally accessible and useful"); product roster correct with Gemini correctly noted as now woven through; commitments accurately tracked: carbon-neutral history, the 24/7 carbon-free-energy-by-2030 goal exactly as Google states it, Google.org and flood-forecasting AI-for-good; company history (founded 1998 by Page and Brin at Stanford; largest Alphabet subsidiary since 2015) correct.
- **Key divergences:** Summary of themes rather than the real page's specific stories/campaigns; nothing wrong found.
- **Confidence:** High.

## 99. https://accounts.google.com/ — web/accounts.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (correctly none — the real card is text-only).
- **Key matches:** Structure is the real flow: title "Sign in — Google Accounts", a centred card asking "Email or phone", "Forgot email?", "Create account" dropdown and "Next" button, and the one-account-for-everything framing (Gmail, Drive, YouTube, Maps, Photos) with security management at myaccount.google.com.
- **Key divergences:** The helper line uses older wording ("Use a private browsing window to sign in") where the current page says "Not your computer? Use Guest mode to sign in privately." — a small wording drift in one of the most-seen pages on the web. The sign-in explanatory text about passkeys/2-Step belongs to help/account pages rather than this card itself.
- **Confidence:** High.

## 100. https://ekantipur.com/ — web/ekantipur.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Ownership and stable facts correct: eKantipur is Kantipur Publications' portal, publisher of Kantipur and The Kathmandu Post; Kantipur daily founded 1993 and Nepal's largest-circulation Nepali paper; Kantipur Television and Radio Kantipur in the same group; the Nepali section labels (राष्ट्रिय National, प्रदेश Provinces, अर्थ/वाणिज्य Business, विश्व World, खेलकुद Sports, मनोरञ्जन Entertainment, विचार Opinion) are the real section names, and cricket's prominence in Nepali sports coverage is right.
- **Key divergences:** Headlines are genre description only (Nepali politics/Kathmandu news) with no specific stories — the news-homepage fallback pattern.
- **Confidence:** Medium-high.

## 101. https://www.nic.net.np/ — web/www.nic.net.np/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded; the real registry site is similarly plain).
- **Key matches:** The genuinely unusual facts are right: the .np ccTLD registry has been run for decades by Mercantile Communications; registration has famously been free for Nepali citizens/organisations against citizenship certificates or company-registration documents; second-level labels com.np / org.np / gov.np / edu.np / net.np; Nepal's ISO code NP and calling code +977; .np delegation dates to the mid-1990s. The page hedges its recall ("as recalled") appropriately.
- **Key divergences:** Branding as "Nepal Network Information Centre" and the register.com.np portal match my knowledge of the Mercantile-run system, but I could not re-verify the current site chrome as firmly as the registry facts themselves — confidence slightly lower for that reason.
- **Confidence:** Medium.

## 102. https://wikimediafoundation.org/ — web/wikimediafoundation.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (community photo/logo described).
- **Key matches:** The quoted mission is essentially the Foundation's real mission statement ("empower people around the world to collect and develop educational content under a free licence… and to disseminate it effectively and globally"); the small-donor funding model, annual plan/reports, finances/transparency pages, Board of Trustees, press/research/technology coverage and San Francisco base are all correct.
- **Key divergences:** Overview-level only; no specific current annual-plan or campaign content.
- **Confidence:** High.

## 103. https://meta.wikimedia.org/ — web/meta.wikimedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (community logo described).
- **Key matches:** Meta-Wiki's role is exactly right: global community coordination site hosting RfCs, steward/global-admin coordination, cross-wiki blacklists, translation coordination, grants, elections and movement strategy, plus the Babel forum.
- **Key divergences:** Its "Other Wikimedia projects" footer still lists **Wikinews** as a live sister project — the same systematic post-closure staleness seen across nearly every recreation's project list.
- **Confidence:** High.

## 104. https://species.wikimedia.org/ — web/species.wikimedia.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (leaf/tree-of-life logo described — the right family of motif for the real Wikispecies logo).
- **Key matches:** Purpose and structure exactly right: a free directory aiming to catalogue all life (animals, plants, fungi, bacteria, archaea, protists, viruses); taxon pages with classification, name authority, type information, synonyms, distribution, references and vernacular names; top-level browsing from Archaea/Bacteria/Eukaryota down through the kingdoms and ranks; links out to Wikidata and Commons.
- **Key divergences:** Only the same Wikinews-in-footer staleness (shared template across the recreations), not a content error.
- **Confidence:** High.

## 105. https://ru.wikipedia.org/ — web/ru.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (puzzle-globe described; the rotating featured content is described generically rather than populated).
- **Key matches:** Written in correct Russian with the real main-page anatomy: Избранные статьи (featured), Хорошие статьи (good articles), Текущие события, Знаете ли вы?, Изображение дня — and sister projects under their correct Russian names (Викисловарь, Викиучебник, Викицитатник, Викитека, Викигид, Викиверситет, Викиданные). "Около двух миллионов статей" is accurate (Russian Wikipedia passed 2 million in 2024).
- **Key divergences:** All daily content is genre description rather than the actual day's articles, and the sister list includes Викиновости (the closed Wikinews) while omitting Wikifunctions.
- **Confidence:** High.

## 106. https://zh.wikipedia.org/ — web/zh.wikipedia.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (puzzle-globe described).
- **Key matches:** Correct Chinese throughout; the real zh main-page modules are all present under their real names: 特色条目 (featured), 优良条目 (good articles), 新闻动态 (in the news), 你知道吗？ (did you know), 历史上的今天 (on this day), 特色图片 (featured picture). Article count "约140多万" matches reality (~1.48 million). The Simplified/Traditional script-variant system is correctly noted.
- **Key divergences:** Daily module contents are described rather than populated; nothing substantively wrong.
- **Confidence:** High.

## 107. https://www.esa.int/Applications/Observing_the_Earth/Copernicus — web/www.esa.int/Applications/Observing_the_Earth/Copernicus/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Institutional structure exactly right: Copernicus is the EU's Earth-observation programme, coordinated/managed by the European Commission in partnership with ESA, which develops and flies the Sentinels. The Sentinel family assignments are correct (1 radar, 2 multispectral land, 3 ocean/land colour and temperature, 5P atmosphere, 6 sea level), as are the six services (land, marine, atmosphere, climate change, emergency management, security) and the free, full and open data policy. The Sentinel-1B failure and its 2024 replacement (Sentinel-1C, launched Dec 2024) are correctly recalled, as is ESA's "most ambitious Earth observation programme to date" line.
- **Key divergences:** Overview length only; nothing wrong found.
- **Confidence:** High.

## 108. https://www.meta.com/quest — web/www.meta.com/quest/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated white Quest-style headset on a gradient embedded; matches Meta's real product photography style and the current headset's design.
- **Key matches:** Hardware facts correct: Quest 3 flagship with pancake lenses and Snapdragon XR2 Gen 2, Quest 3S as the lower-priced model, colour-passthrough mixed reality, storage tiers and accessories (Elite straps, charging docks, cases); Beat Saber as the flagship software title and Horizon Worlds as the social push are right.
- **Key divergences:** App Lab is presented as a separate live channel; Meta folded App Lab into the Horizon Store in 2024, so it survives only as a store section — minor staleness.
- **Confidence:** High.

## 109. https://www.nasa.gov/mission/james-webb-space-telescope — web/www.nasa.gov/mission/james-webb-space-telescope/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Webb image (gold segmented mirror, silver sunshield) embedded and true to the observatory's real appearance.
- **Key matches:** All signature facts correct: 6.5-metre gold-coated mirror, tennis-court-sized sunshield, L2 halo orbit ~a million miles out, infrared mission; launched Christmas Day 2021 on an Ariane 5 from Kourou (ESA's contribution), two-week unfolding, science from July 2022 beginning with the SMACS 0723 deep field; NASA/ESA/CSA partnership operated by STScI; exoplanet-atmosphere molecules (water vapour, CO₂, methane) correctly cited among early results.
- **Key divergences:** Nothing wrong found beyond overview length.
- **Confidence:** High.

## 110. https://www.apple.com/iphone — web/www.apple.com/iphone/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (no product photography embedded at audit time — a notable gap for a page whose entire real design is photography).
- **Key matches:** Lineup anatomy and feature facts right: Pro-first ordering, two sizes per tier; USB-C adopted line-wide with iPhone 15; Action button; Dynamic Island brought down-range; ProRes and spatial video for Vision Pro; Crash Detection and Emergency SOS via satellite; Apple Intelligence woven through.
- **Key divergences:** The headline "iPhone. Forged in titanium" is the iPhone 15 Pro era's phrasing (the page itself hedges "in the Pro era's phrasing"): the current Pro generation moved back to an aluminium unibody and the lineup gained the thin "Air" model, neither reflected here — this page's mental snapshot is ~2023–24, older than most of the crawl's 2025 tinge.
- **Confidence:** High.

## 111. https://mail.google.com/ (Gmail inbox) — web/mail.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none needed; Gmail's real UI is icon/text chrome).
- **Key matches:** Interface anatomy is faithful: Compose button, Inbox with unread count, Starred / Snoozed / Sent / Drafts, label list, Primary | Promotions | Social category tabs, row layout (checkbox, star, sender, subject — snippet, time), and the footer storage line in Google's real format ("4.1 GB of 15 GB used"). This is the rules-sanctioned "private/invented feed" category, and the shell is convincingly the real shell.
- **Key divergences:** All mail content is invented (a library book notice, a "North Peak Airlines" check-in, a garden-club newsletter — plausible generic senders, none real). Inbox count "(3)" matches the tab title, and timestamps are internally consistent, but nothing here tests memory of real data — by design.
- **Confidence:** High.

## 112. https://drive.google.com/ (My Drive) — web/drive.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded; file-type icons are text glyphs as is roughly true of the real list view).
- **Key matches:** Drive chrome is right: "+ New" button, Home / My Drive / Computers / Shared with me / Recent / Starred navigation, search-in-Drive bar, Name–Owner–Last modified–Size column list, storage indicator ("8.2 GB of 15 GB used"), and file rows with sensible types and sizes.
- **Key divergences:** Contents are an invented private file set (holiday photos, house budget, Lisbon itinerary, lease PDF) — again the sanctioned invented-feed pattern rather than a memory failure. One locale slip: the trash is labelled "Bin" (UK wording) where the US product says "Trash".
- **Confidence:** High.

## 113. https://maps.google.com/ — web/maps.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** — the map itself is a self-declared "stylised placeholder, not real cartography", with pin markers.
- **Key matches:** The Maps UI grammar is right: search bar with Directions affordance, category chips along the top, place cards in the real format ("Harbour Coffee House ★★★★☆ 4.6 (1,204) · Café · Closes 18:00"), transit stop card with departure frequency, zoom controls, Satellite/Map layer toggle and the "Map data © Google" attribution line.
- **Key divergences:** The specific places are invented; the attribution year reads ©2025 (the crawl's stale-year pattern); chips include "Petrol" (UK) rather than "Gas stations" (US). The actual cartography — the product's core — is necessarily absent.
- **Confidence:** High.

## 114. https://pt.wikipedia.org/ — web/pt.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (globe described).
- **Key matches:** Correct Portuguese; article count "mais de 1,1 milhão" right (≈1.15M); main-page modules correctly named in Portuguese (artigo em destaque, atualidades, sabia que, imagem do dia).
- **Key divergences:** The page carries a leftover boilerplate block in **Italian** ("Pagina principale / Página principal / Strona główna — La pagina principale presenta i contenuti in evidenza…") — the identical filler paragraph, in Italian, pasted into the Portuguese, Italian and Polish homepages alike; a template artefact from whichever crawler generated this cluster. Daily content again described, not populated.
- **Confidence:** High.

## 115. https://it.wikipedia.org/ — web/it.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Correct Italian; "circa 1,9 milioni di voci" is accurate (≈1.95M); module names correct (voce in evidenza, notizie di attualità, lo sapevi che, immagine del giorno).
- **Key divergences:** Same shared cross-language boilerplate block (here at least the filler is in the page's own language family, but it is still canned text repeated verbatim across three editions); no actual featured content.
- **Confidence:** High.

## 116. https://pl.wikipedia.org/ — web/pl.wikipedia.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only.**
- **Key matches:** Correct Polish; "około 1,6 miliona haseł" accurate (≈1.68M); main-page modules correctly identified (artykuł na medal, aktualności, czy wiesz, ilustracja dnia).
- **Key divergences:** Same Italian-language boilerplate contamination as the Portuguese/Italian pages — the clearest sign this cluster was generated from one template; daily content not populated.
- **Confidence:** High.

## 117. https://nl.wikipedia.org/ — web/nl.wikipedia.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Correct Dutch; "meer dan twee miljoen artikelen" right (≈2.19M); founding in June 2001 correct; main-page pattern accurately described (uitgelicht artikel, "Wist je dat?", actueel nieuws, "Op deze dag", uitgelichte afbeelding, subject portals); Dutch sister projects correctly named (WikiWoordenboek, Wikibooks, Wikisource, Wikivoyage).
- **Key divergences:** Content descriptive rather than populated; count hedged "zoals herinnerd" unnecessarily since it is right.
- **Confidence:** High.

## 118. https://ar.wikipedia.org/ — web/ar.wikipedia.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Correct Arabic (rendered RTL in the page's text flow); article count "أكثر من مليون مقالة" right (≈1.3M); Arabic edition's July 2003 start correct; main-page sections correctly named in Arabic (featured article, in the news, did you know, on this day, featured picture) plus topic portals; sisters listed with Arabic names (ويكاموس، ويكي الكتب، ويكي مصدر، ويكي الاقتباس).
- **Key divergences:** Descriptive rather than populated content; nothing substantively wrong.
- **Confidence:** High.

## 119. https://www.bbc.com/news — web/www.bbc.com/news/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** — a labelled placeholder "a photograph illustrating the section's top story" stands in for the lead image; no story exists for it to illustrate.
- **Key matches:** Section taxonomy correct: World, UK, Politics, Business, Health, Science & Technology as BBC News areas, live pages for developing stories, explainers and correspondent analysis as house formats, regional desks (Europe, Asia, Africa, the Americas, Middle East) all real.
- **Key divergences:** Again zero actual news: the "section front" contains no headlines at all, just a description of what the front brings together — the news-recreation pattern in its purest form. Weather and Sport are described as if subsections of this page rather than sibling sections.
- **Confidence:** High.

## 120. https://www.bbc.com/sport — web/www.bbc.com/sport/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (generic top-story photo placeholder).
- **Key matches:** Coverage map right: football at greatest length (Premier League and internationals), then cricket, Formula 1, rugby, tennis, golf and athletics; BBC Sport's signature formats — live text commentaries, scores and fixtures services — correctly identified.
- **Key divergences:** No scores, fixtures, results or headlines whatsoever; the page is a paragraph about BBC Sport rather than a recreation of it.
- **Confidence:** High.

## 121. https://en.wikipedia.org/wiki/Portal:Science — web/en.wikipedia.org/wiki/Portal:Science/index.html
- **Verdict: close**
- **Images at audit time: complete** — two generated images embedded (DNA double helix, nebula) matching the portal's selected article and header roles.
- **Key matches:** Lead definition tracks the real Science article ("systematic enterprise that builds and organises knowledge in the form of testable explanations and predictions"); natural/social/formal science division correct. Selected-article summary (DNA, 1953 Watson–Crick–Franklin "and colleagues", four bases encoding genes) accurate. All three Did-you-know facts check out: sunlight takes ~8 minutes to reach Earth; human genome ~3 billion base pairs; octopuses have three hearts and blue copper-based blood.
- **Key divergences:** Rotating content (selected article/DYK) is a plausible instance rather than the day's actual picks — inherently unverifiable against a same-day snapshot, but factually clean as written.
- **Confidence:** High.

## 122. https://en.wikipedia.org/wiki/Portal:Mathematics — web/en.wikipedia.org/wiki/Portal:Mathematics/index.html
- **Verdict: close**
- **Images at audit time: complete** — two generated images embedded (Pythagorean-theorem tiling, Newton engraving) matching the selected article and portal art.
- **Key matches:** The introduction reproduces Wikipedia's real Mathematics lead almost exactly ("numbers (arithmetic and number theory), formulas and related structures (algebra), shapes and the spaces in which they are contained (geometry), and quantities and their changes (calculus and analysis)"). Pythagorean theorem section accurate (known to earlier cultures, hundreds of proofs). DYK facts correct: π is irrational and transcendental; primes thin out yet are infinite (Euclid); "algebra" from the title of al-Khwarizmi's 9th-century treatise.
- **Key divergences:** Rotating picks plausible rather than the day's actual selections; nothing wrong found.
- **Confidence:** High.

## 123. https://en.wikipedia.org/wiki/Portal:History — web/en.wikipedia.org/wiki/Portal:History/index.html
- **Verdict: close**
- **Images at audit time: complete** — two generated images embedded (ancient ruins at sunrise for the Roman Empire selected article; a Lincoln portrait) matching their placements.
- **Key matches:** Introduction is a fair summary of the real History article (written records, prehistory before writing, source types, narrative debate). Selected article (Roman Empire) correct: conventionally 27 BC with Octavian/Augustus to AD 476 in the West, greatest extent under Trajan from Britain to Mesopotamia, tens of millions governed. Portal cross-navigation (Arts, Biography, Geography, History, Mathematics, Science, Society, Technology) matches Wikipedia's real portal family.
- **Key divergences:** Rotating content plausible-instance only; nothing wrong found.
- **Confidence:** High.

## 124. https://www.facebook.com/feed — web/www.facebook.com/feed/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — four generated images embedded (stories collage, garden beds, cycling group, farmers-market stalls), each matching its post.
- **Key matches:** The logged-in chrome is faithful: Search Facebook, centre nav (Home · Watch · Marketplace · Groups · Gaming), Menu/Messenger/Notifications, left shortcut column (profile, Friends, Memories, Saved, Groups, Marketplace, Feeds, Events), "What's on your mind, Alex?" composer prompt — the real placeholder format — Stories row, post cards with reaction icons and like/comment/share counts, right-rail Contacts with green presence dots and Group conversations. A Page post is even wryly labelled "Sponsored-ish typical post".
- **Key divergences:** As with the homepage version of the feed, every person and post is invented (Alex Morgan, Priya Sharma, Tom Alvarez, Harbour Cycling Club, City Farmers Market) — sanctioned invented-feed content, but again the invented "Alex Morgan" collides with a real famous athlete's name.
- **Confidence:** High.

## 125. https://www.youtube.com/premium — web/www.youtube.com/premium/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded; the real page is banner- and screenshot-led, so this is a gap in feel, not facts).
- **Key matches:** Benefit set exactly right: ad-free across YouTube and YouTube Kids, downloads, background play, YouTube Music Premium bundled, 1080p Premium enhanced bitrate; plan structure right (Individual, Family — up to five household members, Student, monthly after trial); the recalled US individual price of $13.99/month is still the real current price.
- **Key divergences:** None factual; terser than the real marketing page.
- **Confidence:** High.

## 126. https://en.wikipedia.org/wiki/Portal:Technology — web/en.wikipedia.org/wiki/Portal:Technology/index.html
- **Verdict: close**
- **Images at audit time: complete** — two generated images embedded (vintage WWW browser window, Edison-era lab) matching the selected article and portal theme.
- **Key matches:** Introduction tracks the real Technology article's definition ("application of conceptual knowledge to achieve practical goals, especially in a reproducible way"); selected article on the World Wide Web accurate (Berners-Lee at CERN 1989, document-sharing origin, public opening in the early 1990s); all three DYK facts correct — Lovelace as first programmer (1840s), ARPANET's four nodes in 1969, the transistor at Bell Labs in 1947.
- **Key divergences:** Rotating selections are plausible instances rather than the day's actual picks; nothing wrong found.
- **Confidence:** High.

## 127. https://en.wikipedia.org/wiki/Alan_Turing — web/en.wikipedia.org/wiki/Alan_Turing/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated B&W portrait embedded matching the placeholder's "1950s photograph" description; the real article's lead photo is indeed an early-1950s portrait type.
- **Key matches:** Not a fact out of place: dates (23 June 1912 London – 7 June 1954 Wilmslow), the 1936 paper and Turing machine, Bletchley Park and the Bombe against naval Enigma, ACE stored-program designs, Manchester work and first programmer's manual, the 1950 "Computing Machinery and Intelligence" imitation game, 1952 prosecution and chemical castration, cyanide death ruled suicide, 2013 royal pardon, the 2017 "Alan Turing law", and the Bank of England £50 note issued 2021.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 128. https://en.wikipedia.org/wiki/Big_Bang — web/en.wikipedia.org/wiki/Big_Bang/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated expansion-timeline cone embedded, matching the real article's famous artist's-conception lead image (bright origin widening into CMB and galaxy eras).
- **Key matches:** Age 13.8 billion years; Lemaître's primeval atom (1927–31); Hubble recession; Hoyle coining "Big Bang" dismissively in a 1949 radio broadcast while backing steady-state; CMB predicted 1948, found by Penzias and Wilson 1965, at 2.7 K; primordial nucleosynthesis predicting H/He/Li abundances; COBE/WMAP/Planck progression; accelerating expansion discovered 1998 driving the dark-energy open question — all correct.
- **Key divergences:** Compressed overview of a long article; nothing wrong found.
- **Confidence:** High.

## 129. https://science.nasa.gov/mission/parker-solar-probe — web/science.nasa.gov/mission/parker-solar-probe/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (artist's-concept and corona photographs described; no generated PNGs embedded at audit time).
- **Key matches:** A fact-dense page with everything right: launched 12 August 2018 on a Delta IV Heavy from Cape Canaveral; seven Venus gravity assists; first corona crossing April 2021 ("touching the Sun"); record closest approach 24 December 2024 at ~6.1 million km / 3.8 million miles and ~690,000 km/h (430,000 mph) — correctly glossed as ~0.064% of light speed, with repeat passes in 2025; ~11 cm carbon-composite shield facing ~1,370 °C; Eugene Parker predicted the solar wind in 1958, was the first person to have a NASA mission named for them while living, and watched the launch aged 91; Johns Hopkins APL as builder/manager.
- **Key divergences:** Nothing wrong found. (Note the crawl now spans two NASA domains, www.nasa.gov and science.nasa.gov, with overlapping mission coverage.)
- **Confidence:** High.

## 130. https://en.wikipedia.org/wiki/Deep_learning — web/en.wikipedia.org/wiki/Deep_learning/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated layered-network diagram embedded, matching the standard explanatory imagery for the topic.
- **Key matches:** The history is accurate throughout: perceptron in the 1950s, backpropagation from the 1980s, the 2012 AlexNet/ImageNet GPU breakthrough opening the modern era, CNNs/RNNs and the transformer since 2017 with attention underlying GPT-family LLMs, milestones (AlphaGo, AlphaFold, DALL-E and diffusion models, public conversational systems from 2022), and the standard criticisms (opacity, data hunger, compute cost, confident errors, inherited bias).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 131. https://en.wikipedia.org/wiki/Antibiotic — web/en.wikipedia.org/wiki/Antibiotic/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — the placeholder describes a disc-diffusion assay plate, which is exactly the kind of image the real article leads with.
- **Key matches:** The lead closely tracks the real article's opening ("a type of antimicrobial substance active against bacteria… the most important type of antibacterial agent for fighting bacterial infections… may either kill or inhibit the growth of bacteria"), including the viruses/fungi caveats. Fleming's 1928 penicillin discovery and the Florey/Chain development in the early 1940s correct; major classes all real; antimicrobial resistance framed as WHO does; resistant infections "directly responsible for over a million deaths in 2019" matches the GRAM study's 1.27 million estimate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 132. https://en.wikipedia.org/wiki/Cosmic_microwave_background — web/en.wikipedia.org/wiki/Cosmic_microwave_background/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — the placeholder describes the Planck all-sky CMB map, the real article's signature image.
- **Key matches:** Precision-grade accuracy: recombination ~380,000 years after the Big Bang; temperature 2.725 K; predicted by Gamow, Alpher and Herman in 1948; discovered by Penzias and Wilson in 1965 via the Holmdel antenna hiss; Nobel 1978; fluctuations ~1 part in 100,000 mapped by COBE (1992), WMAP and Planck; composition ordinary matter ~5%, dark matter ~27%, dark energy ~68%; dipole motion ~370 km/s — every number checks out against the real article.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 133. https://www.apple.com/shop/go/buy_iphone — web/www.apple.com/shop/go/buy_iphone/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — a generated iPhone lineup image embedded (row of models from the back), plausible store-style art.
- **Key matches:** The buying-flow structure is right: model tiers with feature summaries, Apple Trade In credit, monthly financing subject to approval, carrier offers and activation at checkout, free delivery or Apple Store pickup — the real buy-flow ingredients, in Apple's voice.
- **Key divergences:** The page conspicuously withholds all specifics — no model names, storage tiers or prices ("From a flagship price, or monthly"), openly hedged as "remembered in outline". Worse, it sells the **iPhone SE with Home button and Touch ID** as the budget tier: the SE was discontinued in February 2025 and replaced by the iPhone 16e (Face-ID design, no Home button), so the lineup snapshot is stale.
- **Confidence:** High.

## 134. https://en.wikipedia.org/wiki/Dwarf_planet — web/en.wikipedia.org/wiki/Dwarf_planet/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Pluto image embedded showing the heart-shaped Sputnik Planitia, matching New Horizons' iconic real photograph used by the article.
- **Key matches:** The IAU definition is reproduced essentially verbatim (direct Sun orbit, hydrostatic equilibrium, neighbourhood not cleared, not a satellite); the five recognised dwarf planets correctly placed (Ceres in the asteroid belt; Pluto, Haumea, Makemake, Eris in the Kuiper belt); candidate examples (Sedna, Orcus, Quaoar) real; the 2005 Eris discovery forcing the 2006 Prague vote; Dawn orbiting Ceres from 2015 and the New Horizons Pluto flyby of July 2015 with its glaciers, water-ice mountains and nitrogen atmosphere — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 135. https://en.wikipedia.org/wiki/Baroque — web/en.wikipedia.org/wiki/Baroque/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Baroque church façade described).
- **Key matches:** Flourishing from the early 17th century to the 1750s, after Renaissance/Mannerism, in Counter-Reformation and absolutist service; Bernini's St Peter's Square colonnade and Versailles as emblems; Caravaggio's chiaroscuro, Rubens, Rembrandt correctly characterised; music c.1600–1750 inventing opera/concerto/sonata and tonal harmony, masters Monteverdi–Vivaldi–Handel–Bach with Bach's 1750 death the conventional period end; basso continuo; colonial spread to Latin America and the Philippines; Rococo and Neoclassicism as successors — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 136. https://en.wikipedia.org/wiki/Electric_motor — web/en.wikipedia.org/wiki/Electric_motor/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (cutaway motor described — the standard explanatory image for this article).
- **Key matches:** Lead definition tracks the real article (converts electrical to mechanical energy via magnetic field and winding current producing shaft torque; generator as the reverse machine); history correct — 1820s–30s demonstrations (Faraday's rotation, Jedlik, Davenport), practical DC motors in the 1870s, Tesla's 1888 AC induction motor as industry's brushless workhorse; type taxonomy (brushed/brushless DC, induction, synchronous, stepper, servo, linear) and the VFD/inverter drive revolution all right.
- **Key divergences:** Compressed; the 80–95% efficiency range for larger motors is a fair generalisation rather than a figure from the article.
- **Confidence:** High.

## 137. https://en.wikipedia.org/wiki/Istanbul — web/en.wikipedia.org/wiki/Istanbul/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded at audit time).
- **Key matches:** Facts all correct: largest city in Turkey at roughly 16 million, straddling the Bosphorus between Europe and Asia; founded as Byzantium c.657 BC, refounded as Constantinople in 330, taken by Mehmed II in 1453, Ottoman capital until dissolution, the name Istanbul official in general usage from 1930; Ankara political capital since 1923; historic peninsula landmarks (Hagia Sophia, Blue Mosque, Topkapi, Grand Bazaar); three Bosphorus bridges plus tunnels — all right.
- **Key divergences:** The page openly stamps itself ("Type: Wikipedia article (recreated from memory)", "Categories: Articles recreated from memory · muse-webcrawl") — an experiment watermark inside the article chrome that the real page obviously lacks (the same marker appears on this crawler's other recent articles, e.g. Manhattan Project and SARS-CoV-2 below). Content itself is clean.
- **Confidence:** High.

## 138. https://en.wikipedia.org/wiki/Manhattan_Project — web/en.wikipedia.org/wiki/Manhattan_Project/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Every load-bearing fact correct: US-led with UK and Canada; Groves commanding, Oppenheimer directing Los Alamos; over 100,000 employed across Oak Ridge, Hanford and Los Alamos; Einstein–Szilárd letter (1939) as prompt; uranium gun-type "Little Boy" and plutonium implosion "Fat Man", tested at Trinity on 16 July 1945; August 1945 bombings killing well over 100,000, mostly civilians; postwar handover to the Atomic Energy Commission; Oak Ridge's three enrichment methods (electromagnetic, gaseous-diffusion, thermal) and Hanford plutonium production building on Fermi's Chicago Pile work.
- **Key divergences:** The self-referential "recreated from memory" type/category markers noted at entry 137; content otherwise clean.
- **Confidence:** High.

## 139. https://en.wikipedia.org/wiki/SARS-CoV-2 — web/en.wikipedia.org/wiki/SARS-CoV-2/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded at audit time — a miss, since the real article's CDC electron-microscope render is iconic).
- **Key matches:** Virology precise and correct: positive-sense single-stranded RNA genome of about 30,000 bases; spike (S) binding ACE2; first identified in Wuhan in late 2019 with genome published January 2020; variant-of-concern succession Alpha–Beta–Gamma–Delta–Omicron; enveloped virion with club-shaped spikes; cytoplasmic replication with an error-prone viral polymerase balanced by a proofreading exonuclease unusual among RNA viruses; emergence route stated with appropriate caution ("remains under investigation").
- **Key divergences:** Same on-page recreation markers as entries 137–138; otherwise nothing wrong found.
- **Confidence:** High.

## 140. https://en.wikipedia.org/wiki/Edward_Jenner — web/en.wikipedia.org/wiki/Edward_Jenner/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** All canonical facts correct: dates (17 May 1749 – 26 January 1823), Berkeley, Gloucestershire base; the 1796 inoculation of eight-year-old James Phipps with cowpox material from milkmaid Sarah Nelmes; publication in 1798; vaccination from Latin vacca; variolation's earlier introduction by Lady Mary Wortley Montagu; compulsory vaccination in England from 1853; smallpox eradication in 1980; Royal Society election and cuckoo/hibernation studies; the "father of immunology" title and the "saved more lives than any other human" assessment.
- **Key divergences:** Same on-page "recreated from memory" type/category markers as entries 137–139; content clean.
- **Confidence:** High.

## 141. https://en.wikipedia.org/wiki/Vaccine — web/en.wikipedia.org/wiki/Vaccine/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The lead tracks the real article's definition ("a biological preparation that provides active acquired immunity to a particular infectious disease"), including agent forms and the inclusion of mRNA platforms. Etymology from variolae vaccinae and Jenner's 1796 demonstration correct; type taxonomy (live-attenuated, inactivated, subunit/conjugate, toxoid, viral-vector, mRNA) correct; B/T-cell memory and herd-immunity explanation accurate.
- **Key divergences:** Same recreation markers; compressed.
- **Confidence:** High.

## 142. https://en.wikipedia.org/wiki/Justinian_I — web/en.wikipedia.org/wiki/Justinian_I/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Dates and reign correct (c.482 – 14 November 565; emperor 527–565); renovatio imperii framing; reconquests (North Africa from the Vandals, Italy from the Ostrogoths) under Belisarius; Theodora as co-ruler; Corpus Juris Civilis with its four components (Code, Digest, Institutes, Novels) and Tribonian's role; Nika riots 532 nearly toppling him; Plague of Justinian 541; Hagia Sophia completed 537 after the riots' fires — every checked fact right.
- **Key divergences:** Same recreation markers; compressed.
- **Confidence:** High.

## 143. https://science.nasa.gov/mission/roman-space-telescope — web/science.nasa.gov/mission/roman-space-telescope/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated artist's-concept image embedded (barrel observatory with a single solar wing over a star field), faithful to the real Roman concept art.
- **Key matches:** Mission facts all current and correct: formerly WFIRST; 2.4-metre mirror like Hubble's but a Wide Field Instrument with ~100× Hubble's infrared field of view at the same resolution; Coronagraph Instrument as a direct-imaging technology demonstration; galactic-bulge microlensing survey expected to find thousands of exoplanets completing Kepler's census; named for Nancy Grace Roman, NASA's first chief astronomer, "Mother of Hubble"; managed by Goddard with JPL/STScI/ESA contributions; launch on a Falcon Heavy no later than May 2027 with work toward autumn 2026, to L2 — the genuine current plan.
- **Key divergences:** None found.
- **Confidence:** High.

## 144. https://en.wikipedia.org/wiki/Jonas_Salk — web/en.wikipedia.org/wiki/Jonas_Salk/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Dates (28 October 1914 – 23 June 1995); IPV announced safe and effective 12 April 1955 after the field trial involving ~1.8 million children; University of Pittsburgh with March of Dimes funding; formaldehyde-killed virus; the no-patent stance with the "patenting the sun" comparison correctly paraphrased; Salk Institute founded at La Jolla; late HIV-vaccine work; Sabin's 1961 oral vaccine as complement, with IPV now favoured in polio-free countries — all correct.
- **Key divergences:** Recreation markers (as entries 137–139); compressed.
- **Confidence:** High.

## 145. https://en.wikipedia.org/wiki/Red_Cross — web/en.wikipedia.org/wiki/Red_Cross/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Founding chain exactly right: Henry Dunant's account of Solferino (1859) → ICRC founded Geneva 1863 → first Geneva Convention 1864. Movement structure (ICRC / IFRC / ~190 national societies) correct; emblems including the later red crystal; the seven Fundamental Principles listed correctly (humanity, impartiality, neutrality, independence, voluntary service, unity, universality); ICRC's three Nobel Peace Prizes — all verified.
- **Key divergences:** Recreation markers; compressed overview of the Movement disambiguation topic.
- **Confidence:** High.

## 146. https://en.wikipedia.org/wiki/Neutron — web/en.wikipedia.org/wiki/Neutron/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Chadwick's 1932 discovery correctly situated after Bothe & Becker's 1930 beryllium radiation and Joliot-Curie's experiments, with the 1935 Nobel; free-neutron decay figures precise (mean lifetime about 15 minutes, half-life roughly 10 minutes) and even the "neutron lifetime puzzle" — the genuine measurement-method discrepancy — correctly flagged; roles in fission initiation and neutron scattering, and deep penetration from neutrality, all accurate.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 147. https://en.wikipedia.org/wiki/Pandemic — web/en.wikipedia.org/wiki/Pandemic/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Definition matches the real article's sense; WHO's "characterised as a pandemic" wording for COVID-19 on 11 March 2020 is quoted precisely (the recreation correctly uses WHO's careful verb); historical exemplars (Plague of Justinian, Black Death, 1918 influenza, HIV/AIDS, COVID-19) all standard; epidemic/outbreak/endemic distinctions correct; International Health Regulations name-checked correctly.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 148. https://en.wikipedia.org/wiki/Virus — web/en.wikipedia.org/wiki/Virus/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The lead's first sentence is the real article's verbatim opening ("A virus is a submicroscopic infectious agent that replicates only inside the living cells of an organism"); capsid/envelope/virion framing, "alive" debate, bacteriophages and archaeal viruses, and the antibiotics-don't-work-on-viruses point all match. Tobacco mosaic virus crystallised by Wendell Stanley in 1935 correctly given as the first virus characterised; Baltimore classification correctly described.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 149. https://en.wikipedia.org/wiki/Wuhan — web/en.wikipedia.org/wiki/Wuhan/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Capital of Hubei at the Yangtze–Han confluence; formed in 1927 by merging Wuchang, Hankou and Hanyang; Yellow Crane Tower as symbol; First Yangtze River Bridge dated 1957; "Chicago of China" nickname is a real one; COVID-19 first identified December 2019 with the 76-day lockdown from 23 January 2020 — the duration and date are exactly right; Optics Valley optoelectronics and East Lake geography correct. Population hedged "roughly 11–14 million" brackets the real figures.
- **Key divergences:** Recreation markers; compressed city profile.
- **Confidence:** High.

## 150. https://en.wikipedia.org/wiki/John_Calvin — web/en.wikipedia.org/wiki/John_Calvin/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Dates (10 July 1509 – 27 May 1564); Institutes first edition 1536 expanded to 1559; Geneva leadership from 1541 after the earlier expulsion; "Protestant Rome" label; Servetus execution 1553 presented as the debated stain; Academy of Geneva founded 1559; spread via Knox to Scotland and to France/Netherlands; Weber's Protestant-ethic thesis flagged as still debated — all accurate and fairly framed.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 151. https://en.wikipedia.org/wiki/Nuclear_physics — web/en.wikipedia.org/wiki/Nuclear_physics/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Field definition and lineage correct (radioactivity 1896, Rutherford's nuclear model 1911, proton/neutron identification); shell and liquid-drop models named as the structure frameworks; applications (power, weapons, medicine, astrophysics); nucleosynthesis and quark–gluon plasma in heavy-ion colliders correctly placed; the historical seeding of particle physics by nuclear/cosmic-ray work is a fair summary.
- **Key divergences:** Recreation markers; overview length.
- **Confidence:** High.

## 152. https://en.wikipedia.org/wiki/Martin_Luther — web/en.wikipedia.org/wiki/Martin_Luther/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Dates (10 November 1483 – 18 February 1546); Ninety-five Theses (1517) against indulgences; excommunication and outlawry at the 1521 Diet of Worms; shelter by Frederick the Wise at the Wartburg and the German New Testament translation there; sola fide and sola scriptura correctly glossed; printing's amplification; the late anti-Jewish writings acknowledged as condemned — all accurate.
- **Key divergences:** Recreation markers; compressed. ('Here I stand' is presented in quotes; historians treat the exact words as possibly legendary, a small traditional simplification.)
- **Confidence:** High.

## 153. https://en.wikipedia.org/wiki/Enigma_machine — web/en.wikipedia.org/wiki/Enigma_machine/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — described Enigma photo (three rotors, plugboard, lampboard) matches the machine's real appearance and the article's usual imagery.
- **Key matches:** Scherbius as inventor with the 1918 patent; rotor/plugboard polyalphabetic mechanism described correctly; Polish break led by Marian Rejewski in the 1930s and the 1939 handover to Britain and France; Bletchley Park bombes under Turing; Ultra's war-shortening reputation — all correct.
- **Key divergences:** Compressed; omits the Polish Cipher Bureau's French liaison details etc., no errors found.
- **Confidence:** High.

## 154. https://en.wikipedia.org/wiki/Europa_Clipper — web/en.wikipedia.org/wiki/Europa_Clipper/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (artist's concept with the huge solar arrays described — the spacecraft's defining visual).
- **Key matches:** Current mission facts all right: launched 14 October 2024 on a Falcon Heavy; JPL-managed; Mars and Earth gravity assists en route; Jupiter arrival planned April 2030; dozens of Europa flybys rather than orbit; instrument types correctly listed (ice-penetrating radar, magnetometers, mass spectrometer); enormous solar arrays and radiation shielding; Enceladus parallel drawn correctly.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 155. https://en.wikipedia.org/wiki/Bubonic_plague — web/en.wikipedia.org/wiki/Bubonic_plague/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Yersinia pestis, flea-vector/rodent-reservoir transmission, buboes in groin/armpit/neck, septicaemic and pneumonic progression with person-to-person pneumonic spread; the three pandemics correctly dated at their onsets (541 Justinian, 1346 Black Death, 1855 Third Pandemic); Yersin's 1894 Hong Kong identification; modern reservoirs (Madagascar, Asia, western US) and first-line antibiotics (gentamicin, doxycycline, streptomycin) all right.
- **Key divergences:** Recreation markers; "a few thousand cases a year" is the long-standing WHO-era figure (recent reported years run lower) — acceptable, not a fabrication.
- **Confidence:** High.

## 156. https://en.wikipedia.org/wiki/Niels_Bohr — web/en.wikipedia.org/wiki/Niels_Bohr/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Dates (7 October 1885 – 18 November 1962); Nobel Prize in Physics 1922; Bohr model 1913 with quantised electron levels and photon transitions; Copenhagen institute and interpretation with Heisenberg; Bohr–Einstein debates and complementarity; 1943 flight from occupied Denmark; Manhattan Project work under the alias "Nicholas Baker" — a correctly recalled insider detail; postwar openness campaigning; son Aage's Nobel. All correct.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 157. https://en.wikipedia.org/wiki/Continental_drift — web/en.wikipedia.org/wiki/Continental_drift/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Pangaea fit map described — the article's standard lead visual).
- **Key matches:** Wegener's 1912 proposal and Pangaea; the evidence trio correctly stated (South America–Africa coastline fit, Mesosaurus and Glossopteris fossil matches, matching ranges and glacial deposits); decades of rejection for want of a mechanism; 1960s vindication via seafloor spreading and plate tectonics. The infobox-style header ("Superseded by: Plate tectonics") captures the real article's framing.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 158. https://en.wikipedia.org/wiki/Cubism — web/en.wikipedia.org/wiki/Cubism/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Cubist still life described).
- **Key matches:** Picasso and Braque in Paris from about 1908; multiple-viewpoint geometric fragmentation correctly characterised; Louis Vauxcelles' "cubes" coinage correctly attributed; analytic then synthetic phases with collage/papier collé in the second; Guernica as a later application of the language; "most influential art movement of the 20th century" is the standard assessment the real article echoes.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 159. https://en.wikipedia.org/wiki/Dalai_Lama — web/en.wikipedia.org/wiki/Dalai_Lama/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (14th Dalai Lama in robes, teaching gesture, described).
- **Key matches:** Gelug school; Avalokiteshvara lineage belief; 14th holder Tenzin Gyatso born 6 July 1935 at Taktser, Amdo; recognised as a small child; fled to India in 1959 after the failed uprising; Dharamshala exile residence; Nobel Peace Prize 1989; 2011 devolution of political authority to elected exile leadership — every checked fact correct and current.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 160. https://en.wikipedia.org/wiki/Enceladus — web/en.wikipedia.org/wiki/Enceladus/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (plume image described — matching the article's iconic Cassini plume visual).
- **Key matches:** Sixth-largest moon of Saturn; discovered by William Herschel in 1789; ~500 km diameter; among the most reflective bodies in the Solar System; Cassini's 2005 discovery of south-polar "tiger stripe" plumes; global salt-water subsurface ocean with tidal heating; hydrogen, salts and organics detected in the plume — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 161. https://en.wikipedia.org/wiki/Albert_Sabin — web/en.wikipedia.org/wiki/Albert_Sabin/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Dates (26 August 1906 – 3 March 1993); oral live-attenuated vaccine licensed 1961–62, given on a sugar cube; the Soviet late-1950s mass trials with Mikhail Chumakov correctly recalled as a Cold War collaboration; intestinal immunity blocking transmission as OPV's advantage; vaccine-derived polio risk and the IPV switch in polio-free countries; refusal to patent — all correct.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 162. https://en.wikipedia.org/wiki/Hans_Geiger — web/en.wikipedia.org/wiki/Hans_Geiger/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Dates (30 September 1882 – 24 September 1945, Potsdam); Geiger–Marsden gold-foil experiment of 1909 in Rutherford's Manchester lab revealing the nucleus; Geiger–Nuttall law; 1928 Geiger–Müller tube with Walther Müller; chairs at Kiel, Tübingen and Berlin — all correct.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 163. https://en.wikipedia.org/wiki/Willard_Libby — web/en.wikipedia.org/wiki/Willard_Libby/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Dates (17 December 1908 – 8 September 1980); radiocarbon dating developed 1949; Nobel Prize in Chemistry 1960; effective range ~50,000 years; wartime gaseous-diffusion work on the Manhattan Project; Chicago counting-lab development with validation on known-age material such as ancient Egyptian wood; later AEC service — all correct.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 164. https://en.wikipedia.org/wiki/Immune_system — web/en.wikipedia.org/wiki/Immune_system/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Architecture correctly laid out: physical barriers, innate defences (phagocytes, inflammation), adaptive immunity in jawed vertebrates (antibody-producing B cells, T cells, memory), vaccination as adaptive training, and the three failure modes (immunodeficiency/AIDS, autoimmunity/type 1 diabetes, allergy). Bone-marrow production and thymic/lymphoid maturation correct.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 165. https://en.wikipedia.org/wiki/Protestant_Reformation — web/en.wikipedia.org/wiki/Protestant_Reformation/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The recreation's article is titled "Reformation", matching Wikipedia's real canonical title for this URL's redirect target. Conventional 1517 start with Luther's Theses at Wittenberg; reformer roster (Luther, Calvin, Zwingli, Henrician/Elizabethan settlements); sola fide and scripture's supremacy against papal primacy; Counter-Reformation via Trent; religious wars closing with Westphalia 1648 — all accurate.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 166. https://en.wikipedia.org/wiki/Carbon — web/en.wikipedia.org/wiki/Carbon/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Symbol C, atomic number 6, tetravalent nonmetal; allotrope family (diamond, graphite, graphene, fullerenes, nanotubes); fourth most abundant element in the universe by mass; ~18.5% of the human body; carbon-12 as the atomic-mass standard, carbon-13 stable, carbon-14 radiometric; name from Latin carbo — every fact correct.
- **Key divergences:** Recreation markers; compressed element profile (no full infobox data).
- **Confidence:** High.

## 167. https://en.wikipedia.org/wiki/Entropy — web/en.wikipedia.org/wiki/Entropy/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (disorder-spreading diagram described — the standard explanatory visual).
- **Key matches:** Clausius introducing entropy in 1865 with the second law (isolated-system entropy never decreases); Boltzmann's statistical reading with S = k log W (correctly noted as his tombstone formula); symbol S and unit J/K correct; the information-theory sense (Shannon uncertainty) included, as the real article does.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 168. https://github.com/ — web/github.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Octocat/globe hero art described; GitHub's real hero is likewise stylised product art).
- **Key matches:** Homepage headline "Build and ship software on a single, collaborative platform" and the sub-line about the world's most widely adopted AI-powered developer platform are GitHub's current real hero copy. Nav (Platform, Solutions, Resources, Open Source, Enterprise, Pricing, "Search or jump to…", Sign in/Sign up) matches. Product blurbs accurate: Copilot as AI pair programmer with agents, Actions CI/CD with a large prebuilt-action marketplace, Advanced Security (code scanning, secret scanning, dependency review), Pages hosting from a repo. Footer column structure (Platform/Features/Support/Company) and the enterprise customer roll (Stripe, Shopify, NASA…) are in GitHub's real idiom. Notably, the footer carries the correct year — © 2026.
- **Key divergences:** "100M+ developers" is the 2023 milestone figure (GitHub passed 150M users in late 2024), so the social-proof number lags even though phrased as a floor. Codespaces is missing from the feature tour.
- **Confidence:** High.

## 169. https://www.nvidia.com/ — web/www.nvidia.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (six section images described, all with the right subjects: GB200 rack, RTX card, data centre, humanoid robot, DRIVE visual, Omniverse digital twin).
- **Key matches:** Brand and product story current and correct: GTC billed as "THE CONFERENCE FOR THE ERA OF AI" (real GTC branding); Blackwell platform leading, with the GB200 rack-scale system as its emblem; GeForce RTX 50 Series; Isaac robotics and Jetson at the edge; NVIDIA DRIVE automotive; Clara and BioNeMo in healthcare/sciences; Omniverse digital twins; CUDA as the developer platform. Top nav (Products, Solutions, Industries, For You, Shop, Drivers, Support) matches nvidia.com's real structure. Footer © 2026 — again the current year.
- **Key divergences:** Summary-tile level rather than the real product-page depth; nothing wrong found.
- **Confidence:** High.

## 170. https://www.tesla.com/ — web/www.tesla.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (six hero/product photographs described with plausible subjects).
- **Key matches:** Lineup order and presentation match tesla.com's real full-bleed product stack (Model Y leading with Order Now / Demo Drive, then 3, S, X, Cybertruck, then energy: Powerwall, Megapack, solar). Facts largely right: Model Y as America's best-selling EV; Model 3 "up to 363 mi range (EPA est.)" matches the Long Range figure; Cybertruck's 11,000 lb towing; Model X seating to seven; "Full Self-Driving (Supervised)" with its supervised-use wording in Tesla's own careful formulation.
- **Key divergences:** Two prices are the pre-June-2025 ones: Model S "From $72,990" and Model X "From $79,990" — Tesla raised both by $5,000 in June 2025 (to $74,990 / $84,990). The Model Y ($44,990) and Model 3 ($38,990) prices match their 2025 list prices.
- **Confidence:** High.

## 171. https://www.mozilla.org/ — web/www.mozilla.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Firefox logo described accurately — orange fox encircling a blue-purple globe).
- **Key matches:** Headline "Internet for people, not profit" is Mozilla's real homepage slogan. The Manifesto quote is genuine Principle 1 ("The internet is a global public resource that must remain open and accessible"). Product family correct: Firefox (tracker blocking by default, all platforms), Mozilla VPN (the up-to-five-devices claim is right), Thunderbird, Firefox Monitor breach alerts, Common Voice. Nav (Firefox, Products, Who We Are, Innovation, Download Firefox) and the California not-for-profit Foundation fact match the real site. © 2026 footer — current year.
- **Key divergences:** Product-tile summary depth; nothing wrong found.
- **Confidence:** High.

## 172. https://www.walmart.com/ — web/www.walmart.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (eight product images described with plausible subjects/prices).
- **Key matches:** Title/slogan assembly real ("Walmart | Save Money. Live Better."); header anatomy matches walmart.com — "Pickup or delivery?" location slot, "Search everything at Walmart online and in store" search placeholder, Reorder / My Items, "Hello, Sign In / Account", cart total; Departments/Services hamburger row and category tiles (Deals, Grocery & Essentials, Fall Shop, Electronics, Home) in house style; Rollback/Clearance badging and strike-through pricing grammar correct; Walmart+ benefits accurately listed (free shipping, free delivery from store, Paramount+ included, fuel discounts, 30-day trial). © 2026 footer correct.
- **Key divergences:** All products/prices invented (openly, with the page confessing "invented product offers"); pickup location defaults to a made-up "Seattle 98101".
- **Confidence:** High.

## 173. https://www.ebay.com/ — web/www.ebay.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (eight listing photos described, subjects matching their listings).
- **Key matches:** Title is eBay's verbatim one: "Electronics, Cars, Fashion, Collectibles & More | eBay". Top utility bar exactly right (Hi! Sign in or register · Daily Deals · Brand Outlet · Gift Cards · Help & Contact · Sell · Watchlist · My eBay), "Shop by category", the "Search for anything" placeholder with Advanced link, and the category strip (Motors, Fashion, Collectibles & Art, Sports, Electronics, Home & Garden, Deals, Sell). Listing grammar flawless: prices with Free shipping, "or Best Offer", watcher counts, "12 bids · Time left: 2d 4h left" auction format, Buy It Now, and the Authenticity Guarantee applied to the right categories (graded cards, designer bags, trainers). Footer "Copyright © 1995-2026 eBay Inc." with the correct year.
- **Key divergences:** The individual listings are invented exemplars (labelled as a styled promotion) — unavoidable for a live marketplace, and grammatically perfect.
- **Confidence:** High.

## 174. https://science.nasa.gov/mission/voyager — web/science.nasa.gov/mission/voyager/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Voyager image embedded (dish + long magnetometer boom), true to the spacecraft's real configuration.
- **Key matches:** The header correctly records the easily-flipped fact: launches in 1977 were Voyager 2 first, then Voyager 1. Grand Tour summary correct (V2 the only spacecraft to visit Uranus 1986 and Neptune 1989); interstellar crossings dated 2012 (V1) and 2018 (V2); Golden Record aboard each; RTG power decline; and the current-events detail of engineers reprogramming Voyager 1 through its 2023–24 data fault — a real, recent episode correctly recalled.
- **Key divergences:** None found.
- **Confidence:** High.

## 175. https://science.nasa.gov/mission/juno — web/science.nasa.gov/mission/juno/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Juno image embedded (three vast solar wings over Jupiter), matching the probe's distinctive real silhouette.
- **Key matches:** Launch 5 August 2011, Jupiter arrival 4 July 2016; solar power via three large arrays (unusual for an outer-planet probe, correctly highlighted); naming rationale (goddess who saw through clouds); findings accurate — polar cyclones, auroras, the dilute/"fuzzy" core, deep zonal winds, microwave water probing; original 2018 end plan with repeated extensions and the Ganymede/Europa/Io flyby tour — all correct.
- **Key divergences:** None found.
- **Confidence:** High.

## 176. https://science.nasa.gov/mission/dragonfly — web/science.nasa.gov/mission/dragonfly/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated artist's-concept image embedded (rotorcraft over orange-hazed Titan dunes), matching NASA's real Dragonfly concept art.
- **Key matches:** New Frontiers rotorcraft lander for Titan, built by Johns Hopkins APL; nuclear-powered, car-sized, flying between dozens of sites; Selk impact crater correctly named as the target where melt water may have mixed with organics; dense-atmosphere/low-gravity flight rationale; schedule stated with appropriate vagueness (launch late 2020s — current plan July 2028 — arrival mid-2030s).
- **Key divergences:** None found.
- **Confidence:** High.

## 177. https://science.nasa.gov/mission/mars-2020-perseverance — web/science.nasa.gov/mission/mars-2020-perseverance/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Perseverance-on-Jezero image embedded with arm and sample tubes, consistent with the rover's real appearance.
- **Key matches:** Launch 30 July 2020 and landing 18 February 2021 in Jezero Crater; Curiosity-derived, nuclear-powered design; ancient lake/delta astrobiology rationale; sample caching as the first stage of a sample-return effort "whose architecture and schedule have been under revision" — an accurate statement of the programme's actual post-2024 status; Ingenuity's arc exactly right (planned five flights, flew dozens, ended in 2024 after rotor damage).
- **Key divergences:** None found.
- **Confidence:** High.

## 178. https://store.steampowered.com/ — web/store.steampowered.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (capsule/key art described for each invented title).
- **Key matches:** Storefront chrome exact: STEAM wordmark row with STORE · COMMUNITY · ABOUT · SUPPORT, Install Steam button, login/language; secondary nav (Your Store, New & Noteworthy, Categories, Points Shop, News, Labs) matches the real store's. Listing grammar is perfect Steam: capsule art, genre tags (RPG · Open World · Space), green discount badge with strike-through pricing ("-40% $59.99 $35.99"), "Featured and recommended" rail. Footer legal set (Privacy Policy · Legal · Steam Subscriber Agreement · Refunds) and © 2026 Valve Corporation correct. Platform description (Valve's store, tens of thousands of games, Steam Deck) accurate.
- **Key divergences:** Every game is invented — candidly labelled as such on the page; unavoidable for a live catalogue, and the style transfer is exact.
- **Confidence:** High.

## 179. https://www.adobe.com/ — web/www.adobe.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Photoshop editing visual described).
- **Key matches:** Title "Adobe: Creative, marketing and document management solutions" is Adobe's real one. Mega-nav pillars (Creativity & Design, PDF & E-signatures, Marketing & Commerce, Learn & Support) match adobe.com. Product tiles use the real two-letter glyph conventions (Ps, Ai, Pr, Lr) with accurate one-line descriptions; Firefly framed exactly as Adobe frames it (generative AI "designed to be safe for commercial use"); Acrobat as "the format Adobe invented"; Experience Manager and the 20+ app full suite both correct. Copyright © 2026 Adobe.
- **Key divergences:** Tile-level summary; nothing wrong found.
- **Confidence:** High.

## 180. https://www.samsung.com/ — web/www.samsung.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (six product visuals described with the right subjects).
- **Key matches:** US-store nav (Mobile, TV & Audio, Appliances, Computing, Displays, Galaxy AI, Support) matches samsung.com's structure; "Galaxy AI is here" is Samsung's actual current hero framing, with the named features (live translation, smarter photos) from its real campaign vocabulary; product facts right — Galaxy Z Fold as tablet-canvas, Neo QLED 8K with Quantum Mini LEDs and AI upscaling, Bespoke custom-panel appliances, Galaxy Buds "tuned by AKG", Odyssey curved gaming monitors, trade-in credit programme. Footer in Samsung's real form: © 1995-2026 SAMSUNG.
- **Key divergences:** Hero copy self-described as "in Samsung's style" rather than a specific campaign; tile-level depth only.
- **Confidence:** High.

## 181. https://www.oracle.com/ — web/www.oracle.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (data-centre hall visual described).
- **Key matches:** Title "Oracle | Cloud Applications and Cloud Platform" is real; nav (Products, Industries, Resources, Customers, Partners, Contact Sales) matches. Product claims accurate, including Autonomous Database's actual marketing triad "self-driving, self-securing and self-repairing"; OCI pitched at AI training; Fusion Cloud Applications across ERP/HCM/SCM; NetSuite as the mid-size suite; Java stewardship; Oracle Health explicitly traced to the Cerner acquisition — all correct. © 2026 footer.
- **Key divergences:** Summary depth; nothing wrong found.
- **Confidence:** High.

## 182. https://docs.google.com/ — web/docs.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (template thumbnails described in text).
- **Key matches:** The Docs home screen is faithfully structured: "Start a new document" band with Blank document plus the real starter templates (Resume, Letter, Project proposal, Brochure, Meeting notes all genuine Google Docs templates), then the Recent documents table (Name / Owner / Last opened) with Drive-style ownership labels ("me", shared owners).
- **Key divergences:** The recent-documents contents are invented private files with the sharers openly flagged "(invented)" — the sanctioned private-view pattern; the real screen's template-gallery expansion and sorting controls are absent.
- **Confidence:** High.

## 183. https://www.harvard.edu/ — web/www.harvard.edu/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (four campus images described with the right subjects: Harvard Yard, lecture hall, lab, Widener steps).
- **Key matches:** Veritas motto; founded 1636 and "the oldest institution of higher education in the United States" (Harvard's own standard claim); twelve degree-granting schools; the largest academic library system in the world; Massachusetts Hall, Cambridge, MA 02138 address; nav pillars (Schools, Research, Admissions, Campus, News) in the real site's idiom.
- **Key divergences:** Feature stories are self-described representatives rather than harvard.edu's actual current stories; nothing factually wrong.
- **Confidence:** High.

## 184. https://www.mit.edu/ — web/www.mit.edu/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (Great Dome/Killian Court, lab robot arm, workshop, Kendall startup — all correct subjects).
- **Key matches:** 77 Massachusetts Avenue, Cambridge, MA 02139 address correct; Kendall Square's "most innovative square mile on the planet" epithet correctly attached; OpenCourseWare and MITx correctly positioned; top nav (Education, Research, Innovation, Admissions + Aid, Campus Life, News, About MIT) matches mit.edu's.
- **Key divergences:** The hero line "Better futures, built here" is presented as the homepage headline; mit.edu's front door is a rotating featured story without that fixed slogan — the line reads as a plausible invention in MIT News' style (the page hedges that story details are representative). The Alumni nav entry is absent.
- **Confidence:** Medium-high.

## 185. https://www.stanford.edu/ — web/www.stanford.edu/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (Palm Drive/Main Quad/Memorial Church/Hoover Tower, lab, the Oval, OR — the right Stanford visual set).
- **Key matches:** Facts correct: Doerr School of Sustainability as the sustainability flagship; full demonstrated financial need met for admitted students; Stanford Health Care alongside the School of Medicine; 450 Jane Stanford Way, Stanford, CA 94305 address; nav (Academics, Research, Health Care, Campus Life, Admission, About) matches stanford.edu's real top bar.
- **Key divergences:** The headline "A purposeful university" is not a Stanford slogan I can verify — Stanford's motto is "Die Luft der Freiheit weht" and its current branding runs "Stanford for a changing planet"; the hero line appears to be an in-style invention (again hedged as representative stories).
- **Confidence:** Medium-high.

## 186. https://www.target.com/ — web/www.target.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (eight product photos described).
- **Key matches:** Title format "Target : Expect More. Pay Less." and the real search prompt "What can we help you find?"; "Pickup" store slot and Categories/Deals/New & featured nav in Target's idiom; Target Circle correctly described (free, automatic deals, member prices, birthday reward) and same-day delivery; © 2026 Target Brands, Inc. legal line in the right form.
- **Key divergences:** All products/prices invented seasonal offers (labelled as such); store defaults to a made-up "Seattle Central".
- **Confidence:** High.

## 187. https://gen.lib.rus.ec/ (Library Genesis) — web/gen.lib.rus.ec/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none; the real LibGen front page is famously a bare search form, like this).
- **Key matches:** The search interface is reproduced in unusual detail and it is right: field list (Title, Author(s), Series, Publisher, Year, ISBN, Language, MD5, Tags, Extension) are LibGen's actual search fields; "Search mode: Match similar words / Exact phrase / Use mask (%)", results-per-page 25/50/100, View Simple/Detailed, and object categories (Books, Articles, Fiction, Comics, Magazines, Standards) are the real form's real options; topics browse (Physics, Mathematics, Computers & IT, Medicine…) matches LibGen's topic tree; Sci-Hub correctly named as the sister project for articles.
- **Key divergences:** The "Latest additions" row is a hall of fame (Sapiens, Thinking Fast and Slow, Dune, The Hobbit…) rather than the real, random recent uploads, and its edition years are invented specifics.
- **Confidence:** High.

## 188. https://en.wikipedia.org/wiki/Alps — web/en.wikipedia.org/wiki/Alps/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** ~1,200 km (750 mi) extent; the eight Alpine countries listed exactly as the standard set (France, Switzerland, Italy, Austria, Germany, Slovenia, Liechtenstein, Monaco); Mont Blanc 4,808 m; African–Eurasian plate collision origin; source rivers correctly named with the Danube handled correctly as tributaries; mountaineering golden age including the Matterhorn's 1865 first ascent; Gotthard, Brenner and Mont Blanc tunnels as the emblematic crossings.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 189. https://en.wikipedia.org/wiki/Black_Sea — web/en.wikipedia.org/wiki/Black_Sea/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** All six bordering states correct (Ukraine, Russia, Georgia, Turkey, Bulgaria, Romania); strait chain correct (Bosphorus–Marmara–Dardanelles to the Mediterranean, Kerch to the Sea of Azov); inflowing rivers (Danube, Dnieper, Don); the signature fact — deep water below ~150–200 m anoxic with hydrogen sulfide, the world's largest anoxic basin, preserving ancient shipwrecks — precisely right; Crimean War and post-2022 grain-corridor framing current.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 190. https://en.wikipedia.org/wiki/Yangtze — web/en.wikipedia.org/wiki/Yangtze/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Longest river in Eurasia and third-longest in the world at ~6,300 km (3,900 mi), flagged "(length figure approximate)"; Tibetan Plateau source to the East China Sea near Shanghai; basin draining about a fifth of China's land; course cities (Chongqing, Wuhan, Nanjing, Shanghai); Three Gorges Dam as the world's largest power station by installed capacity; baiji functionally extinct and Chinese paddlefish declared extinct — both statuses correct.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 191. https://en.wikipedia.org/wiki/Influenza — web/en.wikipedia.org/wiki/Influenza/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Types A–D with A/B causing seasonal human epidemics; the four pandemic strains dated and subtyped exactly right (1918 H1N1, 1957 H2N2, 1968 H3N2, 2009 H1N1); drift versus shift explained by behaviour; annual vaccine reformulation via WHO surveillance; the WHO-cited 290,000–650,000 annual respiratory-death estimate reproduced correctly.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 192. https://en.wikipedia.org/wiki/AIDS — web/en.wikipedia.org/wiki/AIDS/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The recreation is titled "HIV/AIDS", the real canonical article title behind the /AIDS URL. Timeline and framing correct: syndrome recognised 1981, virus isolated 1983 (Barré-Sinoussi and Montagnier named), more than 40 million cumulative deaths, mortality peaking in the mid-2000s, ACT UP's effect on drug approval, antiretroviral therapy from 1996 making HIV manageable, PEPFAR / Global Fund / UNAIDS as the coordinating programmes, sub-Saharan Africa's largest burden.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 193. https://en.wikipedia.org/wiki/Epidemiology — web/en.wikipedia.org/wiki/Epidemiology/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Definition tracks the real article's (distribution of health-related states in populations and their determinants, to control health problems); study designs and measures correctly listed (cohort, case-control, cross-sectional, incidence, prevalence, risk ratios, R₀); John Snow's 1854 Broad Street cholera mapping and Framingham as founding stories; CDC Epidemic Intelligence Service "shoe-leather" investigation correctly placed.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 194. https://en.wikipedia.org/wiki/Mosque — web/en.wikipedia.org/wiki/Mosque/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Terminology all correct (masjid "place of prostration", qibla, mihrab, minbar, sahn, adhan, minaret); Prophet's Mosque in Medina (622) as the first mosque; holiness ordering Mecca (Masjid al-Haram), Medina, Al-Aqsa; regional styles accurately sketched (Ottoman centralised domes, Persian iwans, Maghrebi square minarets, Chinese and Sudano-Sahelian forms); aniconic calligraphy/geometry/arabesque decoration.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 195. https://en.wikipedia.org/wiki/Radiation — web/en.wikipedia.org/wiki/Radiation/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Ionising/non-ionising taxonomy right, with ultraviolet correctly flagged as borderline; natural background given as about 2–3 mSv/yr (the world average is ~2.4), sources correctly listed (cosmic, terrestrial, radon, bodily potassium-40); measurement units correctly assigned (activity becquerel, absorbed dose gray, dose equivalent sievert).
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 196. https://www.costco.com/ — web/www.costco.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (eight warehouse product photos described).
- **Key matches:** Header and nav match costco.com (Search Costco, Sign In / Register, Orders & Returns, cart; Shop, Grocery, Deals, Business Delivery, Travel, Membership, Locations). The one price that is a memory test is passed: the Kirkland Signature rotisserie chicken at $4.99, Costco's famously frozen price. Costco Travel, Digital Shop Card offers, Concierge on electronics and the "Price includes shipping" idiom are all genuine house patterns. © 2026 footer.
- **Key divergences:** Other prices are invented typical offers (labelled). Locale slip: "Tyre Centre" with British spelling where the US site runs a "Tire Center".
- **Confidence:** High.

## 197. https://www.bestbuy.com/ — web/www.bestbuy.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (eight product photos described).
- **Key matches:** Title "Best Buy | Official Online Store | Shop Now & Save" is real. Header grammar right (Menu, search, store picker, My Best Buy Account, cart); strikethrough "Save $250"-style deal tiles in Best Buy's format; My Best Buy Plus™ correctly named with its real perks (exclusive prices, free shipping, extended returns); Geek Squad positioned as the 24/7 support brand.
- **Key divergences:** All prices/offers invented (labelled); the store picker defaults to "Aiea Store" (a real Hawaii location, but an odd national default).
- **Confidence:** High.

## 198. https://www.delta.com/ — web/www.delta.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (jet, Delta One suite, app visuals described).
- **Key matches:** Title "Airline Tickets & Airfare Deals | Delta Air Lines" is delta.com's real title. Nav (Book, My Trips, Check In, Flight Status, Travel Info, SkyMiles, Log In / Join SkyMiles) matches; the booking widget reproduces the real form (trip-type and passenger selectors, "Shop with Miles" checkbox, From/To airport fields with codes, Find Flights); "300+ destinations" is Delta's own claim; Main Cabin to Delta One cabin naming and the Fly Delta app's real-time bag tracking are genuine features. © 2026 Delta Air Lines, Inc.
- **Key divergences:** The example itinerary (Seattle–Tokyo Haneda, November dates) is openly invented dressing.
- **Confidence:** High.

## 199. https://www.intel.com/ — web/www.intel.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Core Ultra chip visual described).
- **Key matches:** Product portfolio current and correct: Core Ultra leading the "AI PC" pitch, Xeon 6 for data centres, Arc graphics, Intel Foundry, vPro for enterprise fleets, Gaudi AI accelerators — all real 2024–26 Intel lines in their real positioning. Nav (Products, Solutions, Support, About Intel, region/language, Sign In) matches intel.com.
- **Key divergences:** The page title "Intel | Data Center Solutions, IoT, and PC Innovation" is Intel's older homepage title, not the current shorter branding — a minor staleness, content itself is up to date.
- **Confidence:** High.

## 200. https://www.linuxfoundation.org/ — web/www.linuxfoundation.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Tux-and-project-logos hero visual described).
- **Key matches:** The headline "Decentralized innovation, built with trust" is the Linux Foundation's actual current tagline. Hosted-project claims all correct: the Linux kernel, Kubernetes under the CNCF, PyTorch under the PyTorch Foundation, Node.js under OpenJS; training/certification examples (LFCS, CKA) are real LF credentials; LF Research correctly placed. Copyright © 2026 The Linux Foundation in the site's real form.
- **Key divergences:** Summary-tile depth; nothing wrong found.
- **Confidence:** High.

## 201. https://gen.lib.rus.ec/book/the-hobbit-tolkien — web/gen.lib.rus.ec/book/the-hobbit-tolkien/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — a generated cover embedded: a dragon curled on a gold hoard in storybook style. Evocative, but the real 2012 Houghton Mifflin edition's cover uses Tolkien's own artwork, so the art is a genre match rather than that edition's cover.
- **Key matches:** The LibGen book-page anatomy is right (cover, Title / Author(s) / Publisher / Year / Language / Pages / ISBN / LibGen ID / MD5 / File table, mirrors row, download block). The metadata is startlingly accurate: the 2012 Houghton Mifflin Harcourt edition, 300 pages, and ISBN 9780547928227 — the genuine ISBN of that edition. The description text (1937 children's fantasy, Bilbo, Gandalf, thirteen dwarves, Smaug, the ring in the goblin tunnels) is correct.
- **Key divergences:** The LibGen ID and the 32-hex MD5 are format-correct inventions (inherently unverifiable from memory — no one can expect these to be recalled); file size "4 Mb, epub" is a plausible exemplar.
- **Confidence:** High on the bibliographic facts; the record IDs are necessarily fabricated.

## 202. https://gen.lib.rus.ec/book/thinking-fast-and-slow-kahneman — web/gen.lib.rus.ec/book/thinking-fast-and-slow-kahneman/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — generated cover embedded, and it nails the real first-edition cover concept: two pencils (one long and sharp, one short and stubby) photographed from above on a minimalist white cover.
- **Key matches:** Metadata again impressively right: Farrar, Straus and Giroux, 2011, 1st edition, 512 pages, and ISBN 9780374275631 — the genuine ISBN-13 of the FSG hardcover. The description (System 1/System 2, the Tversky collaboration, biases/heuristics/prospect theory, experiencing vs remembering self) is an accurate summary of the book.
- **Key divergences:** As with entry 201, the LibGen ID and MD5 are format-correct inventions and the file ("8 Mb, pdf") is an exemplar.
- **Confidence:** High on bibliographic facts; IDs necessarily fabricated.

## 203. https://en.wikipedia.org/wiki/Isotope — web/en.wikipedia.org/wiki/Isotope/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Definition exact (same protons, different neutrons/mass numbers); the term's origin correctly told — coined by Margaret Todd and popularised by Frederick Soddy, from Greek "equal place"; carbon-12/13 stable versus carbon-14 radioactive; uranium-238 carefully glossed "stable-ish"; "nearly 300 stable nuclides and thousands of radioactive ones" in the right range; enrichment identified as the key industrial step.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 204. https://en.wikipedia.org/wiki/Particle_physics — web/en.wikipedia.org/wiki/Particle_physics/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Lead tracks the real article ("studies the nature of the particles that constitute matter and radiation"); Standard Model inventory correct (quarks, leptons, photon/gluon/W/Z gauge bosons, Higgs); landmarks correctly dated (electron 1897, top quark 1995, Higgs at the LHC 2012); open problems correctly listed (dark matter/energy, neutrino mass, matter–antimatter asymmetry); flagship labs (CERN, Fermilab, SLAC) right.
- **Key divergences:** Recreation markers; compressed.
- **Confidence:** High.

## 205. https://en.wikipedia.org/wiki/Engine — web/en.wikipedia.org/wiki/Engine/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (four-stroke cutaway described — the standard explanatory image).
- **Key matches:** Lead definition matches the real article's ("a machine designed to convert one or more forms of energy into mechanical energy/work"); historical arc (water/wind/animal power, steam and the Industrial Revolution, internal combustion dominating transport); Carnot limits for heat engines; type spread (Stirling, jet/rocket, hydraulic) correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 206. https://en.wikipedia.org/wiki/Egyptology — web/en.wikipedia.org/wiki/Egyptology/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (tomb-recording scene described).
- **Key matches:** Discipline scope (prehistory to Roman era) and 19th-century emergence after Napoleon's expedition; Rosetta Stone found 1799 enabling Champollion's 1820s decipherment; Tutankhamun's tomb in 1922 among landmark discoveries; modern fieldwork geography (Giza, Saqqara, Luxor, Aswan) correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 207. https://en.wikipedia.org/wiki/TCP/IP — web/en.wikipedia.org/wiki/TCP/IP/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (four-layer diagram described — the article's standard diagram).
- **Key matches:** Cerf and Kahn's foundational 1974 paper; ARPANET adoption on the 1 January 1983 "flag day"; OSI displaced in practice; the four-layer model with correct contents (link: Ethernet/Wi-Fi; internet: IP routing; transport: TCP reliable streams vs UDP datagrams; application: HTTP/DNS/SMTP); IPv4's 32-bit and IPv6's 128-bit addresses; end-to-end design principle correctly summarised.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 208. https://en.wikipedia.org/wiki/Sleep — web/en.wikipedia.org/wiki/Sleep/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated hypnogram embedded, showing the night's descent into deep sleep and rise into REM in the real chart's grammar.
- **Key matches:** Lead tracks the real article's definition (recurring state of altered consciousness, reduced sensory activity, muscle inhibition); ~90-minute NREM/REM cycles; dual regulation by circadian rhythms via the suprachiasmatic nucleus and adenosine homeostatic pressure; 7–9 hours adult guidance; glymphatic clearance including amyloid, memory consolidation with spindles/slow waves — all accurate, current sleep science.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 209. https://en.wikipedia.org/wiki/The_Persistence_of_Memory — web/en.wikipedia.org/wiki/The_Persistence_of_Memory/index.html
- **Verdict: close**
- **Images at audit time: complete** — a regenerated painting embedded ("image regenerated from memory" per its caption): melting pocket watches over a branch and soft creature on a beach with cliffs and calm sea behind — compositionally the Dalí canvas.
- **Key matches:** Infobox facts exact: Dalí, 1931, oil on canvas, 24 cm × 33 cm, MoMA New York, at MoMA since 1934; Cape Creus cliffs as the landscape source; first shown Paris 1931, New York 1932; the paranoiac-critical method; Dalí's own Camembert-melting-in-the-sun origin story for the watches, explicitly set against the popular relativity reading — all correct and well-judged.
- **Key divergences:** The regenerated artwork necessarily approximates Dalí's hand; facts and composition are right.
- **Confidence:** High.

## 210. https://en.wikipedia.org/wiki/Binomial_nomenclature — web/en.wikipedia.org/wiki/Binomial_nomenclature/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Formatting rules exactly right (capitalised genus + lowercase epithet, italicised, authority may follow); Linnaean anchors correct — Species Plantarum 1753 for plants, the 1758 tenth edition of Systema Naturae for animals; governance by the international codes across zoology, botany, bacteria and viruses; the genus-as-kinship-hypothesis framing matches the real article's discussion.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 211. https://en.wikipedia.org/wiki/Dutch_Golden_Age — web/en.wikipedia.org/wiki/Dutch_Golden_Age/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Period given as roughly 1588–1672 within the seventeenth century, a dating historians genuinely use; VOC founded 1602 and "often called the first multinational corporation" (the standard characterisation); Amsterdam's exchange/bank entrepôt role; tulip mania 1636–37 correctly placed within the prosperity; the art market's unprecedented breadth (Rembrandt, Vermeer, Hals and an estimated millions of paintings) in line with scholarly estimates.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 212. https://en.wikipedia.org/wiki/Yellow_River — web/en.wikipedia.org/wiki/Yellow_River/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (loess-badlands river bend described with caption).
- **Key matches:** Second-longest in China, sixth-longest in the world at about 5,464 km; Bayan Har Mountains source in Qinghai; nine provinces to the Bohai Sea; basin ~750,000 km²; loess silt as the name/colour source and historically the highest sediment load of any major river; "China's Sorrow" with the 1887 and 1931 floods among history's deadliest disasters; the "suspended river" levee phenomenon — all correct.
- **Key divergences:** This crawler closes with an on-page recreation note ("Content is paraphrased and may differ from the current live article") rather than the marker-style category tags of entries 137+; content itself clean.
- **Confidence:** High.

## 213. https://en.wikipedia.org/wiki/Tigris — web/en.wikipedia.org/wiki/Tigris/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Eastern of Mesopotamia's two rivers; Taurus Mountains source in eastern Turkey; course cities in the right order (Mosul, Tikrit, Baghdad, Basra) to the Shatt al-Arab and the Persian Gulf; Nineveh and Ashur as ancient capitals it watered; Baghdad founded on its banks in 762 CE; Turkey's Ilısu dam and regional water disputes current and correct; faster/deeper than the Euphrates is the standard comparison.
- **Key divergences:** Length given as "about 1,850 kilometres" where Wikipedia's article says 1,750 km — the larger figure circulates in older reference works, but against the target article it is a ~100 km overstatement.
- **Confidence:** High.

## 214. https://en.wikipedia.org/wiki/Endocrine_system — web/en.wikipedia.org/wiki/Endocrine_system/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Gland roster and control hierarchy correct (hypothalamus directing the pituitary "master gland", thyroid, parathyroids, adrenals, pancreas, gonads); hormone actions correctly assigned (insulin/glucose, thyroxine/metabolic rate, medullary adrenaline, cortisol); negative-feedback framing and neuroendocrinology bridge; the etymology point is exactly right — "hormone" coined in 1905, for secretin, at endocrinology's early-20th-century start.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 215. https://sci-hub.se/ — web/sci-hub.se/index.html
- **Verdict: close**
- **Images at audit time: complete** — the raven logo regenerated (Sci-Hub's real mark is indeed a raven), embedded in the real site's sparse style.
- **Key matches:** Header motto "...to remove all barriers in the way of science" and the title's "knowledge to all" are Sci-Hub's genuine slogans; home/about/stats nav; founder Alexandra Elbakyan (2011); collection "well over 80 million documents" in line with the project's claims; Library Genesis correctly identified as the sister project. Most striking: the five "frequently requested papers" carry their **real DOIs** — Watson & Crick 10.1038/171737a0, Einstein's electrodynamics paper 10.1002/andp.19053221004, Shannon 10.1002/j.1538-7305.1948.tb01338.x, Turing's On Computable Numbers 10.1112/plms/s2-42.1.230, and Nash's "Equilibrium Points in n-Person Games" 10.1073/pnas.36.1.48 — five for five, including the obscure Nash one.
- **Key divergences:** None of substance; the framing copy is a fair summary of the project's stated mission.
- **Confidence:** High.

## 216. https://sci-hub.se/10.1038/171737a0 — web/sci-hub.se/10.1038/171737a0/index.html
- **Verdict: close**
- **Images at audit time: complete** (raven logo via the shared asset path).
- **Key matches:** The bibliographic record is exact: Watson & Crick, "Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid", Nature 171: 737–738, 1953, DOI 10.1038/171737a0. The paper summary is accurate (antiparallel chains, A–T/G–C hydrogen-bonded pairs, the copying-mechanism implication, the Franklin/Wilkins data acknowledgement).
- **Key divergences:** No paper is served — the page openly states the download is a local placeholder and the data "as remembered". Honest, and the metadata being tested is correct.
- **Confidence:** High.

## 217. https://aws.amazon.com/ — web/aws.amazon.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (product icons and data-centre art described).
- **Key matches:** Service blurbs are AWS's own marketing lines, essentially verbatim: EC2 "secure and resizable compute capacity in the cloud", S3 "object storage built to retrieve any amount of data from anywhere", Lambda "run code without provisioning or managing servers… pay only for the compute time you consume", Bedrock as "the easiest way to build and scale generative AI applications with foundation models". Nav (Products, Solutions, Pricing, Documentation, Learn, Partner Network, Marketplace, console sign-in) matches; 200+ services and 2006 launch correct.
- **Key divergences:** Infrastructure counts are a snapshot behind: "105 Availability Zones within 33 geographic Regions" was true around 2023–24; AWS has since grown well past that (more regions and AZs announced through 2025).
- **Confidence:** High.

## 218. https://www.ibm.com/ — web/www.ibm.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (six section visuals described, including the iconic gold quantum-computer chandelier — a real signature IBM photo subject).
- **Key matches:** Strategy framing current and correct: watsonx as the AI/data platform at the centre; IBM Z mainframes for banks/airlines-scale transactions; hybrid cloud via Red Hat OpenShift; Granite as the open enterprise model family; IBM Quantum's cloud-accessible 100+-qubit systems; "Think" as the insights hub. Nav (Products, Solutions, Consulting, Support, Think, Log in) matches ibm.com.
- **Key divergences:** Campaign sections self-described as representative; nothing wrong found.
- **Confidence:** High.

## 219. https://www.tsmc.com/ — web/www.tsmc.com/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated fab image embedded (cleanroom imagery typical of TSMC's site).
- **Key matches:** Positioning exact: "Dedicated IC Foundry", the pure-play model and the never-compete-with-customers pledge in TSMC's own terms. Technology status current and correct: N2 (2nm) entering risk production in 2025 with nanosheet transistors; A16 with backside power following; N3 family in high-volume production for flagship smartphone and AI/HPC silicon; advanced packaging named correctly (CoWoS, InFO, SoIC) with the HBM/chiplet AI context; fab geography right (Taiwan plus Arizona, Kumamoto, and Dresden); the Open Innovation Platform® ecosystem correctly described.
- **Key divergences:** Overview depth; nothing wrong found.
- **Confidence:** High.

## 220. https://www.thewaltdisneycompany.com/ — web/www.thewaltdisneycompany.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — generated castle hub image embedded, the expected corporate visual.
- **Key matches:** The mission statement's opening clause is Disney's verbatim real mission ("to entertain, inform and inspire people around the globe through the power of unparalleled storytelling"). Studio/network roster correct (Walt Disney Studios, Pixar, Marvel, Lucasfilm, 20th Century Studios; ABC, FX, National Geographic); streaming trio Disney+/Hulu/ESPN+; parks/cruise/Adventures by Disney under Experiences; ESPN's flagship direct-to-consumer service correctly dated to a 2025 launch; "world's largest licensor" claim for consumer products.
- **Key divergences:** The business grouping reflects the older segment schema: since Disney's 2023 reorganisation the company reports Entertainment (which includes direct-to-consumer), Sports, and Experiences — the recreation presents Direct-to-Consumer as a standalone business line alongside Entertainment and a separate ESPN & Sports, the pre-2023 arrangement.
- **Confidence:** High.

## 221. https://sci-hub.se/10.1073/pnas.36.1.48 — web/sci-hub.se/10.1073/pnas.36.1.48/index.html
- **Verdict: close**
- **Images at audit time: complete** (shared raven logo).
- **Key matches:** Bibliographic record exact: John F. Nash Jr., "Equilibrium Points in n-Person Games", Proceedings of the National Academy of Sciences 36(1): 48–49, 1950, DOI 10.1073/pnas.36.1.48. The summary is right (one-page note; every finite n-person game has an equilibrium in mixed strategies; fixed-point argument; game-theory cornerstone).
- **Key divergences:** Download again openly a placeholder; the record itself is correct.
- **Confidence:** High.

## 222. https://gen.lib.rus.ec/upload — web/gen.lib.rus.ec/upload/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none; the real flow is a plain form).
- **Key matches:** The upload-form anatomy is plausible and consistent with LibGen's real metadata culture: accepted formats list (pdf, epub, djvu, mobi, chm, txt, rtf, doc), the full bibliographic field set matching the book-page fields audited at entries 201–202 (Title, Author(s), Publisher, Year, Edition, Language, Pages, ISBN, Series), a topic taxonomy mirroring the browse tree, cover-by-URL-or-extract option, and duplicate/mislabel moderation language.
- **Key divergences:** Workflow specifics (a 250 MB cap, single-page web form with moderator check before cataloguing) are reconstructions I cannot confirm against the live upload system, which has historically used separate upload hosts/accounts; the metadata schema itself is solid.
- **Confidence:** Medium.

## 223. https://store.steampowered.com/steamdeck — web/store.steampowered.com/steamdeck/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Deck, controls close-up, docked play, SteamOS UI all described accurately).
- **Key matches:** Model ladder and prices are the real current ones: 256 GB LCD from $399, 512 GB OLED from $549, 1 TB OLED from $649, with the right per-model features (HDR OLED and Wi-Fi 6E on OLED, anti-glare etched glass on the 1 TB). Hardware description correct (dual sticks, two trackpads, gyro, grip buttons, official Docking Station, Deck Verified programme); SteamOS identified as Valve's Arch-based Linux with the Proton compatibility layer — all true; page appropriately hedges that Valve adjusted the range over the Deck's life.
- **Key divergences:** Marketing headline "the most powerful, full-featured gaming PC ever made" tracks Valve's own Deck copy closely enough; nothing material wrong.
- **Confidence:** High.

## 224. https://www.mozilla.org/en-US/firefox/new — web/www.mozilla.org/en-US/firefox/new/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Firefox logo described).
- **Key matches:** Headline copy is Mozilla's real campaign language for this page: "Get the browser that protects what's important — No shady privacy policies or back doors for advertisers. Just a lightning-fast browser that doesn't sell you out." Feature set accurate: Enhanced Tracking Protection blocking trackers and cryptominers by default, add-ons library, cross-device sync via Mozilla account, Picture-in-Picture, 100+ languages, all five platforms; "not-for-profit… fighting for an open internet since 1998" correct.
- **Key divergences:** The "Quantum engine lineage" boast is dated marketing (Mozilla retired the Quantum branding years ago) — a small fossil in otherwise current copy.
- **Confidence:** High.

## 225. https://www.thunderbird.net/ — web/www.thunderbird.net/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (logo described correctly — blue bird wrapped around an envelope — plus interface screenshot description).
- **Key matches:** "Free Your Inbox" is Thunderbird's real current slogan. Institutional facts right: MZLA Technologies as the Mozilla subsidiary behind it, donation-funded, free/open-source. Feature claims accurate: unified multi-account inbox (IMAP/POP), built-in calendar with CalDAV, remote content blocked by default, native OpenPGP, and Thunderbird for Android built on the K-9 Mail codebase — a real and recent (2024) development, correctly recalled. The "Supernova" UI modernisation (density controls, card view, unified toolbar) is genuine release history.
- **Key divergences:** Calling the calendar "the Lightning calendar" uses the legacy add-on name for what is now built-in — a venial archaism, not an error.
- **Confidence:** High.

## 226. https://sci-hub.se/10.1112/plms/s2-42.1.230 — web/sci-hub.se/10.1112/plms/s2-42.1.230/index.html
- **Verdict: close**
- **Images at audit time: complete** (shared raven logo).
- **Key matches:** Bibliographic record exact: Alan M. Turing, "On Computable Numbers, with an Application to the Entscheidungsproblem", Proceedings of the London Mathematical Society s2-42(1): 230–265, DOI 10.1112/plms/s2-42.1.230, with the journal-issue year given as 1937 (the standard citation form for this two-part 1936–37 publication). The summary correctly uses Turing's own "a-machines" terminology and the halting-problem → Entscheidungsproblem argument chain.
- **Key divergences:** Download openly a placeholder, as with the other Sci-Hub records.
- **Confidence:** High.

## 227. https://github.com/enterprise — web/github.com/enterprise/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (enterprise analytics dashboard described).
- **Key matches:** Structure and claims track GitHub's real enterprise pitch: Cloud (hosted, data-residency options, 99.9% uptime SLA — the genuine GH Enterprise SLA figure) versus Server (self-hosted on AWS/Azure/GCP/on-prem); Advanced Security contents (secret scanning, CodeQL code scanning, Dependabot, dependency review); identity/compliance set (SAML and OIDC SSO, SCIM, Enterprise Managed Users, audit-log streaming, SOC/ISO attestations) — all real features with their real names. The customer roll (Adobe, Ford, Mercedes-Benz, Philips, SAP, Société Générale, Spotify, Stripe…) matches companies GitHub publicly showcases.
- **Key divergences:** Marketing-page depth; nothing wrong found.
- **Confidence:** High.

## 228. https://gen.lib.rus.ec/book/leo-tolstoy-what-is-art — web/gen.lib.rus.ec/book/leo-tolstoy-what-is-art?/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — a generated woodcut-style peasant-choir cover embedded; the actual Penguin cover differs, but the art is thematically apt for Tolstoy's argument.
- **Key matches:** Bibliographic metadata again right: Penguin Classics edition of "What Is Art?" in the Pevear & Volokhonsky translation, 1995, 352 pages, ISBN 9780140449573 — the real ISBN of that edition. Description accurate (1898 treatise; art as communication of feeling; Tolstoy condemning most celebrated art including his own novels as counterfeit; Christian brotherhood and sincerity as criteria).
- **Key divergences:** The crawl path itself contains a stray "?" baked into the directory name (`leo-tolstoy-what-is-art?`), a URL-handling artefact of the crawler. LibGen ID/MD5 remain format-correct inventions, as with entries 201–202.
- **Confidence:** High on the bibliographic facts.

## 229. https://en.wikipedia.org/wiki/Thyroid — web/en.wikipedia.org/wiki/Thyroid/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Anatomy and physiology correct: butterfly-shaped gland wrapping the trachea below the larynx; ~20 g weight; T4, T3 and calcitonin (correctly hedged as "modestly" lowering calcium); pituitary TSH negative feedback; iodine deficiency → goitre and the leading preventable cause of intellectual disability, largely solved by iodised salt; Hashimoto's hypothyroidism treated with levothyroxine, Graves' hyperthyroidism — all standard and accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 230. https://en.wikipedia.org/wiki/Primate — web/en.wikipedia.org/wiki/Primate/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated ring-tailed lemur image embedded, matching its caption ("forward-facing eyes and grasping hands"), a representative-primate lead choice like the real article's imagery.
- **Key matches:** "Over 500 species" correct for the order; trait syndrome accurately described (forward-facing binocular eyes, grasping extremities with nails and sensitive pads, large brains, long development, social learning); chimpanzee/bonobo ~98–99% DNA sequence sharing with humans — the standard figure; strepsirrhines correctly given as the lemur/loris branch in the group breakdown.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 231. https://www.disneyplus.com/ — web/www.disneyplus.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (home-screen mock and four key-art tiles described).
- **Key matches:** Brand-tile row exactly right (Disney, Pixar, MARVEL, STAR WARS, NATIONAL GEOGRAPHIC, plus the regional STAR/HULU tile) — including the correct regional nuance for Hulu/ESPN content; plan facts right: ad-supported and ad-free tiers, the US Disney+/Hulu/Max bundle (a real bundle since 2024), up to 4K UHD with Dolby Vision and Atmos, downloads, and up to four simultaneous streams on standard plans; legal line (Subscriber Agreement, Privacy Policy, Your Privacy Choices) in Disney's real form.
- **Key divergences:** Featured titles are openly generic stand-ins ("Star Wars: The Latest Chapter", "Pixar's Summer Release", "Secrets of the Ice") rather than actual current releases — personalised-surface invention, honestly framed.
- **Confidence:** High.

## 232. https://play.google.com/store/apps — web/play.google.com/store/apps/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (app icons are glyph tiles as the page presents them).
- **Key matches:** Storefront chrome matches Google Play: top tabs (Apps, Games, Books, Kids, Offers) — including the newer Offers tab; sub-tabs (For you, Top charts, Categories, Editors' Choice); listing grammar exactly right (app name, category, "4.6 ★ · 50M+ Downloads"); Play Pass, Play Points, Gift cards and Redeem in the footer rail — all real Play features.
- **Key divergences:** Every app is an invented generic ("StreamWave Music", "Budget Buddy", "NoteNest") — labelled as invented on the page; ratings/download counts are plausible exemplars.
- **Confidence:** High.

## 233. https://www.ebay.com/motors — web/www.ebay.com/motors/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (four vehicle photos described).
- **Key matches:** Motors category tree is the real one (Cars & Trucks, Motorcycles, Parts & Accessories, Tires & Wheels, Boats, Powersports, Trailers, Collectible Cars); "Guaranteed Fit" is eBay Motors' genuine parts-fitment feature with the add-your-vehicle mechanic correctly described; eBay Money Back Guarantee framing correct; auction grammar ("42 bids · Time left 2d 4h") consistent with the main site.
- **Key divergences:** Listings invented (labelled), including one realism slip: a 2019 Mustang GT offered with "Free shipping", where real vehicle listings run on pickup/freight terms, not free shipping.
- **Confidence:** High.

## 234. https://www.tesla.com/solarroof — web/www.tesla.com/solarroof/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (five product/installation visuals described with the right subjects).
- **Key matches:** Product claims check out against Tesla's real spec sheet: 25-year tile and power warranty; Class A fire rating (the highest); 110 mph wind rating; tempered-glass tiles "more than three times stronger than standard roofing tiles" — Tesla's own comparison; solar and non-solar tiles blended to read as one slate/glass roof; Powerwall pairing; address-based satellite design and pricing flow; the cross-sell that Tesla's panels are "among the lowest-cost solar in America" is Tesla's actual claim.
- **Key divergences:** No pricing (Tesla quotes Solar Roof only via the design flow, so the omission matches reality); nothing wrong found.
- **Confidence:** High.

## 235. https://aws.amazon.com/ec2 — web/aws.amazon.com/ec2/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (EC2 cube icon art described).
- **Key matches:** Instance-family tour is current-generation accurate (Graviton families M8g/C8g/R8g, X2/U7i high-memory, P6 Blackwell accelerated instances, Trn2, G6, HPC families — hedged "as remembered from recent AWS announcements"); Graviton's "up to 40% better price performance" is AWS's own claim; Nitro System offload description right; purchasing mix (On-Demand, Savings Plans, Reserved, Spot) correct.
- **Key divergences:** The Free Tier snapshot cites the classic "750 hours/month of t2/t3.micro for 12 months" — AWS replaced that structure for new accounts in mid-2025 with a credits-based free account, so this detail is a generation stale.
- **Confidence:** High.

## 236. https://aws.amazon.com/s3 — web/aws.amazon.com/s3/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (S3 bucket icon art described).
- **Key matches:** The "eleven nines" (99.999999999%) durability headline with replication across at least three AZs is AWS's real S3 framing; the storage-class ladder is complete and correct, including the newer rungs (Intelligent-Tiering, Glacier Instant Retrieval, and S3 Express One Zone with single-digit-millisecond latency); "hundreds of trillions of objects" matches AWS's marketed scale (hedged as from memory).
- **Key divergences:** None material found.
- **Confidence:** High.

## 237. https://www.nvidia.com/en-us/data-center — web/www.nvidia.com/en-us/data-center/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated GB200 rack image embedded, plus the page's described Blackwell package, DGX aisle, networking and Grace visuals all on-subject.
- **Key matches:** Platform story current: B200/GB200 with second-generation Transformer Engine and FP4 inference; the roadmap successor correctly named as the Vera Rubin platform; DGX/HGX and SuperPOD; networking stack (InfiniBand, Spectrum-X Ethernet, ConnectX NICs, BlueField DPUs); Grace Arm CPUs paired in GB200; CUDA plus NVIDIA AI Enterprise/NIM microservices. Title matches the real page's ("Data Center GPUs, Systems & Software | NVIDIA").
- **Key divergences:** Summary depth; nothing wrong found.
- **Confidence:** High.

## 238. https://www.samsung.com/us/smartphones — web/www.samsung.com/us/smartphones/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (six product visuals described accurately).
- **Key matches:** Lineup and most prices are the genuine current US list prices: Galaxy S Ultra from $1,299.99 (with the correct 200MP camera, titanium frame and S Pen), Z Flip from $1,099.99, Galaxy A from $199.99, Watch from $299.99, Buds from $179.99; Galaxy AI features named (Circle to Search, Live Translate, generative photo editing) are real.
- **Key divergences:** The Galaxy Z Fold is priced "From $1,799.99" — that was the Fold 5's 2023 price; the Fold 6 listed at $1,899.99 and the current Fold 7 at $1,999.99, so the flagship foldable is two generations stale.
- **Confidence:** High.

## 239. https://www.tesla.com/modely — web/www.tesla.com/modely/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated hero image embedded (plus described cutaway, interior, rear and Supercharger visuals) matching the refreshed car's design.
- **Key matches:** The page covers the refreshed (2025) Model Y with correct specs: 353-mile EPA range (Long Range), 4.6 s 0–60 (LR AWD), 72 cu ft cargo, up to 182 miles added in 15 minutes of Supercharging, 15.4-inch centre display, wrap-around ambient lighting, ventilated seats, 8-inch rear display, full-width rear light bar — all genuine Juniper-refresh details. "From $44,990" and the best-selling-EV billing are right; the 60,000+ Supercharger figure is safely true.
- **Key divergences:** Nothing material found.
- **Confidence:** High.

## 240. https://www.tesla.com/cybertruck — web/www.tesla.com/cybertruck/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — generated hero image embedded, plus described profile/towing/interior/badge visuals in the truck's correct wedge form.
- **Key matches:** Most of the spec sheet is right: 340-mile estimated range for dual-motor AWD, Cyberbeast 0–60 in 2.6 s with 845 hp, 11,000 lb towing, 48V low-voltage architecture, steer-by-wire with rear steering, Ultra-Hard 30X cold-rolled stainless exoskeleton shared with Starship's alloy family, powered tonneau vault, 120V/240V bed outlets and Powershare bidirectional charging, 18.5-inch display, Foundation Series launch history.
- **Key divergences:** One real spec error: "Payload — 6,834 lbs". Cybertruck's payload capacity is 2,500 lb; 6,834 lb is the Cyberbeast's curb weight, mislabelled as payload. A confident, checkable fabrication of the kind the audit exists to catch.
- **Confidence:** High.

## 241. https://www.tesla.com/semi — web/www.tesla.com/semi/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (four visuals described with correct subjects).
- **Key matches:** Headline specs are Tesla's real Semi claims: 500-mile long-range variant, 82,000 lb gross combination weight, 0–60 mph in 20 s at full load, ~70% charge in 30 minutes on a Megacharger, 0.36 drag coefficient, central driving position between two 15-inch displays, tri-motor powertrain derived from Model 3 units, first fleet deliveries from Giga Nevada (PepsiCo-style fleets depicted), volume ramp at the Nevada expansion — all accurate. (The "$200,000 savings" figure echoes Tesla's published estimate, though Tesla frames it over three years rather than a million miles.)
- **Key divergences:** The savings framing above; nothing else material.
- **Confidence:** High.

## 242. https://www.tesla.com/powerwall — web/www.tesla.com/powerwall/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Powerwall image embedded (wall-mounted unit true to the product).
- **Key matches:** Powerwall 3 specs exact: 13.5 kWh capacity, 11.5 kW continuous output, integrated solar inverter; Storm Watch pre-charging ahead of severe weather is a real feature, correctly described; virtual power plant opt-in selling stored energy at peaks is real; Autobidder correctly named as Tesla's energy-trading platform spanning home-to-Megapack scale.
- **Key divergences:** Nothing wrong found.
- **Confidence:** High.

## 243. https://www.nvidia.com/en-us/geforce — web/www.nvidia.com/en-us/geforce/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated RTX card image embedded, with the described DLSS split-screen, ray-tracing, Studio and laptop visuals on-subject.
- **Key matches:** The RTX 50 Series table is spec-perfect at MSRP: RTX 5090 $1,999 / 32 GB GDDR7; 5080 $999 / 16 GB; 5070 Ti $749 / 16 GB; 5070 $549 / 12 GB; 5060 Ti $429 and 5060 $299 — every price and memory configuration correct. DLSS 4 with Multi Frame Generation, fourth-generation RT Cores, Blackwell architecture, AV1 encoding in NVIDIA Broadcast/Studio, Max-Q laptops and GeForce NOW all correctly positioned.
- **Key divergences:** None found beyond the page's own "MSRP, as remembered" hedge — which turns out to be unnecessary.
- **Confidence:** High.

## 244. https://www.ibm.com/quantum — web/www.ibm.com/quantum/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (System Two, Condor package, Heron die, Nighthawk render, Qiskit editor all described with correct subjects).
- **Key matches:** Processor facts are current and exact: Condor at 1,121 qubits; Heron family at 156 qubits with tunable couplers; Nighthawk at 120 qubits aimed at deeper circuits; the public roadmap toward fault-tolerant computing by 2029 (the Starling system) correctly stated; Qiskit as the open-source Python SDK; quantum data centres across New York, Germany and Japan — all real.
- **Key divergences:** None found.
- **Confidence:** High.

## 245. https://github.com/explore — web/github.com/explore/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none; Explore is a text/list surface).
- **Key matches:** The trending exemplars are real flagship repos with credible counts: freeCodeCamp correctly identified as among the most-starred (~400k+), react ~230k with ~47k forks, tensorflow ~190k/~74k forks, linux ~180k stars, vscode in the same band. The page itself flags counts as "as remembered and drift constantly" — and indeed the vscode figure (~165k) is the stalest of the set, but every number sits within the plausible historical range rather than being invented. Topic chips and the collections framing (including the famous awesome/build-your-own-x lists) match the real Explore surface.
- **Key divergences:** Star/fork counts are approximations by nature; none wildly off.
- **Confidence:** High.

## 246. https://www.oracle.com/cloud — web/www.oracle.com/cloud/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (six section visuals described).
- **Key matches:** The headline "Higher performance, stronger security and real cost savings" is OCI's actual marketing line. Claims verify: OCI Superclusters of tens of thousands of NVIDIA GPUs behind leading AI labs; Autonomous Database on Exadata with the self-driving/securing/repairing triad; Arm Ampere shapes with consistent cross-region pricing; Cloud@Customer and dedicated/sovereign regions as differentiators; Oracle Database running inside Azure, Google Cloud and AWS data centres through the multicloud partnerships — a real 2023–25 development, correctly recalled; OKE and the Always Free tier correctly placed.
- **Key divergences:** Summary depth; nothing wrong found.
- **Confidence:** High.

## 247. https://gen.lib.rus.ec/book/capital-and-ideology-piketty — web/gen.lib.rus.ec/book/capital-and-ideology-piketty/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated cover embedded (cream ground, chart/flag grid, bold sans-serif title), a fair approximation of the real Belknap cover design.
- **Key matches:** Bibliographic record exact: Belknap Press (Harvard University Press), 2020, Arthur Goldhammer's English translation, 1,200 pages, ISBN 9780674980822 — the genuine ISBN of that edition. Description correctly summarises the book (inequality regimes across slave/colonial and post-communist societies, shifting party coalitions, closing "participatory socialism" proposals with co-management).
- **Key divergences:** LibGen ID/MD5/file are the usual format-correct inventions.
- **Confidence:** High.

## 248. https://gen.lib.rus.ec/book/philosophical-investigations-wittgenstein — web/gen.lib.rus.ec/book/philosophical-investigations-wittgenstein/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — generated cover embedded: plain black design with white type and the duck-rabbit figure, which genuinely matches the 4th edition's real cover concept.
- **Key matches:** Edition data right: Wiley-Blackwell 2009, 4th edition edited by P. M. S. Hacker and Joachim Schulte, ISBN 9781405159286 — the real ISBN of that edition. Description accurate (posthumous 1953 publication, meaning-as-use in language-games, family resemblance, rule-following, private language argument, numbered remarks).
- **Key divergences:** Pages given as 292; the edition is more commonly listed at ~321 pages, so the count looks short (the discrepancy may reflect text-only pagination). IDs/MD5 invented as usual.
- **Confidence:** High on edition/ISBN; medium on the page-count quibble.

## 249. https://en.wikipedia.org/wiki/Algae — web/en.wikipedia.org/wiki/Algae/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The article correctly frames algae as an informal, polyphyletic grade united by aquatic photosynthesis; the lineage list (green, red, brown algae, diatoms, dinoflagellates, euglenids) and the endosymbiosis explanation are accurate; marine phytoplankton producing "about half" of Earth's oxygen is the standard cited estimate; diatom sediments, coccolithophore chalk, red tides, agar/carrageenan uses all right.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 250. https://en.wikipedia.org/wiki/Digestion — web/en.wikipedia.org/wiki/Digestion/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The human sequence is correctly staged: salivary amylase on starch in the mouth; acid and pepsin starting protein digestion in the stomach; bile and pancreatic enzymes completing breakdown in the small intestine with absorption into blood; large-intestine water absorption and microbiome fermentation; total transit "one to three days" — the standard range; ulcers correctly reassigned mostly to Helicobacter pylori.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 251. https://en.wikipedia.org/wiki/DNA_repair — web/en.wikipedia.org/wiki/DNA_repair/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Damage load ("tens of thousands of lesions per cell per day") matches the canonical estimates; the repair toolkit is correctly assigned (base excision, nucleotide excision for thymine dimers, mismatch repair, homologous recombination vs error-prone NHEJ); the subtle fact that photolyases are absent in placental mammals is right; disease links correct (xeroderma pigmentosum/NER, BRCA1/2 break repair, Lynch syndrome/MMR); the 2015 Chemistry Nobel trio (Lindahl, Modrich, Sancar) correctly attached.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 252. https://en.wikipedia.org/wiki/Survival_of_the_fittest — web/en.wikipedia.org/wiki/Survival_of_the_fittest/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Herbert Spencer's coinage in Principles of Biology (1864) after reading the Origin; Darwin's adoption in later editions of the Origin and in The Descent of Man; fitness correctly defined as reproductive success rather than strength; the tautology objection and its standard resolution; the Social Darwinism appropriation flagged without endorsement — the real article's framing faithfully reproduced.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 253. https://en.wikipedia.org/wiki/Biogeography — web/en.wikipedia.org/wiki/Biogeography/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Founders correctly assigned (Humboldt, Darwin, Wallace with the Wallace Line through Indonesia still separating Asian from Australasian faunas); MacArthur and Wilson's 1967 island-biogeography theory correctly characterised (richness as immigration–extinction balance set by area and isolation) and as a conservation cornerstone; Gondwana relic examples (marsupials, ratites, southern beech) textbook-correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 254. https://en.wikipedia.org/wiki/Ribozyme — web/en.wikipedia.org/wiki/Ribozyme/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Altman and Cech's early-1980s discovery with the shared 1989 Nobel Prize in Chemistry; the two founding cases correctly identified (Cech's Tetrahymena self-splicing intron, Altman's RNase P); the ribosome-as-ribozyme point (RNA peptidyl-transferase centre) and its RNA-world evidentiary role; natural ribozyme examples (hammerhead, hairpin, hepatitis delta virus) all real.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 255. https://en.wikipedia.org/wiki/Super_Bowl — web/en.wikipedia.org/wiki/Super_Bowl/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Lombardi Trophy image embedded (silver football on a kicking tee), matching the trophy's real form.
- **Key matches:** The recent-results table is score-perfect for all five games listed: LV Buccaneers 31–9 Chiefs (7 Feb 2021), LVI Rams 23–20 Bengals (13 Feb 2022), LVII Chiefs 38–35 Eagles (12 Feb 2023), LVIII Chiefs 25–22 OT over the 49ers (11 Feb 2024), LIX Eagles 40–22 Chiefs (9 Feb 2025). Framing facts right: first played 15 January 1967, played on the second Sunday in February, Steelers and Patriots tied on six wins, trophy named for Lombardi.
- **Key divergences:** Coverage stops at LIX (Feb 2025), consistent with the crawl's ~2025 knowledge snapshot — the "current champions" line is one edition behind the calendar by audit time.
- **Confidence:** High.

## 256. https://en.wikipedia.org/wiki/Interstate_Highway_System — web/en.wikipedia.org/wiki/Interstate_Highway_System/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated interchange image embedded (sweeping ramps at dusk), a representative real-style aerial.
- **Key matches:** Length given as about 46,876 miles (75,440 km) — Wikipedia's own figure; Federal-Aid Highway Act of 1956 under Eisenhower; red-white-and-blue shield numbering and controlled-access standards; defence as an official rationale with the urban-destruction critique included.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 257. https://en.wikipedia.org/wiki/Winston_Churchill — web/en.wikipedia.org/wiki/Winston_Churchill/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated V-sign portrait in 1940s photo style embedded, matching the era's iconic imagery.
- **Key matches:** Dates (30 November 1874 Blenheim Palace – 24 January 1965 London); premierships 1940–45 and 1951–55; the 1940 speeches correctly quoted; Gallipoli (1915) as his championed disaster; early warnings about Hitler; 1945 election loss and 1951 return; Nobel Prize in Literature 1953; two party switches across the career — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 258. https://en.wikipedia.org/wiki/Aristotle — web/en.wikipedia.org/wiki/Aristotle/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated marble bust embedded (the standard sculptural representation type).
- **Key matches:** Born 384 BC at Stagira, died 322 BC on Euboea; taught by Plato; founder of the Lyceum and the Peripatetic school; tutor to Alexander the Great; works list correct (Organon, Nicomachean Ethics, Politics, Poetics, Physics, Metaphysics); logic as his formal invention and the two-millennia dominance of his system in Western and Islamic thought — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 259. https://en.wikipedia.org/wiki/Martin_Luther_King_Jr. — web/en.wikipedia.org/wiki/Martin_Luther_King_Jr./index.html
- **Verdict: close**
- **Images at audit time: complete** — generated image embedded of King addressing the crowd at the Lincoln Memorial, the defining photograph-type of the 1963 march.
- **Key matches:** Dates (15 January 1929 Atlanta – 4 April 1968 Memphis, assassinated); movement leadership 1955–1968; the 1963 March on Washington crowd figure (~250,000); Nobel Peace Prize 1964 as, at the time, its youngest laureate; federal-holiday status of his birthday — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 260. https://en.wikipedia.org/wiki/Yosemite — web/en.wikipedia.org/wiki/Yosemite/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — generated Tunnel View image embedded, with the caption correctly identifying El Capitan, Bridalveil Fall and Half Dome — the real view's exact composition.
- **Key matches:** Established 1 October 1890; the 1864 federal grant to California (Galen Clark, Lincoln's signature, later Muir's advocacy); around four million visitors a year; El Capitan as a ~900 m monolith; Yosemite Falls 739 m in three sections (exact); Ahwahneechee habitation and the Mariposa Battalion's 1851 incursion; UNESCO listing — all correct.
- **Key divergences:** Area given as "about 3,080 km²" where the article's figure is ~3,029 km² — a small (~2%) numeric drift, of the order of the Tigris length slip (entry 213).
- **Confidence:** High.

## 261. https://en.wikipedia.org/wiki/Genetic_code — web/en.wikipedia.org/wiki/Genetic_code/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** 64 codons for 20 standard amino acids, redundant but unambiguous, is exactly the code's characterisation. The decipherment history is right: Nirenberg and Matthaei's 1961 poly-U experiment (UUU → phenylalanine), completion by 1966 via Khorana's synthetic RNAs and Nirenberg's binding assays, the 1968 Nobel, and Crick's phage experiments proving the triplet reading frame. Near-universality (with mitochondrial/microbial variants) as common-descent evidence, faithfully framed.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 262. https://en.wikipedia.org/wiki/Atomic_number — web/en.wikipedia.org/wiki/Atomic_number/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Z as proton count defining the element (carbon 6, uranium 92); the tellurium–iodine atomic-weight anomaly correctly used as the motivating puzzle; Moseley's 1913 X-ray law establishing nuclear charge as the table's basis and predicting missing elements; his death at Gallipoli in 1915 aged 27; neutral-atom electron equality and transmutation via nuclear change — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 263. https://en.wikipedia.org/wiki/Corundum — web/en.wikipedia.org/wiki/Corundum/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Aluminium oxide Al₂O₃ defining Mohs hardness 9; gem nomenclature exactly right (red = ruby, all other colours = sapphire); chromophores correctly assigned (chromium for ruby's red and UV fluorescence, iron + titanium for blue sapphire, padparadscha for pink-orange); Mogok "pigeon's blood" as the finest ruby standard; Verneuil-process synthetic corundum from 1902; the first laser (1960) correctly identified as a ruby rod.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 264. https://en.wikipedia.org/wiki/Talc — web/en.wikipedia.org/wiki/Talc/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Mohs 1 reference mineral; hydrated magnesium silicate formed by metamorphism of magnesium-rich rocks; soapstone as its massive form with the right cultural examples (Indus seals, Scandinavian pots, Christ the Redeemer's soapstone mosaic skin); the asbestos-contamination litigation history and Johnson & Johnson's worldwide withdrawal of talc-based baby powder by 2023 toward cornstarch — current and correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 265. https://en.wikipedia.org/wiki/Roman_roads — web/en.wikipedia.org/wiki/Roman_roads/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated basalt-slab road image embedded, true to surviving Roman road photography.
- **Key matches:** Network size at peak ~50,000 miles (80,000 km) of paved road — the standard figure; layered, cambered, drained construction and famous straightness; Via Appia begun 312 BC; distances measured from Rome's Golden Milestone; modern European routes still following Roman lines.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 266. https://en.wikipedia.org/wiki/History_of_the_periodic_table — web/en.wikipedia.org/wiki/History_of_the_periodic_table/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The whole canonical arc is correct: Döbereiner's triads (1820s), the Karlsruhe Congress of 1860 standardising atomic weights, Newlands' mocked 1864 law of octaves, Lothar Meyer's 1864/1870 tables, Mendeleev's 1869 table with successful gallium/scandium/germanium predictions, noble gases adding a column in the 1890s, Moseley's 1913 atomic-number resolution, quantum-mechanical shell explanation of period lengths, and Seaborg's 1944 actinide concept.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 267. https://en.wikipedia.org/wiki/René_Descartes — web/en.wikipedia.org/wiki/René_Descartes/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated portrait "after Frans Hals" embedded, correctly identifying the source of the famous Descartes likeness.
- **Key matches:** Dates (31 March 1596 La Haye en Touraine – 11 February 1650 Stockholm); Jesuit education at La Flèche, law at Poitiers; settlement in the Dutch Republic in 1628; Discourse on the Method (1637) published in French with its optics, meteorology and geometry essays correctly listed; Meditations (1641) and the cogito; Cartesian dualism; the Stockholm ending under Queen Christina with the 5 a.m. lessons and pneumonia — the standard account, presented with a "reputedly" hedge where it shades into legend.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 268. https://en.wikipedia.org/wiki/Immanuel_Kant — web/en.wikipedia.org/wiki/Immanuel_Kant/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated old-age portrait embedded.
- **Key matches:** Königsberg life dates (22 April 1724 – 12 February 1804); the critical bibliography in correct order (Critique of Pure Reason 1781, Groundwork 1785, Critique of Practical Reason 1788, Critique of Judgment 1790); the "Copernican revolution" self-description; both categorical-imperative formulations correctly stated (universal law; humanity as end); the decade of publication silence; the watch-setting walk anecdote hedged as reputation.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 269. https://en.wikipedia.org/wiki/Friedrich_Nietzsche — web/en.wikipedia.org/wiki/Friedrich_Nietzsche/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated portrait photograph (walrus moustache) embedded, matching his well-known likenesses.
- **Key matches:** Dates (15 October 1844 Röcken – 25 August 1900 Weimar); Basel chair at 24; The Birth of Tragedy (1872) with the Apollonian/Dionysian distinction; resignation for ill health in 1879 and the itinerant decade; works and dates correct (Zarathustra 1883–85, Beyond Good and Evil 1886, Genealogy 1887); ideas list accurate (death of God, Übermensch, eternal recurrence, master–slave morality).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 270. https://en.wikipedia.org/wiki/Stoicism — web/en.wikipedia.org/wiki/Stoicism/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Marcus Aurelius bust embedded (the standard sculptural subject for this article).
- **Key matches:** Zeno of Citium founding the school in Athens c.300 BC, named for the Stoa Poikile; the four cardinal virtues as the only good; dichotomy of control; Chrysippus as systematiser; the Roman transmission correctly cast (Seneca, the freed slave Epictetus with Discourses and Enchiridion, Marcus Aurelius' Meditations as private notebooks); logos physics; the through-line to Spinoza, the Enlightenment and cognitive therapy — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 271. https://en.wikipedia.org/wiki/Taoism — web/en.wikipedia.org/wiki/Taoism/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated taijitu (yin-yang with trigrams) embedded, the tradition's canonical symbol correctly rendered in description.
- **Key matches:** Textual tradition correctly anchored (Tao Te Ching/Laozi, Zhuangzi, Daozang); religious Taoism's 2nd-century AD organisation with Zhang Daoling among key figures; the Three Treasures correctly listed (compassion, moderation, humility); wu wei and ziran glossed correctly; one of China's five officially recognised religions; Zhengyi and Quanzhen lineages named — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 272. https://en.wikipedia.org/wiki/Sikhism — web/en.wikipedia.org/wiki/Sikhism/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Golden Temple image embedded (gilded façade reflected in the sarovar at dawn), true to the site's iconic view.
- **Key matches:** Guru Nanak (1469–1539), late-15th-century Punjab origin; Ik Onkar monotheism; ten human Gurus with authority vested in the Guru Granth Sahib by Guru Gobind Singh, who founded the Khalsa in 1699; adherents c.25–30 million; vand chakko and seva correctly named/glossed; the five vices and the langar institution — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 273. https://en.wikipedia.org/wiki/Shinto — web/en.wikipedia.org/wiki/Shinto/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Itsukushima floating torii image embedded, the tradition's most famous view.
- **Key matches:** Kami concept and Amaterasu's imperial-descent role correctly framed; chronicle dates exact (Kojiki 712, Nihon Shoki 720); jinja/torii/shimenawa vocabulary right; Ise Grand Shrine's twenty-year ritual rebuilding; State Shinto bounded 1868–1945; syncretic coexistence with Buddhism — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 274. https://en.wikipedia.org/wiki/International_Court_of_Justice — web/en.wikipedia.org/wiki/International_Court_of_Justice/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Peace Palace image embedded with the caption correctly identifying it as the Court's seat.
- **Key matches:** Principal judicial organ of the UN, established 1945 under the Charter, seated at the Peace Palace in The Hague; 15 judges elected for nine-year terms by the General Assembly and Security Council; states-only contentious jurisdiction resting on consent, with optional-clause declarations by "roughly seventy states" (the right count); binding, unappealable judgments with Security Council enforcement; advisory-opinion examples correctly dated (nuclear weapons 1996, the West Bank barrier 2004, Kosovo 2010, Chagos following) — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 275. https://en.wikipedia.org/wiki/Zoroastrianism — web/en.wikipedia.org/wiki/Zoroastrianism/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated fire-temple image embedded (flame in a silver urn tended by a priest in white), the faith's central devotional image correctly rendered.
- **Key matches:** Zoroaster's era appropriately hedged (possibly c.1200–1000 BC); Ahura Mazda as uncreated creator; asha vs druj framing with the "good thoughts, good words, good deeds" maxim; Gathas as the Avesta's oldest layer; state religion across Achaemenid, Parthian and Sasanian empires; 7th-century Arab conquest and the Parsi migration to Gujarat — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 276. https://en.wikipedia.org/wiki/Greek_mythology — web/en.wikipedia.org/wiki/Greek_mythology/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Olympian feast painting embedded (classical style, appropriate subject).
- **Key matches:** Hesiod's Theogony (c.700 BC) correctly placed as the ordering source from Chaos and Gaia; the twelve-Olympian roster handled with the genuine Dionysus/Hestia ambiguity and Hades placed below; hero cycle (Heracles' labours, Perseus/Medusa, Theseus/Minotaur, Jason, Achilles, Odysseus) and the hubris/Prometheus material all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 277. https://en.wikipedia.org/wiki/Charge_of_the_Light_Brigade — web/en.wikipedia.org/wiki/Charge_of_the_Light_Brigade/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Battle data precise: 25 October 1854, North Valley at Balaclava; the command chain (Raglan, Lucan, Cardigan) against Liprandi; strength ~660–670 behind the traditional "six hundred"; casualties roughly 40% with ~110–120 killed; the blunder's mechanics correctly told (Causeway Heights redoubts invisible from the valley, Nolan carrying the written order); Tennyson's poem published weeks later making it famous.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 278. https://en.wikipedia.org/wiki/Baháʼí_Faith — web/en.wikipedia.org/wiki/Baháʼí_Faith/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Shrine of the Báb image embedded (golden dome, terraced gardens on Mount Carmel), true to the landmark.
- **Key matches:** Baháʼu'lláh (1817–1892); Kitáb-i-Aqdas among the scriptures; World Centre at Haifa; progressive-revelation Manifestations list; the Báb's 1844 herald declaration; Baháʼu'lláh's 1863 Baghdad announcement; Ottoman exile to Acre; the social programme (abolishing wealth extremes, universal education, equality of the sexes) — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 279. https://en.wikipedia.org/wiki/Pizza — web/en.wikipedia.org/wiki/Pizza/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated margherita image embedded (charred crust, tomato, mozzarella, basil), the canonical pizza photograph composition.
- **Key matches:** The lead is the real article's own opening ("a dish of Italian origin consisting of a flat, round base of leavened wheat dough topped with tomatoes, cheese and often other ingredients… baked at a high temperature, traditionally in a wood-fired oven"); first record of the word at Gaeta in 997 AD; Naples working-class origin and the tomato's late-1700s adoption; the 1889 Margherita story; UNESCO's 2017 listing of the Neapolitan pizzaiuolo art — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 280. https://en.wikipedia.org/wiki/Sushi — web/en.wikipedia.org/wiki/Sushi/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated nigiri/maki platter with ginger and wasabi embedded, the standard representation.
- **Key matches:** Definition (vinegared sushi-meshi with neta) right; style taxonomy correct (nigiri, maki, chirashi, Osaka oshizushi); narezushi fermentation origins with the rice once discarded; Hanaya Yohei credited with nigiri in 1820s Edo; post-war global spread and the California roll — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 281. https://en.wikipedia.org/wiki/Michelin_Guide — web/en.wikipedia.org/wiki/Michelin_Guide/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated fine-dining plate image embedded (appropriate generic).
- **Key matches:** Édouard and André Michelin's first guide in 1900 as a motorists' handbook; stars beginning in 1926 with the three-tier system in 1931; the star definitions quoted in Michelin's own terms ("worth a detour", "worth a special journey"); Bib Gourmand and the Green Star (since 2020) correctly placed; Bernard Loiseau's 2003 suicide in the pressure discussion — the standard, if sombre, reference point.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 282. https://en.wikipedia.org/wiki/Julia_Child — web/en.wikipedia.org/wiki/Julia_Child/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated 1960s TV-kitchen image (tall chef, copper pans) embedded, matching her iconic presentation.
- **Key matches:** Dates (15 August 1912 – 13 August 2004, née McWilliams); OSS service in Ceylon and China where she met Paul; Le Cordon Bleu training in Paris; Mastering the Art of French Cooking (1961) with Simone Beck and Louisette Bertholle correctly credited; The French Chef on WGBH (1963–1973); the Smithsonian-preserved Cambridge kitchen; Presidential Medal of Freedom 2003; first woman in the Culinary Institute of America's Hall of Fame — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 283. https://en.wikipedia.org/wiki/Ramen — web/en.wikipedia.org/wiki/Ramen/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated ramen bowl (chashu, egg, nori) embedded, the canonical presentation.
- **Key matches:** Chinese noodle origins via Yokohama's Chinatown in the late 19th/early 20th century; post-1945 reconstruction-era boom; Momofuku Ando's Chicken Ramen (1958) and Cup Noodles (1971); the regional map correctly drawn (Sapporo miso, Kitakata and Tokyo shoyu, Hakata tonkotsu, tsukemen); broth/tare/noodle component vocabulary accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 284. https://en.wikipedia.org/wiki/Croissant — web/en.wikipedia.org/wiki/Croissant/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated croissants image (one cut to show lamination) embedded.
- **Key matches:** Austrian kipferl descent; August Zang's Viennese bakery in Paris (1838–39) as the transmission point, with the laminated form developed in mid-19th-century Paris; the 1683-siege and Marie Antoinette stories correctly labelled legend; production details right (détrempe around beurre de tourage, classically 27 layers, honeycomb interior).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 285. https://en.wikipedia.org/wiki/Ice_cream — web/en.wikipedia.org/wiki/Ice_cream/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated gelateria scoops image embedded.
- **Key matches:** Ancient precedents (Persian faloodeh, snow-chilled syrups) with the Medici story flagged as legend; industrialisation dated correctly — Nancy Johnson's 1843 hand-crank freezer patent and Jacob Fussell's 1850s factory production; the cone popularised at the 1904 St. Louis World's Fair; variety distinctions (gelato's density/warmth, kulfi's unstirred condensed milk, dairy-free sorbet/granita, soft serve's higher extrusion temperature) all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 286. https://en.wikipedia.org/wiki/Kimchi — web/en.wikipedia.org/wiki/Kimchi/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated kimchi-and-banchan image embedded.
- **Key matches:** Composition and seasoning vocabulary exact (napa cabbage/Korean radish, gochugaru, jeotgal, glutinous rice paste); red-chilli standardisation correctly placed after the Americas chillies arrived in the 16th–17th centuries; onggi fermentation vessels; kimjang's UNESCO listing in 2013 — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 287. https://en.wikipedia.org/wiki/Hamburger — web/en.wikipedia.org/wiki/Hamburger/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated cheeseburger-and-fries image embedded.
- **Key matches:** Origin treatment matches the real article's honest contest: Hamburg steak via German immigrants (US menus by the 1870s–80s), frikadelle ancestry, and the standard rival claimants (Charlie Nagreen, Seymour 1885; the Menches brothers 1885; Louis Lassen of Louis' Lunch); White Castle (1921) as the systematiser and McDonald's-led globalisation; regional variants (Japanese teriyaki, Australian beetroot) are the canonical examples.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 288. https://en.wikipedia.org/wiki/Paella — web/en.wikipedia.org/wiki/Paella/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Valencian paella image embedded (saffron rice in the wide pan).
- **Key matches:** Named for the pan; the paella valenciana ingredient canon exactly right (short-grain rice, green beans, garrofó, tomato, chicken, rabbit, sometimes snails, saffron); Albufera lagoon farm-worker origins over orange-wood fires; socarrat as the prized crust; midday communal eating from the pan; the chorizo controversy with Valencian custodians — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 289. https://en.wikipedia.org/wiki/Taco — web/en.wikipedia.org/wiki/Taco/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated tacos al pastor image embedded.
- **Key matches:** Lead tracks the real article ("a small hand-sized corn or wheat tortilla topped with a filling, folded around it and eaten by hand"); pre-Hispanic antecedents and the miners' paper-wrapped gunpowder-charge etymology theory — a genuine theory the article discusses; al pastor correctly traced to Lebanese shawarma technique; canasta, Baja fish, dorados and Texas breakfast tacos as regional forms; UNESCO's recognition of Mexican cuisine invoked correctly.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 290. https://en.wikipedia.org/wiki/Food — web/en.wikipedia.org/wiki/Food/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated world-food spread image embedded.
- **Key matches:** The lead is essentially the real article's current opening ("any substance consumed by an organism for nutritional support and pleasure… of plant, animal, or fungal origin… carbohydrates, fats, proteins, vitamins and minerals… to provide energy, maintain life, and stimulate growth"); Neolithic agriculture ~12,000 years ago with wheat/rice/maize staples; cooking predating farming; a food system feeding "more than eight billion people" — the current population framing.
- **Key divergences:** Compressed hub article; nothing wrong found.
- **Confidence:** High.

## 291. https://en.wikipedia.org/wiki/Indian_cuisine — web/en.wikipedia.org/wiki/Indian_cuisine/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated thali image embedded (curries, dal, rice, breads), the representative presentation.
- **Key matches:** The lead reproduces the real article's opening nearly verbatim ("a variety of regional and traditional cuisines native to the Indian subcontinent… diversity of soil, climate, culture, ethnic groups and occupations… vary substantially… locally available spices, herbs, vegetables and fruits"), including the religious-influence roll (Hindu, Muslim, Jain, Sikh, Christian) and the Mughal-to-British historical layers; garam masala and tadka correctly named as signature blend and technique; Indus Valley cultivation five thousand years ago correctly placed.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 292. https://en.wikipedia.org/wiki/Italian_cuisine — web/en.wikipedia.org/wiki/Italian_cuisine/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated tagliatelle-with-ragù trattoria image embedded.
- **Key matches:** Lead again essentially verbatim from the real article ("a Mediterranean cuisine consisting of the ingredients, recipes and cooking techniques developed across the Italian Peninsula since antiquity, and later spread around the world together with the Italian diaspora"), including the Columbian-exchange ingredient list (potatoes, tomatoes, capsicums, maize) and the north-butter/rice versus south-olive-oil/tomato regional characterisation.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 293. https://en.wikipedia.org/wiki/Dinosaur — web/en.wikipedia.org/wiki/Dinosaur/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — two generated images embedded (mounted T. rex skeleton, matching the museum-mount lead-image tradition, plus a life restoration).
- **Key matches:** First-appearance range "between 243 and 233 million years ago" is the real article's own figure; K–Pg extinction 66 million years ago; more than 1,000 named non-avian genera; more than 11,000 living bird species as cladistic dinosaurs; upright under-body posture as the defining gait; sauropod maxima (>30 m, >50 tonnes) all correct.
- **Key divergences:** One framing slip: dinosaurs are said to have been "the dominant terrestrial vertebrates for over 170 million years, from the beginning of the Jurassic until the end of the Cretaceous" — ~170+ million years is the clade's total span, while Jurassic-to-Cretaceous dominance is ~135 million years; two numbers from the article have been fused.
- **Confidence:** High.

## 294. https://en.wikipedia.org/wiki/Singapore — web/en.wikipedia.org/wiki/Singapore/index.html
- **Verdict: close**
- **Images at audit time: complete** — generated Marina Bay image embedded, the skyline-and-bay composition of the article's usual lead.
- **Key matches:** Population "about 6 million (mid-2020s, including non-residents)" matches current official figures; land area roughly 730 km² with reclamation growth; independence 9 August 1965 by separation from Malaysia; Temasek trading settlement from the 14th century; Raffles' 1819 free port; crown colony rubber/tin prosperity; February 1942 fall and 1942–45 Japanese occupation; four official languages correctly listed; world's busiest transshipment port fairly claimed "by most measures".
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 295. https://en.wikipedia.org/wiki/Dmitri_Mendeleev — web/en.wikipedia.org/wiki/Dmitri_Mendeleev/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — an "[Image placeholder: Dmitri Mendeleev in 1897]" box; the 1897 portrait it names is indeed the article's classic lead photograph, but no generated image had arrived at audit time (in-flight, not an error).
- **Key matches:** Dates and places exact (8 February 1834, Verkhnie Aremzyani near Tobolsk – 2 February 1907, Saint Petersburg, aged 72); the lead closely tracks the real article, including correcting uranium's valence/atomic weight and the three eka- predictions (eka-aluminium, eka-silicon, eka-boron); glass-factory mother and teacher father; Heidelberg period; element 101 Mendelevium named for him — all correct.
- **Key divergences:** None in content; formatting uses markdown-style bold in places, a rendering quirk not a factual one.
- **Confidence:** High.

## 296. https://en.wikipedia.org/wiki/Schrödinger_equation — web/en.wikipedia.org/wiki/Schrödinger_equation/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — an "[Image placeholder: Erwin Schrödinger…]" caption naming the subject; no generated image yet at audit time (in-flight).
- **Key matches:** Lead tracks the real article ("a linear partial differential equation that governs the wave function of a non-relativistic quantum-mechanical system"); 1926 formulation; time-dependent iħ ∂Ψ/∂t = ĤΨ and time-independent Ĥψ = Eψ forms rendered correctly with the Hamiltonian gloss; de Broglie lineage, equivalence with Heisenberg's matrix mechanics, Born's interpretation following — all accurate.
- **Key divergences:** None in content.
- **Confidence:** High.

## 297. https://en.wikipedia.org/wiki/James_Watson — web/en.wikipedia.org/wiki/James_Watson/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — "[Image placeholder: James Watson in 2012]" named but not yet generated at audit time (in-flight).
- **Key matches:** Facts all correct: born 6 April 1928 in Chicago; Quiz Kids radio appearance as a teenager; University of Chicago entry at 15 and Indiana PhD; aged 25 at the 1953 double-helix proposal at the Cavendish; 1962 Nobel shared with Crick and Wilkins; Cold Spring Harbor leadership; first director of the US Human Genome Project at NIH; The Double Helix (1968) and Molecular Biology of the Gene.
- **Key divergences:** The page is written in the present tense with a born-only infobox ("is an American molecular biologist"); James Watson died in November 2025, so against the live article the recreation is a snapshot behind — the same staleness class as the Super Bowl champions line (entry 255), not a fabrication.
- **Confidence:** High.

## 298. https://en.wikipedia.org/wiki/Francis_Crick — web/en.wikipedia.org/wiki/Francis_Crick/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (later-life portrait placeholder; in-flight generation).
- **Key matches:** Dates (8 June 1916, Weston Favell – 28 July 2004, San Diego, aged 88); 1953 double helix with Franklin's and Wilkins' X-ray data properly credited in the lead; 1962 Nobel trio; the central dogma, adaptor hypothesis and wobble hypothesis correctly listed as his later theoretical contributions; Salk Institute consciousness research as the late career — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 299. https://en.wikipedia.org/wiki/Mohs_scale_of_mineral_hardness — web/en.wikipedia.org/wiki/Mohs_scale_of_mineral_hardness/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (reference-minerals lineup placeholder; in-flight).
- **Key matches:** Friedrich Mohs, 1812; qualitative ordinal scratch scale 1–10; the full reference ladder correctly ordered (talc, gypsum, calcite, fluorite, apatite, orthoclase, quartz, topaz, corundum, diamond) with the common-object calibrations right (fingernail ~2.5, copper coin ~3, knife/nail ~5.5, steel file ~6.5); the non-linearity correctly quantified (diamond about four times corundum in absolute hardness, corundum roughly twice topaz).
- **Key divergences:** None found.
- **Confidence:** High.

## 300. https://en.wikipedia.org/wiki/Economy_of_China — web/en.wikipedia.org/wiki/Economy_of_China/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Lujiazui skyline placeholder; in-flight).
- **Key matches:** The lead's structure tracks the real article (socialist market economy with industrial policies and five-year plans); rankings right — second nominally behind the US, largest by PPP since about 2016; roughly 18–19% of the global economy in recent years; population about 1.41 billion; labour force about 740 million; reform and opening up from 1978 under Deng Xiaoping; the 2020s challenge list (property downturn, local-government debt, weak consumption, ageing/shrinking population) is the current consensus framing.
- **Key divergences:** Compressed overview of a huge article; headline GDP totals are given as rankings rather than dollar figures, so nothing numeric to fault.
- **Confidence:** High.

## 301. https://en.wikipedia.org/wiki/Hydroelectricity — web/en.wikipedia.org/wiki/Hydroelectricity/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — Three Gorges Dam placeholder named (its generated file was in flight); the caption's claim (world's largest power station by installed capacity) is correct.
- **Key matches:** Global shares right (roughly 15% of all electricity, more than half of renewable electricity); Three Gorges at 22,500 MW exact, with Baihetan and Itaipu correctly in the leadership set; pumped storage as the great majority of grid-scale storage; history beats correct (1870s first schemes at Cragside and in US industry, Hoover Dam 1936).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 302. https://en.wikipedia.org/wiki/Polaris — web/en.wikipedia.org/wiki/Polaris/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (star-trails placeholder; in-flight).
- **Key matches:** α Ursae Minoris in Ursa Minor, apparent magnitude fluctuating around 1.98; a yellow supergiant with two smaller companions at roughly 450 light-years (estimates vary — a fair hedge given the measurement history); classical Cepheid whose pulsations famously faded in the 1990s and partially recovered; precession sequence right (Thuban around 2700 BC, Vega in roughly 12,000 years).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 303. https://en.wikipedia.org/wiki/Vienna_Convention — web/en.wikipedia.org/wiki/Vienna_Convention/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (Vienna International Centre placeholder; in-flight).
- **Key matches:** Unusually, the recreation correctly recognises that the real Wikipedia "Vienna Convention" is a **disambiguation page** and says so on the page, then lists the principal instruments with correct dates and descriptions: Diplomatic Relations 1961, Consular Relations 1963, Road Traffic 1968, Law of Treaties 1969, Ozone Layer protection 1985. The meta-knowledge (what kind of page the target even is) is right, which most recreations never attempt.
- **Key divergences:** It expands the disambiguation into a short overview rather than a bare link list — a deliberate, disclosed deviation.
- **Confidence:** High.

### Auditor's addendum (live-verification spot checks, 21:41 PDT)
- **Entry 73 (Saturn) refined:** live check of Wikipedia's "Moons of Saturn" confirms the audit's core claim (128 moons announced 11 March 2025 taking the total to 274, versus the recreation's 146) and extends it: further 2026 announcements (March–June 2026) have since raised the live total to **293**. The recreation's staleness is therefore slightly larger than first recorded.
- **Entry 240 (Cybertruck) confirmed:** live spec sources confirm max payload 2,500 lb for AWD/Cyberbeast and Cyberbeast curb weight ≈6,843 lb — the recreation's "Payload — 6,834 lbs" is the curb-weight figure (with a transposed digit) under the wrong label, as recorded.
- **Entries 201–202 (LibGen ISBNs) confirmed live:** bookseller/catalogue records verify *Thinking, Fast and Slow* — Farrar, Straus and Giroux, 2011, first edition, 512 pages, ISBN 9780374275631 — and *The Hobbit* — Houghton Mifflin Harcourt/Mariner, 18 September 2012, 75th-anniversary paperback, ISBN 978-0-547-92822-7, whose cover references Tolkien's original 1937 layout (golden mountains, birds, red sun), as entry 201 described.

## 304. https://en.wikipedia.org/wiki/Scandium — web/en.wikipedia.org/wiki/Scandium/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Sc, atomic number 21, first d-block metal, named for Scandinavia; discovered 1879 by Lars Fredrik Nilson at Uppsala in euxenite and gadolinite; recognised as Mendeleev's predicted eka-boron; by-product extraction and the leading producer countries; aluminium–scandium alloys in aerospace and sporting goods; scandium-iodide stadium/film lighting — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 305. https://en.wikipedia.org/wiki/Calcite — web/en.wikipedia.org/wiki/Calcite/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** CaCO₃, the most stable calcium-carbonate polymorph, principal mineral of limestone and marble; defines Mohs 3; cold dilute HCl effervescence field test; Iceland spar double refraction and the Viking "sunstone" hypothesis (properly hedged with "may have"); predominantly biogenic origin via shells/skeletons of corals, foraminifera and coccoliths — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 306. https://en.wikipedia.org/wiki/Topaz — web/en.wikipedia.org/wiki/Topaz/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Defines Mohs 8; aluminium fluorosilicate; perfect basal cleavage making it brittle despite hardness; imperial topaz from Ouro Preto; commercial blue topaz as irradiated-and-heated colourless material, disclosed as standard treatment; the historical Topazios-island confusion with peridot — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 307. https://en.wikipedia.org/wiki/Road — web/en.wikipedia.org/wiki/Road/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — a "[Image placeholder: A preserved Roman road…]" whose referenced PNG path matches the Roman roads article's generated image (cross-page asset reuse); no image rendered on this page itself at audit time.
- **Key matches:** Lead tracks the real article's definition, including the roads-versus-streets functional distinction (channels between population centres vs serving fronting buildings); network ranking correct (United States largest national road network, then India and China); Roman-road engineering summary consistent with entry 265.
- **Key divergences:** Compressed hub article; nothing wrong found.
- **Confidence:** High.

## 308. https://en.wikipedia.org/wiki/Double_jeopardy — web/en.wikipedia.org/wiki/Double_jeopardy/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Legal content precise: ne bis in idem equivalence; the Fifth Amendment clause quoted verbatim; ICCPR Article 14(7) and EU Charter Article 50 correctly cited; medieval autrefois acquit/convict pleas; jeopardy attachment points (jury sworn / first witness in bench trials); the acquittal bar, mistrial and reversed-conviction rules including the insufficient-evidence exception; the US separate-sovereigns doctrine; and the UK's post-2003 retrial route for serious offences on new and compelling evidence — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 309. https://en.wikipedia.org/wiki/Deterrence_theory — web/en.wikipedia.org/wiki/Deterrence_theory/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Bernard Brodie's 1946 inversion (military establishments exist to avert wars, not win them) correctly stated; Schelling's The Strategy of Conflict (1960) with commitment, brinkmanship and the "threat that leaves something to chance"; the Cold War doctrine sequence (massive retaliation, flexible response, second-strike survivability, MAD) and the ABM Treaty's deterrence-stabilising rationale — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 310. https://en.wikipedia.org/wiki/Suffrage — web/en.wikipedia.org/wiki/Suffrage/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The milestone chain is date-perfect: British Reform Acts 1832/1867/1884; New Zealand's world-first women's suffrage 1893; US Fifteenth (1870, with the Jim Crow nullification and 1965 Voting Rights Act restoration), Nineteenth (1920), Twenty-fourth (1964 poll tax) and Twenty-sixth (1971, age 18) Amendments; South Africa 1994; current-exclusion debates correctly characterised (UK prisoner-voting stand-off under the ECHR, Austria's votes at 16).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 311. https://en.wikipedia.org/wiki/Balance_of_power_(international_relations) — web/en.wikipedia.org/wiki/Balance_of_power_(international_relations)/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Theory statement matches the real article's; historical anchors right (Renaissance Italy, Utrecht 1713 invoking the balance by name, the post-1815 Concert of Europe, Bismarck's alliance web and the pre-1914 rigidity cautionary tale); the theorist sequence correct (Morgenthau, Waltz's balancing prediction in neorealism, Stephen Walt's balance-of-threat refinement); post-Cold War unipolarity debate fairly summarised.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 312. https://en.wikipedia.org/wiki/Jurisprudence — web/en.wikipedia.org/wiki/Jurisprudence/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The schools are cast correctly: natural law (Aquinas, Finnis) with validity tied to moral content; positivism (Bentham, Austin, Hart's rule of recognition, Kelsen, Raz) separating existence from merit; Hart's The Concept of Law (1961) as the modern anchor; Dworkin's interpretivism as the internal liberal challenge; Holmes/Llewellyn realism — all accurate intellectual history.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 313. https://en.wikipedia.org/wiki/Universal_jurisdiction — web/en.wikipedia.org/wiki/Universal_jurisdiction/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Definition exact, with piracy as the classical basis and the modern crime list right (Geneva grave breaches, torture, genocide, war crimes, crimes against humanity); landmark practice correctly dated (Eichmann trial 1961; Pinochet in the Lords 1998–99 on Torture Convention grounds; Belgium/Spain statutes later narrowed; Germany's Koblenz Syrian-torture trials 2021–22 under the Code of Crimes against International Law); ICJ Arrest Warrant judgment (2002) correctly placed in the immunity friction.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 314. https://en.wikipedia.org/wiki/Responsibility_to_protect — web/en.wikipedia.org/wiki/Responsibility_to_protect/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** 2005 World Summit endorsement by all UN member states; the four protected-against crimes listed exactly (genocide, war crimes, ethnic cleansing, crimes against humanity); ICISS (2001, Canadian-convened) origins after Kosovo/Rwanda/Srebrenica with the prevent–react–rebuild continuum; Libya 2011 as the Security Council's R2P-authorised intervention and the BRIC backlash it provoked — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 315. https://en.wikipedia.org/wiki/Statute_of_limitations — web/en.wikipedia.org/wiki/Statute_of_limitations/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Lead tracks the real article's definition (legislatively set maximum time to initiate proceedings; "period of prescription" in civil-law systems); accrual and tolling (minority, concealment, absence) correctly explained; the typical 2–6-year civil ranges; no limitation for murder and — under the 1968 UN Convention and custom — for war crimes and crimes against humanity; child-sexual-abuse revival/lookback windows correctly noted as the recurring political exception.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 316. https://en.wikipedia.org/wiki/Verdict — web/en.wikipedia.org/wiki/Verdict/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Procedural law precise and current: Scots law's third "not proven" verdict (with its abolition in recent Scottish reform legislation correctly noted); England-and-Wales majority verdicts of 10–2 or 11–1; US unanimity including state courts since Ramos v. Louisiana (2020); special vs general verdicts, hung juries, directed verdicts and JNOV all correctly characterised.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 317. https://en.wikipedia.org/wiki/Term_limit — web/en.wikipedia.org/wiki/Term_limit/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Washington's 1797 two-term precedent, its sole breach by FDR (four elections, 1932–44), codification in the Twenty-second Amendment (1951); term-limit evasion as a documented backsliding mechanism (China's 2018 removal of the presidential limit the flagship case); the political-science trade-off (rotation vs power shifting to executives/staff) fairly stated.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 318. https://en.wikipedia.org/wiki/Recall_election — web/en.wikipedia.org/wiki/Recall_election/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Origins right (Los Angeles municipal adoption 1903; Oregon first state 1908; Progressive Era/Swiss roots); 19 US states with recall; the UK's narrow Recall of MPs Act 2015; case file accurate (California 2003 — Davis recalled, Schwarzenegger successor; California 2021 — Newsom retained; Wisconsin 2012; Venezuela 2004 — Chávez retained; Taiwan's recall waves).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 319. https://en.wikipedia.org/wiki/One-party_state — web/en.wikipedia.org/wiki/One-party_state/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** De jure/de facto distinction correctly drawn; the current de jure list is exactly right (China, Cuba, Laos, North Korea, Vietnam); nomenklatura staffing and party–state fusion; China's post-1978 market combination with the authoritarian-resilience/performance-legitimacy literature; dominant-party examples (Japan's LDP, Singapore's PAP) correctly classed as formally competitive.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 320. https://en.wikipedia.org/wiki/Constitutionalism — web/en.wikipedia.org/wiki/Constitutionalism/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The core distinction is right — constitutionalism as enforceable constraint on power, not mere possession of a constitution (the sham/window-dressing constitution caveat); intellectual lineage and wave structure (medieval fundamental law, Locke, American/French revolutions, post-1945 and post-1989 court-centred constitution-making); internal tensions correctly named (counter-majoritarian difficulty, abusive constitutionalism).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 321. https://en.wikipedia.org/wiki/Electoral_fraud — web/en.wikipedia.org/wiki/Electoral_fraud/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Lead matches the real article's definition (illegal interference increasing a favoured candidate's share, depressing rivals', or both); the methods catalogue is comprehensive and accurate, including "administrative resource" misuse and the clean conceptual separation from legal manipulation such as gerrymandering and from non-illegal malpractice.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 322. https://en.wikipedia.org/wiki/Plaintiff — web/en.wikipedia.org/wiki/Plaintiff/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Definition correct with a well-recalled jurisdictional detail — "claimant" in England-and-Wales practice since 1999 (the Civil Procedure Rules rename); burden on the balance of probabilities; US standing triad (injury, causation, redressability); parens patriae government suits; class actions and strategic/test-case litigation via advocacy organisations — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 323. https://en.wikipedia.org/wiki/Alliance — web/en.wikipedia.org/wiki/Alliance/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** NATO Article 5 collective-defence correctly characterised; the theorist's toolkit all present and right (balance-of-threat alignment logic, alliance reliability empirics, the entrapment–abandonment dilemma, burden-sharing as NATO's permanent dispute, institutionalisation distinguishing NATO from looser pacts, 1914 as the cautionary alliance-system case).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 324. https://en.wikipedia.org/wiki/Great_Wall_of_China — web/en.wikipedia.org/wiki/Great_Wall_of_China/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (no images directory yet).
- **Key matches:** Lead near-verbatim to the real article (fortifications of "stone, brick, tamped earth, wood and other materials" along an east-to-west line across China's historical northern borders against steppe incursions); earliest walls 7th century BC; the best-preserved sections Ming (1368–1644); total length of all branches 21,196 km from the 2012 Chinese survey announcement; the not-visible-from-the-Moon myth correctly debunked.
- **Key divergences:** Compressed; the "(year as remembered)" last-edited footer artefact again.
- **Confidence:** High.

## 325. https://en.wikipedia.org/wiki/Apollo_11 — web/en.wikipedia.org/wiki/Apollo_11/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (no images directory yet).
- **Key matches:** Mission facts exact: Eagle landing 20 July 1969 with Armstrong and Aldrin, Collins in Columbia; first step dated 21 July UTC — the recreation handles the UTC nuance correctly; the "one small step" wording debate fairly noted; splashdown 24 July 1969; Kennedy's 1961 end-of-decade goal as the framing achievement.
- **Key divergences:** Compressed; "(year as remembered)" footer artefact.
- **Confidence:** High.

## 326. https://en.wikipedia.org/wiki/International_Space_Station — web/en.wikipedia.org/wiki/International_Space_Station/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (no images directory yet).
- **Key matches:** Lead matches the real article's: the five partner agencies listed exactly (NASA, Roscosmos, ESA, JAXA, CSA); first component launched 1998; continuously occupied since November 2000; ~400 km average altitude and ~93-minute orbital period as usually given; largest human-made structure in space, naked-eye visible — all correct.
- **Key divergences:** Compressed; "(year as remembered)" footer artefact.
- **Confidence:** High.

## 327. https://ekantipur.com/ — web/ekantipur.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Identity and group structure right — the online portal of Kantipur Publications, publisher of Kantipur and The Kathmandu Post; Kantipur daily founded 1993 and Nepal's largest-circulation Nepali paper; Kantipur Television and Radio Kantipur in the same group; bilingual Nepali/English offering; section taxonomy (National, Provinces, Business, World, Sports with cricket prominent, Entertainment, Opinion) matches the real portal's organisation.
- **Key divergences:** The standard news-homepage failure — zero specific headlines, stories described by genre; section labels self-flagged "as recalled from the Nepali edition".
- **Confidence:** High on structure, medium on section labels.

## 328. https://www.microsoft.com/ — web/www.microsoft.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — the generated hero shows a Surface-style 2-in-1 (kickstand visible) displaying the Windows 11 "Bloom" wallpaper in its correct blue-green folded form: subject and photographic style match Microsoft's real hero imagery closely.
- **Key matches:** Title ("Microsoft — Cloud, Computers, Apps & Gaming") matches the real page title; the home/business split and product grids (Microsoft 365 with Copilot fronting, Windows 11/Copilot+ PCs, Surface Pro/Laptop, Xbox/Game Pass, Azure, Teams, Dynamics 365) reflect the real homepage's current campaigns; the Copilot-everywhere marketing centre since 2023 is correctly identified.
- **Key divergences:** Top-nav slightly off (Azure is not a consumer top-nav item on the real site; Deals/Small Business are missing); body copy is descriptive summary rather than the real rotating campaign headlines; recreation footer on-page.
- **Confidence:** High.

## 329. https://www.amazon.com/ — web/www.amazon.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — four generated category-card photos (cordless vacuum, wireless headphones, e-reader, board game), generic but appropriate product photography for Amazon's card grid.
- **Key matches:** Homepage chrome faithfully recalled: "Deliver to" location slot, "Hello, sign in / Account & Lists", Returns & Orders, the "All · Today's Deals · Prime Video · Buy Again · Customer Service · Registry · Gift Cards · Sell" strip, and the four footer link columns (Get to Know Us / Make Money with Us / Amazon Payment Products / Let Us Help You) with Conditions of Use / Privacy Notice / Interest-Based Ads and the © 1996-2025 format — all match the real page.
- **Key divergences:** The card content and seasonal promotion are invented (though honestly labelled on-page as "invented seasonal promotion in Amazon's style"); the "Deliver to Seattle 98101" default is an invented localisation.
- **Confidence:** High.

## 330. https://www.tiktok.com/ — web/www.tiktok.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — two generated video stills (kitchen flatbread hack; street dancer at golden hour), plausible TikTok content frames.
- **Key matches:** Title/slogan "TikTok - Make Your Day" exact; logged-out web chrome matches the real experience (For You / Explore / Upload / LIVE / Profile rail, Log in button, Discover/Following split); post furniture right (handle, like/comment/share counts, caption hashtags, "original sound" attribution).
- **Key divergences:** Both posts are invented creators with invented engagement counts (the real logged-out feed shows real trending videos); the format necessarily freezes a video product into stills.
- **Confidence:** High.

## 331. https://home.cern/ — web/home.cern/index.html
- **Verdict: close**
- **Images at audit time: complete** — the generated LHC tunnel photograph is one of the best images of the run: blue-and-silver dipole cryostats curving away down the tunnel, grated walkway, hi-vis technician for scale, cryogenic signage — compositionally and technically true to CERN's real tunnel photography.
- **Key matches:** Strapline "Accelerating science" matches CERN's real branding; institutional facts complete and correct (founded 1954, Franco-Swiss border near Geneva, 27 km LHC ring, ATLAS/CMS/ALICE/LHCb, Higgs discovery 2012, Berners-Lee's 1989 invention of the Web at CERN, Science Gateway opened 2023).
- **Key divergences:** Nav is sparse versus the real site and the news rotation is summarised rather than reproduced; recreation footer on-page.
- **Confidence:** High.

## 332. https://www.berkshirehathaway.com/ — web/www.berkshirehathaway.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none — correctly, as the real page has none).
- **Key matches:** One of the most faithful recreations in the crawl: the famously plain text-link homepage is reproduced almost exactly — 3555 Farnam Street, Omaha, NE 68131, "Official Corporate Website", the link list (A Message From Warren E. Buffett; Annual & Interim Reports; SEC Filings; Annual Meeting Information; Berkshire Hathaway Energy; Links to Berkshire Subsidiary Companies; the stock-pledge letters; Corporate Governance; Common Stock Information; even the quirky "Facts Regarding Berkshire's 2021 Investments in Activision Securities" and "Berkshire Hathaway on Wikipedia"), the "due to the limited number of personnel in our corporate office, we are unable to provide a direct response" disclaimer, and the © 1978–2025 line — all match the real page; the "Updated May 3, 2025" dates even align with the 2025 annual meeting.
- **Key divergences:** Only the recreation credit line, which itself notes the real page's plainness.
- **Confidence:** High.

## 333. https://www.harvard.edu/ — web/www.harvard.edu/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — a generated Harvard Yard autumn view (red brick, fallen leaves) plus altar-style card images for learning/research/libraries matching the page's own captions.
- **Key matches:** Veritas motto; founded 1636 and oldest US institution of higher education; twelve degree-granting schools; the largest academic library system claim; Massachusetts Hall, Cambridge, MA 02138 address — all correct.
- **Key divergences:** Feature stories are representative inventions in Harvard's style rather than the day's real features; layout is a summarised evocation of the real media-rich homepage.
- **Confidence:** High.

## 334. https://www.khanacademy.org/ — web/www.khanacademy.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The mission is quoted near-verbatim ("provide a free, world-class education to anyone, anywhere"); course taxonomy by subject and grade right; Khanmigo correctly identified as the recent AI tutor; the official SAT prep built with the College Board; mastery-based practice with instant feedback and teacher dashboards; Sal Khan's mid-2000s remote-tutoring origin story — all accurate.
- **Key divergences:** Rendered as descriptive prose rather than the real homepage's learner/teacher entry-point layout; no specific course catalogue reproduced.
- **Confidence:** High.

## 335. https://www.nature.com/ — web/www.nature.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — a generated false-colour cell-microscopy hero in the journal's typical research-image style.
- **Key matches:** Section architecture matches nature.com (News, Latest Research, Careers, Podcast, Books & Arts, Collections; Sign in / Subscribe / Search); journal anchors right (founded 1869; published the 1953 DNA-structure papers; carried the first exoplanet signatures — the 1995 Mayor & Queloz result).
- **Key divergences:** Lead headlines are invented, though one is honestly self-flagged on-page as "a plausible feature in the journal's current style; specific headlines rotate daily" — the news-rotation limitation again, mitigated by disclosure.
- **Confidence:** High.

## 336. https://www.apache.org/ — web/www.apache.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (a described feather-logo/world-map graphic not yet rendered).
- **Key matches:** Title "Welcome to The Apache Software Foundation!" matches the real homepage; the 300+ projects scale claim current; project blurbs accurate (HTTP Server a leading web server since 1995; Kafka event streaming; Spark unified analytics; Hadoop big-data framework; Tomcat servlet container; Airflow workflow scheduling); "The Apache Way" correctly summarised (meritocracy, "community over code", consensus-based decision-making, volunteer stewardship).
- **Key divergences:** Nav is compressed; nothing factually wrong found.
- **Confidence:** High.

## 337. https://www.ligo.org/ — web/www.ligo.org/index.html
- **Verdict: close**
- **Images at audit time: complete** — the generated aerial shows the observatory's two long arms meeting at a right angle at the corner station, matching LIGO's iconic site geometry.
- **Key matches:** Designed and operated by Caltech and MIT; twin 4-km L-shaped interferometers at Hanford, Washington and Livingston, Louisiana; sub-proton-width arm distortions; GW150914 announced February 2016; the 2017 Nobel to Weiss, Barish and Thorne; observing runs O1–O4 alongside Virgo and KAGRA with open data and alerts; the catalogue's hundreds of mostly black-hole-merger events — all correct.
- **Key divergences:** Homepage compressed into a summary; nothing wrong found.
- **Confidence:** High.

## 338. https://www.mit.edu/ — web/www.mit.edu/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (described Great Dome/Killian Court and lab images not yet rendered).
- **Key matches:** Top-level structure matches mit.edu (Education, Research, Innovation, Admissions + Aid, Campus Life, News, About MIT); Kendall Square's "most innovative square mile on the planet" billing correctly used; OpenCourseWare and MITx correctly placed as the open-education offer; the featured story is honestly self-flagged as representative, not a specific day's headline.
- **Key divergences:** Hero content is a style evocation rather than the real rotating research stories; the "Better futures, built here" line is a plausible campaign-style invention.
- **Confidence:** High.

## 339. https://www.stanford.edu/ — web/www.stanford.edu/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (described Palm Drive/Quad images not yet rendered).
- **Key matches:** Section structure right (Academics, Research, Health Care, Campus Life, Admission, About); the Doerr School of Sustainability correctly featured as the climate/energy school; full-demonstrated-need financial aid correctly stated; 450 Jane Stanford Way, Stanford, CA 94305 address exact; campus landmarks (Palm Drive, Main Quad, Memorial Church, Hoover Tower, the Oval) correctly assembled.
- **Key divergences:** Featured stories are representative inventions (self-flagged); the "A purposeful university" strapline could not be verified as Stanford's current branding.
- **Confidence:** Medium-high.

## 340. https://www.instagram.com/ — web/www.instagram.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — three generated feed photos (ridge sunrise hiker, pasta bowl, aurora cabin) matching their captions as plausible Instagram content.
- **Key matches:** Web-app furniture matches the real logged-in home: the left rail (Home, Search, Explore, Reels, Messages, Notifications, Create, Profile, plus the Threads cross-link), stories row, like/comment/share/save furniture, and the footer link set (About · Help · Press · API · Jobs · Privacy · Terms · Locations · Meta) all correspond to the real product.
- **Key divergences:** All accounts and posts are invented (necessarily, for a private feed) — including a suggested account "alex.morgan.ig" colliding with the real athlete's name, the same invented-name pattern as Facebook's "Alex Morgan"; the © 2025 Meta footer is a year stale.
- **Confidence:** High on chrome, content invented by design.

## 341. https://www.threads.net/ — web/www.threads.net/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (text-first recreation, matching the product's text-first nature).
- **Key matches:** Minimal chrome matches the real logged-out/web Threads (icon rail, For you | Following tabs, "Threads by Instagram · Log in with Instagram" framing); post furniture (relative timestamps, like/reply/repost glyphs and counts) right.
- **Key divergences:** All four posts are invented — though they reuse the same invented persona set (maya.k, jon.trails, north.peak) as the Instagram recreation, giving the two recreations a coherent shared fake social graph.
- **Confidence:** High on chrome, content invented by design.

## 342. https://www.tsmc.com/ — web/www.tsmc.com/index.html
- **Verdict: close**
- **Images at audit time: complete** — the generated fab photograph (cleanroom-scale facility) suits the page; further described technology images are referenced in the layout.
- **Key matches:** "Dedicated IC Foundry" is TSMC's real self-descriptor; technology status current and correct — N2 nanosheet technology in risk production in 2025 with A16 backside-power following, N3 family in high-volume production for flagship smartphone and AI/HPC silicon, and the advanced-packaging trio named exactly (CoWoS, InFO, SoIC) with the AI-accelerator/HBM role right; the pure-play "never competing with our customers" model and Arizona fab expansion correctly presented.
- **Key divergences:** Nav compressed versus the real corporate site; nothing factually wrong found.
- **Confidence:** High.

## 343. https://www.intel.com/ — web/www.intel.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (described Core Ultra chip image not yet rendered).
- **Key matches:** Product architecture current (Core Ultra as the AI-PC line, Xeon 6 for data centre, Arc graphics, Intel Foundry, vPro for enterprise fleets); nav skeleton (Products / Solutions / Support / About Intel, locale selector, Sign In) matches Intel's site conventions.
- **Key divergences:** The page title ("Data Center Solutions, IoT, and PC Innovation") is Intel's vintage late-2010s homepage title rather than the current one; Gaudi is headlined as a going concern although Intel de-emphasised the line after Gaudi 3 (Falcon Shores was cancelled in early 2025) — mild staleness.
- **Confidence:** High.

## 344. https://www.delta.com/ — web/www.delta.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described jet/Delta One/app images not yet rendered).
- **Key matches:** Page title matches Delta's real one; primary nav exact (Book, My Trips, Check In, Flight Status, Travel Info, SkyMiles, Log In / Join SkyMiles); the booking widget reproduces Delta's real pattern including the "Shop with Miles" checkbox; "300+ destinations" network claim correct; Main Cabin-to-Delta One product ladder and real-time bag tracking in the Fly Delta app correctly cited; © 2026 footer current.
- **Key divergences:** The example itinerary (Seattle–Tokyo) is invented — but explicitly flagged on-page as an invented example with "fares shown are illustrative only".
- **Confidence:** High.

## 345. https://www.disneyplus.com/ — web/www.disneyplus.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (described home-screen and key-art images not yet rendered).
- **Key matches:** Title exact; the brand-hub structure matches the real service (Disney, Pixar, Marvel, Star Wars, National Geographic, plus Star/Hulu by region); commercial facts current — ad-supported and ad-free tiers, and the US Disney+/Hulu/Max bundle is real; sign-up framing accurate.
- **Key divergences:** Showcase titles are deliberately vague placeholders ("Star Wars: The Latest Chapter", "Marvel Studios' Newest Film") rather than real current releases — self-flagged as representative, but no actual catalogue content is recalled.
- **Confidence:** High.

## 346. https://www.adobe.com/ — web/www.adobe.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described Photoshop artwork image not yet rendered).
- **Key matches:** Page title matches adobe.com's long-standing real title; product blurbs accurate across the line (Photoshop, Illustrator, Premiere Pro, Lightroom, Express) including the two positioning claims Adobe itself makes — Firefly as generative AI "designed to be safe for commercial use" and Acrobat/PDF as "the format Adobe invented"; nav taxonomy (Creativity & Design, PDF & E-signatures, Marketing & Commerce, Learn & Support) matches the real site's organisation.
- **Key divergences:** Hero copy is summarised rather than the current campaign's; nothing factually wrong found.
- **Confidence:** High.

## 347. https://www.target.com/ — web/www.target.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (described product-card images not yet rendered).
- **Key matches:** Slogan "Expect More. Pay Less." in the title as on the real site; chrome right (Pickup store selector, Categories / Deals / New & featured, Target Circle savings framing, same-day delivery); seasonal assortment (fall/Halloween) matches the real mid-October homepage's themes.
- **Key divergences:** All prices and offers invented (self-flagged as "invented typical offers"); the "Seattle Central" store localisation is invented.
- **Confidence:** High.

## 348. https://www.bestbuy.com/ — web/www.bestbuy.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (described deal-card images not yet rendered).
- **Key matches:** Page title matches the real one exactly; My Best Buy Plus™ named correctly as the membership programme; deal-card grammar (list price, sale price, "Save $X") matches Best Buy's merchandising format; category spread (laptops, TVs, headphones, consoles, appliances, cameras) representative of the real homepage.
- **Key divergences:** All prices invented (self-flagged "invented typical offers"); the "Aiea Store" local-store header is an invented localisation (a real Aiea, Hawaii store exists, but it is not a plausible default for this user).
- **Confidence:** High.

## 349. https://www.oracle.com/ — web/www.oracle.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described data-centre image not yet rendered).
- **Key matches:** Page title matches oracle.com's real title; OCI positioning current (AI-training workloads, consistent global pricing — a signature OCI claim); the Autonomous Database triad quoted correctly ("self-driving, self-securing and self-repairing"); Fusion Cloud Applications, NetSuite, Java stewardship and Oracle Health (the Cerner EHR business) all correctly placed; Free Tier call to action real.
- **Key divergences:** Body is a structured summary rather than the real page's campaign content; nothing factually wrong found.
- **Confidence:** High.

## 350. https://www.meta.com/ — web/www.meta.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Tagline "Build the future of human connection" is Meta's real current line; the consumer/corporate split (meta.com storefront vs about.meta.com) correctly drawn; product facts current (Quest 3 and Quest 3S as the headset line, Ray-Ban Meta glasses with EssilorLuxottica, Meta AI across the apps and glasses, built on Llama).
- **Key divergences:** Rendered as a prose summary of the storefront rather than its product-grid layout; nothing factually wrong found.
- **Confidence:** High.

## 351. https://meta.wikimedia.org/ — web/meta.wikimedia.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described community logo not yet rendered).
- **Key matches:** Purpose stated exactly as the real Meta-Wiki's (global community coordination for the Wikimedia projects and movement); the activity catalogue is right (requests for comment, steward and global-admin coordination, spam/vandalism blacklists, translation coordination, grants, elections, movement strategy, the Babel language forum) — insider-accurate for a working wiki few outsiders know.
- **Key divergences:** The logo description ("circle of community figures") could not be verified against the real Meta-Wiki logo at audit time; content otherwise compressed but correct.
- **Confidence:** High on text, low on the logo description.

## 352. https://species.wikimedia.org/ — web/species.wikimedia.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described logo not yet rendered).
- **Key matches:** Tagline "The free species directory that anyone can edit" matches Wikispecies' real one; scope (all life — animals, plants, fungi, bacteria, archaea, protists, viruses) and the taxon-page anatomy (classification, name and authority, type information, synonyms, distribution, references, vernacular names) correctly described; tree-of-life navigation from Archaea/Bacteria/Eukaryota accurate.
- **Key divergences:** Compressed; the logo gloss ("leaf / tree of life motif") is approximate.
- **Confidence:** High.

## 353. https://en.wikiversity.org/ — web/en.wikiversity.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described logo not yet rendered).
- **Key matches:** Slogan "Set learning free" is Wikiversity's real one; structure right (Featured Project, schools/portals organisation, level grouping from pre-school to tertiary and non-formal); the distinguishing point — Wikiversity hosts research, uniquely permissive among the Wikimedia projects — correctly identified.
- **Key divergences:** Compressed main page; nothing wrong found.
- **Confidence:** High.

## 354. https://www.nhm.ac.uk/ — web/www.nhm.ac.uk/index.html
- **Verdict: close**
- **Images at audit time: complete** — the generated Hintze Hall photograph is excellent: the blue whale skeleton suspended beneath Waterhouse's Romanesque terracotta arches, matching the real hall's iconic view.
- **Key matches:** Collection facts exact (some 80 million items across the five collections — botany, entomology, mineralogy, palaeontology, zoology); Waterhouse's "cathedral to nature" opened 1881; Hope the blue whale in Hintze Hall since 2017, succeeding Dippy, correctly sequenced; Darwin Centre cocoon, free permanent galleries, and Wildlife Photographer of the Year as the flagship competition-exhibition — all right.
- **Key divergences:** Exhibitions/events summarised rather than the day's listings; nothing factually wrong found.
- **Confidence:** High.

## 355. https://www.royalsociety.org/ — web/www.royalsociety.org/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Oldest scientific academy in continuous existence, founded 1660; Nullius in verba motto correctly translated and framed; Philosophical Transactions (1665) as the world's first science journal; Copley Medal as the oldest surviving scientific award; annual Summer Science Exhibition; grants/policy/events portfolio — all correct.
- **Key divergences:** The "~1,700 Fellows and Foreign Members" figure is plausible and hedged "as recalled", but "around 85 Nobel laureates" understates the Society's commonly cited cumulative total (280+ laureates among past and present Fellows) unless it means currently living laureates — recorded as an unverified/possibly conflated figure.
- **Confidence:** Medium-high.

## 356. https://news.google.com/ — web/news.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Product anatomy exactly right: "Your briefing", Top stories clusters with multi-publisher coverage and the "Full coverage" view, the standing section tabs (World · U.S. · Business · Technology · Entertainment · Sports · Science · Health), Local, and the real Fact Check section; personalisation ("For you" with more/less controls) correctly identified as the defining post-2018 design.
- **Key divergences:** Contains no actual headlines (a structural description of the product rather than today's front page) — the news-rotation limitation in its purest form.
- **Confidence:** High.

## 357. https://play.google.com/ — web/play.google.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: placeholder-only** (app-icon glyphs only).
- **Key matches:** Storefront architecture matches the real Play web store (Apps / Games / Books / Kids tabs, Offers, Top free / Top grossing / Trending / Top paid charts, star ratings with download counts in the real formats); footer entries real (Play Pass, Play Points, Gift cards, Redeem, Refund policy).
- **Key divergences:** Every app listing is invented — disclosed on-page ("App names below are invented generic examples"); no real chart-toppers (the actual top-free list) are recalled.
- **Confidence:** High.

## 358. https://music.youtube.com/ — web/music.youtube.com/index.html
- **Verdict: broadly-right**
- **Images at audit time: complete** — three generated album-art images (abstract shapes, desert landscape, forest canopy) suited to their invented mixes.
- **Key matches:** Chrome matches the real YouTube Music web app (Home / Explore / Library rail, search prompt, Cast and Sign in, "Listen again" shelf, Quick picks, persistent playback bar with progress).
- **Key divergences:** All artists and releases invented — self-labelling ones at that ("The Example Band", "Sample Quartet", "The Placeholders", "Sample Singer"), so the page is a UI shell with placeholder taste instead of the user's real personalised mixes.
- **Confidence:** High.

## 359. https://www.ams.org/ — web/www.ams.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Society facts exact: founded 1888; the journal portfolio (Journal of the AMS, Transactions, Notices as the membership magazine); MathSciNet's lineage from Mathematical Reviews (1940) correctly given; the Joint Mathematics Meetings each January as among the world's largest mathematics gatherings; the Cole and Steele Prizes correctly named as AMS prizes.
- **Key divergences:** Homepage compressed into a summary; nothing wrong found.
- **Confidence:** High.

## 360. https://www.rsc.org/ — web/www.rsc.org/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Publishing portfolio exact (Chemical Science as the gold open-access flagship, Chemical Communications, Chemical Society Reviews, the Journal of Materials Chemistry family); membership grades through Fellow (FRSC); degree accreditation and RSC Education correctly placed; institutional roots in the Chemical Society of 1841 correctly stated.
- **Key divergences:** Compressed; the mission sentence is presented as a quotation and matches the Society's published mission language as recalled, but was not live-verified word-for-word.
- **Confidence:** High on journals/history, medium on the quotation.

## 361. https://www.nic.net.np/ — web/www.nic.net.np/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** An obscure registry recreated with its distinctive facts intact: .np administered for decades by Mercantile Communications; registrations famously free to Nepali citizens and organisations against citizenship certificates or company-registration documents; the second-level labels (com.np, org.np, gov.np, edu.np, net.np) and the register.com.np processing route; .np dating to 1995; Nepal's +977 calling code — all correct as recalled, and appropriately hedged where the crawler was unsure.
- **Key divergences:** Compressed; hedging phrases ("as recalled") appear on-page.
- **Confidence:** Medium-high.

## 362. https://en.wikipedia.org/wiki/Borda_count — web/en.wikipedia.org/wiki/Borda_count/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Method and history right: proposed by Jean-Charles de Borda in 1770 for French Academy of Sciences elections, positional points summed over rankings; the property analysis is the real one (consensus winners, can defeat a Condorcet winner, acute vulnerability to teaming/clone nomination); current public uses correctly cited — Slovenia's ethnic-minority parliamentary seats, Nauru's weighted variant, Kiribati's presidential nomination stage.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 363. https://en.wikipedia.org/wiki/Condorcet_method — web/en.wikipedia.org/wiki/Condorcet_method/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Definition exact (elects the pairwise-beats-all Condorcet winner when one exists); the Condorcet paradox correctly stated as cyclic majorities; the completion methods all real and correctly grouped (Copeland, Schulze, ranked pairs, minimax, Kemeny–Young) with the Smith set correctly characterised; criteria discussion (majority/mutual-majority satisfaction vs plurality/IRV, Arrow and Gibbard–Satterthwaite framing) accurate; the rare-adoption note (including Marquette, Michigan's early-20th-century experiment) right.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 364. https://en.wikipedia.org/wiki/Space_Shuttle_Challenger_disaster — web/en.wikipedia.org/wiki/Space_Shuttle_Challenger_disaster/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** — a bracketed description of the famous breakup photograph (branching smoke trails) stands where the real article's lead image sits; no PNG embedded yet.
- **Key matches:** Facts exact: breakup 73 seconds after liftoff on 28 January 1986 from Kennedy Space Center; all seven crew named with correct roles (Scobee, Smith, Onizuka, Resnik, McNair, Jarvis, and Christa McAuliffe as the Teacher in Space participant); cause chain correct (right-SRB O-ring resiliency lost in the cold, Morton Thiokol engineers' warnings overruled, hot-gas burn-through, external-tank collapse, orbiter destroyed by aerodynamic forces — not a simplistic "explosion").
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 365. https://en.wikipedia.org/wiki/Roscosmos — web/en.wikipedia.org/wiki/Roscosmos/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described Soyuz/Baikonur image not yet rendered).
- **Key matches:** Institutional history right (state-corporation form in 2015, succeeding the Federal Space Agency founded 1992); operations correctly summarised (Soyuz crew and Progress cargo to the ISS from leased Baikonur, GLONASS management, Plesetsk and Vostochny launch sites, post-2022 ISS-partnership strain after the invasion of Ukraine).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 366. https://en.wikipedia.org/wiki/Treaty_of_Ghent — web/en.wikipedia.org/wiki/Treaty_of_Ghent/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Treaty record exact: signed at Ghent (United Netherlands) on 24 December 1814; status quo ante bellum restoration; the US Senate's unanimous ratification on 16 February 1815 and proclamation on 17 February; the treaty's famous silence on impressment and neutral rights, mooted by Napoleon's fall; the US negotiators correctly named (John Quincy Adams, Henry Clay, Albert Gallatin, James A. Bayard Sr., Jonathan Russell).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 367. https://en.wikipedia.org/wiki/Battle_of_New_Orleans — web/en.wikipedia.org/wiki/Battle_of_New_Orleans/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described battle image not yet rendered).
- **Key matches:** Fought 8 January 1815, some 5 miles south-east of the city, Pakenham against Brevet Major General Andrew Jackson; the force composition is right down to the colourful details (regulars, militia, free men of colour, Choctaw warriors, Lafitte's Baratarian privateers); the casualty asymmetry (~2,000 British vs a few dozen American) and the roughly half-hour main assault; the "fifteen days after the Treaty of Ghent" framing with the sophisticated correction — ratification was still pending, so the "needless battle" trope is too simple.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 368. https://en.wikipedia.org/wiki/JAXA — web/en.wikipedia.org/wiki/JAXA/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described Hayabusa2/Ryugu artist's impression not yet rendered).
- **Key matches:** Formed 1 October 2003 by merging three aerospace organisations; headquartered in Chōfu, Tokyo; Hayabusa as the first asteroid sample return (Itokawa, 2010) and Hayabusa2's Ryugu return (2020); Kibo as the largest single ISS module; Tanegashima launches on H-II/H3; SLIM's 2024 pinpoint lunar landing; Artemis partnership — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 369. https://en.wikipedia.org/wiki/Kennedy_Space_Center — web/en.wikipedia.org/wiki/Kennedy_Space_Center/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described VAB image not yet rendered).
- **Key matches:** One of NASA's ten field centres; primary US human-spaceflight launch site since 1968; Merritt Island location beside Cape Canaveral; Launch Complex 39 and the VAB (among the world's largest buildings by volume) serving Apollo, Skylab, Shuttle and now SLS/Artemis; Pad 39A's lease to SpaceX for Falcon 9 and Falcon Heavy; the wildlife-refuge setting — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 370. https://about.meta.com/ — web/about.meta.com/index.html
- **Verdict: close**
- **Images at audit time: complete** — three generated illustrations (Quest VR user, family video call, Meta AI chat) matching the page's three technology pillars.
- **Key matches:** The corporate tagline is reproduced in full ("Build the future of human connection and the technology that makes it possible" — Meta's real line, also used in shorter form on meta.com, entry 350); Family of Apps list complete and correct (Facebook, Instagram, Messenger, Threads, WhatsApp); Reality Labs correctly framed for Quest/Horizon; founded 2004 as Facebook, renamed Meta in October 2021, Menlo Park headquarters — all exact.
- **Key divergences:** Corporate news/careers content summarised; nothing wrong found.
- **Confidence:** High.

## 371. https://www.thewaltdisneycompany.com/ — web/www.thewaltdisneycompany.com/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated castle photograph leads, with described segment images (studio lot, streaming interface, park aerial, stadium) in the layout.
- **Key matches:** The mission statement is verbatim ("to entertain, inform and inspire people around the globe through the power of unparalleled storytelling"); the post-2023 segment structure is correctly reproduced (Entertainment — Studios/Pixar/Marvel/Lucasfilm/20th Century plus ABC, FX, National Geographic; Direct-to-Consumer — Disney+, Hulu, ESPN+; Experiences — parks, Cruise Line, Adventures by Disney, consumer products; ESPN & Sports as its own segment).
- **Key divergences:** Business descriptions compressed; ESPN's standalone streaming app (launched August 2025) is not separately noted.
- **Confidence:** High.

## 372. https://about.google/ — web/about.google/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Mission quoted verbatim; commitment themes match the real about site (carbon-neutral history with the 24/7 carbon-free-energy-by-2030 goal, crisis response, Google.org and flood-forecasting AI-for-good work); company facts right (founded 1998 by Page and Brin at Stanford; largest Alphabet subsidiary since 2015); Gemini correctly woven through the product story.
- **Key divergences:** Summarised rather than the real page's story format; nothing wrong found.
- **Confidence:** High.

## 373. https://accounts.google.com/ — web/accounts.google.com/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (correctly none — the real page is a bare card).
- **Key matches:** The sign-in card's microcopy is faithfully reproduced: "Email or phone" field, "Forgot email?", "Not your computer? Use a private browsing window to sign in", Create account ▾ and Next; the surrounding explanation (one account across Gmail/Drive/YouTube/Maps/Photos, security checkups, passkeys and two-step verification managed via myaccount.google.com) is accurate to the real flow.
- **Key divergences:** Rendered as a described mock rather than an interactive form; nothing factually wrong.
- **Confidence:** High.

## 374. https://en.wikipedia.org/wiki/Michel_Foucault — web/en.wikipedia.org/wiki/Michel_Foucault/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described Collège de France lecture image not yet rendered).
- **Key matches:** Biographical record exact: born 15 October 1926, Poitiers; died 25 June 1984, Paris; the Collège de France chair named precisely ("History of Systems of Thought", held 1970 until his death); bibliography dates all right (Madness and Civilization 1961, The Birth of the Clinic 1963, The Order of Things 1966, Discipline and Punish 1975, The History of Sexuality 1976–2018 including the posthumous fourth volume); the archaeology/genealogy periodisation, epistemes and the panopticon emblem all correctly deployed.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 375. https://en.wikipedia.org/wiki/Wok — web/en.wikipedia.org/wiki/Wok/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described wok image not yet rendered).
- **Key matches:** Origin and diffusion right (~two thousand years in China, spreading as the Malay/Indonesian kuali and cognates); the fuel-scarcity design logic; heat-gradient cooking technique; wok hei as the prized Cantonese smoky flavour; carbon-steel/cast-iron materials and seasoning — all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 376. https://en.wikipedia.org/wiki/Pressure_cooker — web/en.wikipedia.org/wiki/Pressure_cooker/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described cooker image not yet rendered).
- **Key matches:** Physics right (sealed steam raising water's boiling point from 100 °C to ~120 °C, cutting times to a third or less); Denis Papin's 1679 steam digester with his own safety valve correctly given as the origin; the "jiggle-top" early-domestic era and modern multi-valve safety fairly summarised.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 377. https://en.wikipedia.org/wiki/Simmering — web/en.wikipedia.org/wiki/Simmering/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described simmering-pot image not yet rendered).
- **Key matches:** Technique defined correctly — liquids held just below boiling, in the commonly cited ~85–96 °C (185–205 °F) band with occasional lazy bubbles; the gentleness rationale (delicate foods keep shape, tough meats tenderise without tightening) and the stock/soup/braise/rice applications all match standard culinary references and the real article.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 378. https://en.wikipedia.org/wiki/Perjury — web/en.wikipedia.org/wiki/Perjury/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Elements correctly stated (lawful oath, competent authority, falsity, materiality, knowledge and intent); the classic exclusion is correctly illustrated by Bronston v. United States (1973) — the literally-true-but-misleading answer is not perjury; enforcement realities (selective prosecution, oath-against-oath disfavour, the historical two-witness corroboration rule) all accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 379. https://en.wikipedia.org/wiki/Insider_trading — web/en.wikipedia.org/wiki/Insider_trading/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Doctrine presented with case-law precision: the US regime built without a statutory definition; classical theory vs the misappropriation theory of United States v. O'Hagan (1997); tippee liability's personal-benefit requirement through Dirks (1983) and Salman (2016); the EU Market Abuse Regulation's direct definitional ban as the contrast; the lawful/illegal insider-trading distinction correctly drawn up front.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 380. https://en.wikipedia.org/wiki/Sexagesimal — web/en.wikipedia.org/wiki/Sexagesimal/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described cuneiform tablet not yet rendered).
- **Key matches:** Base-60 positional system from third-millennium-BC Sumer, perfected by Babylonian astronomers; the highly-composite convenience argument with 60's divisor set correctly enumerated; transmission through Ptolemy's Almagest; survivals in degrees/minutes/seconds of arc and time exactly as the real article presents them.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 381. https://en.wikipedia.org/wiki/Equinox — web/en.wikipedia.org/wiki/Equinox/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described equinox diagram not yet rendered).
- **Key matches:** Definition and dates right (~20 March, ~22–23 September; Sun over the Equator; near-equal day and night); the sophisticated correction is included — refraction and the solar disc make the truly equal day (equilux) fall a few days off the equinox; seasonal assignments for both hemispheres correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 382. https://en.wikipedia.org/wiki/Contempt_of_court — web/en.wikipedia.org/wiki/Contempt_of_court/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Lead tracks the real article's definition; the criminal/civil split correctly characterised, including civil contempt's coercive logic in the classic aphorism (the contemnor "carries the keys of his prison in his own pocket"); England's strict-liability rule under the Contempt of Court Act 1981 correctly placed against press freedom; summary punishment by the offended judge noted as the tolerated anomaly it is.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 383. https://en.wikipedia.org/wiki/Tax_evasion — web/en.wikipedia.org/wiki/Tax_evasion/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The evasion/avoidance line drawn exactly where the law draws it, with Judge Learned Hand's dictum (no duty to pay more than the law demands) correctly invoked; the US tax gap scale; Capone's 1931 tax conviction; the modern enforcement stack all real (whistleblower bounties, Swiss Leaks and the Panama/Pandora Papers, OECD Common Reporting Standard, US FATCA, beneficial-ownership registers).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 384. https://en.wikipedia.org/wiki/Solstice — web/en.wikipedia.org/wiki/Solstice/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described solstice diagram not yet rendered).
- **Key matches:** Dates and geometry right (≈20–21 June, ≈21–22 December; axial tilt ≈23.44°; noon Sun over the Tropic of Cancer in June and Capricorn in December; polar day/night framing); solstitium ("the Sun stands still") etymology correctly explained via the halting noon-altitude trend.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 385. https://en.wikipedia.org/wiki/Great_circle — web/en.wikipedia.org/wiki/Great_circle/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described sphere diagram not yet rendered).
- **Key matches:** Definition exact (sphere ∩ centre-plane, two equal hemispheres); equator and meridian-pair examples right; non-equatorial latitude circles correctly classed as small circles; great-circle arcs as geodesics with the Europe–Japan Arctic-routing illustration the real article's topic demands.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 386. https://en.wikipedia.org/wiki/Krishna — web/en.wikipedia.org/wiki/Krishna/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described flute-playing Krishna image not yet rendered).
- **Key matches:** Theology and narrative accurate: eighth avatar of Vishnu and Supreme God in Krishna-centred traditions (Gaudiya Vaishnavism named); the lead's "protection, compassion, tenderness and love" matches the real article's wording; birth in Mathura to Devaki and Vasudeva, the Yamuna crossing to escape Kamsa, Vrindavan upbringing, butter theft, Kaliya's subjugation, Govardhan's lifting, Radha and the gopis; sources correctly given (Mahābhārata, Harivaṃśa, Bhāgavata Purāṇa) and Janmashtami as the birth festival.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 387. https://en.wikipedia.org/wiki/Saffron — web/en.wikipedia.org/wiki/Saffron/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described saffron-threads image not yet rendered).
- **Key matches:** Production facts exact: three crimson stigmas per Crocus sativus flower, hand-picked, roughly 150,000 flowers per kilogram — hence the world's most expensive spice by weight; Iran's ~90% production share; the sterile crocus propagated by corms with a brief autumn bloom; the signature-dish list (paella, tahdig, biryani, Kashmiri kahwa, risotto alla milanese, bouillabaisse) all genuine saffron dishes.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 388. https://en.wikipedia.org/wiki/Artemis — web/en.wikipedia.org/wiki/Artemis/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described huntress statue not yet rendered).
- **Key matches:** Identity and domains right (Zeus and Leto, Apollo's twin, one of the twelve Olympians; hunt, wild animals, childbirth, young girls; later lunar association; Roman Diana); the myth cycle accurately retold — first-born on Delos who helped deliver Apollo, Actaeon's stag transformation and death by his own hounds, Callisto's bear transformation, and the Iphigenia sacrifice with the deer substitution correctly hedged as version-dependent.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 389. https://en.wikipedia.org/wiki/Chili_pepper — web/en.wikipedia.org/wiki/Chili_pepper/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described peppers image not yet rendered).
- **Key matches:** Capsicum domesticated in the Americas (evidence ~6000 BCE) and globalised only after 1492; Scoville figures all in their true ranges (bell pepper 0; jalapeño 2,500–8,000; habanero 100,000–350,000; Carolina Reaper/Pepper X class above 1.5 million); the cuisine-transformation observation (Thai, Sichuan, Indian, Korean food all acquired chilies within 500 years) is the real article's point, correctly made.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 390. https://en.wikipedia.org/wiki/John_Harrison — web/en.wikipedia.org/wiki/John_Harrison/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated portrait embedded (period-style likeness of the clockmaker).
- **Key matches:** Vital dates exact (born 3 April 1693, Foulby; died 24 March 1776, London — matching Wikipedia's given dates); technical biography precise: wooden precision clocks with self-lubricating lignum vitae and the grasshopper escapement; H1 completed 1735 and its Lisbon trial; H2/H3's two decades with the bimetallic strip and caged roller bearings; H4 (1759) as a 13 cm watch and its 1761–62 Jamaica trial; the Board of Longitude obstruction narrative fairly told.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 391. https://en.wikipedia.org/wiki/Yalta_Conference — web/en.wikipedia.org/wiki/Yalta_Conference/index.html
- **Verdict: close**
- **Images at audit time: complete** — the generated "Big Three" photograph is remarkable: black-and-white, Churchill in greatcoat and cap at left, Roosevelt in his dark cape at centre, Stalin in marshal's uniform at right, seated in the Livadia courtyard arcade — matching the famous photograph's composition and the page caption's left-to-right order (Churchill, Roosevelt, Stalin).
- **Key matches:** Lead near-verbatim to the real article: 4–11 February 1945, Livadia Palace, second of the three Big Three conferences (Tehran 1943 before, Potsdam July 1945 after), agenda (Germany's occupation, Poland, UN founding, Soviet entry against Japan) and even the conference codename — the Argonaut Conference — correctly recalled.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 392. https://en.wikipedia.org/wiki/Eratosthenes — web/en.wikipedia.org/wiki/Eratosthenes/index.html
- **Verdict: close**
- **Images at audit time: complete** — the generated experiment diagram is one of the finest images of the run: fully and correctly labelled (parallel solar rays, Alexandria obelisk shadow angle 7.2°, the shadowless Syene well, arc distance ≈5,000 stadia ≈800 km, central angle θ = 7.2°, conclusion ≈250,000 stadia, dated c. 240 BCE), with coherent geometry throughout.
- **Key matches:** Biography and method exact: c. 276–c. 194 BC, Cyrene to Alexandria, chief librarian, coiner of "geography" and founder of the discipline, the sieve; the measurement narrative correct in every number (7.2° as one-fiftieth of a circle, ~5,000 stadia baseline, ×50 circumference).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 393. https://en.wikipedia.org/wiki/War_of_1812 — web/en.wikipedia.org/wiki/War_of_1812/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated naval-action image (Constitution vs Guerrière, the war's famous frigate duel) embedded.
- **Key matches:** Lead matches the real article's framing, including its exact date span (18 June 1812 – 17 February 1815, the US ratification date) and full causes list (war-driven trade restrictions, impressment, British support for Native tribes resisting expansion, American ambitions in Canada); theatres and the status-quo-ante-bellum outcome correctly stated.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 394. https://en.wikipedia.org/wiki/Antarctic_Treaty_System — web/en.wikipedia.org/wiki/Antarctic_Treaty_System/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Treaty record exact: signed in Washington on 1 December 1959 by the twelve IGY-active states — all twelve named correctly — entering into force 23 June 1961; the prohibitions (military activity, weapons testing, nuclear explosions and waste disposal) and the Article IV territorial-claims freeze correctly stated as the system's famous diplomatic device; the lead's "Earth's only continent without a native human population" matches the real article's own opening.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 395. https://en.wikipedia.org/wiki/Bhagavad_Gita — web/en.wikipedia.org/wiki/Bhagavad_Gita/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated traditional-style painting of Krishna as charioteer teaching Arjuna at Kurukshetra, matching the page's own caption and the subject's standard iconography.
- **Key matches:** Textual placement exact (700-verse dialogue within the Mahābhārata, Bhishma Parva chapters 23–40); the teaching synthesis correctly summarised (karma, bhakti and jñāna yogas toward moksha), including the canonical rendering of 2.47 ("You have a right to your actions, but never to your actions' fruits") and the universal-form vision as the climax.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 396. https://en.wikipedia.org/wiki/Quetzalcoatl — web/en.wikipedia.org/wiki/Quetzalcoatl/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described feathered-serpent image not yet rendered).
- **Key matches:** Name etymology correct (quetzal + cōātl, "Feathered Serpent"); cult history right (Teotihuacan's Feathered Serpent Pyramid, Toltecs, Aztecs; Maya counterparts Kukulkan and Gucumatz both named); the Ehecatl wind aspect who sweeps the rain's path; the creation myth correctly told (retrieving the bones of previous humanity from the underworld and animating them with his own blood for the Fifth Sun); the Ce Acatl Topiltzin priest-king legend correctly introduced.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 397. https://en.wikipedia.org/wiki/Anansi — web/en.wikipedia.org/wiki/Anansi/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described storyteller image not yet rendered).
- **Key matches:** Akan origin (Ghana/Côte d'Ivoire) and the anansesem ("spider stories") genre name correct; the signature tale accurately retold — Anansi buying Nyame's stories by capturing hornets, a python, a leopard and a fairy, becoming owner of all stories; diaspora forms right (Anancy in Jamaica, Aunt Nancy in the US South); the trickster's celebrated-yet-reproached character fairly drawn.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 398. https://en.wikipedia.org/wiki/John_Maynard_Keynes — web/en.wikipedia.org/wiki/John_Maynard_Keynes/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated 1930s-style portrait embedded.
- **Key matches:** Vital dates and places exact (5 June 1883, Cambridge; 21 April 1946, Firle); career arc right (King's College, India Office and Treasury, Paris Peace Conference resignation for The Economic Consequences of the Peace, 1919); the General Theory's apparatus correctly enumerated (aggregate demand and volatile investment, consumption function, multiplier, liquidity preference, under-employment equilibrium).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 399. https://en.wikipedia.org/wiki/Iraq_War — web/en.wikipedia.org/wiki/Iraq_War/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** The contested history is stated accurately and even-handedly: invasion 20 March 2003 by the US/UK-led coalition, Ba'athist government overthrown within three weeks; the stated justifications (WMD, al-Qaeda links) followed by the findings (no stockpiles found; the 9/11 Commission's no-operational-relationship conclusion); no explicit Security Council authorisation; the largest anti-war protests in history; the CPA's army-disbanding and de-Ba'athification decisions; the 2006–08 sectarian civil war; Abu Ghraib; al-Qaeda in Iraq as the Islamic State's ancestor — all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 400. https://en.wikipedia.org/wiki/New_York_Stock_Exchange — web/en.wikipedia.org/wiki/New_York_Stock_Exchange/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated photograph of the neoclassical Broad Street facade embedded, matching the real building's famous frontage.
- **Key matches:** Institutional record exact: Buttonwood Agreement 1792, organised 1817, owned by Intercontinental Exchange since 2013; 11 Wall Street landmark opened 1903; the hybrid floor/electronic model with designated market makers correctly explained; ~2,300 listings and world's-largest-by-market-cap status right.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 401. https://en.wikipedia.org/wiki/Avocado — web/en.wikipedia.org/wiki/Avocado/index.html
- **Verdict: close**
- **Images at audit time: complete** — a generated halved-avocado photograph (green flesh, single brown seed) matching the botanical description.
- **Key matches:** Persea americana of the laurel family, native to south-central Mexico; a large single-seeded berry; fat profile (mostly monounsaturated oleic acid) and low sugar correctly stated; Nahuatl āhuacatl etymology; the Hass story right (chance seedling, patented in California in 1935 by Rudolph Hass) with Mexico as the dominant producer.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 402. https://en.wikipedia.org/wiki/Deng_Xiaoping — web/en.wikipedia.org/wiki/Deng_Xiaoping/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (none embedded).
- **Key matches:** Lead exact: 22 August 1904 – 19 February 1997; paramount leader 1978 to his 1989 retirement without ever holding head-of-state/government office — including the connoisseur detail that after 1989 his only post was the honorary presidency of the China Bridge Association; rule via the Party and the Central Military Commission (chaired until 1989); reform-and-opening-up programme correctly itemised (special economic zones, decollectivisation, "socialism with Chinese characteristics"); the authoritarian counterweight equally present (Democracy Wall suppression, Four Cardinal Principles, the 1989 crackdown with a responsibly ranged death toll).
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 403. https://en.wikipedia.org/wiki/Physiocracy — web/en.wikipedia.org/wiki/Physiocracy/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described farm-landscape image not yet rendered).
- **Key matches:** School history precise: name coined by Pierre Samuel du Pont de Nemours (1767) meaning "government of nature"; Quesnay, physician to Louis XV, and the Tableau Économique (1758) as the first schematic of economic circulation; the three-class schema (productive farmers, proprietary landowners, sterile manufacturers/merchants) exactly right; impôt unique, grain free trade and Turgot's 1774–76 reform attempt correctly placed; laissez-faire correctly traced to this school.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 404. https://en.wikipedia.org/wiki/Remittance — web/en.wikipedia.org/wiki/Remittance/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described money-transfer image not yet rendered).
- **Key matches:** Magnitudes right: officially recorded flows to low- and middle-income countries of roughly US$650–670 billion a year in the early 2020s, exceeding FDI and dwarfing aid; India the largest recipient (over $100 billion), followed by Mexico, China and the Philippines; remittance-to-GDP shares above a quarter for Nepal, Lebanon, Tonga and others; the ~6% average sending cost against the UN SDG 3% target; hawala and de-risking correctly included.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 405. https://en.wikipedia.org/wiki/Economic_sanctions — web/en.wikipedia.org/wiki/Economic_sanctions/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described border-checkpoint image not yet rendered).
- **Key matches:** Instrument range correct (tariffs and export controls to asset freezes, SWIFT exclusion, full embargoes); regime summaries right (Iran with the 2015 JCPOA relief and 2018 US reimposition; Cuba's embargo since the 1960s; Russia post-2022 as the largest-scale case with central-bank freezes and oil price caps); the effectiveness literature fairly stated via Hufbauer (success in a minority of cases, better for modest goals) with the smart-sanctions response.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 406. https://en.wikipedia.org/wiki/Cooperative — web/en.wikipedia.org/wiki/Cooperative/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described co-op image not yet rendered).
- **Key matches:** Lead closely paraphrases the International Co-operative Alliance's canonical definition (autonomous, voluntary, jointly owned, democratically controlled); movement history right (Rochdale Pioneers 1844 and their Principles, ICA founded 1895, the ~1 billion members claim); exemplars correctly chosen (Mondragon as the largest worker-cooperative federation, Fonterra for agricultural co-ops, credit unions); the governance economics (trust/commitment advantages vs capital-raising difficulty, surprisingly good survival rates) fairly reflects the literature.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 407. https://en.wikipedia.org/wiki/Occupy_movement — web/en.wikipedia.org/wiki/Occupy_movement/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described encampment image not yet rendered).
- **Key matches:** Chronology and mechanics exact: Occupy Wall Street begins in Zuccotti Park on 17 September 2011, called into being by an Adbusters poster, inspired by the Arab Spring and Spain's indignados; "We are the 99%" framing; leaderless general assemblies and the no-unified-demands structure; Zuccotti cleared November 2011; offshoots right (Occupy Sandy 2012, Rolling Jubilee debt abolition); the linguistic legacy ("the 1%" entering everyday vocabulary, the Piketty context) correctly assessed.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 408. https://en.wikipedia.org/wiki/Knowledge_economy — web/en.wikipedia.org/wiki/Knowledge_economy/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described laboratory image not yet rendered).
- **Key matches:** Intellectual history right: popularised by Peter Drucker (The Age of Discontinuity, 1969), developed through 1990s OECD analysis; the intangibles finding (R&D, data, brands, software and organisational capital rivalling or exceeding tangible investment in leading economies) matches the Corrado–Hulten–Sichel evidence the real article cites; non-rivalry, increasing returns and endogenous-growth framing all correct.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 409. https://en.wikipedia.org/wiki/Planned_economy — web/en.wikipedia.org/wiki/Planned_economy/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described Soviet-poster-style image not yet rendered).
- **Key matches:** System description and history right (USSR from the First Five-Year Plan, 1928; post-1945 satellites; Mao-era China; attenuated survival in Cuba and North Korea); Gosplan mechanics (physical and value targets, input allocation, fixed prices and wages, consumer goods as residual claimant); the twin theoretical critiques correctly dated and attributed — Mises's calculation argument (1920) and Hayek's knowledge problem; the achieved-industrialisation-vs-chronic-shortage balance fairly struck.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 410. https://en.wikipedia.org/wiki/Wage — web/en.wikipedia.org/wiki/Wage/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described payslip image not yet rendered).
- **Key matches:** Wage/salary/commission distinctions correct; determination theory complete and balanced (marginal productivity alongside bargaining power, unions, minimum-wage law, efficiency wages, firm rents and discrimination); real wage, wage share, rigidity and the post-1970s productivity–pay decoupling all correctly placed as the field's central concepts.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

## 411. https://en.wikipedia.org/wiki/Profit_(economics) — web/en.wikipedia.org/wiki/Profit/index.html
- **Verdict: close**
- **Images at audit time: placeholder-only** (described ledger image not yet rendered).
- **Key matches:** Accounting vs economic profit (explicit vs explicit-plus-opportunity costs) and normal vs super-normal profit correctly defined; long-run zero-profit tendency under perfect competition; persistent profit correctly attributed to market power, risk, Schumpeterian innovation rents or luck; Frank Knight's 1921 uncertainty theory correctly dated and stated; the Ricardo-to-Marx distributional framing accurate.
- **Key divergences:** Compressed; nothing wrong found.
- **Confidence:** High.

---

# CLOSING SUMMARY — Audit of Run 1 (finalised 22:15 PDT, 2026-10-17)

**Coverage.** 411 pages audited (entries 1–411 above; machine-readable record in `audit/audit.jsonl`, 411 valid JSON lines), sampled across all 109 domains present in the crawl at audit close (~4,487 recreated pages). Sampling prioritised homepages, high-traffic pages, the seed and its descendants, and pages with generated images; it was not random, so the rates below describe the audited sample, not the whole crawl.

**Verdict totals.**
- **close: 301 (73%)**
- **broadly-right: 100 (24%)**
- **divergent: 10 (2%)**
- **largely-invented: 0**

No audited page was wholly fabricated. Even the weakest pages reproduced their site's identity, structure and purpose correctly; failure was always a matter of missing specifics, staleness, or invented filler, never of wholesale invention.

**Images.** 124 of the 411 audited pages had generated images embedded at audit time (119 complete sets, 5 partial); the other 287 were placeholder-only at the moment of audit (image generation lagged page creation throughout, so this reflects timing, not omission). Judged against the real pages' notable lead images, the generated imagery was a strength of the run: portraits and historical "photographs" (Einstein, the Yalta Big Three, Keynes), landmarks (Hintze Hall's whale, Chicago skyline, Howrah Bridge, Everest from Rongbuk, the Golden Temple, Itsukushima), logos (MediaWiki, Wikipedia globe concept), scientific subjects (LHC tunnel, ISS-era spacecraft concept art, Parker-era probes) and even a fully labelled Eratosthenes diagram were usually true to subject and composition. The failures clustered where the real image is a specific artwork or news photograph: the Mona Lisa's face drifts modern, the Guardian's "lead photo" is a fake print newspaper front page, CNN's lead is a generic local-TV studio graphic, and Marie Curie's portrait invents a labelled-bottle laboratory set the real c.1920 portrait does not have.

**Most striking matches.**
- Wikipedia article recreations were factually near-flawless in the sample: across ~250 articles checked, dates, figures and case names were almost always exactly right — e.g. the Super Bowl LV–LIX results table (scores, dates, the LVIII overtime note), Sci-Hub's five landmark-paper DOIs with exact citations, LibGen book records with genuine ISBNs (live-verified for Kahneman and Tolkien), the CMB's 2.725 K / 380,000-year recombination figures, the Antarctic Treaty's twelve named signatories, Challenger's crew and cause chain, and Eratosthenes' 7.2° / 5,000-stadia / 250,000-stadia chain.
- Static institutional and commercial copy was often verbatim or near-verbatim: Berkshire Hathaway's entire link list (down to the Activision-securities link and the personnel disclaimer), Disney's and Google's mission statements, Mozilla's "Internet for people, not profit", Wikidata's Douglas Adams = Q42, the Wikisource iceberg logo, Wiktionary's Beer Parlour, eBay's and Amazon's chrome.
- Current product data was frequently live-accurate (RTX 50-series pricing table, Steam Deck ladder, IBM Quantum roadmap, TSMC's N2/A16 status, Costco's $4.99 rotisserie chicken).

**Worst divergences (the 10 "divergent" verdicts and systematic issues).**
1. **News homepages contain no news.** BBC, NYT, Reuters, CNN, AP, Guardian, Al Jazeera and BBC Sport recreations have zero specific headlines — pure genre description (AP's page literally says "Summarised generically here"). Google News is a structural description only.
2. **Wikinews is dead and the recreations don't know.** The Wikimedia Board closed Wikinews; all editions have been read-only since 4 May 2026. Recreations present it as a live sister project everywhere; real sister-project lists dropped it and added Wikifunctions, which is missing throughout the crawl.
3. **A ~2025 knowledge snapshot.** © 2025 footers on US social/commerce pages, Portal:Current_events topping out in October 2025, Super Bowl champions stopping at LIX, James Watson written as living (he died in November 2025), stale counts (English Wikipedia 6.9M vs ~7.25M articles; ESA "22 Member States" vs 23 since Slovenia joined in 2025; AWS's pre-2025 region count), and pre-price-rise Tesla Model S/X pricing.
4. **Individual factual errors worth noting:** Tesla Cybertruck's payload given as "6,834 lbs" (the curb weight, digit-transposed; real payload 2,500 lb — live-verified); Galaxy Z Fold priced from the 2023 Fold 5; the seed page's entire daily content invented (featured article, picture of the day, statistics); Saturn's moons as 146 against a live total of 293; Tigris length and Yosemite area figures off; Reddit promoting Coins/Premium features discontinued in 2023.
5. **Template artefacts:** identical Italian boilerplate paragraphs left on the Portuguese, Italian and Polish Wikipedia homepages; UK spellings leaking into US sites ("Bin", "Tyre Centre", "Petrol"); a literal "?" inside one LibGen path; "(year as remembered)" last-edited footers and on-page "recreated from memory" markers on many pages, contrary to the run's ledger-only uncertainty convention.

**Overall assessment.** Muse's memory of the stable, factual web — encyclopaedia articles, institutional pages, product specifications, bibliographic records, historical events — is remarkably precise, often to the exact number, DOI, ISBN or codename (Yalta's "Argonaut"). Its memory fails predictably at the moving edges: anything personalised, rotating or time-sensitive (news fronts, feeds, featured content, prices after mid-2025, counts and office-holders) is either described generically, honestly flagged as invented, or silently frozen at a ~2025 snapshot. The generated images follow the same pattern: strong on famous, stable subjects; weakest on specific artworks and news photography.

— Audit agent, Run 1.
