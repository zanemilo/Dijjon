

class Quest():


    def __init__(self, quest_name, objective, completion, reward, priority='misc', task=''):
        """Quest Class for handling building quest and tracking quest progress."""

        self.quest_name = quest_name
        self.objective = objective
        self.task = task
        self.reward = reward
        self.completion = completion
        self.priority = priority

        self.info = {
            'quest Name' : self.quest_name,
            'objective' : self.objective,
            'task' : self.task,
            'reward' : self.reward,
            'completion' : self.completion,
        }

        self.quests = { 
            'primary' : {},
            'secondary' : {},
            'misc' : {}
        }

        

    def check_quest_status(self):
        """Return instance quest info"""
        print(f'{self.info}')
        return self.info

    def check_all_quest_status(self):
        """Return all quest status"""
        print(f'{self.quests}')
        return self.quests

    def add_quest_tracker(self, priority):
        """Used during  instatiation to place into proper priority tracker"""
        self.new_quest = {}
        self.new_quest = self.info
        if priority == 'primary':
            self.quests['primary'] = self.new_quest
        elif priority == 'secondary':
            self.quests['secondary'] = self.new_quest
        elif priority == 'misc':
            self.quests['misc'] = self.new_quest
        else:
            print(f'Error while adding {self.quest_name} to quest tracker')
            print(priority)

        

    # def create_quest():  #Quest Generation: Create a function that generates quests based on certain criteria, such as the player's level, location, and faction affiliation. This function can randomly select a quest template from a pool of pre-defined quests and fill in the details based on the criteria.
    #     if m.playerOne.level == 1:
    #         print("LEVEL 1 DETECTED")
    #         print(f"Generating level {m.playerOne.level} quest for {m.playerOne.name}\n")


    #     elif m.playerOne.level == 2:
    #         print("LEVEL 2 DETECTED")
    #         print(f"Generating level {m.playerOne.level} quest for {m.playerOne.name}\n")


    #     else:
    #         print("LEVEL 3 or greator DETECTED")
    #         print(f"Generating level {m.playerOne.level} quest for {m.playerOne.name}\n")

# test quest instance
starter_quest = Quest('Humble Beginnings', 'Find your way to the docks.', False, 'Big Fish', 'primary')

starter_quest.add_quest_tracker(starter_quest.priority)
        
Quest.check_all_quest_status(starter_quest)



