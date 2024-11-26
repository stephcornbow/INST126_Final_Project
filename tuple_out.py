"""
Tuple Out Dice Game
This program simulates the "Tuple Out" dice game where players take turns rolling dice to score points.
The game continues until a player reaches the target score.
"""

import random  # Used for generating random dice rolls
import sys     # Used for handling command-line arguments
from collections import Counter  # Used for counting dice value

def roll_dice(num_dice=3):
    """
    Rolls a specified number of dice and returns the results as a list.

    Args:
        num_dice (int): Number of dice to roll. Default is 3.

    Returns:
        list: A list containing the results of the dice rolls.
    """
    return [random.randint(1, 6) for _ in range(num_dice)]

def display_scores(scores):
    """
    Displays the current scores of all players.

    Args:
        scores (dict): A dictionary containing player names and their scores.
    """
    print("\nCurrent Scores:")
    for player, score in scores.items():
        print("{0}: {1}".format(player, score))  # FIX for ANTI 0.1.1: Replaced f-string with string concatenation

def get_user_choice(prompt, choices):
    """
    Prompts the user to make a choice from the provided options.

    Args:
        prompt (str): The message displayed to the user.
        choices (list): A list of valid choices.

    Returns:
        str: The user's validated choice.
    """
    while True:
        choice = input(prompt).lower()  
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please choose from " + str(choices) + ".")  # FIX for ANTI 0.1.1: Replaced f-string with string concatenation
