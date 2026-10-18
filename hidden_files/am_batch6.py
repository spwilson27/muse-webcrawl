import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl/hidden_files")
from build_am import build, queue, L

# ---------------- Columbia disaster ----------------
build("Space_Shuttle_Columbia_disaster", "Space Shuttle Columbia disaster", [
 ("thumb","columbia-launch","Space Shuttle Columbia lifting off on STS-107, the flight on which foam debris struck its wing","Columbia launches on STS-107, 16 January 2003."),
 ("p",["The <b>Space Shuttle Columbia disaster</b> occurred on 1 February 2003, when the orbiter Columbia disintegrated as it re-entered the atmosphere over Texas at the end of mission STS-107, killing all seven crew members: Rick Husband, William McCool, Michael Anderson, Kalpana Chawla, David Brown, Laurel Clark and Ilan Ramon, the first Israeli astronaut."]),
 ("p",["The cause was damage during launch eighty-two seconds after liftoff, when a piece of insulating foam broke off the external tank and struck the leading edge of the left wing, punching a hole in its reinforced carbon-carbon heat shield. During ",L("Atmospheric_entry","re-entry")," superheated gas entered the wing, melting its internal structure until the orbiter broke apart. Engineers who reviewed launch imagery during the mission suspected damage but their requests for spy-satellite inspection were not acted on by management — a failure the Columbia Accident Investigation Board compared to the organisational causes of the Challenger disaster."]),
 ("h2","Aftermath"),
 ("p",["The ",L("Space_Shuttle")," fleet was grounded for more than two years. The investigation led to on-orbit inspection and repair procedures, the stationing of a rescue shuttle for Hubble missions, and ultimately the decision to retire the shuttle after completing the ",L("International_Space_Station")," in 2011."]),
], ["Crew and timeline details from memory; foam strike timing (81.7 s) rounded."])

# ---------------- Sergei Korolev ----------------
build("Sergei_Korolev", "Sergei Korolev", [
 ("thumb","korolev","A black-and-white photograph of Sergei Korolev in a suit, the anonymous 'Chief Designer' of the Soviet space programme","Korolev, whose identity was a state secret until his death."),
 ("p",["<b>Sergei Pavlovich Korolev</b> (12 January 1907 – 14 January 1966) was the lead Soviet rocket engineer and spacecraft designer during the ",L("Space_Race"),". As head of the OKB-1 design bureau he was the mastermind behind the R-7 rocket — the world's first intercontinental ballistic missile and the ancestor of the Soyuz launcher family — and the programme that launched Sputnik 1, ",L("Laika"),", and ",L("Yuri_Gagarin"),"."]),
 ("p",["Korolev's identity was a state secret: publicly he was known only as the 'Chief Designer', and his name was revealed only after his death. In the 1930s he had been arrested during the Great Purge and spent years in prison and a sharashka design bureau. His early death during surgery in 1966, amid the Soviet effort to beat America to the Moon, is often seen as a turning point after which the Soviet lunar programme faltered. The town near Moscow that hosts Russia's mission control is now named Korolyov in his honour."]),
], ["Biographical dates from memory; 'turning point' assessment is the standard historical judgement."])

# ---------------- Goddard ----------------
build("Robert_H._Goddard", "Robert H. Goddard", [
 ("thumb","goddard-rocket","Robert Goddard standing beside his first liquid-fuelled rocket on a launch frame in Auburn, Massachusetts, 1926","Goddard with the first liquid-fuel rocket, 1926."),
 ("p",["<b>Robert Hutchings Goddard</b> (5 October 1882 – 10 August 1945) was an American engineer, professor and inventor credited with creating the first liquid-fuelled rocket. A physics professor at Clark University, he published his visionary 1919 monograph 'A Method of Reaching Extreme Altitudes', which was ridiculed by some newspapers for suggesting a rocket could work in the vacuum of space."]),
 ("p",["On 16 March 1926, at his aunt's farm in Auburn, Massachusetts, Goddard launched the first liquid-fuelled rocket: it flew for 2.5 seconds and rose 12.5 metres. Working with little funding — later supported by the Guggenheim family and championed by aviator Charles Lindbergh — he moved his tests to Roswell, New Mexico, and developed gyroscopic control, steerable thrust and multistage concepts that German rocketeers later used in the V-2. Under-recognised in life, he is now honoured alongside ",L("Konstantin_Tsiolkovsky")," as a founder of modern rocketry; NASA's Goddard Space Flight Center bears his name."]),
], ["First-flight figures (2.5 s, 41 ft) are the standard cited values."])

# ---------------- Sputnik 2 ----------------
build("Sputnik_2", "Sputnik 2", [
 ("thumb","sputnik2-model","A model of Sputnik 2, a conical satellite with the spherical cabin compartment for Laika at its front","Sputnik 2 (model)."),
 ("p",["<b>Sputnik 2</b> was the second spacecraft launched into Earth orbit, on 3 November 1957, a month after Sputnik 1. The 508 kg satellite carried the dog ",L("Laika")," — the first living creature to orbit the Earth — in a pressurised cabin with a life-support system, food and instruments to measure the effects of spaceflight on a living organism."]),
 ("p",["The mission was assembled in roughly four weeks on Nikita Khrushchev's demand for another spectacular flight near the anniversary of the October Revolution. Sputnik 2 did not separate from its rocket core, and a thermal control failure caused the cabin to overheat; Laika died within hours, though this was concealed for decades. The satellite re-entered and burned up on 14 April 1958 after 162 days in orbit. It also carried instruments that detected the outer radiation belt, though its data could not be received over most of the Soviet Union and the discovery went largely uncredited."]),
], ["Mass (508.3 kg) and flight duration from memory."])

# ---------------- Explorer 1 ----------------
build("Explorer_1", "Explorer 1", [
 ("thumb","explorer1","Wernher von Braun, James Van Allen and William Pickering holding a model of Explorer 1 above their heads at a press conference, 1958","Explorer 1 is celebrated after its launch, February 1958."),
 ("p",["<b>Explorer 1</b> was the first satellite launched by the United States, and the third artificial satellite overall, following Sputnik 1 and 2. It was launched on 1 February 1958 (UTC) from Cape Canaveral by a Juno I rocket developed by ",L("Wernher_von_Braun"),"'s Army team, in America's answer to the Sputnik shock."]),
 ("p",["The pencil-shaped, 14 kg satellite carried a cosmic-ray detector designed by James Van Allen. Its readings revealed zones where counts dropped unexpectedly — evidence, once understood, of intense radiation trapped in Earth's magnetic field: the Van Allen radiation belts, the first major scientific discovery of the space age. Explorer 1 transmitted for about four months and stayed in orbit until 1970. The success led directly to the creation of ",L("NASA")," later in 1958."]),
], ["Launch date given in UTC (31 January local time in Florida); both dates appear in sources."])

# ---------------- Rocket engine ----------------
build("Rocket_engine", "Rocket engine", [
 ("thumb","rocket-engine-test","A rocket engine on a test stand firing at night, a brilliant Mach-diamond exhaust plume beneath the bell nozzle","A static test firing of a rocket engine."),
 ("p",["A <b>rocket engine</b> is a reaction engine that carries both its fuel and its oxidiser, producing thrust by expelling exhaust gases at high velocity — so it works in vacuum, unlike jet engines. By the ",L("Tsiolkovsky_rocket_equation"),", performance depends above all on exhaust velocity, measured for real engines as specific impulse in seconds."]),
 ("p",["Most large rockets burn liquid propellants: the ",L("Saturn_V"),"'s F-1 engines burned kerosene and liquid oxygen, while the ",L("Space_Shuttle"),"'s RS-25s and many upper stages burn liquid hydrogen and oxygen for higher efficiency at the cost of bulky tanks. Solid rocket motors — simple, powerful and storable, like the shuttle's boosters — cannot be throttled or shut down once lit. Newer engines such as SpaceX's Raptor burn methane, which can in principle be manufactured on ",L("Mars"),". Electric propulsion, such as the ",L("Ion_thruster"),", produces tiny thrust with extreme efficiency for deep-space cruise."]),
], ["Engine examples summarised; specific impulse figures omitted."])

# ---------------- Space debris ----------------
build("Space_debris", "Space debris", [
 ("thumb","debris-field","A visualisation of thousands of tracked debris objects as dots crowding low Earth orbit around the planet","Tracked objects in Earth orbit (visualisation)."),
 ("p",["<b>Space debris</b> (or space junk) consists of defunct human-made objects in orbit — dead satellites, spent rocket stages, fragments from explosions and collisions, and even tools lost on spacewalks. Tens of thousands of objects larger than 10 cm are tracked from the ground, and millions of smaller, untrackable fragments are estimated to exist, all moving at velocities where even a fleck of paint can damage a spacecraft."]),
 ("p",["The debris population grew sharply with the 2007 Chinese anti-satellite test that destroyed the FengYun-1C satellite, and the 2009 collision between Iridium 33 and the dead Kosmos 2251 — together creating thousands of new fragments. The ",L("International_Space_Station")," periodically manoeuvres to dodge tracked debris, and crews have sheltered in their return vehicles during close passes. The feared runaway scenario, in which collisions breed fragments that breed more collisions, is called the Kessler syndrome. Proposed remedies range from stricter disposal rules to active removal missions that grapple or harpoon dead satellites."]),
], ["Tracked-object counts change constantly; stated qualitatively."])

# ---------------- Ion thruster ----------------
build("Ion_thruster", "Ion thruster", [
 ("thumb","ion-thruster-glow","An ion thruster firing in a vacuum chamber, emitting a faint blue beam of ionised xenon","An ion engine under test, glowing blue."),
 ("p",["An <b>ion thruster</b> is a form of electric spacecraft propulsion that ionises a propellant — usually xenon — and accelerates the ions through an electric field to extremely high exhaust velocities. The thrust produced is tiny, comparable to the weight of a sheet of paper, but it can be sustained for months or years, gradually accumulating very large ",L("Delta-v")," with a fraction of the propellant a chemical rocket would need."]),
 ("p",["Ion propulsion powered ",L("NASA"),"'s Deep Space 1 technology demonstrator (1998) and the Dawn mission, which used its ion engine to orbit two different worlds, the asteroids Vesta and Ceres — something no chemical spacecraft could have done. Japan's Hayabusa probes also used ion engines. Gridded ion thrusters and Hall-effect thrusters are now standard for station-keeping on many satellites, and are planned for elements of the Lunar Gateway station."]),
], ["Dawn's Vesta/Ceres itinerary summarised; thrust analogy is the commonly used one."])

# ---------------- Geostationary orbit ----------------
build("Geostationary_orbit", "Geostationary orbit", [
 ("thumb","geo-belt","A diagram of the geostationary belt: a thin ring of satellites 35,786 km above the equator","The geostationary ring (not to scale)."),
 ("p",["A <b>geostationary orbit</b> (GEO) is a circular orbit 35,786 km above Earth's equator in which a satellite's orbital period exactly matches Earth's rotation, so the satellite appears fixed in the sky. Fixed ground antennas can therefore point at it permanently, making GEO the home of most communications and many weather satellites. The concept was popularised by science-fiction writer Arthur C. Clarke in 1945, and the ring is sometimes called the Clarke Belt."]),
 ("p",["Slots in the belt are allocated internationally because satellites must be spaced to avoid interference and collision. At the end of their lives, GEO satellites are required to boost themselves a few hundred kilometres higher into a 'graveyard orbit' rather than polluting the working ring. Reaching GEO costs far more ",L("Delta-v")," than ",L("Low_Earth_orbit"),", so satellites often travel via an elliptical geostationary transfer orbit and circularise with their own engines."]),
], ["Altitude and graveyard-orbit figures are the standard values from memory."])

for q in ["V-2_rocket","Kessler_syndrome","Arthur_C._Clarke","Graveyard_orbit","Dawn_(spacecraft)",
          "Deep_Space_1","Hall-effect_thruster","F-1_(rocket_engine)","Vostochny_Cosmodrome",
          "Apollo_10","Apollo_7","Apollo_1"]:
    queue(q, "Space_Shuttle_Columbia_disaster")
print("batch6 done")
