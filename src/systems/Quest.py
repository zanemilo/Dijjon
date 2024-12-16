# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest instances dynamically as to remove need to hard code quests.

from Event import Event  


class Quest(Event):
    """
    Quest Class for dynamically handling quest instances, inheriting from the Event class.

    Attributes:
        name (str): The name of the quest.
        description (str): A description of the quest.
        qtype (dict): Dictionary containing all possible quest/task types mapped to their corresponding methods.
        tasks (dict): Dictionary containing the tasks associated with the quest.
    """

    def __init__(self, name, description, qtype, tasks):
        """
        Initializes a new Quest instance with the given name, description, quest types, and tasks.

        Args:
            name (str): The name of the quest.
            description (str): A brief description of the quest.
            qtype (dict): A dictionary mapping quest/task types to their corresponding methods.
            tasks (dict): A dictionary containing the tasks associated with the quest.
        """
        super().__init__(name, description)  # Initialize the parent Event class with name and description
        self.qtype = qtype  # Dictionary of all possible quest/task types mapped to their methods
        self.tasks = tasks  # Dictionary of tasks associated with the quest
    
    def run_task(self, task_id):
        """
        Executes a task based on the provided task ID. Continuously runs until the task is marked as complete.

        Args:
            task_id (int): The identifier of the task to run.
        
        Note:
            This method utilizes a dispatcher pattern where quest/task types are mapped to their corresponding methods.
            It handles user interactions by presenting narrative and choices, executing scripts based on player choices.
        """
        # Retrieve the task dictionary for the given task_id
        task = self.tasks[task_id]
        
        # Continue running the task until it is marked as complete
        while task["complete"] != True:
            i = 1  # Initialize the narrative step index
            
            # Check if the task type exists in the qtype dispatcher
            if task["type"] in self.qtype:
                # Execute the method associated with the task type
                while self.qtype[task["type"]](self, task_id, self.tasks) == False:
                    # Iterate through the narrative steps of the task
                    while i <= len(task["narrative"]):
                        choice = None  # Initialize the player's choice
                        number_answers = []  # List to store valid numerical choices
                        
                        # Populate number_answers with string numbers corresponding to the answers
                        for k in range(1, len(task["answers"][i]) + 1):
                            number_answers.append(str(k))
                        
                        # Loop until the player makes a valid choice
                        while choice not in task["answers"][i] and choice not in number_answers:
                            # Display the current narrative step
                            print(task["narrative"][i])
                            j = 1  # Initialize the answer option index
                            print("Select an option:\n")
                            
                            # Display available answers/options for the current narrative step
                            for answer in task["answers"][i]:
                                print(f"{j}. {answer}")
                                j += 1
                            
                            # Prompt the player to make a choice
                            choice = str(input())
                            
                            # Update the task with the player's choice
                            task.update({"choice": choice})
                        
                        # Check if there is a script associated with the chosen answer
                        if task["scripts"][i] != None:
                            # Execute the associated script/method
                            task["scripts"][i](self, task_id, self.tasks)
                            i += 1  # Move to the next narrative step
                        else:
                            i += 1  # Move to the next narrative step without executing a script

    def complete_task(self, task_id, tasks):
        """
        Marks a task as complete.

        Args:
            task_id (int): The identifier of the task to mark as complete.
            tasks (dict): The dictionary containing all tasks.
        """
        self.tasks[task_id]["complete"] = True  # Set the 'complete' flag to True for the specified task

    def method_call1(self, task_id, tasks):
        """
        Placeholder method representing the first type of method call during a task.

        Args:
            task_id (int): The identifier of the current task.
            tasks (dict): The dictionary containing all tasks.
        """
        print(f"method call 1 called")
    
    def method_call2(self, task_id, tasks):
        """
        Placeholder method representing the second type of method call during a task.

        Args:
            task_id (int): The identifier of the current task.
            tasks (dict): The dictionary containing all tasks.
        """
        print(f"method call 2 called")

    def method_call3(self, task_id, tasks):
        """
        Placeholder method representing the third type of method call during a task.

        Args:
            task_id (int): The identifier of the current task.
            tasks (dict): The dictionary containing all tasks.
        """
        print(f"method call 3 called")
        print(f"setting task to complete")
        self.complete_task(task_id, tasks)  # Mark the task as complete
    
    def find(self, task_id, tasks):
        """
        Method to handle 'find' type tasks.

        Args:
            task_id (int): The identifier of the current task.
            tasks (dict): The dictionary containing all tasks.

        Returns:
            bool: True if the task is complete, False otherwise.
        """
        print(f"find called")
        return True if self.tasks[task_id]["complete"] else False

    def kill(self, task_id, tasks):
        """
        Method to handle 'kill' type tasks.

        Args:
            task_id (int): The identifier of the current task.
            tasks (dict): The dictionary containing all tasks.

        Returns:
            bool: True if the task is complete, False otherwise.
        """
        print(f"kill called")
        return True if self.tasks[task_id]["complete"] else False

    def skill_check(self, task_id, tasks):
        """
        Method to handle 'skill_check' type tasks.

        Args:
            task_id (int): The identifier of the current task.
            tasks (dict): The dictionary containing all tasks.

        Returns:
            bool: True if the task is complete, False otherwise.
        """
        print(f"skill_check called")
        return True if self.tasks[task_id]["complete"] else False

    def test_class(self):
        """
        Test method to demonstrate the functionality of the Quest class.

        Creates a test quest with predefined task types and tasks, then runs each task.

        Note:
            This method is for testing and demonstration purposes to show how the Quest class functions.
        """
        # Define a dispatcher mapping task types to their corresponding methods
        # FIX ME: This may better serve as a library of questtypes and associated
        # methods to observe specific quest completion requirements
        qtype = {
            "find": Quest.find, 
            "kill": Quest.kill, 
            "skill_check": Quest.skill_check,
        }
        
        # Define a dictionary of tasks associated with the quest
        tasks = {
            1: {
                "name": "Find Finn",
                "type": "find",
                "complete": False,
                "narrative": {
                    1: "You arrive at the bustling town square. People are hurrying by, but you can't shake the feeling that Finn is nearby.",
                    2: "You catch a glimpse of someone matching Finn's description heading towards the old tavern.",
                    3: "The tavern door creaks as you step inside, the air thick with the smell of ale and the sound of quiet conversation.",
                },
                "answers": {
                    1: ["look around", "scan the crowd", "watch from afar", "gaze through the people", "peek about", "take a gander"],
                    2: ["follow", "head to tavern"],
                    3: ["enter", "step inside"],
                },
                "scripts": {
                    1: Quest.method_call1,  # Call class method for script step 1
                    2: Quest.method_call2,  # Call method from imported Temp class for script step 2
                    3: Quest.method_call3,
                },
                "data": {
                    "pos": "town_square",
                },
            },
            2: {
                "name": "Kill 10 Goblins",
                "type": "kill",
                "complete": False,
                "narrative": {
                    1: "The forest is dark and silent, save for the rustling of leaves underfoot. You know goblins are near.",
                    2: "You hear guttural voices ahead. The goblins have set up a camp in a small clearing.",
                    3: "The goblins are alerted to your presence and draw their crude weapons, ready to fight.",
                },
                "answers": {
                    1: ["advance", "move quietly"],
                    2: ["observe", "prepare to attack"],
                    3: ["fight", "engage"],
                },
                "scripts": {
                    1: Quest.method_call1,
                    2: None,
                    3: Quest.method_call3,
                },
                "data": {
                    "amount": 10,
                    "entity": "goblin",
                },
            },
            3: {
                "name": "Persuade Donnie",
                "type": "skill_check",
                "complete": False,
                "narrative": {
                    1: "Donnie glares at you from across the table, his arms crossed defensively. He's not going to be easy to persuade.",
                    2: "You present your case, carefully choosing your words to avoid triggering Donnie's temper.",
                    3: "Donnie leans back, considering your words. You can tell he's wavering, but you need to close the deal.",
                },
                "answers": {
                    1: ["start with empathy", "mention common goals"],
                    2: ["explain benefits", "highlight risks"],
                    3: ["offer compromise", "ensure trust"],
                },
                "scripts": {
                    1: Quest.method_call1,
                    2: None,
                    3: Quest.method_call3,
                },
                "data": {
                    "skill": "persuasion",
                    "entity": "Donnie",
                },
            }
        }
        
        # Create a Quest instance with a name, description, quest types, and tasks
        quest = Quest("Test Quest", "This is a description for the test quest", qtype, tasks)  

        # Iterate through task IDs 1 to 3 and run each task
        for i in range(1, 4):
            quest.run_task(i)

# # For Testing and example of how this class functions see test_class method
# Quest.test_class(Quest)  # Calls the test_class method of Quest to demonstrate functionality
