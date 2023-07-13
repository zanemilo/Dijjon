

class Settings:
    """A class to store all settings for Dijjon"""

    def __init__(self):
        """Initialize game settings"""
    


        # difficulty settings
        def difficulty(self):
            """this can be accessed or referenced while building mobs, weighting an event for example, a mob in normal may have d20 + 0 while very_hard is d20 + 4"""
            self.cant_lose = -30 # still possible to lose, fail, die
            self.easy = -1
            self.normal = 0
            self.hard = 2
            self.very_hard = 4
            self.cant_win = 30 # still possible to win or suceed, damn near impossible tho

            
            
        
