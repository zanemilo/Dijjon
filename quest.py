import main

class Quest():


    def __init__(self, name, objectives, reward, completion_status):
        self.name = name
        self.objectives = objectives
        self.reward = reward
        self.completion_status = completion_status

    def create_quest():  #Quest Generation: Create a function that generates quests based on certain criteria, such as the player's level, location, and faction affiliation. This function can randomly select a quest template from a pool of pre-defined quests and fill in the details based on the criteria.
        if playerOne.level == 1:
            print("LEVEL 1 DETECTED")
            print(f"Generating level {playerOne.level} quest for {playerOne.name}\n")


        elif playerOne.level == 2:
            print("LEVEL 2 DETECTED")
            print(f"Generating level {playerOne.level} quest for {playerOne.name}\n")


        else:
            print("LEVEL 3 or greator DETECTED")
            print(f"Generating level {playerOne.level} quest for {playerOne.name}\n")