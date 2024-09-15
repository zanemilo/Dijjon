import unittest
from scripts.game_mechanics.Quest import Quest

class TestQuest(unittest.TestCase):
    def setUp(self):
        """
        Set up the necessary components for the tests.
        """
        self.quest = Quest("Test Quest", "Description", "Main", ["Task 1", "Task 2"])
    
    def test_quest_initialization(self):
        """
        Test the initialization of a quest.
        """
        self.assertEqual(self.quest.name, "Test Quest")
        self.assertEqual(self.quest.description, "Description")
        self.assertEqual(self.quest.qtype, "Main")
        self.assertEqual(len(self.quest.tasks), 2)
    
    def tearDown(self):
        """
        Clean up after tests.
        """
        self.quest = None

if __name__ == '__main__':
    unittest.main()
