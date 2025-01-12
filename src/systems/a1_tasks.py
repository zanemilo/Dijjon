from systems.Quest import Quest

tasks = {
    # Act 1 - Scene 1: The Summit at Hollowreach Citadel
    1: {
        "name": "The Summit at Hollowreach Citadel",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "The world of Dijjon had always been one of tension, a taut string pulled between the opposing "
                "forces of Zyra and Drajh. For centuries, the river known as the Vale of Dusk divided their lands—a "
                "shimmering silver lifeline carved into a wounded earth. On one side, the magocrats of Zyra shaped "
                "the elements themselves, their floating cities a testament to ambition and control. On the other, the "
                "Drajhan theocracy, resolute and unyielding, found divine purpose in iron discipline and unwavering "
                "faith. "
                "Both nations claimed righteousness. Both nations claimed power. Neither could lay claim to peace. "
                "Fields once golden with wheat now lay scorched by arcane fire, while forests stood lifeless, their ashen "
                "boughs reaching skyward like the hands of the damned. Yet even in the shadow of war, life endured. "
                "Farmers toiled in battered fields, merchants whispered rumors of old grudges reigniting, and travelers "
                "clutched their blades, wary of the creatures that prowled the night. "
                "At the heart of it all stood Hollowreach Citadel, a fortress of neutrality perched atop the cliffs of the Vale. "
                "Its ancient walls bore the weight of countless failed treaties, etched with glyphs of fleeting truces and shattered promises. "
                "It was here, amid the uneasy murmurs of diplomats and the flickering light of stained-glass windows, that the latest "
                "attempt at peace would take place. "
                "For now, the world watched, holding its breath. But for how long could the string of tension hold before it snapped?"
            ),
            2: (
                "The protagonist arrives at Hollowreach Citadel, a majestic fortress nestled in the Vale of Dusk. "
                "The reception area is grand, adorned with banners representing various factions. As the protagonist "
                "enters the antechamber, they notice subtle tensions among the delegates. Conversations reveal underlying "
                "alliances and past grievances. In the back corridor, whispers hint at a possible betrayal planned against the "
                "summit."


            ),
            3: (
                "Midway through the peace negotiations, a sudden explosion rocks the citadel. Smoke fills the air as "
                "debris falls from the ceiling. Chaos ensues as guards scramble to secure the area and civilians flee in panic. "
                "Amidst the turmoil, the protagonist witnesses the aftermath of the attack, with key figures either injured or "
                "missing."
            ),
            4: (
                "In the midst of the chaos, the protagonist faces a critical decision that will shape the course of events: "
                "1) Save General Althera Vyrne, a respected military leader whose survival is crucial for maintaining order; "
                "2) Pursue a suspicious figure seen fleeing the scene, potentially the mastermind behind the attack; or "
                "3) Secure the dormant Shard of Ascendance, a powerful artifact that could change the balance of power if it falls into the wrong hands."
            ),
        },
        "answers": {
            1: [
                "Reception Area: (Defiant) – 'We don’t need to arrest you. Your own kind will turn soon enough.'",
                "Reception Area: (Diplomatic) – 'I came to listen, not start a fight.'",
                "Reception Area: (Suspicious) – 'You sound nervous. What are you hiding?'",
                "Main Antechamber: (Optimistic) – 'That’s why we’re here—to make sure history doesn’t repeat itself.'",
                "Main Antechamber: (Pessimistic) – 'Peace is fragile. One spark, and it all burns down.'",
                "Main Antechamber: (Curious) – 'What’s your take? Will this treaty last?'",
                "Back Corridor: (Confrontational) – 'What do you know? Speak clearly.'",
                "Back Corridor: (Reassuring) – 'Calm down. If something’s wrong, we can figure it out.'",
                "Back Corridor: (Dismissive) – 'You’re paranoid. Go sober up.'",
                "Delegate from the Northern Clans: (Urgent) – 'We need immediate action to prevent further chaos.'",
                "Ambassador Saelros: (Calm) – 'Let us maintain order and find the truth behind this attack.'",
            ],
            2: [
                "As Diplomat’s Aide: 'Ambassador, the Drajhan envoy appears unsettled. Shall I intervene?'",
                "As Guard: 'General, I noticed movement along the north corridor. Do I investigate?'",
                "As Servant: 'The chalice... it’s enchanted? Are we certain it’s safe?'",
                "As Spy: 'I have information that could lead us to the perpetrator. Should I share it?'",
                "As Healer: 'Several delegates are injured. Where should I prioritize my efforts?'",
            ],
            3: [
                "Branch A1 – Save General Vyrne: 'Stay with me, General! The shard can wait—we need to get you out of here!'",
                "Branch A2 – Save General Vyrne: 'We must evacuate the general to ensure the military remains intact.'",
                "Branch B1 – Pursue Suspicion: 'Seal the exits! Don’t let them escape!'",
                "Branch B2 – Pursue Suspicion: 'Track the suspect through the labyrinthine corridors.'",
                "Branch C1 – Secure the Dormant Shard: 'If we leave it, it’s as good as lost. We need to secure it—now.'",
                "Branch C2 – Secure the Dormant Shard: 'Protect the shard from falling into enemy hands at all costs.'",
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call1,
            3: Quest.method_call1,
        },
        "data": {
            'Branching Choices': [
                'Save General Vyrne',
                'Pursue Suspicion',
                'Secure the Dormant Shard'
            ],
            'Environment': 'Hollowreach Citadel, Vale of Dusk',
            'Event Trigger': 'Explosion caused by a hooded figure with a golden shard',
            'Key NPCs': [
                'Ambassador Saelros (Zyra)',
                'General Althera Vyrne (Drajh)',
                'Steward Caervas (Neutral Zone Host)'
            ],
            'Protagonist Roles': [
                'Diplomat’s Aide (Zyra)',
                'Neutral Guard',
                'Servant (Neutral)'
            ]
        },
    },

    # Act 1 - Scene 2: The Ember of Discord - Fallout and Propaganda
    2: {
        "name": "The Ember of Discord - Fallout and Propaganda",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "Following the explosion at Hollowreach Citadel, the city of Zyra becomes a hotbed of arcane energy and rampant propaganda. "
                "Chancellor Aeris employs illusion magic to manipulate public perception, ensuring that the official narrative maintains her "
                "hold on power. Street performers and public speakers spread messages that glorify Zyra’s leadership while subtly undermining "
                "opposition factions."
            ),
            2: (
                "Meanwhile, in the rival city of Drajh, High Inquisitor Kaelith interprets the citadel's explosion as divine retribution. "
                "He rallies the populace to prepare for a holy war, claiming that the attack was a sign of the gods' displeasure. His fervent speeches "
                "and strict enforcement of religious laws stir both fear and devotion among the citizens."
            ),
            3: (
                "Amidst the escalating tensions, the protagonist must navigate the complex political landscape. They face a pivotal choice: "
                "1) Spread propaganda to support Zyra's narrative and boost state favor, solidifying Chancellor Aeris's control; "
                "2) Question the official narrative, potentially gaining trust with scholars and dissenters who seek the truth; or "
                "3) Remain neutral, focusing on defending the city and gaining favor with moderates who desire stability without bias."
            ),
        },
        "answers": {
            1: [
                "Spread Propaganda - Support Zyra's narrative and boost state favor.",
                "Question Narrative - Increase trust with scholars or dissenters.",
                "Remain Neutral - Focus on defending the city and gain favor with moderates.",
                "Collaborate with Propagandists - Enhance the reach and effectiveness of propaganda efforts.",
                "Sabotage Opposition - Undermine dissenting voices to maintain control.",
            ],
            2: [
                "Fan the Flames - Boost support from zealots.",
                "Urge Caution - Strengthen ties with commanders.",
                "Deflect Focus - Gain favor with defensive strategists.",
                "Engage Diplomatically - Open channels for dialogue with rival factions.",
                "Gather Intelligence - Learn more about High Inquisitor Kaelith’s plans.",
            ],
            3: [
                "Spread Propaganda - Gain influence within ruling factions.",
                "Question the Narrative - Build alliances with scholars or dissenters.",
                "Remain Neutral - Maintain flexibility and avoid extreme positions.",
                "Forge Alliances - Partner with key NPCs to sway public opinion.",
                "Investigate Truth - Seek out evidence to confirm or debunk official claims.",
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call1,
            3: Quest.method_call1,
        },
        "data": {
            'Environment': 'Zyra and Drajh are key locations with distinct atmospheres and political tensions.',
            'Key NPCs': 'Chancellor Aeris, High Inquisitor Kaelith, and Steward Caervas play pivotal roles.',
            'Protagonist Role': "The protagonist's actions influence the unfolding events and alliances."
        },
    },

    # Act 1 - Scene 3: The First Skirmish
    3: {
        "name": "The First Skirmish",
        "type": "kill",
        "complete": False,
        "narrative": {
            1: (
                "The Vale of Dusk stretches into the horizon, its mists shifting like restless spirits. Jagged cliffs and sparse forests "
                "create natural chokepoints, while patches of scorched earth hint at past battles. The protagonist and their allies traverse this "
                "treacherous landscape, aware that both Zyrian and Drajhan forces may be lurking nearby."
            ),
            2: (
                "As dawn breaks, the mist swirls unnaturally, revealing silhouettes of soldiers marching into formation. The distant echo of war horns "
                "and prayers for divine protection mingle with the crackling hum of Zyrian spellcasters preparing their wards. Tension mounts as both "
                "sides prepare for confrontation."
            ),
            3: (
                "As the battle nears its peak, a Zyrian mage desperately channels the Shard’s power, triggering an explosion that tears open a glowing "
                "rift. Demonic creatures spill forth, attacking both armies indiscriminately. The protagonist must act swiftly to respond to this unforeseen "
                "threat."
            ),
        },
        "answers": {
            1: [
                "Reinforce the wards and fortify the chokepoints. We hold them here.",
                "Advance on their flank! Break their formation before they regroup!",
                "Send a small team to the ruins. We need answers about this resonance.",
                "Call for an aerial reconnaissance to gain tactical advantage.",
                "Coordinate with spellcasters to enhance defensive magic.",
            ],
            2: [
                "Fall back! Form defensive lines and cover the retreat!",
                "We stand and fight! Hold the line—buy time for survivors!",
                "We need to close it! Ashki, can you contain the magic?",
                "Use the terrain to set traps for the demonic creatures.",
                "Prioritize evacuating wounded soldiers to safety.",
            ],
            3: [
                "Seek a truce with the enemy to face the common demonic threat.",
                "Focus solely on defeating the demons, ignoring the enemy forces.",
                "Attempt to use the Shard’s energy to seal the rift.",
                "Distract the demons to create an opportunity for a counterattack.",
                "Retreat and regroup to plan a more effective strategy against the demons.",
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call1,
            3: Quest.method_call1,
        },
        "data": {
            'climactic_event': 'The rift opens, unleashing demons.',
            'environment': 'The Vale of Dusk with jagged cliffs and sparse forests.',
            'key_npcs': [
                'Commander Eryndel (Zyra)',
                'Captain Morvek (Drajh)',
                'Ashki (Companion - Sorcerer)'
            ],
            'protagonist_role': [
                'Spread Propaganda',
                'Question the Narrative',
                'Remain Neutral'
            ]
        },
    },

    # Act 1 - Scene 4: Refugee Exodus and Rift Encounter
    4: {
        "name": "Refugee Exodus and Rift Encounter",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "The Vale of Dusk lies in ruin. Smoke rises from scorched earth, and cries of the wounded echo in the distance. "
                "Survivors from the skirmish form caravans, desperately seeking safety from both the ongoing conflict and the demonic "
                "threat unleashed by the rift. The protagonist encounters various groups, each with their own needs and agendas."
            ),
            2: (
                "As the caravans navigate the treacherous terrain, the sky darkens with swirling rift energy. Demons begin to pour through, "
                "targeting the vulnerable refugees. The protagonist must decide how to respond to the escalating danger."
            ),
            3: (
                "The protagonist faces a dire situation as the rift demons intensify their assault on the caravan. Choices made now will determine "
                "the fate of the survivors and the direction of the group's journey."
            ),
        },
        "answers": {
            1: [
                "Trust Myrra - Escape Route: Follow Myrra's plan to lead the caravan through a hidden path to safety.",
                "Support Kelgar - Defend Refugees: Assist Kelgar in organizing defenses to protect the caravan from demon attacks.",
                "Back Ashki - Investigate Rift: Prioritize Ashki's research on the rift to find a way to close it.",
                "Coordinate Evacuation - Streamline the evacuation process to minimize casualties.",
                "Secure Resources - Ensure the caravan is well-supplied with necessary provisions.",
            ],
            2: [
                "Protect Refugees: Focus on shielding the vulnerable members from demon attacks.",
                "Retreat Through Cliffs: Lead the caravan through the dangerous cliffside paths to evade demons.",
                "Empower Ashki: Provide Ashki with the means to enhance their magical abilities against the rift.",
                "Establish a Safe Zone - Create a temporary shelter to hold the caravan until the threat passes.",
                "Signal for Reinforcements - Attempt to call for help from nearby allied forces.",
            ],
            3: [
                "Divert Resources - Allocate supplies and aid to those most in need.",
                "Organize Defense - Set up barricades and patrols to fend off demons.",
                "Research Rift - Work with Ashki to understand and mitigate the rift's effects.",
                "Negotiate with Leaders - Communicate with caravan leaders to unify efforts.",
                "Prioritize Survivors - Make tough decisions on who receives limited resources.",
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Branching Paths': 'Branch F1, F2, F3',
            'Climactic Event': 'Rift Demons Attack',
            'Environment': 'The Vale of Dusk is in ruin with smoke and cries of the wounded.',
            'Key NPCs': 'Myrra, Kelgar, Ashki',
            'Protagonist Role': 'Branch E1, E2, E3',
            'Transition': 'Scene 5 - The Sunken Hold'
        },
    },

    # Act 1 - Scene 5: The Sunken Hold
    5: {
        "name": "The Sunken Hold",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "The Sunken Hold emerges from the mist, half-submerged in black water. Moss-covered stone towers rise like jagged teeth from the swamp. "
                "Faint runes glow along crumbled walls, whispering ancient warnings. The air hums with residual energy, hinting at the arcane power "
                "sealed within. The protagonist and their group navigate the treacherous landscape, seeking shelter and answers."
            ),
            2: (
                "Inside the Sunken Hold, broken staircases and collapsed archways create hazards. Pools of stagnant water ripple unnaturally, hiding unseen "
                "dangers beneath the surface. The group must carefully explore the structure, avoiding traps and uncovering hidden secrets that may aid them "
                "in their quest."
            ),
            3: (
                "Reaching the vault chamber, the group finds ancient seals crackling with energy. Ashki activates a glyph, triggering a pulse that awakens a bound "
                "demon. The chamber fills with malevolent energy as the demon stirs, presenting a new and formidable challenge."
            ),
        },
        "answers": {
            1: [
                "Follow Myrra - Escape Quickly: Trust Myrra to lead the group out swiftly through the hidden passages.",
                "Support Kelgar - Protect the Group: Assist Kelgar in safeguarding the group against potential threats.",
                "Back Ashki - Explore Further: Help Ashki delve deeper into the Sunken Hold to uncover more secrets.",
                "Investigate Runes - Study the ancient symbols for clues.",
                "Secure the Area - Ensure the perimeter is safe before proceeding.",
            ],
            2: [
                "Protect Ashki: Focus on defending Ashki as they work on arcane tasks.",
                "Seal the Vault: Attempt to reinforce or close the vault to prevent further demonic incursions.",
                "Use Relics: Utilize discovered relics to gain an advantage against threats.",
                "Clear the Hazards - Remove obstacles and neutralize traps within the hold.",
                "Map the Area - Create a detailed map of the Sunken Hold for future reference.",
            ],
            3: [
                "Engage the Demon - Confront the awakened demon head-on.",
                "Evacuate the Chamber - Retreat to a safer area and regroup.",
                "Attempt to Rebind - Use Ashki's magic to try and seal the demon once more.",
                "Distract the Demon - Create diversions to mitigate its attacks.",
                "Seek Allies - Call upon nearby NPCs for assistance in dealing with the demon.",
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Branching Paths': 'Escape Quickly, Protect the Group, Explore Further',
            'Climactic Event': 'Vault Unsealing',
            'Environment': 'The Sunken Hold',
            'Key NPCs': 'Myrra, Kelgar, Ashki',
            'Protagonist Role': 'Branch Continuation',
            'Transition': 'Scene 6 - The Broken Path'
        },
    },

    # Act 1 - Scene 6: The Broken Path
    6: {
        "name": "The Broken Path",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "The group emerges from the ruins of the Sunken Hold into a fog-laden wasteland. Jagged rocks and twisted trees frame the broken path, "
                "their silhouettes looming like sentinels. Ashes and embers drift through the air, remnants of fires left in the demons’ wake. Cries "
                "echo faintly from the distance, hinting at unseen dangers lurking beyond the mist."
            ),
            2: (
                "The survivors move cautiously, their footsteps muffled by damp earth. The road splits ahead—a narrow path leads deeper into the wilderness, "
                "while the other curves toward an abandoned outpost rumored to hold valuable resources and potential allies."
            ),
            3: (
                "As the group advances, demonic figures emerge from the fog, stalking their every move. Their glowing eyes pierce the mist, and guttural growls "
                "echo through the shadows. The protagonist must decide how to handle the approaching threat."
            ),
        },
        "answers": {
            1: [
                "Follow Myrra - Keep Moving: Continue following Myrra's lead to navigate through the wasteland quickly.",
                "Support Kelgar - Fortify the Outpost: Help Kelgar secure the abandoned outpost as a new base.",
                "Back Ashki - Pursue the Rift: Assist Ashki in investigating the source of the rift's power.",
                "Scout the Area - Send a scout to gather information about the surroundings.",
                "Set Up Defenses - Prepare the group for potential attacks from demons.",
            ],
            2: [
                "Retreat Quietly: Withdraw to avoid confrontation with the demonic entities.",
                "Hold the Line: Stand your ground and defend against the incoming demons.",
                "Empower Ashki: Provide Ashki with resources to enhance their magical defenses.",
                "Create a Diversion - Distract the demons to allow the group to escape.",
                "Form a Tactical Plan - Strategize the best approach to handle the threat.",
            ],
            3: [
                "Engage the Demons - Fight the demonic creatures to protect the group.",
                "Use Magic - Utilize Ashki's sorcery to counter the demons' attacks.",
                "Coordinate with Allies - Work together with Kelgar and Myrra to fend off the threat.",
                "Evade the Demons - Find a way to slip past the demons without direct confrontation.",
                "Analyze Weaknesses - Identify and exploit the demons' vulnerabilities.",
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Branching Paths': 'Branch H1, Branch H2, Branch H3',
            'Climactic Event': 'The Demon Pursuit',
            'Environment': 'Fog-laden wasteland with jagged rocks and twisted trees.',
            'Key NPCs': 'Myrra, Kelgar, Ashki',
            'Protagonist Role': 'Branch G1, Branch G2, Branch G3',
            'Transition': 'Scene 7 – Rift’s Threshold'
        },
    },
}
