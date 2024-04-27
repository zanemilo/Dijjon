# Dijjon Visibility Class
# Developed & designed by: Zane M Deso
# Purpose: Compositional Relationship with Player Class. Handles visibility calculations

class Visibility:
    def __init__(self, level='normal', special_senses=[]):
        self.level = level  # normal, dim, darkness
        self.special_senses = special_senses  # e.g., ['darkvision', 'truesight']

    def update_visibility(self, environment_condition):
        if 'darkness' in environment_condition and 'darkvision' not in self.special_senses:
            self.level = 'blinded'
        elif 'fog' in environment_condition:
            self.level = 'obscured'
        else:
            self.level = 'normal'

    def check_visibility(self):
        return self.level
