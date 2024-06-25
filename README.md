Dijjon Beta

This is the official documentation for Dijjon Beta, a text-based game set in the Fantasy RPG world of Dijjon. The game is inspired by the creative work of John Philip Swanson and takes the player through a dynamic version of the DnD 5e campaign he wrote.

Author: Zane M Deso
Last Updated: June 25, 2024
Table of Contents

    Introduction
    Current Sprint Goal
    Backlog
    Bugs to Fix
    Roadmap
    Major Change Log
    Story Arch Plans

Introduction

Dijjon (current working name) is a text-based game that incorporates RNG into every interaction, encounter, and outcome, ensuring that no two playthroughs are the same. As of June 16, 2024, Agile practices have been enacted, and development will proceed in mini sprints.
Current Sprint Goal

    Flesh out EnchantedForest HardCoded Quest.
    Make functional puzzle aspect.
    Implement continue function. (Idea here is to have beginning -> middle -> end of the quest, although some quests do not warrant having to finish objectives. This one the palyer could just mosey on by)

Previous Sprint Goal

    Create a start menu with some playable functionality.
    Plug in some of the hard-coded quests into the main game.
    Work on story points if time permits.

Backlog
High Priority

    [H] Make functional intro quest line
    [H] Inject encounters into hardcoded quests to add dynamic feel to 'traveling', 'exploring', or 'continuing'
    [H] Refactor Player class to be a child of an Entity class; set NPCs and Mobs as children of the Entity class.
    [H] Finish Implementation of Combat Class.
    [H] Finish Implementation of First Bandit Quest Prototype.
    [H] Refactor code into dedicated files for better readability and maintainability.

Medium Priority

    [M] Integrate Quest Journal with Quests.
    [M] Improve UI functionality for the quest journal.
    [M] Enhance menu functions for better user experience.
    [M] Build compositional relationships within the Player class.
    [M] Implement character classes and abilities with a CharacterClassFactory.

Low Priority

    [L] Track map expansion using nodes.
    [L] Add functionality for quest generation.
    [L] Create mad-lib type phrases for commoner jobs.
    [L] Improve Player Inventory UI.
    [L] Add optional check types based on location or event type.
    [L] Enhance roll_stats function in dice_Roll file.
    [L] Add accessors and mutators to each class.
    [L] Implement enchants to Melee_Items class.

Bugs to Fix

    [M] Fix the give_item function to properly update or remove items in the player's inventory.

Roadmap
Core Game Mechanics

    Combat System: Refine combat mechanics and integrate AI strategies for NPCs.
    Quest System: Expand the quest system to include more complex and branching quests.

Character Development

    Character Classes: Enhance character class system with unique abilities and progression paths.
    Entities and NPCs: Develop detailed attributes and behaviors for entities.

Item and Inventory Management

    Items: Add item durability and special effects.
    Trading System: Implement a trading system for interactions with NPC vendors and players.

World Building

    Environment: Define more environments and locations for exploration.
    Mob Generation: Dynamically create challenges for players.

User Interface and Experience

    Settings and Customization: Update the settings module for more customization options.
    Feedback System: Implement a system to collect player feedback.

Technical Improvements

    Code Refactoring: Regularly review and refactor the codebase.
    Testing and Debugging: Increase focus on testing all modules.

Documentation and Help System

    Game Documentation: Create comprehensive documentation for players.
    Developer Documentation: Maintain clear developer documentation.

Major Change Log

    Integrated DijjonAlphaDevelopment folder with Git: Enhanced tracking of progress.
    Refactoring player and NPC creation: Expanded classes and races, refactored to core library (1/6/2024).
    Race and class selection enumeration: Improved user input handling (Done).
    Changed attribute name convention for "int" in Player class: Resolved conflicts with int() function (Done).
    Integrated repository with GitHub: Improved version control and collaboration.

Story Arch Plans
Branching Choices

    Key Decision Points: Define moral, strategic, and information-based decisions.
    Consequences and Repercussions: Implement immediate, delayed, and subtle changes.

Random Elements

    Random Encounters: Introduce variability in challenges and opportunities.
    Luck-Based Elements: Incorporate dice rolls for certain outcomes.

Character Development and Relationships

    Emotional Ties: Affect NPC relationships based on player decisions.
    Reputation: Influence NPC interactions based on player's reputation.

Time-Sensitive Quests

    Seasonal and Time-Based Events: Include quests available during specific in-game times.
    Missable Quests: Opportunities that disappear if not acted upon.

Tracking Past Choices

    State Tracking: Log decisions and their outcomes.
    Dialogue Changes: Alter NPC dialogues based on player history.

Multiple Endings

    Cumulative Decisions: Plan multiple endings based on player choices.

Feedback and Adaptation

    Environmental Changes: Reflect player actions in the game world.
    NPC Adaptations: Change NPC strategies based on player reputation.