import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl/hidden_files")
from build_am import build, queue, L

# ---------------- Voyager 2 ----------------
build("Voyager_2", "Voyager 2", [
 ("thumb","voyager2-spacecraft","The Voyager spacecraft with its large white dish antenna, gold foil bus and long instrument boom","The Voyager spacecraft, showing the 3.7 m high-gain antenna."),
 ("p",["<b>Voyager 2</b> is a space probe launched by ",L("NASA")," on 20 August 1977, sixteen days before its twin ",L("Voyager_1"),". Taking advantage of a rare alignment of the outer planets, it is the only spacecraft to have visited all four giant planets: Jupiter (1979), Saturn (1981), Uranus (1986) and Neptune (1989), returning the first close-up images of the two ice giants and discovering volcanic activity on Jupiter's moon Io and plumes on Neptune's moon Triton."]),
 ("p",["Voyager 2 crossed into interstellar space in November 2018 at about 119 astronomical units from the Sun, joining Voyager 1 in the space between the stars. Powered by three radioisotope generators whose output declines yearly, it still returns data from a handful of instruments. Like its twin it carries the Golden Record, a phonograph disc of sounds and images of Earth. Signals from Voyager 2 now take more than eighteen hours to reach Earth."]),
], ["Light-time figure grows continually; stated approximately. Uranus/Neptune encounter years certain."])

# ---------------- Galileo ----------------
build("Galileo_(spacecraft)", "Galileo (spacecraft)", [
 ("thumb","galileo-jupiter","The Galileo orbiter approaching Jupiter, with its umbrella-like high-gain antenna that never fully opened","Galileo at Jupiter (artist's impression)."),
 ("p",["<b>Galileo</b> was a ",L("NASA")," space probe that studied Jupiter and its moons from 1995 to 2003. Launched from the ",L("Space_Shuttle")," Atlantis in October 1989, it took six years to reach Jupiter, flying past Venus and Earth for ",L("Gravity_assist"),"s and becoming the first spacecraft to encounter an asteroid (951 Gaspra, and Ida — where it discovered the first asteroid moon, Dactyl)."]),
 ("p",["Galileo's main antenna failed to unfurl, forcing engineers to return data at very low rates through a small antenna with upgraded ground stations and compression — a celebrated salvage. Its atmospheric probe plunged into Jupiter in December 1995, returning the first direct measurements of a giant planet's atmosphere. The orbiter's observations of Europa built the case for a global salty ocean beneath its ice. To avoid any chance of contaminating Europa, Galileo was deliberately crashed into Jupiter on 21 September 2003."]),
], ["Asteroid flyby order and dates summarised from memory."])

# ---------------- Juno ----------------
build("Juno_(spacecraft)", "Juno (spacecraft)", [
 ("thumb","juno-spacecraft","The Juno spacecraft with its three huge solar panel wings orbiting over Jupiter's swirling poles","Juno orbiting Jupiter (artist's impression)."),
 ("p",["<b>Juno</b> is a ",L("NASA")," space probe orbiting Jupiter, launched on 5 August 2011 and arriving on 4 July 2016. Named after the Roman goddess Juno, who could see through the clouds her husband Jupiter drew around himself, the mission studies the planet's composition, gravity and magnetic fields, and polar magnetosphere to understand how Jupiter formed."]),
 ("p",["Juno is the most distant solar-powered spacecraft ever flown, using three enormous solar arrays because sunlight at Jupiter is twenty-five times weaker than at Earth. It flies a highly elliptical polar orbit that skims close over the poles while minimising time in the planet's intense radiation belts; its sensitive electronics sit inside a titanium radiation vault. Juno has revealed Jupiter's cyclonic polar storms, measured its deep atmospheric winds, and in its extended mission has flown close past the moons Ganymede, Europa and Io."]),
], ["Juno's end-of-mission date has been extended more than once; described without a firm date."])

# ---------------- Curiosity rover ----------------
build("Curiosity_(rover)", "Curiosity (rover)", [
 ("thumb","curiosity-selfie","The Curiosity rover's self-portrait: a car-sized white rover with a robotic arm and camera mast on rusty-red Martian ground","Curiosity's self-portrait at a drill site on Mars."),
 ("p",["<b>Curiosity</b> is a car-sized ",L("Mars")," rover operated by ",L("NASA")," as part of the Mars Science Laboratory mission. Launched on 26 November 2011, it landed in Gale Crater on 6 August 2012 using a daring rocket-powered 'sky crane' that lowered it on cables from a hovering descent stage — a sequence dubbed the 'seven minutes of terror'."]),
 ("p",["Powered by a plutonium radioisotope generator, Curiosity carries ten science instruments including cameras, spectrometers, a drill and an onboard chemistry laboratory. It has shown that Gale Crater once held a freshwater lake with conditions suitable for microbial life, found organic molecules in ancient rocks, and measured radiation levels relevant to future human missions. The rover has spent years climbing Mount Sharp, reading the layered record of Mars's changing climate in its rocks."]),
], ["Distance driven and sample counts omitted as they grow steadily; stated generally."])

# ---------------- Perseverance rover ----------------
build("Perseverance_(rover)", "Perseverance (rover)", [
 ("thumb","perseverance-landing","The Perseverance rover hanging beneath its sky crane seconds before touchdown in Jezero Crater, dust swirling","Perseverance descending on the sky crane, February 2021."),
 ("p",["<b>Perseverance</b> is a ",L("NASA")," Mars rover launched on 30 July 2020 and landed in Jezero Crater on 18 February 2021 as the centrepiece of the Mars 2020 mission. Based on the ",L("Curiosity_(rover)","Curiosity")," design, it carries improved wheels, cameras and instruments to search for signs of ancient microbial life in a crater that once held a lake and river delta."]),
 ("p",["Perseverance is the first leg of a planned Mars sample return: it seals drilled rock cores in titanium tubes for potential pickup by later missions. Its MOXIE experiment produced oxygen from the carbon-dioxide atmosphere, and its companion, the ",L("Ingenuity_(helicopter)","Ingenuity")," helicopter, made the first powered flights on another planet — 72 flights between 2021 and 2024, far beyond its five-flight technology demonstration. The rover's landing was filmed in high definition by cameras on the spacecraft and descent stage."]),
], ["Sample return programme architecture has been under revision; described as 'planned'.",
    "Ingenuity flight count (72) as widely reported at end of mission."])

# ---------------- Space Shuttle program ----------------
build("Space_Shuttle_program", "Space Shuttle program", [
 ("thumb","shuttle-launch","Space Shuttle Columbia lifting off on STS-1 in April 1981, white orbiter mounted on a rust-orange external tank with two white boosters","STS-1: the first Space Shuttle launch, 12 April 1981."),
 ("p",["The <b>Space Shuttle program</b> was ",L("NASA"),"'s human spaceflight programme from 1981 to 2011, flying the world's first reusable orbital spacecraft. The shuttle system consisted of a winged orbiter with three main engines, fuelled by a large external tank and boosted by two solid rocket boosters. Five orbiters — Columbia, Challenger, Discovery, Atlantis and Endeavour — flew 135 missions."]),
 ("p",["Shuttles deployed and repaired satellites, most famously servicing the ",L("Hubble_Space_Telescope"),", carried the Spacelab laboratory, docked with ",L("Mir"),", and assembled most of the ",L("International_Space_Station"),". The programme lost two orbiters and fourteen astronauts: Challenger broke apart 73 seconds after launch in 1986, and Columbia disintegrated during re-entry in 2003. Both accidents grounded the fleet for years and reshaped NASA's safety culture."]),
 ("h2","Retirement"),
 ("p",["The final mission, STS-135 by Atlantis, landed on 21 July 2011. The surviving orbiters went on museum display, and the United States relied on Russian ",L("Soyuz_(spacecraft)","Soyuz")," spacecraft for crew transport until SpaceX's Crew Dragon entered service in 2020."]),
], ["Mission count (135) and accident summaries from memory."])

# ---------------- Challenger disaster ----------------
build("Space_Shuttle_Challenger_disaster", "Space Shuttle Challenger disaster", [
 ("thumb","challenger-breakup","The Space Shuttle Challenger breaking apart 73 seconds after launch, with branching white smoke trails against a blue sky","Challenger breaks up, 28 January 1986."),
 ("p",["On 28 January 1986 the ",L("Space_Shuttle")," Challenger broke apart 73 seconds after liftoff from ",L("Kennedy_Space_Center"),", killing all seven crew members: commander Dick Scobee, pilot Michael Smith, mission specialists Ellison Onizuka, Judith Resnik and Ronald McNair, payload specialist Gregory Jarvis, and Christa McAuliffe, a schoolteacher selected as the first participant in the Teacher in Space project."]),
 ("p",["The disaster was caused by the failure of O-ring seals in the right solid rocket booster, whose rubber had lost resilience in the unusually cold weather that morning — engineers at contractor Morton Thiokol had warned against launching in such cold, but were overruled. Hot gas burned through the booster joint, and the external tank collapsed, tearing the orbiter apart in the resulting aerodynamic forces; the crew cabin survived intact until ocean impact."]),
 ("h2","Aftermath"),
 ("p",["The Rogers Commission, whose members included ",L("Neil_Armstrong")," and ",L("Sally_Ride"),", exposed deep flaws in NASA's decision-making and safety culture. Physicist Richard Feynman's televised demonstration — dropping a piece of O-ring rubber in ice water to show it lost elasticity — became famous. The shuttle fleet was grounded for nearly three years, and the boosters were redesigned with a third O-ring and joint heaters."]),
], ["Timeline and commission details paraphrased from memory."])

# ---------------- Roscosmos ----------------
build("Roscosmos", "Roscosmos", [
 ("thumb","roscosmos-launch","A Russian Soyuz rocket launching from Baikonur Cosmodrome at dawn, white rocket with an orange flame plume over the Kazakh steppe","A Soyuz launch from Baikonur."),
 ("p",["<b>Roscosmos</b>, formally the Roscosmos State Corporation for Space Activities, is the state corporation responsible for space flights, cosmonautics programmes and aerospace research of the Russian Federation. It was formed in its current state-corporation form in 2015, succeeding the Russian Federal Space Agency founded in 1992 after the dissolution of the Soviet Union."]),
 ("p",["Roscosmos operates Russia's human spaceflight programme, flying ",L("Soyuz_(spacecraft)","Soyuz")," crew vehicles and Progress cargo ships to the ",L("International_Space_Station")," from ",L("Baikonur_Cosmodrome")," in Kazakhstan, which Russia leases. It also manages the GLONASS navigation system and launches from Plesetsk and the newer Vostochny Cosmodrome in the Russian Far East. Russia's role in the ISS partnership has been strained since 2022 by geopolitical tensions following the invasion of Ukraine, though station operations have continued cooperatively."]),
], ["Organisational history summarised; current programme status described in general terms."])

# ---------------- JAXA ----------------
build("JAXA", "JAXA", [
 ("thumb","hayabusa2","Japan's Hayabusa2 spacecraft approaching the dark, rubble-covered asteroid Ryugu","Hayabusa2 at asteroid Ryugu (artist's impression)."),
 ("p",["<b>JAXA</b>, the Japan Aerospace Exploration Agency, is Japan's national space agency, formed on 1 October 2003 by merging three earlier aerospace organisations. Headquartered in Chōfu, Tokyo, JAXA conducts satellite launches, space science, aeronautical research and Japan's contributions to human spaceflight."]),
 ("p",["JAXA is known for ambitious small-body missions: Hayabusa, the first spacecraft to return a sample from an asteroid (Itokawa, 2010), and Hayabusa2, which returned samples of asteroid Ryugu in 2020. Its Kibo module is the largest single module of the ",L("International_Space_Station"),", and Japanese astronauts fly regularly to the station. JAXA launches from the Tanegashima Space Center on H3 and earlier H-II rockets, operates the SLIM lunar lander that achieved a pinpoint Moon landing in 2024, and is a partner in the ",L("Artemis_program"),"."]),
], ["SLIM landing outcome described briefly; module-size claim ('largest single module') as commonly stated."])

# ---------------- Kennedy Space Center ----------------
build("Kennedy_Space_Center", "Kennedy Space Center", [
 ("thumb","ksc-vab","The enormous Vehicle Assembly Building at Kennedy Space Center, with the American flag and blue NASA roundel on its side","The Vehicle Assembly Building, Kennedy Space Center."),
 ("p",["<b>Kennedy Space Center</b> (KSC) is one of ",L("NASA"),"'s ten field centres and, since 1968, the primary launch site for American human spaceflight. Located on Merritt Island, Florida, next to the Air Force's Cape Canaveral launch range, it is named for President John F. Kennedy, who set the goal of landing on the Moon."]),
 ("p",["KSC's Launch Complex 39 was built for the ",L("Saturn_V"),": its Vehicle Assembly Building — one of the largest buildings in the world by volume — stacked Apollo, Skylab, every ",L("Space_Shuttle")," and now assembles the ",L("Space_Launch_System")," for ",L("Artemis_program")," missions. Pad 39A, from which ",L("Apollo_11")," departed, is leased to SpaceX for ",L("Falcon_9")," and Falcon Heavy launches. The centre sits within a wildlife refuge, and launches share the island with alligators, manatees and migratory birds."]),
], ["'Largest by volume' claim for the VAB is the standard description from memory."])

for q in ["Voyager_program","Golden_Record","Galileo_probe","Mars_Science_Laboratory","MOXIE",
          "Richard_Feynman","Morton_Thiokol","Teacher_in_Space","GLONASS","Vostochny_Cosmodrome",
          "Tanegashima_Space_Center","Kibo_(ISS_module)","Cape_Canaveral_Space_Force_Station","Progress_(spacecraft)"]:
    queue(q, "Voyager_2")
print("batch4 done")
