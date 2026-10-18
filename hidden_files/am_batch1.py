import sys; sys.path.insert(0, "/home/hatch/workspace/muse-webcrawl/hidden_files")
from build_am import build, queue, L

# ---------------- Project Mercury ----------------
build("Project_Mercury", "Project Mercury", [
 ("thumb","mercury-atlas-launch","A Mercury-Atlas rocket lifting off from Cape Canaveral carrying a Mercury capsule","A Mercury-Atlas launch from Cape Canaveral."),
 ("p",["<b>Project Mercury</b> was the first human spaceflight program of the United States, run by ",L("NASA")," from 1958 to 1963. Its goals were to put a human in orbit around Earth, investigate the ability of humans to function in space, and recover both astronaut and spacecraft safely. It was named after Mercury, the Roman god of travel."]),
 ("p",["The program flew six crewed missions. ",L("Alan_Shepard")," became the first American in space on the suborbital Mercury-Redstone 3 flight (Freedom 7) on 5 May 1961, twenty-three days after ",L("Yuri_Gagarin"),"'s orbital flight for the Soviet Union. On 20 February 1962 ",L("John_Glenn")," became the first American to orbit Earth aboard Friendship 7. The final flight, Mercury-Atlas 9 (Faith 7), carried Gordon Cooper on 22 orbits in May 1963."]),
 ("h2","Spacecraft"),
 ("p",["The Mercury capsule was a small conical crew compartment, about 1.9 metres across at the base, with a blunt heat shield for ",L("Atmospheric_entry","atmospheric entry"),". It carried one astronaut, who had little ability to manoeuvre the craft — a limitation its pilots joked about, calling themselves 'spam in a can'. Two booster types were used: the Redstone for suborbital flights and the much larger Atlas for orbital missions."]),
 ("h2","The Mercury Seven"),
 ("p",["The seven original astronauts — Scott Carpenter, Gordon Cooper, ",L("John_Glenn"),", Gus Grissom, Wally Schirra, ",L("Alan_Shepard")," and Deke Slayton — were military test pilots announced to the public in April 1959. They became national celebrities and helped define the image of the astronaut. Project Mercury was succeeded by ",L("Project_Gemini"),", which developed the techniques needed for the ",L("Apollo_program"),"."]),
], ["Exact capsule dimensions and flight dates are from memory and may differ slightly from the real article.",
    "The 'spam in a can' quip is commonly attributed to the Mercury pilots' frustrations; exact attribution is uncertain."])

# ---------------- Project Gemini ----------------
build("Project_Gemini", "Project Gemini", [
 ("thumb","gemini-rendezvous","Two Gemini spacecraft flying in formation during the first rendezvous in orbit, December 1965","Gemini 6A and Gemini 7 rendezvous, December 1965."),
 ("p",["<b>Project Gemini</b> was ",L("NASA"),"'s second human spaceflight program, conducted between 1961 and 1966. Conceived as a bridge between ",L("Project_Mercury")," and the ",L("Apollo_program"),", it developed the techniques Apollo would need: long-duration flight, rendezvous and docking, and working outside the spacecraft (",L("Extravehicular_activity"),"). The name comes from the Latin word for twins, reflecting its two-person crew."]),
 ("p",["Ten crewed missions flew between March 1965 and November 1966, launched by Titan II rockets from Cape Kennedy. Gemini 3 carried Gus Grissom and John Young on the first flight; Gemini 4 saw Edward White perform the first American spacewalk; Gemini 6A and 7 achieved the first rendezvous of two crewed spacecraft in December 1965; and Gemini 8, commanded by ",L("Neil_Armstrong"),", achieved the first docking in space — before a stuck thruster forced an emergency return."]),
 ("h2","Achievements"),
 ("p",["By the end of the program the United States had demonstrated flights of up to fourteen days (Gemini 7), precision rendezvous and docking, and multiple spacewalks. These successes put NASA ahead in practical orbital operations and cleared the technical path to the Moon. Gemini astronauts included future Moonwalkers ",L("Neil_Armstrong"),", ",L("Buzz_Aldrin")," and David Scott."]),
], ["Mission-by-mission crew details are summarised from memory; Gemini 5 and 9A details omitted for brevity.",
    "Gemini pronunciation ('GEM-in-ee' vs 'GEM-in-eye') debate not covered."])

# ---------------- Apollo 8 ----------------
build("Apollo_8", "Apollo 8", [
 ("thumb","earthrise","The famous Earthrise photograph: Earth rising above the grey lunar horizon, December 1968","Earthrise, photographed from Apollo 8 in lunar orbit."),
 ("p",["<b>Apollo 8</b> was the first crewed spacecraft to leave low Earth orbit, reach the Moon, orbit it, and return safely to Earth. Launched on 21 December 1968 atop a ",L("Saturn_V"),", it carried Frank Borman, James Lovell and William Anders on a six-day mission that orbited the Moon ten times on Christmas Eve."]),
 ("p",["The mission was a bold change of plan: with the ",L("Lunar_Module")," delayed, NASA sent the command module alone to the Moon to test navigation, communications and the ",L("Saturn_V")," with a crew. During a televised broadcast from lunar orbit on Christmas Eve, the crew read the opening verses of the Book of Genesis — one of the most watched broadcasts of its time. Anders' colour photograph of the Earth rising over the lunar horizon, known as ",L("Earthrise","Earthrise"),", became one of the most influential images of the twentieth century."]),
 ("h2","Return"),
 ("p",["Apollo 8 splashed down in the Pacific on 27 December 1968. Its success paved the way for Apollo 10's dress rehearsal and the ",L("Apollo_11")," landing seven months later. All three crew members were named Time magazine's Men of the Year for 1968."]),
], ["Genesis reading details and broadcast audience figures are paraphrased from memory."])

# ---------------- Apollo 13 ----------------
build("Apollo_13", "Apollo 13", [
 ("thumb","apollo13-service-module","The damaged Apollo 13 service module after separation, showing the panel blown out by the oxygen tank explosion","Apollo 13's damaged service module, photographed after jettison."),
 ("p",["<b>Apollo 13</b> was the seventh crewed mission in the ",L("Apollo_program")," and was intended to be the third Moon landing. Launched on 11 April 1970 with James Lovell, Jack Swigert and Fred Haise aboard, the mission was aborted after an oxygen tank in the service module exploded two days into the flight, crippling the spacecraft."]),
 ("p",["Swigert's report to Houston — 'Okay, Houston, we've had a problem here' — began one of the most famous rescue efforts in spaceflight history. The crew used the ",L("Lunar_Module")," Aquarius as a 'lifeboat', rationing power and water and improvising a carbon-dioxide filter from plastic bags and duct tape, while engineers in Houston worked around the clock on procedures to bring them home. A free-return trajectory swing around the Moon put the crew on course for Earth."]),
 ("h2","Outcome"),
 ("p",["Apollo 13 splashed down safely in the South Pacific on 17 April 1970. The mission was classified a 'successful failure' because of the experience gained in rescuing the crew. An investigation traced the explosion to damaged wiring and a thermostat failure in oxygen tank two during pre-flight testing. The story was dramatised in the 1995 film Apollo 13."]),
], ["Exact wording/timing of the famous quote is paraphrased; the film's shorter version differs slightly from the actual transmission."])

# ---------------- Apollo 17 ----------------
build("Apollo_17", "Apollo 17", [
 ("thumb","apollo17-schmitt","Apollo 17 astronaut Harrison Schmitt standing beside a large split boulder at Taurus-Littrow","Harrison Schmitt at Tracy's Rock, Apollo 17."),
 ("p",["<b>Apollo 17</b> was the eleventh and final crewed mission in ",L("NASA"),"'s ",L("Apollo_program"),", landing on the Moon on 11 December 1972. Commander Eugene Cernan and Lunar Module Pilot Harrison Schmitt spent three days exploring the Taurus–Littrow valley while Ronald Evans orbited above in the command module. Schmitt, a geologist, remains the only professional scientist to have walked on the Moon."]),
 ("p",["Apollo 17 was the first night launch of the ",L("Saturn_V")," and the longest Apollo mission, at just over twelve days. The crew drove the Lunar Roving Vehicle further than any previous mission, collected about 110 kg of lunar samples, and discovered orange volcanic glass in the soil at Shorty Crater — evidence of ancient lunar volcanism. Cernan, the last person to leave the lunar surface, spoke of returning 'with peace and hope for all mankind'."]),
 ("h2","Legacy"),
 ("p",["No human has travelled beyond low Earth orbit since Apollo 17 returned on 19 December 1972. The ",L("Artemis_program")," aims to return crews to the lunar surface in the 2020s, more than half a century later."]),
], ["Sample mass and traverse distances are approximate from memory."])

# ---------------- Artemis program ----------------
build("Artemis_program", "Artemis program", [
 ("thumb","artemis-sls-launch","NASA's Space Launch System lifting off at night on the uncrewed Artemis I mission, November 2022","Artemis I lifts off from Kennedy Space Center, 16 November 2022."),
 ("p",["The <b>Artemis program</b> is a ",L("NASA"),"-led human spaceflight program, run with international and commercial partners, to return humans to the Moon for the first time since ",L("Apollo_17")," in 1972 and to establish a sustainable lunar presence as preparation for crewed missions to ",L("Mars"),". It is named after the Greek goddess Artemis, twin sister of Apollo."]),
 ("p",["The program's core vehicles are the Space Launch System (SLS) heavy-lift rocket and the Orion crew capsule. The uncrewed Artemis I test flight launched on 16 November 2022, sending Orion around the Moon and back. Artemis II, the first crewed flight, will loop around the Moon without landing; Artemis III aims to land two astronauts near the lunar south pole, including the first woman and first person of colour to walk on the Moon, using a version of SpaceX's ",L("SpaceX_Starship","Starship")," as the human landing system."]),
 ("h2","Elements"),
 ("p",["Supporting elements include the Lunar Gateway, a small space station planned for lunar orbit; commercial landers from SpaceX and ",L("Blue_Origin"),"; and new spacesuits for surface operations. Schedules have slipped repeatedly, and the program's cost and the expendable SLS have drawn criticism, but Artemis represents the central direction of American human spaceflight in the 2020s. Partner agencies include the ",L("European_Space_Agency"),", ",L("JAXA")," and the Canadian Space Agency."]),
], ["Artemis II/III target dates have shifted several times; dates are stated generally rather than as firm schedule commitments.",
    "Gateway's status and configuration have been under review; described here in general terms."])

# ---------------- Human spaceflight ----------------
build("Human_spaceflight", "Human spaceflight", [
 ("thumb","iss-crew","Astronauts floating inside a space station module, working and exercising in weightlessness","Crew members aboard the International Space Station."),
 ("p",["<b>Human spaceflight</b> (also called crewed spaceflight) is spaceflight with a crew or passengers aboard the spacecraft. It began on 12 April 1961, when Soviet cosmonaut ",L("Yuri_Gagarin")," completed one orbit of Earth aboard ",L("Vostok_1"),". Since then more than six hundred people have flown in space, and humans have maintained a continuous presence in orbit aboard the ",L("International_Space_Station")," and Chinese stations since 2000."]),
 ("p",["Human spaceflight programs have been run by the Soviet Union and Russia (",L("Soyuz_(spacecraft)","Soyuz"),"), the United States (Mercury, Gemini, Apollo, the ",L("Space_Shuttle")," and commercial crew vehicles), and China (Shenzhou). Crewed vehicles must keep their occupants alive with life-support systems, protect them during launch and ",L("Atmospheric_entry","re-entry"),", and in most designs return them safely to Earth."]),
 ("h2","Milestones"),
 ("p",["Key firsts include the first spacewalk by ",L("Alexei_Leonov")," in 1965, the first Moon landing by ",L("Apollo_11")," in 1969, the first space station (",L("Salyut_1"),") in 1971, and the first privately developed crewed orbital vehicle, SpaceX's Crew Dragon, in 2020. Human spaceflight has also seen fatal accidents, including Soyuz 1, Soyuz 11, and the Challenger and Columbia shuttle losses, which killed twenty-one people in total across those four events."]),
], ["Total people flown in space is approximate and grows yearly; stated as 'more than six hundred'.",
    "Fatality tally combines the four named accidents as remembered."])

# ---------------- Vostok 1 ----------------
build("Vostok_1", "Vostok 1", [
 ("thumb","vostok-capsule","The spherical Vostok re-entry capsule on display, with its hatch and portholes","The Vostok 1 re-entry module."),
 ("p",["<b>Vostok 1</b> was the first spaceflight of the Soviet Vostok programme and the first human spaceflight in history. On 12 April 1961, cosmonaut ",L("Yuri_Gagarin")," completed a single orbit of Earth in 108 minutes, launching from ",L("Baikonur_Cosmodrome")," in Kazakhstan aboard a rocket derived from the R-7 intercontinental ballistic missile."]),
 ("p",["Gagarin's call sign was Kedr (Siberian pine). Famously, he is reported to have said 'Poyekhali!' ('Let's go!') at liftoff. Because engineers were unsure how weightlessness would affect a pilot, the capsule's manual controls were locked, with an override code sealed in an envelope. At the end of the orbit the service module initially failed to separate cleanly, causing a violent tumble before the cables burned through. Gagarin ejected from the capsule at about 7 km altitude and landed by parachute near Engels, in Saratov Oblast — a detail kept secret for years, since aviation records rules technically required a pilot to land with his craft."]),
 ("h2","Aftermath"),
 ("p",["Gagarin became an international celebrity and a hero of the Soviet Union. 12 April is celebrated as Cosmonautics Day in Russia and as the International Day of Human Space Flight. The flight opened the ",L("Space_Race")," era of crewed competition that culminated in the ",L("Apollo_program"),"."]),
], ["The ejection-and-parachute landing detail and the sealed override envelope are as commonly reported; some specifics remain debated."])

# queues from batch 1
for q in ["Earthrise","Gordon_Cooper","Titan_II","Edward_White_(astronaut)","David_Scott_(astronaut)",
          "Gus_Grissom","Shenzhou_(spacecraft)","Crew_Dragon","Lunar_Gateway","Orion_(spacecraft)",
          "Space_Launch_System","Salyut_programme"]:
    queue(q, "Project_Mercury")
print("batch1 done")
