# Dijjon quest_journal Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest creation, rewards, main objectives, task, each task status, completion requirement and other associated player centered functions.

from typing import Dict, List, Optional, Any

from Quest import Quest


class QuestJournal:
    """
    Journal for tracking multiple quests, organized by priority.

    Attributes:
        _journal (Dict[str, List[Quest]]): Quests grouped under 'primary', 'secondary', and 'misc'.
    """

    def __init__(self) -> None:
        """
        Initialize an empty QuestJournal with predefined priority buckets.
        """
        # Prepare empty lists for each priority category
        self._journal: Dict[str, List[Quest]] = {
            'primary': [],
            'secondary': [],
            'misc': []
        }

    def add_quest(self, quest: Quest) -> None:
        """
        Add a Quest to the journal under its priority.

        Args:
            quest: Instance of Quest, which must have a valid `priority` attribute.

        Raises:
            ValueError: If quest.priority is not one of the journal categories.
        """
        prio = quest.priority
        if prio not in self._journal:
            raise ValueError(f"Unknown quest priority '{prio}'")
        self._journal[prio].append(quest)

    def remove_quest(self, name: str) -> bool:
        """
        Remove a quest by its name across all priority groups.

        Args:
            name: The unique name of the quest to remove.

        Returns:
            True if removed successfully; False if no matching quest found.
        """
        for prio, quests in self._journal.items():
            for i, q in enumerate(quests):
                if q.name == name:
                    del quests[i]
                    return True
        return False

    def find_quest(self, name: str) -> Optional[Quest]:
        """
        Find and return a Quest by name.

        Args:
            name: The unique name of the quest to locate.

        Returns:
            The Quest instance if found; otherwise, None.
        """
        for quests in self._journal.values():
            for q in quests:
                if q.name == name:
                    return q
        return None

    def mark_complete(self, name: str) -> bool:
        """
        Mark the specified quest as complete (all its tasks).

        Args:
            name: The unique name of the quest to mark complete.

        Returns:
            True if quest found and marked; False otherwise.
        """
        quest = self.find_quest(name)
        if not quest:
            return False
        # Mark all tasks as complete
        for idx, task in enumerate(quest.tasks):
            quest.complete_task(idx)
        return True

    def get_quests_by_priority(self, priority: str) -> List[Quest]:
        """
        Retrieve the list of quests for a given priority.

        Args:
            priority: One of 'primary', 'secondary', or 'misc'.

        Returns:
            List of Quest instances under that priority.

        Raises:
            ValueError: If priority is invalid.
        """
        if priority not in self._journal:
            raise ValueError(f"Unknown quest priority '{priority}'")
        return list(self._journal[priority])

    def get_all_quests(self) -> Dict[str, List[Quest]]:
        """
        Get the full journal of quests, grouped by priority.

        Returns:
            A dict mapping each priority to its list of quests.
        """
        # Return a shallow copy to prevent external mutation
        return {prio: list(qs) for prio, qs in self._journal.items()}

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize the journal to plain data structures.

        Returns:
            Dict where keys are priorities and values are lists of quest dicts.
        """
        return {
            prio: [q.to_dict() for q in quests]
            for prio, quests in self._journal.items()
        }

