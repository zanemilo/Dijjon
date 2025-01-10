from ..core import settings

class InteractionManager:
    """
    InteractionManager class for handling interactions between entities. 
    """

    def __init__(self):
        pass

    def check(self, check_type, player_roll, bias=r.randint(1, 18)):  # passed testing in new main
        """
        Handle validating different types of checks and calculate the Difficulty Class (DC).

        This function determines whether a player's roll meets or exceeds the DC required for a specific check type.

        Args:
            check_type (str): The type of check being performed (e.g., 'acrobatics', 'strength').
            player_roll (int): The result of the player's roll.
            bias (int, optional): A bias value added to the DC. Defaults to a random integer between 1 and 18.

        Returns:
            bool: True if the player's roll is sufficient to pass the check, False otherwise.
        """
        check_type = check_type.lower()  # Convert check type to lowercase for consistency
        valid_types = [
            'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 
            'history', 'insight', 'intimidation', 'investigation', 'medicine', 
            'nature', 'perception', 'performance', 'persuasion', 'religion', 'sleight_of_hand', 
            'stealth', 'survival', 'str','dex', 'con', 'int', 'wis', 'cha']  # List of valid check types

        check_dc = 0  # Initialize difficulty class
        passed_check = False  # Initialize check result

        if check_type.lower() in valid_types:
            # Calculate the difficulty class (DC) based on bias and settings
            check_dc = bias + settings.current_difficulty + settings.location_difficulty
            # print(f'Check DC: {check_dc}')  # Debug print statement
            if player_roll >= check_dc:
                passed_check = True  # Player passes the check if roll meets or exceeds DC

            return passed_check  # Return the result of the check
        
    def skill_check_test(self):
        """
        Tests various skill checks and opposing checks between the player and a bandit.
        Used for a means to quickly test fucntionality in main.

        Steps:
        1. Instantiates a bandit player with random race and class.
        2. Displays the bandit's character sheet.
        3. Performs and prints the results of dexterity and investigation checks for the player.
        4. Determines and prints the winner of a strength-based opposing check between the player and the bandit.
        """
        # Instantiate a new bandit player with random race and class, marked as an enemy
        bandit = p.Player('Bandit', r.choice(list(races)), r.choice(list(classes)), is_enemy=True)
        
        # Display the bandit's character sheet using the Master class
        bandit.sheet()
        
        # Perform a dexterity check for the player and print the result
        dex_passed = self.check("dex", player.player_check_roll("dex"))
        print(f'Did {player.get_name()} pass the dex Check?: {dex_passed}')
        
        # Perform an investigation check for the player and print the result
        investigation_passed = check("investigation", player.player_check_roll("investigation"))
        print(f'Did {player.get_name()} pass the investigation Check?: {investigation_passed}')
        
        # Conduct an opposing strength check between the player and the bandit and print the winner
        winner = self.opposing_check(player, bandit, "str")
        print(f'The winner of the opposing check is: {winner}')

    def opposing_check(self, entity_one, enitity_two, check_type):  # passed testing in new main
            """
            Conduct a check between two opposing Player instances based on a specific check type.

            Args:
                entity_one (Player): The first player entity.
                enitity_two (Player): The second player entity.
                check_type (str): The type of check to perform (e.g., 'strength', 'dexterity').

            Returns:
                str: The name of the entity that wins the check.
            """
            # Perform a check for entity one using their roll for the specified check type
            e_one_roll = self.check(check_type, entity_one.player_check_roll(check_type))  # FIX ME: To adjust this once I have used inheritance correctly,
            # Perform a check for entity two using their roll for the specified check type
            e_two_roll = self.check(check_type, enitity_two.player_check_roll(check_type))  # just use the check_roll method associated from the parent class

            if e_one_roll < e_two_roll:
                return enitity_two.get_name()  # Return entity two's name if they win the check
            elif e_two_roll < e_one_roll:
                return entity_one.get_name()  # Return entity one's name if they win the check
            elif e_one_roll == e_two_roll:
                return self.opposing_check(entity_one, enitity_two, check_type)  # Repeat the check in case of a tie
      