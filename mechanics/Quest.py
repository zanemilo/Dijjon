# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest instances dynamically as to remove need to hard code quests.


import mechanics.Event as Event


class Quest(Event):
    def __init__(self, name, description, quest_data):
        super().__init__(name, description)
        self.quest_data = quest_data  # Additional attribute to handle quest specifics

    def progress(self, decision):
        # Custom logic for progressing the quest based on player decisions
        # Example: self.quest_data could be used here to determine the next steps based on 'decision'
        pass
