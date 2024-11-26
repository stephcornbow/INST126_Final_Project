"""
Utility Module for Tuple Out Dice Game
This module contains utility functions used in the Tuple Out Dice Game.
"""

import json
import os

def save_high_score(player, score, filename="high_scores.json"):
    """
    Saves the high score of a player to a JSON file.

    Args:
        player (str): The name of the player.
        score (int): The score achieved by the player.
        filename (str): The filename to save the high scores. Default is 'high_scores.json'.
    """
    high_scores = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                high_scores = json.load(file)
            except json.JSONDecodeError:
                high_scores = {}

    if player in high_scores:
        if score > high_scores[player]:
            high_scores[player] = score
    else:
        high_scores[player] = score

    with open(filename, 'w') as file:
        json.dump(high_scores, file, indent=4)

def load_high_scores(filename="high_scores.json"):
    """
    Loads high scores from a JSON file.

    Args:
        filename (str): The filename to load the high scores from. Default is 'high_scores.json'.

    Returns:
        dict: A dictionary of high scores.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}
