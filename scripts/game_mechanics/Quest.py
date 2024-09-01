# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest instances dynamically as to remove need to hard code quests.


from Event import Event


class Quest(Event):
    def __init__(self, name, description, qtype, tasks):
        super().__init__(name, description)
        self.qtype = qtype  # Dict of all possible quest/task types
        self.tasks = tasks  # Dict of tasks 
        
    


    def run_task(self, task_id):
        """# Note on calling methods from a dictionary: Credit to Praveen Gollakota on Stackoverflow, Feb 9, 2012
    # https://stackoverflow.com/questions/9205081/is-there-a-way-to-store-a-function-in-a-list-or-dictionary-so-that-when-the-inde
        

    # Functions are first class objects in Python and so you can dispatch using a dictionary. For example, if foo and bar are functions, and dispatcher is a dictionary like so.

    # dispatcher = {'foo': foo, 'bar': bar}

    # Note that the values are foo and bar which are the function objects, and NOT foo() and bar().

    # To call foo, you can just do dispatcher['foo']()

    # EDIT: If you want to run multiple functions stored in a list, you can possibly do something like this.

    # dispatcher = {'foobar': [foo, bar], 'bazcat': [baz, cat]}

    # def fire_all(func_list):
    #     for f in func_list:
    #         f()

    # fire_all(dispatcher['foobar'])"""
        task = self.tasks[task_id]
        while task["complete"] != True:
            i = 1
            if task["type"] in self.qtype:
                while self.qtype[task["type"]](self, task_id) == False:  # Call the task type method call
                    while i <= len(task["narrative"]):
                        choice = None
                        while choice not in task["answers"][i]:
                            print(task["narrative"][i])
                            j = 1
                            print("Select an option:\n")
                            for answer in task["answers"][i]:
                                print(f"{j}. {answer}")
                                j += 1
                            choice = input()
                        if task["scripts"][i] != None:
                            task["scripts"][i](self, task_id)
                            i += 1
                        else:
                            i += 1
    
    def complete_task(self, task_id):
        self.tasks[task_id]["complete"] = True

    def method_call1(self, task_id):
        print(f"method call 1 called")
    
    def method_call2(self, task_id):
        print(f"method call 2 called")

    def method_call3(self, task_id):
        print(f"method call 3 called")
        print(f"setting task to complete")
        self.complete_task(task_id)
    
    def find(self, task_id):
        print(f"find called")
        return True if self.tasks[task_id]["complete"] else False

    def kill(self, task_id):
        print(f"kill called")
        return True if self.tasks[task_id]["complete"] else False

    def skill_check(self, task_id):
        print(f"skill_check called")
        return True if self.tasks[task_id]["complete"] else False

    def test_class(self):
        qtype = {"find": Quest.find, "kill": Quest.kill, "skill_check": Quest.skill_check,}
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
                    1: ["look around", "scan the crowd"],
                    2: ["follow", "head to tavern"],
                    3: ["enter", "step inside"],
                },
                "scripts": {
                    1: Quest.method_call1,
                    2: None,
                    3: Quest.method_call3,
                },
                "data": {
                    "pos": "town_square"
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
                    "entity": "goblin"
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
        quest = Quest("Test Quest", "This is a description for the test quest", qtype, tasks)  

        for i in range(1, 4):
            quest.run_task(i)

# For Testing and example of how this class functions see test_class method
# Quest.test_class(Quest)