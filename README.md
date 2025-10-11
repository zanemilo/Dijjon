# Dijjon Alpha

This is the official documentation for Dijjon Alpha, a text-based game set
in the Fantasy RPG world of Dijjon.

## Author: Zane Milo Deso

### Last Updated: 10/10/2025

## Table of Contents
- [Introduction](#introduction)
- [Why I’m Making This Game](#why-im-making-this-game)
- [Key Features](#key-features)
- [Roadmap](#roadmap)
- [Major Change Log](#major-change-log)

## Introduction

Dijjon Alpha is a text-based fantasy RPG that combines RNG mechanics with dynamic storytelling. No two playthroughs are alike, offering unique encounters and outcomes with each session. 

# Why I’m Making This Game

Dijjon is more than just a game to me; it’s a deeply personal project that combines my love for storytelling, my fascination with systems, and my desire to create something meaningful. Growing up, video games were my escape, a source of wonder and connection to stories that stayed with me long after the credits rolled. They offered moments of joy, introspection, and even a sense of purpose during times when life felt overwhelming.

This game is my way of channeling that inspiration into something new. It’s a chance to create a world where players can lose themselves in a story that resonates emotionally and challenges them to think about choices, consequences, and the complexity of relationships. I want Dijjon to be a space where creativity meets mechanics, where every interaction feels alive, and every decision matters.

At its core, this project is about expression—about finding a way to share my love for games and storytelling while building something I can be proud of. It’s a personal journey, one fueled by a passion for crafting experiences that might inspire others the way games once inspired me.

## Key Features

### Custom Engine Architecture

- **Modular Design:** The codebase is organized into dedicated modules (e.g., `Quest`, `QuestManager`, `DialogueManager`, `InteractionManager`) to separate concerns and enhance maintainability.


Primary Goals:

---
### Planned Refactor: Data-Driven Narrative System

#### Why
The current design uses Python scripts/classes per scene (`a1_tasks`, etc.), which mixes **content (story text, choices)** with **logic (branching, checks, events)**.  
This becomes harder to maintain as scenes multiply — logic repeats, imports get messy, and changes risk breaking previous scenes.
  
**JSON defines what happens** — dialogue, branching, and triggers.

Benefits:
- Write once, reuse everywhere (DRY principle)
-  Add new scenes without editing Python
-  Save/load works cleanly via dialogue IDs and node IDs
-  Writers/designers can edit content directly
-  Easier to test, validate, and localize
-  Engine is reusable for future projects or sequels

---

#### How

1. **Data → JSON**
- Each dialogue, quest, or event becomes a JSON file (e.g., `data/dialogue/act1_scene1.json`).
- JSON stores:
    - Dialogue text and speaker
    - Choices with `goto` (local or cross-file)
    - Optional skill checks or side-effects (`ops`)
    - Optional high-level triggers (`events`) like “start combat” or “push new scene”

Example:
```json
{
    "id": "dlg.act1.scene1",
    "start": "intro",
    "nodes": {
    "intro": {
        "line": {"speaker": "Narrator", "text": "You arrive at Hollowreach Citadel."},
        "choices": [
        {"text": "Survey the crowd", "goto": "survey_check"},
        {"text": "Approach the mage", "goto": "approach_mage"}
        ]
    },
    "survey_check": {
        "ops": [{"op": "skill_check", "skill": "perception", "dc": 5}],
        "branch": {"on_pass": "survey_pass", "on_fail": "survey_fail"}
    },
    "survey_pass": {
        "line": {"speaker": "Narrator", "text": "You notice key diplomats whispering nervously."},
        "ops": [{"op": "set_flag", "name": "intel.gala", "value": true}]
    }
    }
}
````

**Engine → Parser**

* A single Python class interprets the JSON.
* Runs each node, executes its `ops`, and moves to the next `goto` or `branch`.
* Returns:

    * A **view** (speaker, text, choices)
    * A list of **events** for the SceneManager (e.g., push new scene, start combat)

**Logic → Ops System**

* Tiny modular functions handle gameplay logic:

    ```python
    def op_skill_check(gs, args, rng):
        total = gs.player.check_roll(args["skill"])
        passed = total >= args["dc"]
        return {"pass": passed}
    ```
* Registered in an `OPCODES` dictionary so JSON can call them by name.
* Keeps engine flexible — add new mechanics by adding a new op, not rewriting scenes.

**Flow → SceneManager**

* SceneManager remains focused on stack transitions (`push`, `pop`, `replace`).

---
  
## Roadmap

### Core Game Mechanics

    Combat System: Refine combat mechanics and integrate AI strategies
    for NPCs.
    Quest System: Expand the quest system to include more complex and
    branching quests.
    Race: Create dedicated race.py file that will handle race
          functions and features.
    Exploration: Implement a more detailed exploration system with
    environmental interactions and dynamic events. This will allow
    players to interact with the world in meaningful ways, such as
    discovering hidden areas, solving puzzles, and encountering
    random events that can affect their journey. They will be able
    to explore the world of Dijjon in a more immersive way, with
    detailed environments and interactive elements, such as merchants,
    NPCs, and more.



## Major Change Log

<ul>
    <li>Implemented basic visuals, narrative engine, UI, bg music and SFX.
    Plans to refector into Data-Driven model -> Scene -> SceneManager (10/8/2025)
    <li>Refactored import statements to avoid circular imports:
    All imports now delegated to main
    <li>Implemented a new `Quest` class to handle quest
    management and dynamic task execution. (6/14/2025)
    Minor narrative flow required to be fully functional.
    <li>Refactored codebase to align with better practices
    for directory design flow. (11/2/2024)
    main is functional after merging with Master.
    <li>Created base level unit tests, plans to expand and
    automate (9/15/2024)
    <li>Implemented Quest Class to dynamically handle creating and 
    playing quests. (9/1/2024)
    <li>Major refactor on codebase: No need to clutter one folder with
    all of the scripts so everything is now in dedicated folders.
    (8/12/2024)
    <li>Integrated DijjonAlphaDevelopment folder with Git: Enhanced
    tracking of progress.
    <li>Refactoring player and NPC creation: Expanded classes and races,
    refactored to core library (1/6/2024).
    <li>Race and class selection enumeration: Improved user input
    handling (Done).
    <li>Changed attribute name convention for "int" in Player class:
    <li>Resolved conflicts with int() function (Done).
    <li>Integrated repository with GitHub: Improved version control
    and collaboration.
</ul>



