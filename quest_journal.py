# Dijjon quest_journal Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest creation, rewards, main objectives, task, each task status, completion requirement and other associated player centered functions.
# EDIT: I am considering using this as a quest journal instead as to track quest statuses, display them etc for the player to analyze. Will refactor into quest_journal
# and create a new quest class that will be the subclass to Event.

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

        self.quests = { # This dict separates each quest type where primary is non optional, secondary is usually a requirment to complete before finishing primary and misc is completely optional
            'primary' : {},
            'secondary' : {},
            'misc' : {}
        }


    def get_all_quest_status(self):
        """Return all quest status"""
        print(f'{self.quests}')
        return self.quests

    def add_quest_tracker(self, priority):
        """Used during instatiation to place into proper priority tracker ['primary', 'secondary', or 'misc']"""
        if priority == 'primary':
            self.quests['primary'] = self.info
        elif priority == 'secondary':
            self.quests['secondary'] = self.info
        elif priority == 'misc':
            self.quests['misc'] = self.info
        else:
            print(f'Error while adding {self.quest_name} to quest tracker')
            print(priority)

     # Accessor functions
    def get_quest_name(self):
        """Return the quest name."""
        return self.quest_name

    def get_objective(self):
        """Return the quest objective."""
        return self.objective

    def get_task(self):
        """Return the current task for the quest."""
        return self.task

    def get_reward(self):
        """Return the quest reward."""
        return self.reward

    def get_completion(self):
        """Return the completion status of the quest."""
        return self.completion

    def get_priority(self):
        """Return the priority of the quest."""
        return self.priority

    def get_info(self):
        """Return a dictionary containing quest information."""
        return self.info

    def get_all_quests(self):
        """Return the dictionary containing all quests."""
        return self.quests

    # Mutator functions
    def set_task(self, new_task):
        """Set a new task for the quest."""
        self.task = new_task
        self.info['task'] = new_task

    def set_completion(self, new_completion):
        """Set the completion status of the quest."""
        self.completion = new_completion
        self.info['completion'] = new_completion

    def set_priority(self, new_priority):
        """Set the priority of the quest."""
        self.priority = new_priority
        self.info['priority'] = new_priority

    def set_reward(self, new_reward):
        """Set a new reward for the quest."""
        self.reward = new_reward
        self.info['reward'] = new_reward


# # test quest instances
# starter_quest = Quest('Humble Beginnings', 'Find your way to the docks.', False, 'Big Fish', 'primary')
# starter_quest.add_quest_tracker(starter_quest.priority)     
# print(starter_quest.get_info())

# find_boat_quest = Quest('Find a boat', 'Find a Boat', False, 'Boat', 'secondary')
# find_boat_quest.add_quest_tracker(find_boat_quest.priority)  
# print(find_boat_quest.get_info())

# next_quest = Quest('Second is the Worst', 'Navigate the open sea.', False, 'Pearl', 'primary')
# next_quest.add_quest_tracker(next_quest.priority)
# print(next_quest.get_info())



