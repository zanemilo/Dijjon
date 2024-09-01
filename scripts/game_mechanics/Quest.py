# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest instances dynamically as to remove need to hard code quests.


from Event import Event


class Quest(Event):
    def __init__(self, name, description, qtype, tasks):
        super().__init__(name, description)
        self.qtype = qtype  # Dict of all possible quest/task types = {"find": find, "go": go, "kill_all": kill_all} to check for to call proper method call to check for taks completion
        self.tasks = tasks  # Dict of tasks = { 1 : {
                                            #     "name" : "Find Finn",
                                            #     "type" : "find",
                                            #     "complete" : False,
                                            #     "narrative" {
                                            #     1 : "lorem",
                                            #     2 : "impsum",
                                            #     3 : "lorem-impsum",
                                            #     },
                                            #     "answers" {
                                            #     1 : ["lorem", ],
                                            #     2 : ["impsum", "lorem",],
                                            #     3 : ["lorem-impsum", "lorem",],
                                            #     },
                                            #     "scripts" {
                                            #     1 : method_object1,
                                            #     2 : None,
                                            #     3 : method_object3,
                                            #     },
                                            #     "data" {
                                            #     "pos": "town_square"
                                            #     },
                                            #   },
                                            #   2 : {
                                            #     "name" : "Kill 10 Goblins",
                                            #     "type" : "kill",
                                            #     "complete" : False,
                                            #     "narrative" {
                                            #     1 : "lorem",
                                            #     2 : "impsum",
                                            #     3 : "lorem-impsum",
                                            #     },
                                            #     "answers" {
                                            #     1 : ["lorem", ],
                                            #     2 : ["impsum", "lorem",],
                                            #     3 : ["lorem-impsum", "lorem",],
                                            #     },
                                            #     "scripts" {
                                            #     1 : method_object1,
                                            #     2 : None,
                                            #     3 : method_object3,
                                            #     },
                                            #     "data" {
                                            #     "amount": "10",
                                            #     "entity": "goblin"
                                            #     },
                                            #   },
                                            #   3 : {
                                            #     "name" : "Persuade Donnie",
                                            #     "type" : "skill_check",
                                            #     "complete" : False,
                                            #     "narrative" {
                                            #     1 : "lorem",
                                            #     2 : "impsum",
                                            #     3 : "lorem-impsum",
                                            #     },
                                            #     "answers" {
                                            #     1 : ["lorem", ],
                                            #     2 : ["impsum", "lorem",],
                                            #     3 : ["lorem-impsum", "lorem",],
                                            #     },
                                            #     "scripts" {
                                            #     1 : method_object1,
                                            #     2 : None,
                                            #     3 : method_object3,
                                            #     },
                                            #     "data" {
                                            #     "skill": "persuasion",
                                            #     "entity": Donnie,
                                            #     },
                                            #   }
                                            # } 
        
    # Note on calling methods from a dictionary: Credit to Praveen Gollakota on Stackoverflow, Feb 9, 2012
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

    # fire_all(dispatcher['foobar'])


    def run_task(self, task_id):
        task = self.tasks[task_id]
        while task["complete"] != True:
            i = 1
            if task["type"] in self.qtype:
                while self.qtype[task["type"]](self) == False:  # Call the task type method call
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
                            task["scripts"][i](self)
                            i += 1
                        else:
                            i += 1
    
    def complete_task(self, task_id):
        task = self.tasks[task_id]
        task["complete"] = True

    def method_call1(self):
        print(f"method call 1 called")
    
    def method_call2(self):
        print(f"method call 2 called")

    def method_call3(self):
        print(f"method call 3 called")
    
    def find(self):
        print(f"find called")
        return False

    def kill(self):
        print(f"kill called")
        return True

    def skill_check(self):
        print(f"skill_check called")
        return True


qtype = {"find": Quest.find, "kill": Quest.kill, "skill_check": Quest.skill_check,}
tasks = { 1 : {
                                                "name" : "Find Finn",
                                                "type" : "find",
                                                "complete" : False,
                                                "narrative": {
                                                1 : "lorem",
                                                2 : "impsum",
                                                3 : "lorem-impsum",
                                                },
                                                "answers": {
                                                1 : ["lorem", ],
                                                2 : ["impsum", "lorem",],
                                                3 : ["lorem-impsum", "lorem",],
                                                },
                                                "scripts": {
                                                1 : Quest.method_call1,
                                                2 : None,
                                                3 : Quest.method_call3,
                                                },
                                                "data": {
                                                "pos": "town_square"
                                                },
                                              },
                                              2 : {
                                                "name" : "Kill 10 Goblins",
                                                "type" : "kill",
                                                "complete" : False,
                                                "narrative": {
                                                1 : "lorem",
                                                2 : "impsum",
                                                3 : "lorem-impsum",
                                                },
                                                "answers": {
                                                1 : ["lorem", ],
                                                2 : ["impsum", "lorem",],
                                                3 : ["lorem-impsum", "lorem",],
                                                },
                                                "scripts": {
                                                1 : Quest.method_call1,
                                                2 : None,
                                                3 : Quest.method_call3,
                                                },
                                                "data": {
                                                "amount": "10",
                                                "entity": "goblin"
                                                },
                                              },
                                              3 : {
                                                "name" : "Persuade Donnie",
                                                "type" : "skill_check",
                                                "complete" : False,
                                                "narrative": {
                                                1 : "lorem",
                                                2 : "impsum",
                                                3 : "lorem-impsum",
                                                },
                                                "answers": {
                                                1 : ["lorem", ],
                                                2 : ["impsum", "lorem",],
                                                3 : ["lorem-impsum", "lorem",],
                                                },
                                                "scripts": {
                                                1 : Quest.method_call1,
                                                2 : None,
                                                3 : Quest.method_call3,
                                                },
                                                "data": {
                                                "skill": "persuasion",
                                                "entity": "Donnie",
                                                },
                                              }
                                            }
quest = Quest("Test Quest", "This is a description for the test quest", qtype, tasks)  

quest.run_task(1)
