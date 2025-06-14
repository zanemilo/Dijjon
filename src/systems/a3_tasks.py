from systems.Quest import Quest

tasks = {
    # Act 3 - Scene 1: The Shattered Plain
    1: {
        "name": "The Shattered Plain",
        "type": "skill_check",
        "complete": False,
        "narrative": {
            1: (
                "The Shattered Plain stretches endlessly, a graveyard of ruined towers and shattered weapons. "
                "Craters pulse faintly with residual energy from the Rift, and jagged cliffs rise like broken ribs, "
                "casting long shadows. Dust and ash choke the air as echoes of distant battles rumble."
            ),
            2: (
                "The Rift looms on the horizon, its pulsating light painting the sky in ominous hues. "
                "In the distance, remnants of the Black Vanguard and Azure Order clash amid the ruins, "
                "their banners torn and bloodied. Faction leaders struggle for dominance as the ground quakes "
                "beneath the weight of unstable energies."
            ),
            3: (
                "Explosions ripple across the Plain as the Rift flares. Factions scatter, and demons rise from fissures "
                "in the ground. Smoke and ash cloud the battlefield as survivors rally or flee, their fates hanging by a thread."
            ),
        },
        "answers": {
            1: [
                "Support Myrra - Abandon the Mission and preserve the survivors.",
                "Follow Kelgar - Defend the Plain and hold defensive lines.",
                "Side with Ashki - Seize the Rift's power, risking instability.",
                "Confront Rivals - Attack Enemy Leaders to gain control."
            ],
            2: [
                "Retreat - Sacrifice control of the Rift but ensure safety.",
                "Hold the Line - Protect the Rift but sustain casualties.",
                "Claim the Rift - Gain powerful abilities at great risk.",
                "Eliminate Leaders - Decimate enemies but risk faction collapse."
            ],
            3: [
                "Survivors scatter, leaving the Rift unchallenged, but Myrra vows to return.",
                "Hold the Rift's perimeter against waves of enemies, but Kelgar warns of exhaustion.",
                "Gain access to powerful abilities but trigger instability, Ashki's ambition grows.",
                "Defeat rival leaders, scattering their forces, but the Azure Order vows revenge."
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Branching Choices': ['Branch I1 – Abandon the Mission',
                                 'Branch I2 – Defend the Plain',
                                 'Branch I3 – Seize the Rift',
                                 'Branch I4 – Attack Enemy Leaders'],
            'Environment': 'The Shattered Plain with unstable energies, fractured terrain, and ongoing battles.',
            'Immediate Consequences': ['Survivors scatter, leaving the Rift unchallenged.',
                                       'Hold the Rift’s perimeter against waves of enemies.',
                                       'Gain access to powerful abilities but trigger instability.',
                                       'Defeat rival leaders, scattering their forces.'],
            'Key NPCs': ['Myrra (Smuggler)', 'Kelgar (Cleric)', 'Ashki (Sorcerer)', 'Black Vanguard Captain (Antagonist)', 'Azure Order Magus (Antagonist)'],
            'Protagonist Role': ['Branch H1 (Destroy the Heart)', 'Branch H2 (Seal the Heart)', 'Branch H3 (Harness the Heart)'],
            'Transition': 'Transition to Scene 2: The Last Stand',
        },
    },

    # Act 3 - Scene 2: The Last Stand
    2: {
        "name": "The Last Stand",
        "type": "Dynamic Quest",
        "complete": False,
        "narrative": {
            1: (
                "The group reaches the Rift’s inner sanctum, a massive chamber of swirling light and collapsing terrain. "
                "Molten rivers carve through crystalline spires, and unstable energy hums through the air. The walls pulse "
                "with the rhythm of an ancient force, threatening to collapse the chamber at any moment."
            ),
            2: (
                "Key NPCs reveal their motives—Myrra urges caution and survival, Kelgar seeks divine guidance to restore order, "
                "and Ashki grows unstable, consumed by ambition to control the Rift’s power. Opposing factions, the Black Vanguard "
                "and Azure Order, prepare for final clashes, each driven by fear and desperation."
            ),
            3: (
                "The protagonist faces critical choices that will shape the battle’s outcome—whether to preserve the survivors, "
                "fight for dominance, or embrace the Rift’s unstable power. Demonic creatures emerge as chaos intensifies."
            ),
        },
        "answers": {
            1: [
                "Support Myrra - Evacuate Survivors and focus on retreat.",
                "Support Kelgar - Hold the Line and resist the Rift’s forces.",
                "Side with Ashki - Use the Rift’s power to gain control.",
                "Challenge the Leaders - Direct Combat to secure dominance."
            ],
            2: [
                "Evacuate Survivors and accept losses but preserve morale.",
                "Hold the Line to fortify positions but risk resources.",
                "Use the Rift and unleash instability but gain power.",
                "Defeat Factions and scatter enemies, risking internal collapse."
            ],
            3: [
                "Survivors escape, leaving the Rift unstable, Myrra vows to return.",
                "The line holds, but Kelgar warns of exhaustion and future threats.",
                "Ashki's power surges, reshaping the Rift but risking corruption.",
                "Enemies scatter, but the Azure Order vows revenge against the protagonist."
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Environment': 'Rift’s inner sanctum with molten rivers, crystalline spires, and collapsing terrain.',
            'Immediate Consequences': 'Chamber collapse, demon emergence, faction clashes.',
            'Key NPCs': ['Myrra', 'Kelgar', 'Ashki', 'Black Vanguard Leader', 'Azure Order Magus'],
            'Protagonist Role': ['Branch I1', 'Branch I2', 'Branch I3', 'Branch I4'],
            'Transition': 'Scene 3: The World Reforged',
        },
    },

    # Act 3 - Scene 3: The World Reforged
    3: {
        "name": "The World Reforged",
        "type": "Dynamic Quest",
        "complete": False,
        "narrative": {
            1: (
                "The Rift has collapsed—or expanded—depending on previous choices. The sky shifts unnaturally, painted in streaks "
                "of crimson, gold, or void-like blackness. Crystalline shards float midair, and rivers of molten energy carve paths "
                "through ruins. Survivors gather in scattered groups, tending to the wounded and sifting through debris."
            ),
            2: (
                "Structures shimmer, half-dissolved by Rift energy. Factions either rebuild or descend into infighting. Ashki’s fate "
                "depends on earlier choices—godlike, corrupted, or dead. Myrra debates leaving, while Kelgar offers prayers."
            ),
            3: (
                "Protagonist must decide whether to rebuild, dominate, embrace chaos, or walk away, shaping the world’s final state."
            ),
        },
        "answers": {
            1: [
                "Focus on Rebuilding and diplomacy.",
                "Enforce Control through strength and fear.",
                "Embrace Chaos and risk destabilization.",
                "Walk Away and let the world shape its own fate."
            ],
            2: [
                "Rebuild the Plain, restoring order and hope.",
                "Dominate the factions, establishing a new regime.",
                "Embrace chaos, allowing the Rift's power to reshape reality.",
                "Walk away, leaving the world to its own devices."
            ],
            3: [
                "Rebuilding Peace - Survivors unite, rebuilding the Plain with Myrra’s leadership.",
                "Dominion - The protagonist rules with an iron fist, controlling the Rift’s power.",
                "Chaos Unleashed - The Rift’s energy reshapes reality, leading to unpredictable outcomes.",
                "Abandonment - The protagonist leaves, allowing factions to fight for control."
            ],
        },
        "scripts": {
            1: Quest.method_call1,
            2: Quest.method_call2,
            3: Quest.method_call3,
        },
        "data": {
            'Branching Endings': ['Rebuilding Peace', 'Dominion', 'Chaos Unleashed', 'Abandonment'],
            'Environment': 'Post-Rift collapse with molten rivers, floating shards, and fractured terrain.',
            'Key NPCs': ['Myrra', 'Kelgar', 'Ashki', 'Survivors and Factions'],
            'Protagonist Role': ['Evacuate Survivors', 'Hold the Line', 'Use the Rift', 'Defeat Leaders'],
        },
    },
}
