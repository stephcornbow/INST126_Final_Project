# Tuple Out Dice Game

## Overview

**Tuple Out** is a dice game where players take turns rolling dice to score points. The objective is to be the first to reach a target score or to have the highest score after a set number of turns.

## Features

- **Multiple Players:** Play with two players taking alternate turns.
- **Customizable Target Score:** Set a custom target score via command-line arguments.
- **High Score Tracking:** The game records and saves the highest scores achieved by each player.
- **Interactive Gameplay:** Choose to re-roll non-fixed dice or stop to secure your points each turn.
- **Score Visualization:** Automatically showcasing a bar chart with final scores.

## Requirements

- Python 3.x
- Libraries:
    - 'pandas'
    - 'seaborn'
    - 'matplotlib'

To install, run:
```bash
pip install pandas seaborn matplotlib
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/stephcornbow/INST126_Consolidation_Project.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd tuple-out-dice-game
   ```

## Usage

Run the game using the Python command. You can optionally specify a target score as a command-line argument. If no target score is provided, the default is set to 50 points.

### Running the Game

```bash
python tuple_out.py [target_score]
```

- **`target_score` (optional):** An integer representing the score a player needs to reach to win the game.

### Gameplay Instructions

1. **Starting the Game:**
   - The game welcomes you and displays the target score.

2. **Taking Turns:**
   - Players take turns to roll three dice.
   - If all three dice show the same number, the player "tuples out" and scores zero points for that turn.
   - If two dice have the same value, those dice are "fixed" and cannot be re-rolled.
   - The player can choose to re-roll the non-fixed dice as many times as desired to increase their score.
   - At any point, the player can choose to stop rolling and secure their current points.

3. **Winning the Game:**
   - The first player to reach or exceed the target score wins the game.
   - Final player statistics and scores are displayed.
   - A bar chart visualizing player scores is generated.

## High Scores

The game maintains a `high_scores.json` file that records the highest score achieved by each player. This file is automatically updated at the end of each game.

## Player Statistics

Player statistics are tracked and displayed at the end of the game:

- **Total Turns:** Number of turns taken by the player.
- **Total Score:** Cumulative score achieved.
- **Average Score:** Average points per turn.
- **"Tuple Outs":** Number of times a player rolled three matching dice.
- **Highest Score:** Highest score achieved during the game.

## Code Structure

- **`tuple_out.py`:** The main game script that handles the game logic and player interactions.
- **`utils.py`:** Contains utility functions for saving and loading high scores.
- **`high_scores.json`:** JSON file that stores high scores for each player.
- **`README.md`:** This readme file with instructions and information about the game.

## License

This project is licensed under the MIT License.