import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl/hidden_files")
from build_am import build, queue, L

# ---------------- Buzz Aldrin ----------------
build("Buzz_Aldrin", "Buzz Aldrin", [
 ("thumb","aldrin-lunar","Buzz Aldrin descending the ladder of the Lunar Module Eagle to the lunar surface, July 1969","Aldrin climbing down to the lunar surface, photographed by Armstrong."),
 ("p",["<b>Buzz Aldrin</b> (born Edwin Eugene Aldrin Jr., 20 January 1930) is an American former astronaut, engineer and fighter pilot. Along with ",L("Neil_Armstrong"),", he was one of the first two humans to land on the Moon, as Lunar Module Pilot of ",L("Apollo_11")," on 20 July 1969. Minutes after Armstrong, he became the second person to walk on the lunar surface."]),
 ("p",["Aldrin flew combat missions in the Korean War and earned a doctorate in astronautics from MIT — his thesis on orbital rendezvous earned him the nickname 'Dr. Rendezvous'. Selected as an astronaut in 1963, he flew on Gemini 12 in 1966, performing spacewalks totalling more than five hours that proved astronauts could work effectively outside a spacecraft, a key step toward Apollo."]),
 ("h2","Later life"),
 ("p",["After Apollo 11 Aldrin struggled with depression and alcoholism, which he described candidly in memoirs. He became a prominent advocate for human exploration of ",L("Mars"),", promoting his 'Aldrin cycler' concept — a spacecraft on a perpetual orbit cycling between Earth and Mars. He is the last surviving crew member of Apollo 11."]),
], ["Korean War mission count and EVA durations are approximate from memory."])

# ---------------- Valentina Tereshkova ----------------
build("Valentina_Tereshkova", "Valentina Tereshkova", [
 ("thumb","tereshkova","Valentina Tereshkova in her spacesuit and helmet before the Vostok 6 flight, 1963","Tereshkova before launch, June 1963."),
 ("p",["<b>Valentina Vladimirovna Tereshkova</b> (born 6 March 1937) is a Russian engineer, politician and former cosmonaut. On 16 June 1963, aboard Vostok 6, she became the first woman to fly in space, completing 48 orbits of Earth in just under three days — more flight time in a single mission than all American astronauts combined up to that point."]),
 ("p",["Tereshkova was a textile factory worker and amateur parachutist when she was selected, partly for her proletarian background and skydiving experience, which mattered because Vostok pilots ejected and parachuted to the ground separately from the capsule. Her call sign was Chaika (Seagull). She remains the only woman to have flown a solo space mission, and the youngest woman in space at age 26."]),
 ("h2","After the flight"),
 ("p",["Tereshkova never flew again. She became a prominent public figure and politician, serving in the Soviet parliament and later in Russia's State Duma. Nearly twenty years passed before the second woman, Svetlana Savitskaya, flew in 1982; the first American woman, ",L("Sally_Ride"),", flew in 1983."]),
], ["The 'more flight time than all Americans combined' comparison is as commonly stated in accounts of the flight."])

# ---------------- Alexei Leonov ----------------
build("Alexei_Leonov", "Alexei Leonov", [
 ("thumb","leonov-spacewalk","Alexei Leonov floating outside the Voskhod 2 spacecraft during the first spacewalk, tethered, March 1965","Leonov during the first EVA, 18 March 1965."),
 ("p",["<b>Alexei Arkhipovich Leonov</b> (30 May 1934 – 11 October 2019) was a Soviet and Russian cosmonaut, Air Force general and artist. On 18 March 1965 he became the first human to conduct a spacewalk, exiting the Voskhod 2 spacecraft and floating in space for about twelve minutes at the end of a 5-metre tether."]),
 ("p",["The spacewalk nearly ended in disaster: Leonov's spacesuit ballooned in vacuum until he could not fit back through the airlock, and he had to bleed off pressure to squeeze inside. The mission's dangers continued — the automatic landing system failed and the crew landed manually, far off course in deep snow in the Urals, spending a night in the forest before rescue. A decade later Leonov commanded the Soviet half of the Apollo–Soyuz Test Project, the first joint US–Soviet mission, shaking hands in orbit with Thomas Stafford in July 1975."]),
 ("h2","Art and later life"),
 ("p",["Leonov was also an accomplished artist whose paintings of space, some created in orbit, were widely exhibited. He had been selected as the Soviet cosmonaut most likely to make the first crewed lunar flight before the Soviet Moon programme was cancelled."]),
], ["EVA duration is commonly given as 12 minutes 9 seconds; rounded here."])

# ---------------- John Glenn ----------------
build("John_Glenn", "John Glenn", [
 ("thumb","glenn-friendship7","John Glenn in his silver Mercury pressure suit beside the Friendship 7 capsule, 1962","Glenn and Friendship 7, 1962."),
 ("p",["<b>John Herschel Glenn Jr.</b> (18 July 1921 – 8 December 2016) was an American astronaut, Marine Corps fighter pilot and United States Senator. On 20 February 1962, aboard Friendship 7, he became the first American to orbit Earth, circling the planet three times during a flight of just under five hours in ",L("Project_Mercury"),"."]),
 ("p",["A decorated combat pilot of the Second World War and Korea, and a record-setting test pilot who made the first supersonic transcontinental flight across the United States in 1957, Glenn was one of the original Mercury Seven astronauts. During his orbital flight a telemetry signal falsely suggested his heat shield had come loose; controllers kept his retropack attached during re-entry as a precaution, and Glenn watched flaming debris — actually pieces of the retropack — stream past his window."]),
 ("h2","Senator and second flight"),
 ("p",["Glenn served as a Democratic senator from Ohio from 1974 to 1999. On 29 October 1998, at age 77, he flew aboard the ",L("Space_Shuttle")," Discovery on mission STS-95, becoming by far the oldest person to fly in space — a record he held until 2021. He remains the only person to have flown in both the Mercury and Shuttle programmes."]),
], ["Flight duration stated approximately ('just under five hours')."])

# ---------------- Alan Shepard ----------------
build("Alan_Shepard", "Alan Shepard", [
 ("thumb","shepard-launch","The Mercury-Redstone rocket carrying Alan Shepard lifting off on the first American crewed spaceflight, 5 May 1961","Freedom 7 lifts off, 5 May 1961."),
 ("p",["<b>Alan Bartlett Shepard Jr.</b> (18 November 1923 – 21 July 1998) was an American astronaut and naval aviator. On 5 May 1961, piloting the Freedom 7 spacecraft, he became the first American — and the second person, after ",L("Yuri_Gagarin")," — to travel into space. His Mercury-Redstone flight was a 15-minute suborbital hop reaching 187 km altitude."]),
 ("p",["Grounded for most of the 1960s by an inner-ear disorder (Ménière's disease), Shepard became chief of the Astronaut Office until an experimental operation restored him to flight status. He then commanded Apollo 14 in 1971, landing in the Fra Mauro highlands — the site originally targeted by ",L("Apollo_13")," — and famously hit two golf balls on the lunar surface with a makeshift club. He is the only Mercury Seven astronaut to walk on the Moon, and at 47 was the oldest person to do so."]),
 ("h2","Later life"),
 ("p",["Shepard retired from NASA and the Navy in 1974, became a successful businessman, and helped found the Mercury Seven Foundation (now the Astronaut Scholarship Foundation) to support science students."]),
], ["Flight altitude and duration are the commonly cited figures (116 miles / 15 minutes)."])

# ---------------- Sally Ride ----------------
build("Sally_Ride", "Sally Ride", [
 ("thumb","ride-challenger","Sally Ride aboard Space Shuttle Challenger during STS-7, floating at a control panel in 1983","Ride aboard Challenger, 1983."),
 ("p",["<b>Sally Kristen Ride</b> (26 May 1951 – 23 July 2012) was an American physicist and astronaut. On 18 June 1983, at age 32, she became the first American woman in space and the youngest American to fly, as a mission specialist aboard the ",L("Space_Shuttle")," Challenger on mission STS-7, where she operated the shuttle's robotic arm to deploy and retrieve a satellite."]),
 ("p",["Ride joined ",L("NASA")," as part of Astronaut Group 8 in 1978, the first class to include women. She flew a second mission, STS-41-G, in 1984, and was training for a third when the Challenger disaster grounded the fleet; she served on the Rogers Commission that investigated the accident, and later on the board that investigated the Columbia loss. After leaving NASA she became a physics professor at the University of California, San Diego, and co-founded Sally Ride Science to encourage girls in STEM education."]),
], ["STS-7 satellite details summarised; the SPAS-01 free-flyer operations paraphrased."])

# ---------------- Orbital mechanics ----------------
build("Orbital_mechanics", "Orbital mechanics", [
 ("thumb","orbit-diagram","A diagram of an elliptical orbit showing apoapsis, periapsis and the central body at one focus","An elliptical orbit around a central body."),
 ("p",["<b>Orbital mechanics</b> (or astrodynamics) is the study of the motion of artificial satellites and spacecraft under the influence of gravity and thrust. It builds on Kepler's laws of planetary motion and Newton's law of universal gravitation: a body in orbit follows a conic section — circle, ellipse, parabola or hyperbola — with the central body at one focus."]),
 ("p",["Key quantities include the semi-major axis, which sets the orbital period; eccentricity, which sets the ellipse's shape; and the apoapsis and periapsis, the highest and lowest points of the orbit. Changing an orbit requires changing velocity, measured as ",L("Delta-v")," — the currency of spaceflight, limited by the ",L("Tsiolkovsky_rocket_equation"),". Energy-efficient transfers between circular orbits use the ",L("Hohmann_transfer_orbit"),", while spacecraft visiting other planets use ",L("Gravity_assist")," manoeuvres to gain or shed energy."]),
 ("h2","Applications"),
 ("p",["Orbital mechanics governs launch windows, rendezvous and docking, station-keeping, interplanetary trajectories and re-entry. Real orbits are perturbed by atmospheric drag, the Earth's equatorial bulge and the gravity of the Moon and Sun, all of which mission designers must model."]),
], ["Introductory summary; mathematical formalism (vis-viva equation etc.) omitted."])

# ---------------- Extravehicular activity ----------------
build("Extravehicular_activity", "Extravehicular activity", [
 ("thumb","eva-iss","An astronaut in a white spacesuit working on the outside of the International Space Station, Earth far below","An ISS spacewalk high above Earth."),
 ("p",["<b>Extravehicular activity</b> (EVA) is any activity done by an astronaut outside a spacecraft in space — popularly called a spacewalk when the astronaut floats free of the vehicle. The first EVA was performed by ",L("Alexei_Leonov")," on 18 March 1965, followed three months later by Edward White on Gemini 4."]),
 ("p",["Spacewalks are essential for assembling and repairing stations and telescopes: astronauts have serviced the ",L("Hubble_Space_Telescope")," on five missions and built much of the ",L("International_Space_Station")," by hand. An EVA is among the most demanding tasks in spaceflight — the pressurised suit is stiff, work is slow and fatiguing, and the astronaut depends entirely on the suit's life support. Modern suits provide oxygen, cooling, communications and micrometeoroid protection for up to about eight hours."]),
 ("h2","Records"),
 ("p",["Anatoly Solovyev holds the record for the most spacewalks, with sixteen, and the most cumulative EVA time at over 82 hours. The longest single spacewalk, by James Voss and Susan Helms in 2001, lasted 8 hours 56 minutes. China, whose astronauts first walked in space in 2008, now conducts regular EVAs from the ",L("Tiangong_space_station"),"."]),
], ["Record figures are from memory and cumulative totals change with new missions."])

# ---------------- Atmospheric entry ----------------
build("Atmospheric_entry", "Atmospheric entry", [
 ("thumb","reentry-plasma","A returning capsule glowing white-hot as it plunges through the upper atmosphere, trailing plasma","Atmospheric entry heating on a returning capsule."),
 ("p",["<b>Atmospheric entry</b> (or re-entry) is the movement of an object from outer space into and through the atmosphere of a planet. It is one of the most dangerous phases of spaceflight: a vehicle returning from orbit travels at about 7.8 km/s, and must shed that enormous kinetic energy as heat in the atmosphere before it can land."]),
 ("p",["Blunt bodies are used because a rounded heat shield pushes the shockwave away from the vehicle, keeping most of the plasma-heated gas from touching the surface. Heat shields either ablate — chars and erodes away, as on Apollo and Orion — or insulate with reusable tiles and reinforced carbon, as on the ",L("Space_Shuttle"),". Entry angle is critical: too shallow and the vehicle skips off the atmosphere; too steep and deceleration and heating exceed survivable limits. ",L("Apollo_13"),"'s crew and the Columbia disaster in 2003, caused by heat-shield damage from launch debris, show the stakes."]),
 ("h2","Beyond Earth"),
 ("p",["Entry techniques have been adapted for other worlds: Mars landers use heat shields, parachutes and rocket-powered descent in an atmosphere a hundred times thinner than Earth's, while probes entering the atmospheres of Venus and Titan and sample-return capsules from comets and asteroids have survived some of the fastest entries ever attempted — Stardust's capsule re-entered at about 12.9 km/s."]),
], ["Speed figures are the commonly cited values from memory."])

for q in ["Voskhod_2","Apollo_14","Apollo–Soyuz_Test_Project","Rogers_Commission","Kepler's_laws_of_planetary_motion",
          "Anatoly_Solovyev","Zhai_Zhigang","Ablative_heat_shield","Stardust_(spacecraft)","STS-95",
          "Mercury_Seven","Fra_Mauro_formation"]:
    queue(q, "Buzz_Aldrin")
print("batch3 done")
