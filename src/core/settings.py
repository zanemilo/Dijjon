# Dijjon Quest Class
# Developed & designed by: Zane M Deso
# Purpose: Used to handle settings for the game.


class Settings:
    """A class to store all settings for Dijjon"""

    def __init__(self, current_difficulty = 2, location_difficulty = 0):
        """Initialize game settings"""
        self.current_difficulty = current_difficulty
        self.location_difficulty = location_difficulty

    
    def get_diff(self):
        """Returns current difficulty"""
        return self.current_difficulty
    
    def set_diff(self, difficulty):
        """Change current difficulty"""

        if difficulty in range(1, 11):
            self.current_difficulty = difficulty
        else:
            print(f'Error: Difficulty arg out of range (1-10)\nDifficulty remains unchanged.')

    def get_loc_diff(self):
        return self.current_difficulty
    
    def set_loc_diff(self, difficulty):
        
        valid_difficulties = [0, 1, 2, 3, 4, 5]

        if difficulty in valid_difficulties:
            self.current_difficulty = difficulty
        elif difficulty not in valid_difficulties:
            print(f'Error: Location difficulty arg out of range (0-5)\nLocation difficulty remains unchanged.')
        



            
            
        
