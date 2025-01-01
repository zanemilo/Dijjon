task = "{\n    \"name\": \"The First Skirmish\",\n    \"type\": \"Dynamic Quest\",\n    \"complete\": false,\n    \"narrative\": {\n        1: \"The Vale of Dusk stretches into the horizon, its mists shifting like restless spirits. Jagged cliffs and sparse forests create natural chokepoints, while patches of scorched earth hint at past battles.\",\n        2: \"As dawn breaks, the mist swirls unnaturally, revealing silhouettes of soldiers marching into formation. The distant echo of war horns and prayers for divine protection mingle with the crackling hum of Zyrian spellcasters preparing their wards.\",\n        3: \"As the battle nears its peak, a Zyrian mage desperately channels the Shard\u2019s power, triggering an explosion that tears open a glowing rift. Demonic creatures spill forth, attacking both armies indiscriminately.\"\n    },\n    \"answers\": {\n        1: [\n            \"Defend the Line - Focus on Defense\",\n            \"Lead the Charge - Focus on Offense\",\n            \"Scout Ahead - Investigate Artifact\"\n        ],\n        2: [\n            \"Protect Allies\",\n            \"Engage Demons\",\n            \"Focus on the Rift\"\n        ],\n        3: [\n            \"Spread Propaganda\",\n            \"Question Narrative\",\n            \"Remain Neutral\"\n        ]\n    },\n    \"scripts\": {\n        1: \"Quest.defend_line\",\n        2: \"Quest.engage_demons\",\n        3: \"Quest.spread_propaganda\"\n    },\n    \"data\": {\n        \"environment\": \"The Vale of Dusk with jagged cliffs and sparse forests.\",\n        \"key_npcs\": [\n            \"Commander Eryndel (Zyra)\",\n            \"Captain Morvek (Drajh)\",\n            \"Ashki (Companion - Sorcerer)\"\n        ],\n        \"protagonist_role\": [\n            \"Branch D1 (Spread Propaganda)\",\n            \"Branch D2 (Question the Narrative)\",\n            \"Branch D3 (Remain Neutral)\"\n        ],\n        \"climactic_event\": \"A Zyrian mage triggers an explosion that tears open a glowing rift, unleashing demons.\"\n    }\n}"
