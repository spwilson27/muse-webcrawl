import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl/hidden_files")
from build_am import build, queue, L

# ---------------- Space station ----------------
build("Space_station", "Space station", [
 ("thumb","station-comparison","A diagram comparing historical space stations: Salyut, Skylab, Mir, the ISS and Tiangong at the same scale","Space stations compared to scale."),
 ("p",["A <b>space station</b> is a spacecraft in orbit that can support a human crew for extended periods, with docking ports for visiting vehicles but no major propulsion or landing capability of its own. Stations serve as laboratories for research in microgravity, Earth observation and technology development, and as waypoints for exploration."]),
 ("p",["The Soviet Union launched the first station, ",L("Salyut_1"),", in 1971. The United States followed with ",L("Skylab")," in 1973. The modular Soviet ",L("Mir")," station (1986–2001) pioneered long-duration stays and international visits. The ",L("International_Space_Station"),", assembled from 1998 by five space agencies, is the largest structure ever built in orbit and has been continuously occupied since November 2000. China's ",L("Tiangong_space_station","Tiangong station")," was completed in 2022."]),
 ("h2","Design"),
 ("p",["Stations are either monolithic — launched in one piece, like Salyut and Skylab — or modular, assembled in orbit from separately launched sections, like Mir, the ISS and Tiangong. All rely on visiting spacecraft for crew rotation and resupply, on solar arrays for power, and on periodic reboosts to counter orbital decay. Several commercial stations are in development to succeed the ISS in the 2030s."]),
], ["Commercial station names/dates omitted as fast-moving; general statement only."])

# ---------------- Mir ----------------
build("Mir", "Mir", [
 ("thumb","mir-orbit","The Mir space station in orbit in 1998, its modules and solar arrays arranged around the core, photographed from a visiting shuttle","Mir seen from Space Shuttle Atlantis, 1998."),
 ("p",["<b>Mir</b> was a modular space station operated by the Soviet Union and then Russia in low Earth orbit from 1986 to 2001. Its name means 'peace' and also 'world' or 'village' in Russian. Mir was the first modular station, assembled over ten years from a core module and six specialised modules including Kvant, Kristall, Spektr and Priroda, and it hosted a near-continuous human presence for a decade."]),
 ("p",["Mir was the platform for many endurance records: Valeri Polyakov spent 437 consecutive days aboard in 1994–95, still the longest single spaceflight. In the 1990s the Shuttle–Mir programme brought American astronauts to the station as preparation for the ",L("International_Space_Station"),". The station's later years were marked by accidents, including a fire and a collision with a Progress cargo ship in 1997 that punctured the Spektr module."]),
 ("h2","Deorbit"),
 ("p",["Funding shortages and the shift of Russian resources to the ISS led to Mir's controlled deorbit on 23 March 2001. The station broke up over the South Pacific, ending fifteen years in orbit during which it had circled the Earth more than 86,000 times."]),
], ["Orbit count and Polyakov record dates are from memory and approximate."])

# ---------------- Skylab ----------------
build("Skylab", "Skylab", [
 ("thumb","skylab-orbit","Skylab in orbit in 1973 with its improvised gold sunshade deployed over the damaged workshop","Skylab with its parasol sunshade, 1973."),
 ("p",["<b>Skylab</b> was the first space station launched and operated by ",L("NASA"),". Built from a converted upper stage of the ",L("Saturn_V")," rocket, it was launched on 14 May 1973 and occupied by three successive three-person crews between 1973 and 1974, for a total of 171 days."]),
 ("p",["The station was damaged during launch: its micrometeoroid shield tore away, taking one solar array with it and jamming the other. The first crew saved the station by deploying a parasol sunshade through a scientific airlock to cool the overheating workshop, and later freed the jammed array during a spacewalk. Skylab crews conducted extensive solar astronomy, Earth observation and medical experiments, proving that humans could live and work in space for months."]),
 ("h2","Re-entry"),
 ("p",["With the ",L("Space_Shuttle")," delayed, Skylab's orbit decayed and it re-entered the atmosphere on 11 July 1979, scattering debris across the Indian Ocean and sparsely populated Western Australia. The incident drew worldwide attention and a tongue-in-cheek littering fine from the shire of Esperance, paid decades later by a radio listener fundraiser."]),
], ["Esperance fine anecdote as commonly told; the amount is not stated."])

# ---------------- Tiangong ----------------
build("Tiangong_space_station", "Tiangong space station", [
 ("thumb","tiangong-orbit","China's Tiangong space station in orbit: the Tianhe core module with Tianzhou cargo ships and large rotating solar wings","The completed Tiangong station configuration."),
 ("p",["The <b>Tiangong space station</b> is a modular Chinese space station in low Earth orbit, operated by the China Manned Space Agency. Its name means 'heavenly palace'. The station was assembled between 2021 and 2022 from three modules: the Tianhe core module, and the Wentian and Mengtian laboratory modules, forming a T-shaped complex of about 55 metres across its solar wings."]),
 ("p",["Tiangong has been continuously crewed since 2021 by rotating three-person Shenzhou crews on roughly six-month missions. It is China's third-generation station, following the Tiangong-1 and Tiangong-2 prototype laboratories, and it makes China the second nation to operate a permanent modular station, after the partners of the ",L("International_Space_Station"),". The station is planned to expand with additional modules and to host the Xuntian space telescope flying in formation nearby."]),
], ["Station mass and dimensions are approximate from memory; expansion plans described generally."])

# ---------------- Soyuz spacecraft ----------------
build("Soyuz_(spacecraft)", "Soyuz (spacecraft)", [
 ("thumb","soyuz-docked","A Soyuz spacecraft approaching the International Space Station, showing its green orbital module, bell-shaped descent module and two solar wings","Soyuz MS approaching the ISS."),
 ("p",["<b>Soyuz</b> is a series of Soviet and Russian spacecraft designed by the Korolev design bureau in the 1960s. First flown in 1966 and crewed from 1967, it has become the longest-serving and most-flown crewed spacecraft design in history, and for a decade after the ",L("Space_Shuttle"),"'s retirement in 2011 it was the only vehicle carrying crews to the ",L("International_Space_Station"),"."]),
 ("p",["The spacecraft has three parts: a spherical orbital module at the front, a bell-shaped descent module in the middle — the only section that returns through the atmosphere — and a cylindrical service module with solar panels at the rear. Soyuz launches on the Soyuz rocket from ",L("Baikonur_Cosmodrome")," in Kazakhstan, leased by Russia, and lands under parachutes on the Kazakh steppe, using small rockets to soften the touchdown."]),
 ("h2","History"),
 ("p",["The programme suffered two fatal accidents early on: Soyuz 1 in 1967, which killed Vladimir Komarov, and Soyuz 11 in 1971, whose three-man crew died from a cabin depressurisation — the only deaths to have occurred above the Kármán line. Since then the design has flown for decades without a fatality, through versions including Soyuz-T, Soyuz-TM, Soyuz-TMA and the current Soyuz MS."]),
], ["Flight totals omitted as they change with every mission; design description from memory."])

# ---------------- Falcon 9 ----------------
build("Falcon_9", "Falcon 9", [
 ("thumb","falcon9-landing","A Falcon 9 first stage returning to land vertically on a drone ship at sea, engine firing","Falcon 9 booster landing on a drone ship."),
 ("p",["<b>Falcon 9</b> is a partially reusable two-stage medium-lift launch vehicle designed and manufactured by ",L("SpaceX"),". Named for its nine Merlin engines on the first stage, it first flew in 2010 and has become the most frequently launched rocket in the world, carrying satellites, cargo and crews to orbit."]),
 ("p",["In December 2015 a Falcon 9 first stage landed vertically at Cape Canaveral — the first time an orbital-class booster had been recovered — and ship-based landings on autonomous drone ships followed in 2016. Reflight of recovered boosters, once considered impractical, became routine; individual boosters have flown more than twenty times. The current Block 5 version, introduced in 2018, carries SpaceX's Dragon spacecraft to the ",L("International_Space_Station")," and deploys the ",L("Starlink")," satellite constellation in batches."]),
 ("h2","Variants"),
 ("p",["Falcon Heavy, first flown in 2018, straps three Falcon 9 cores together for heavy payloads. Falcon 9's reliability and low cost — driven by reusability and high flight rate — reshaped the global launch industry and pushed competitors toward reusable designs of their own."]),
], ["Booster flight-count records change frequently; stated as 'more than twenty'.",
    "Launch totals omitted deliberately as they date quickly."])

# ---------------- Starship ----------------
build("SpaceX_Starship", "SpaceX Starship", [
 ("thumb","starship-launch","SpaceX Starship lifting off from Starbase, Texas: the stainless-steel Starship vehicle atop the Super Heavy booster, a tower of flame below","Starship's integrated flight test from Starbase."),
 ("p",["<b>Starship</b> is a fully reusable super heavy-lift launch vehicle under development by ",L("SpaceX"),". The system consists of the Super Heavy booster, powered by 33 Raptor engines burning liquid methane and oxygen, and the Starship spacecraft itself, with six Raptors. At about 120 metres tall it is the largest and most powerful rocket ever flown."]),
 ("p",["Starship made its first integrated flight test in April 2023 from Starbase in Boca Chica, Texas; the vehicle was destroyed after stage separation failed. Subsequent tests achieved stage separation, orbital-velocity flight, a booster catch by the launch tower's 'chopstick' arms in October 2024, and ship landings in the Indian Ocean. ",L("NASA")," has selected a lunar variant of Starship as the human landing system for the ",L("Artemis_program"),"'s return to the Moon, and SpaceX intends the vehicle for cargo and crew missions to ",L("Mars"),"."]),
], ["Test-flight details up to the tower catch are as remembered; the programme is evolving rapidly and later outcomes may differ.",
    "Height figure varies slightly by version (121–124 m); stated as 'about 120 metres'."])

# ---------------- Lunar Module ----------------
build("Lunar_Module", "Apollo Lunar Module", [
 ("thumb","lunar-module","The Apollo Lunar Module in orbit around the Moon, a gold-foil-wrapped angular craft with four spindly legs","The Lunar Module Eagle in lunar orbit, Apollo 11."),
 ("p",["The <b>Apollo Lunar Module</b> (LM, pronounced 'lem') was the lunar lander spacecraft of the ",L("Apollo_program"),", built by Grumman. It carried two astronauts from lunar orbit to the surface of the Moon and back — the only crewed vehicle ever to operate beyond low Earth orbit as a standalone spacecraft, and the first true spaceship, designed never to fly in an atmosphere."]),
 ("p",["The ungainly, foil-covered craft had two parts: a descent stage with the engine and landing gear that stayed behind on the surface, and an ascent stage with the cramped crew cabin from which the astronauts stood to fly. Fifteen were built; ten flew in space. The most famous, Apollo 11's Eagle, landed in the Sea of Tranquility on 20 July 1969. In April 1970 ",L("Apollo_13"),"'s LM Aquarius served as a lifeboat that kept its crew alive after the service module explosion."]),
], ["Production numbers (15 built, 10 flown) from memory and may be off by one."])

for q in ["Salyut_1","Valeri_Polyakov","Shuttle–Mir_program","China_Manned_Space_Agency",
          "Shenzhou_(spacecraft)","Soyuz_(rocket_family)","Merlin_(rocket_engine)","Falcon_Heavy",
          "Raptor_(rocket_engine)","Grumman","Lunar_Roving_Vehicle","Starlink"]:
    queue(q, "Space_station")
print("batch2 done")
