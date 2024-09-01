# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle quest instances dynamically as to remove need to hard code quests.


import scripts.game_mechanics.Event as Event


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
                                            #   },
                                            #   2 : {
                                            #     "name" : "Go to the well",
                                            #     "year" : 2007
                                            #   },
                                            #   3 : {
                                            #     "name" : "Linus",
                                            #     "year" : 2011
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
        while self.tasks[task_id]["complete"] != True:
            if task["type"] in self.qtype:
                while self.qtype[task["type"]]() == False:  # Call the task type method call
                    i = 1
                    while i < len(task["narrative"]):
                        choice = None
                        while choice not in task["answers"]:
                            print(task["narrative"][i])
                            j = 1
                            print("Select an option:\n")
                            for answer in task["answers"][i]:
                                print(f"{j}. {answer}")
                                j += 1
                            choice = input()
                        if task["script"][i] != None:
                            task["script"][i]()
                        else:
                            i += 1


