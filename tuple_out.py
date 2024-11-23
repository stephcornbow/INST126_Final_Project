"""
Tuple Out Dice Game
This program simulates the "Tuple Out" dice game where players take turns rolling dice to score points.
The game continues until a player reaches the target score.
"""

# PATT 3.1: imported (and used) a Standard Library module
import random  # Used for generating random dice rolls
import sys     # Used for handling command-line arguments
from collections import Counter  # Used for counting dice values


def roll_dice(num_dice=3):
    """
    Rolls a specified number of dice and returns the results as a list.

    Args:
        num_dice (int): Number of dice to roll. Default is 3.

    Returns:
        list: A list containing the results of the dice rolls.
    """
    # PATT 2.3: used correct function definition syntax
    return [random.randint(1, 6) for _ in range(num_dice)]
