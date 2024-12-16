# Tuple Out Dice Game
"""
This program simulates the "Tuple Out" dice game where players take turns rolling dice to score points.
The game continues until a player reaches the target score.
"""

import random  
import sys    
from collections import Counter 
import utils
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Rolls a specified number of dice and returns the results as a list
def roll_dice(num_dice=3):
    """
    Args:
        num_dice (int): Number of dice to roll. Default is 3.

    Returns:
        list: A list containing the results of the dice rolls.
    """
    return [random.randint(1, 6) for _ in range(num_dice)]

# Displays the current scores of all players
def display_scores(scores):
    """
    Args:
        scores (dict): A dictionary containing player names and their scores.
    """
    print("\nCurrent Scores:")
    for player, score in scores.items():
        print("{0}: {1}".format(player, score))

# Prompts the user to make a choice from the provided options
def get_user_choice(prompt, choices):
    """
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
            print("Invalid choice. Please choose from " + str(choices) + ".") 

# Executes a single turn for a player
def play_turn(player, scores, target_score, stats):
    """
    Args:
        player (str): The name of the current player.
        scores (dict): The current scores of all players.
        target_score (int): The score needed to win the game.
        stats (dict): The current statistics of all players.
    """
    print("\n" + player + "'s turn:") 
    fixed_dice = []
    total_points = 0

    while True:
        num_dice_to_roll = 3 - len(fixed_dice)
        current_roll = roll_dice(num_dice_to_roll)
        print(player + " rolled: " + str(current_roll + fixed_dice))  

        # Count occurrences of each die using Counter
        counts = Counter(current_roll + fixed_dice)

        # Check for tuples
        if any(count == 3 for count in counts.values()):
            print(player + " has tupled out! Scores 0 points this turn.")
            stats[player]["tuples"] += 1 #Increment tuple count
            return

        # Fix dice with two of the same value
        new_fixed = [die for die, count in counts.items() if count == 2]
        if new_fixed:
            fixed_dice = new_fixed
            print("Fixed dice: " + str(fixed_dice)) 

        total_points = sum(current_roll) + sum(fixed_dice)
        print("Total points this turn: " + str(total_points)) 

        # Ask to continue or stop
        choice = get_user_choice("Do you want to (r)eroll or (s)top? ", ['r', 's'])
        if choice == 's':
            scores[player] += total_points
            print(player + " ends their turn with " + str(total_points) + " points.")  
            return

# Displays player statistics using Pandas DataFrame
def display_statistics(stats):
    """
    Displays player statistics using Pandas DataFrame.

    Args:
        stats (dict): A dictionary containing player statistics.
    """
    df = pd.DataFrame(stats).T
    df['average_score'] = df['total_score'] / df['total_turns']
    print("\nPlayer Statistics:")
    print(df[['total_turns', 'total_score', 'average_score', 'tuples', 'highest_score']])

# Creates a bar chart of player scores using Seaborn
def visualize_scores(scores):
    """
    Creates a bar chart of player scores using Seaborn.

    Args:
        scores (dict): A dictionary containing player names and their scores.
    """
    sns.set(style="whitegrid")
    players = list(scores.keys())
    scores_values = list(scores.values())
    
    plt.figure(figsize=(8, 6))
    sns.barplot(x=players, y=scores_values, palette="viridis")
    plt.title("Final Scores of Players")
    plt.xlabel("Players")
    plt.ylabel("Scores")
    
    # Save the plot as an image file
    plt.savefig("score_distribution.png")
    print("Score distribution chart saved as 'score_distribution.png'.")
    
    # Optionally, display the plot
    plt.show()
    
# The main function to run the Tuple Out Dice Game
def main():

    print("Welcome to the Tuple Out Dice Game!")

    # Setting target score 
    target_score = 50  # Default target score
    if len(sys.argv) > 1:
        try:
            target_score = int(sys.argv[1])
            print("Target score set to " + str(target_score) + " points.")  
        except ValueError:
            print("Invalid target score provided. Using default of 50 points.")  

    players = ["Player 1", "Player 2"]  
    scores = {player: 0 for player in players}  

    # Display scores of players at the end of each turn
    while all(score < target_score for score in scores.values()):  
        for player in players:
            play_turn(player, scores, target_score)
            display_scores(scores)

            # Display final scores
            if scores[player] >= target_score:
                print("\n" + player + " has reached " + str(target_score) + " points and wins the game!")  
                utils.save_high_score(player, scores[player])  
                return

    # Using a tuple to display final scores
    final_scores = tuple(scores.items())
    print("\nFinal Scores:")
    for player, score in final_scores:
        print(player + ": " + str(score))  

    winner = max(scores, key=scores.get)
    print("\nCongratulations " + winner + "! You win the game.")

if __name__ == "__main__":
    main()
