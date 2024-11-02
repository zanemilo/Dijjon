import unittest
import core.master as m
from scripts.entities.Player import Player
from core.core_library import classes as cls
from core.core_library import races as rc
import random as r

class TestMasterFunctions(unittest.TestCase):
    def setUp(self):
        """
        Set up the necessary components for the tests.
        """
        self.master = m.Master()
        self.bandit = Player('Bandit', r.choice(list(rc)), r.choice(list(cls)), is_enemy=True)
    
    def test_sheet_display(self):
        """
        Test the display of the character sheet.
        """
        # This test might need to check the output or a side effect
        self.master.sheet(self.bandit)
        # Assert conditions if possible, or manually verify the output

    def tearDown(self):
        """
        Clean up after tests.
        """
        self.master = None
        self.bandit = None

if __name__ == '__main__':
    unittest.main()
