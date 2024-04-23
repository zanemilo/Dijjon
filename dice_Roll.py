# Dijjon dice_Roll Class
# Developed & designed by: Zane M Deso
# Purpose: Simply used to simulate die roll according to what rolls would typically be made in DnD 5e

import random


# Function, create rolls list populated with 4 random integers between 1-6, then drops lowest value, then returns sum
def roll_stats():
    rolls = [random.randint(1, 6) for i in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

# dice roll functions
def roll_d4():
    return random.randint(1, 4)

def roll_d6():
    return random.randint(1, 6)

def roll_d8():
    return random.randint(1, 8)

def roll_d10():
    return random.randint(1, 10)

def roll_d12():
    return random.randint(1, 12)

def roll_d20():
    return random.randint(1, 20)

def roll_d100():
    return random.randint(1, 100)