import Quest

# Branch 1 of the quest
finn_quest_branch01 = {
    1: {
        "narrative": {
            1: "You spot a hooded figure lurking in the shadows.",
            2: "The figure darts into a nearby alley.",
            3: "You hear footsteps approaching from behind.",
        },
        "answers": {
            1: ["Confront the figure", "Follow from a distance"],
            2: ["Chase after them", "Wait to see what they do"], # if user chooses 2 -> current quest main task info becomes finn_quest_branch02
            3: ["Turn around", "Prepare for an attack"],
        },
        "scripts": {
            1: None,
            2: Quest.method_call1,
            3: None,
        },
    }
}

# Branch 2 of the quest
finn_quest_branch02 = {
    1: {
        "narrative": {
            1: "You catch up to the figure in a dark alley.",
            2: "They turn to face you, revealing a scarred face.",
            3: "A fight seems inevitable.",
        },
        "answers": {
            1: ["Demand information", "Attack immediately"],
            2: ["Try to negotiate", "Prepare for combat"],
            3: ["Stand your ground", "Flee"], # if user chooses 2 -> skillcheck user for dex DC:14-16 -> flee else combat with entities
        },
        "scripts": {
            1: None,
            2: None,
            3: Quest.method_call2,
        },
    }
}
