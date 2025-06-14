from systems.Quest import Quest

tasks = {
    # Act 2 - Scene 1: The Rift's Threshold
    1: {
        "name": "The Rift's Threshold",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "The group emerges at the Rift's edge, a towering vortex of swirling violet and crimson energy. "
                "Jagged rocks jut out like broken teeth around the abyss. Pulses of light ripple outward, distorting "
                "shadows and warping the terrain. The ground hums with unstable energy, and faint whispers echo "
                "from the Rift's depths, barely audible yet deeply unsettling."
            ),
            2: (
                "Scorched earth and remnants of collapsed towers mark a failed attempt to seal the Rift, serving as grim "
                "reminders of past failures. Wind howls through fractured stones, carrying the scent of ash and decay."
            ),
            3: (
                "Lightning arcs from the Rift as its energy pulses violently. Demonic creatures begin to stir within its depths, "
                "their glowing eyes piercing the shadows. The group prepares for the next step, knowing their choices "
                "may determine survival or annihilation."
            ),
        },
        "answers": {
            1: [
                "Myrra's right. We keep moving—fast and quiet.",
                "We set up a perimeter. Hold position until we understand what we're facing.",
                "We came here for answers. Let's take the risk and see what the Rift reveals."
            ],
            2: [
                "The group avoids major confrontations, preserving resources but missing key information about the Rift.",
                "Survivors set up defensive positions, successfully repelling demonic scouts but drawing the attention of larger enemies.",
                "Uncover ancient glyphs and relic fragments, unlocking powerful tools and insights but triggering a Rift surge that attracts hostile creatures."
            ],
            3: [
                "Scene 2 begins with limited knowledge but stronger group morale and supplies.",
                "Scene 2 starts with fortified defenses but strained resources and injured NPCs.",
                "Scene 2 emphasizes dealing with the fallout of tampering with unstable magic."
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Environment': "The ground hums with unstable energy, and faint whispers echo from the Rift's depths.",
            'Key NPCs': ['Myrra', 'Kelgar', 'Ashki'],
            'Protagonist Roles': ['Branch E1', 'Branch E2', 'Branch E3'],
        },
    },

    # Act 2 - Scene 2: Descent into the Abyss
    2: {
        "name": "Descent into the Abyss",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "The group steps into the Rift, and the world twists. Darkness coils around flickering beams of light that "
                "pulse like veins, feeding into crystalline growths that emerge from cracked ground. The air hums with "
                "vibrations, warping sound and disorienting movement. Gravity shifts in brief waves, pulling debris upward "
                "before releasing it."
            ),
            2: (
                "The landscape changes with every step—bridges of light stretch over voids, only to collapse moments later. "
                "Shadows move unnaturally, forming shapes that dissolve upon closer inspection. Echoes of whispers and "
                "screams seem to come from every direction, hinting at unseen watchers."
            ),
            3: (
                "As the group ventures deeper, illusions and time loops blur reality. Ashki's obsession grows, creating tension "
                "with Myrra and Kelgar, who struggle to keep focus. Decisions made here may lead to breakthroughs—or despair."
            ),
        },
        "answers": {
            1: [
                "Follow Myrra - Escape Quickly",
                "Support Kelgar - Defend the Group",
                "Back Ashki - Investigate the Rift"
            ],
            2: [
                "Prioritize speed and survival, minimizing exposure but sacrificing deeper insights.",
                "Establish protective barriers and defend against Rift threats, sustaining injuries and depleting resources.",
                "Solve puzzles and explore hidden passages, uncovering relics but escalating instability."
            ],
            3: [
        
            "Time itself warps around the party—each step forward snaps them back through fractured echoes, collapsing light-bridges beckoning with false exits as they race on.",
        
            "Behind hastily woven wards, the air trembles with distant screams; shadows ooze through the cracks, leaving the group bruised and their supplies steadily drained.",
        
            "Deeper tunnels pulse with half-formed visions; relics whisper forgotten memories, and Ashki's gaze darkens with obsession as phantom voices lure her further into the Rift's heart."
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Environment': 'The Rift twists reality, shifting gravity and creating illusions.',
            'Key NPCs': ['Myrra', 'Kelgar', 'Ashki'],
            'Branching Choices': ['Branch G1', 'Branch G2', 'Branch G3'],
            'Transition': 'Scene 3 begins as either a final push deeper, desperate defense, or recovery from collapse.',
        },
    },

    # Act 2 - Scene 3: The Heart of Corruption
    3: {
        "name": "The Heart of Corruption",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "The group arrives at the Rift's core, a cavernous chamber pulsating with raw energy. The walls writhe with "
                "veins of molten light converging into a suspended mass of fractured crystal—the Heart. It beats like a "
                "living thing, sending waves of distortion outward."
            ),
            2: (
                "Echoes of past battles linger—charred skeletons, broken weapons, and collapsed barriers form grim reminders."
            ),
            3: (
                "The chamber shakes as the Heart pulses violently, and demonic figures emerge. The Black Vanguard leader "
                "arrives, pushing to harness the Heart's power. Tensions rise as NPCs split on whether to destroy, seal, "
                "or control it."
            ),
        },
        "answers": {
            1: [
                "Follow Myrra - Destroy the Heart",
                "Support Kelgar - Seal the Heart",
                "Back Ashki - Harness the Heart"
            ],
            2: [
                "Destroy the Heart, causing massive instability but scattering enemies.",
                "Seal the Heart, stabilizing the Rift but drawing future power struggles.",
                "Harness the Heart, gaining immense power but risking corruption."
            ],
            3: [
                "With the Heart shattered, reality fractures and the group escapes through a collapsing corridor, forever changed by the sacrifice.",
                "The seal's glow fades into silence as the team steps into a calm beyond the Rift, their resolve tested but their bond unbroken.",
                "Empowered by the Heart's essence, Ashki stands between worlds as the Rift reshapes itself, and the group braces for her next command."
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Environment': 'Cavernous chamber of fractured crystal, pulsating energy, and floating shards.',
            'Key NPCs': ['Myrra', 'Kelgar', 'Ashki', 'Black Vanguard Leader'],
            'Branching Choices': ['H1', 'H2', 'H3'],
            'Immediate Consequences': 'Chamber shakes, Heart pulses, demonic figures emerge.',
        },
    },
}
