import random as r

class Settings:
    """A class to store all settings for Dijjon"""

    def __init__(self, current_difficulty):
        """Initialize game settings"""
        self.current_difficulty = current_difficulty

    def check(self, check_type):
        """Handles validating check types and calculating DC amount based on randint range and current_difficulty settings"""

        valid_types = [
        'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 
        'history', 'insight', 'intimidation', 'investigation', 'medicine', 
        'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 
        'stealth', 'survival', 'str','dex', 'con', 'int', 'wis', 'cha']

        check_dc = 0

        if check_type.lower() in valid_types:
            check_dc = r.randint(5, 13) + self.current_difficulty
            return check_dc
            
# # Settings instance for testing
# settings = Settings(2)
# history_check = settings.check("history") # test history check

# print(f'History check DC: {history_check}') # Print test results



            
            
        
