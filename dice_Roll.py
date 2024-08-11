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
    return random.randint(1, 4) * 4999 % 4 + 1

def roll_d6():
    return random.randint(1, 6) * 4999 % 6 + 1

def roll_d8():
    return random.randint(1, 8) * 4999 % 8 + 1

def roll_d10():
    return random.randint(1, 10) * 4999 % 10 + 1

def roll_d12():
    return random.randint(1, 12) * 4999 % 12 + 1

def roll_d20():
    return random.randint(1, 20) * 4999 % 20 + 1

def roll_d100():
    return random.randint(1, 100) * 4999 % 100 + 1

def test_rolls():
    print(f"D4: {roll_d4()}")
    print(f"D6: {roll_d6()}")
    print(f"D8: {roll_d8()}")
    print(f"D10: {roll_d10()}")
    print(f"D12: {roll_d12()}")
    print(f"D20: {roll_d20()}")
    print(f"D100: {roll_d100()}")

test_rolls()