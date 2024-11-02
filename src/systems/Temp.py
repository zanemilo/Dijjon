# File: Temp.py
# Author: Zane M Deso
# Purpose: Serve as a imported method test point for other classes to call from.

class Temp:
    def __init__(self):
        pass

    def blip(self, task_id, tasks):
        task = tasks[task_id]
        print(f'blip: {task["data"]}')