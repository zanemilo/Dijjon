import Player as p

class Master:
    """Class for actions or deciscions a DM would typically make in the overarching gameplay, story etc."""

    def sheet(character): 
        """Generate and display the character sheet"""
    
        #dictionary of character instance's stats used for sheet to pull updated info
        stats = {
        "STR": character.str,
        "DEX": character.dex,
        "CON": character.con,
        "INT": character.int,
        "WIS": character.wis,
        "CHA": character.cha,
        "HP": character.hp,
        "AC": character.arm_c,
        "GP": character.gold,
        "SPD": character.spd,
        "LEVEL": character.lvl,
        "XP" : character.xp,
        }

        # This may be redundant, will need to test
        stats["STR"] = character.str
        stats["DEX"] = character.dex
        stats["CON"] = character.con
        stats["INT"] = character.int
        stats["WIS"] = character.wis
        stats["CHA"] = character.cha
        stats["HP"] = character.hp
        stats["AC"] = character.arm_c
        stats["GP"] = character.gold
        stats["SPD"] = character.spd
        stats["LEVEL"] = character.lvl
        stats["XP"] = character.xp

        print(f"""\n
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        | NAME: {character.name.upper().center(39)}   |
        | RACE: {character.race.upper().center(39)}   |
        | CLASS: {character.char_class.upper().center(38)}   |
        | LEVEL: {stats['LEVEL']}{' '*(2-len(str(stats['LEVEL'])))}                                       |
        |                                                 |
        | STR: {stats['STR']}{' '*(2-len(str(stats['STR'])))} | DEX: {stats['DEX']}{' '*(2-len(str(stats['DEX'])))} | CON: {stats['CON']}{' '*(2-len(str(stats['CON'])))} | INT: {stats['INT']}{' '*(2-len(str(stats['INT'])))} | WIS: {stats['WIS']}{' '*(2-len(str(stats['WIS'])))} | 
        | CHA: {stats['CHA']}{' '*(2-len(str(stats['CHA'])))} |                                       |
        | ARMOR CLASS: {stats['AC']}{' '*(2-len(str(stats['AC'])))} | SPEED: {stats['SPD']}{' '*(2-len(str(stats['SPD'])))}                     |
        |                                                 |
        | HIT POINTS: {stats['HP']}{' '*(2-len(str(stats['HP'])))} | SPELL SLOTS: {'0'+' '*(2-len('2'))}                |
        |                                                 |
        | GOLD: {stats['GP']}{' '*(2-len(str(stats['GP'])))} | XP: {stats['XP']}{' '*(2-len(str(stats['XP'])))}                               |
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        \n\n\n\n""")