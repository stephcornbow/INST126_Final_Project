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

def play_turn(player, scores, target_score):
    """
    Executes a single turn for a player.

    Args:
        player (str): The name of the current player.
        scores (dict): The current scores of all players.
        target_score (int): The score needed to win the game.
    """
    print("\n" + player + "'s turn:")  # FIX for ANTI 0.1.1: Replaced f-string with string concatenation
    fixed_dice = []
    total_points = 0

    while True:
        num_dice_to_roll = 3 - len(fixed_dice)
        current_roll = roll_dice(num_dice_to_roll)
        print(player + " rolled: " + str(current_roll + fixed_dice))  # FIX for ANTI 0.1.1: Replaced f-string with string concatenation

        # Count occurrences of each die using Counter
        counts = Counter(current_roll + fixed_dice)

        # Check for tuples
        if any(count == 3 for count in counts.values()):
            print(player + " has tupled out! Scores 0 points this turn.")  # FIX for ANTI 0.1.1: Replaced f-string with string concatenation
            return

        # Fix dice with two of the same value
        new_fixed = [die for die, count in counts.items() if count == 2]
        if new_fixed:
            fixed_dice = new_fixed
            print("Fixed dice: " + str(fixed_dice))  # FIX for ANTI 0.1.1: Replaced f-string with string concatenation

        total_points = sum(current_roll) + sum(fixed_dice)
        print("Total points this turn: " + str(total_points))  # FIX for ANTI 0.1.1: Replaced f-string with string concatenation

        # Ask to continue or stop
        choice = get_user_choice("Do you want to (r)eroll or (s)top? ", ['r', 's'])
        if choice == 's':
            scores[player] += total_points
            print(player + " ends their turn with " + str(total_points) + " points.")  # FIX for ANTI 0.1.1: Replaced f-string with string concatenation
            return