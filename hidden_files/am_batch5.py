import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl/hidden_files")
from build_am import build, queue, L

# ---------------- Tsiolkovsky ----------------
build("Konstantin_Tsiolkovsky", "Konstantin Tsiolkovsky", [
 ("thumb","tsiolkovsky-portrait","A portrait photograph of Konstantin Tsiolkovsky, bearded, in his later years in Kaluga","Tsiolkovsky in the 1920s–30s."),
 ("p",["<b>Konstantin Eduardovich Tsiolkovsky</b> (17 September 1857 – 19 September 1935) was a Russian and Soviet rocket scientist and pioneer of astronautics. Largely self-taught and working as a provincial schoolteacher in Kaluga, he derived the fundamental mathematics of rocket flight decades before practical rockets existed."]),
 ("p",["In 1903 Tsiolkovsky published 'Exploration of the World of Space by Reactive Devices', which contained the ",L("Tsiolkovsky_rocket_equation")," relating a rocket's velocity change to its exhaust velocity and mass ratio. He went on to describe multistage rockets, liquid hydrogen and oxygen propellants, space stations with rotating sections for artificial gravity, and colonies in space. His famous dictum holds that Earth is the cradle of humanity, but that one cannot live in a cradle forever. Deaf from childhood illness, he built many of his ideas in isolation; his work was little known in the West until the space age, but he is honoured as one of the three founding fathers of rocketry, alongside ",L("Robert_H._Goddard")," and Hermann Oberth."]),
], ["The 'cradle' quotation is widely attributed and paraphrased here."])

# ---------------- Tsiolkovsky rocket equation ----------------
build("Tsiolkovsky_rocket_equation", "Tsiolkovsky rocket equation", [
 ("thumb","rocket-equation","The rocket equation written as delta-v equals exhaust velocity times the natural logarithm of the mass ratio","Δv = vₑ ln(m₀/m_f)."),
 ("p",["The <b>Tsiolkovsky rocket equation</b>, also called the ideal rocket equation, describes the motion of a rocket: the maximum change in velocity (",L("Delta-v"),") equals the effective exhaust velocity multiplied by the natural logarithm of the ratio of the rocket's initial mass (including propellant) to its final mass. It was derived independently by ",L("Konstantin_Tsiolkovsky")," (published 1903) and others."]),
 ("p",["The equation's logarithm is the source of the 'tyranny of the rocket equation': because the ratio grows exponentially, reaching high delta-v demands that almost all of a rocket's mass be propellant. Doubling the delta-v does not double the fuel needed — it squares the mass ratio. This is why rockets are mostly fuel tank, why staging (discarding empty tanks en route, as on the ",L("Saturn_V"),") is so valuable, and why high exhaust velocity — efficient engines such as the ",L("Ion_thruster")," — matters more than raw thrust for deep-space missions."]),
], ["Historical derivation credits (also William Moore, 1810s) noted only generally."])

# ---------------- von Braun ----------------
build("Wernher_von_Braun", "Wernher von Braun", [
 ("thumb","vonbraun-saturn","Wernher von Braun standing in front of the five F-1 engines of a Saturn V first stage","Von Braun at the base of a Saturn V."),
 ("p",["<b>Wernher Magnus Maximilian Freiherr von Braun</b> (23 March 1912 – 16 June 1977) was a German-American aerospace engineer and the leading figure in the development of rocket technology in Nazi Germany and then the United States."]),
 ("p",["As technical director of the German Army's rocket programme at Peenemünde, von Braun led the team that created the V-2, the world's first long-range ballistic missile, built with concentration-camp labour under murderous conditions — a legacy that permanently shadows his reputation. Surrendering to American forces in 1945, he and much of his team were brought to the United States under Operation Paperclip. There he directed the team that launched America's first satellite, Explorer 1, in 1958, and then, as first director of ",L("NASA"),"'s Marshall Space Flight Center, led development of the ",L("Saturn_V")," that carried ",L("Apollo_11")," to the Moon."]),
 ("h2","Later career"),
 ("p",["After Apollo, von Braun advocateded crewed Mars missions without success, left NASA in 1972 for industry, and died of cancer in 1977 at age 65."]),
], ["V-2 production death toll (often cited as exceeding deaths from V-2 attacks) not quantified here."])

# ---------------- Laika ----------------
build("Laika", "Laika", [
 ("thumb","laika","Laika, a small black-and-white mongrel dog, fitted in her harness inside the Sputnik 2 capsule","Laika in her flight harness, 1957."),
 ("p",["<b>Laika</b> was a Soviet space dog who became the first animal to orbit Earth, aboard ",L("Sputnik_2")," on 3 November 1957. A stray mongrel from the streets of Moscow, probably about three years old, she was chosen because Soviet scientists believed stray dogs, hardened by hunger and cold, would cope best with the ordeal."]),
 ("p",["Laika's flight proved a living passenger could survive launch and weightlessness, paving the way for human spaceflight — but there was never a plan to bring her home, as the technology for safe re-entry did not yet exist for her capsule. For decades the Soviet account said she survived several days and was euthanised; in 2002 it was revealed she most likely died within hours, from overheating after a thermal control failure. Her sacrifice is commemorated by statues in Moscow, and her name became a byword for the animals who died in early space research."]),
], ["Exact time and cause of death reflect the 2002 disclosures as commonly reported."])

# ---------------- Salyut 1 ----------------
build("Salyut_1", "Salyut 1", [
 ("thumb","salyut1","The Salyut 1 space station in orbit: a stepped cylinder with three solar panel wings and a docked Soyuz","Salyut 1 with a docked Soyuz spacecraft."),
 ("p",["<b>Salyut 1</b> was the world's first space station, launched by the Soviet Union on 19 April 1971. Derived from the military Almaz station programme, the 20-metre, roughly 18-tonne station carried telescopes and cameras for Earth observation and astronomy, and was designed for crews of three arriving by ",L("Soyuz_(spacecraft)","Soyuz")," ferries."]),
 ("p",["The first crew, aboard Soyuz 10, reached the station but could not dock properly and returned after two days. The second crew — Georgy Dobrovolsky, Vladislav Volkov and Viktor Patsayev, on Soyuz 11 — lived aboard for 23 days, setting an endurance record. During their return on 30 June 1971 a ventilation valve opened prematurely in the descent module, the cabin air escaped, and all three cosmonauts died of asphyxiation — the only human deaths in space itself. Salyut 1 was deorbited in October 1971 after 175 days."]),
], ["Mass and length figures approximate from memory."])

# ---------------- Low Earth orbit ----------------
build("Low_Earth_orbit", "Low Earth orbit", [
 ("thumb","leo-diagram","A diagram showing low Earth orbit as a band around Earth, with the ISS, Hubble and satellite constellations within it","Low Earth orbit occupies the first 2,000 km above Earth."),
 ("p",["A <b>low Earth orbit</b> (LEO) is an orbit around Earth with an altitude of 2,000 km or less — roughly the lowest third of the region of space around the planet. Most human spaceflight takes place in LEO: the ",L("International_Space_Station")," circles at about 400 km, completing an orbit every 93 minutes or so, and crews there are partly protected by Earth's magnetosphere from radiation."]),
 ("p",["LEO is favoured because it takes the least energy to reach, offers low communications latency and high-resolution Earth imaging, and allows heavy payloads. It hosts most Earth-observation and weather satellites, the Hubble Space Telescope, and mega-constellations such as ",L("Starlink"),". Its drawbacks are rapid orbital decay from atmospheric drag below about 600 km, and a growing ",L("Space_debris")," problem that raises collision risks for everything there. Higher regimes include medium Earth orbit (used by navigation satellites) and ",L("Geostationary_orbit")," at 35,786 km."]),
], ["ISS period/altitude figures approximate and vary slightly."])

# ---------------- Delta-v ----------------
build("Delta-v", "Delta-v", [
 ("thumb","deltav-map","A stylised delta-v map of the Solar System, showing the velocity changes needed between planets and moons","Delta-v requirements across the Solar System (schematic)."),
 ("p",["<b>Delta-v</b> (Δv, 'change in velocity') is the measure of the impulse a spacecraft can deliver — in effect, how much it can change its own trajectory. Expressed in metres or kilometres per second, it is the fundamental budget of spaceflight: every manoeuvre, from reaching orbit to landing on the Moon, 'costs' delta-v, and a mission is feasible only if its spacecraft carries enough."]),
 ("p",["Reaching low Earth orbit from the surface costs about 9.4 km/s of delta-v (including gravity and drag losses); going from there to the lunar surface and back needs roughly another 9 km/s, more than the trip to orbit itself. Delta-v is set by the ",L("Tsiolkovsky_rocket_equation"),": the ratio of propellant to spacecraft mass and the efficiency of the engine. Mission planners draw delta-v maps of the Solar System — with stops at Lagrange points and aerobraking shortcuts — much as sailors once charted winds."]),
], ["Delta-v figures are standard textbook approximations from memory."])

# ---------------- Gravity assist ----------------
build("Gravity_assist", "Gravity assist", [
 ("thumb","gravity-assist","A spacecraft swinging around a planet and leaving on a new trajectory with greater speed relative to the Sun","A gravity assist: the spacecraft trades momentum with the planet."),
 ("p",["A <b>gravity assist</b> (or slingshot) is a manoeuvre in which a spacecraft flies close by a planet and uses its gravity to change speed and direction without burning fuel. Passing behind the planet in its orbit adds some of the planet's orbital momentum to the spacecraft; passing in front removes it. The planet's own velocity changes by an immeasurably small amount in exchange."]),
 ("p",["Gravity assists made the outer Solar System reachable: ",L("Voyager_2")," used a rare alignment to tour all four giant planets, ",L("Galileo_(spacecraft)","Galileo")," looped past Venus and Earth twice to reach Jupiter, and ",L("Cassini-Huygens")," used four assists on its way to Saturn. The technique also works in reverse — to slow down — as when MESSENGER shed energy to fall into orbit around Mercury, and it can change a trajectory's plane, as when ",L("Ulysses_(spacecraft)","Ulysses")," swung over Jupiter's poles to study the Sun's."]),
], ["Ulysses is linked here but not yet built; logged queued in this shard."])

# ---------------- Baikonur ----------------
build("Baikonur_Cosmodrome", "Baikonur Cosmodrome", [
 ("thumb","baikonur-pad","The Baikonur launch pad known as Gagarin's Start, with a Soyuz rocket erected amid service towers on the flat Kazakh steppe","Gagarin's Start at Baikonur."),
 ("p",["The <b>Baikonur Cosmodrome</b> is the world's first and largest space launch facility, built by the Soviet Union in the 1950s on the steppe of Kazakhstan. From its pads were launched Sputnik 1, the first satellite, in 1957, and ",L("Vostok_1")," carrying ",L("Yuri_Gagarin")," in 1961. After the Soviet collapse the site found itself in independent Kazakhstan; Russia leases it — an arrangement currently running to 2050 — and it remains the launch site for all Russian crewed ",L("Soyuz_(spacecraft)","Soyuz")," missions."]),
 ("p",["The cosmodrome sprawls over some 6,700 square kilometres around the closed city of Baikonur (formerly Leninsk), which flies the Russian flag and uses the rouble. Its most storied pad, Site 1/5, is 'Gagarin's Start', from which every Soviet and Russian human spaceflight began for decades. Baikonur's inland location means spent rocket stages fall on the steppe, and its latitude of about 46°N is less favourable for equatorial launches than coastal sites — costs Russia accepted for secrecy and safety when the site was chosen."]),
], ["Lease end date (2050) and site area are as commonly reported from memory."])

# ---------------- Starlink (promote from queue) ----------------
build("Starlink", "Starlink", [
 ("thumb","starlink-train","A train of newly launched Starlink satellites crossing the night sky in a line of bright dots","A Starlink 'train' shortly after deployment."),
 ("p",["<b>Starlink</b> is a satellite internet constellation operated by Starlink Services, a subsidiary of ",L("SpaceX"),". Thousands of small satellites in ",L("Low_Earth_orbit"),", at about 550 km altitude, relay traffic between user terminals and ground stations, providing broadband internet across most of the Earth, including remote and maritime areas poorly served by terrestrial networks."]),
 ("p",["The first operational satellites launched in May 2019 aboard a ",L("Falcon_9"),", and the constellation has grown to several thousand satellites — the largest ever deployed — launched in batches that appear after deployment as a 'train' of bright lights in the twilight sky. Astronomers have criticised the satellites' brightness for interfering with observations, prompting SpaceX to add sunshades and darker coatings, while regulators have raised concerns about collision risk and orbital debris. Starlink terminals became strategically significant after 2022 as communications infrastructure in Ukraine during the war there."]),
], ["Satellite count changes with every launch; stated as 'several thousand'."])

for q in ["Robert_H._Goddard","Hermann_Oberth","Operation_Paperclip","Explorer_1","Almaz",
          "Soyuz_11","Geostationary_orbit","Ion_thruster","Ulysses_(spacecraft)","MESSENGER",
          "Space_debris","V-2_rocket","Marshall_Space_Flight_Center"]:
    queue(q, "Konstantin_Tsiolkovsky")
print("batch5 done")
