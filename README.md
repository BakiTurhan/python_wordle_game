# Python Wordle Game

This Python application allows you to play the popular **Wordle** game in the terminal. The player attempts to guess a 5-letter word within 6 attempts. After each guess, the program highlights the correct letters and their positions using colors.

## Features

- The player is given 6 attempts to guess the correct word.
- After each guess:
  - <span style="color:green">Green</span> indicates that the letter is correct and in the correct position.
  - <span style="color:yellow">Yellow</span> indicates that the letter is correct but in the wrong position.
  - <span style="color:gray">Gray</span> indicates that the letter is not in the word.
- The word list is loaded from the `words.txt` file.
- The player can only guess 5-letter words.
- If the player guesses correctly, the program congratulates them. If they fail to guess the word in 6 attempts, the correct word is revealed.

## Requirements

- Python 3.x
- The `termcolor` library. You can install it via pip:

  ```bash
  pip install termcolor

## File Structure

**wordle_game.py** - The main Python game file.
**words.txt** - A text file containing the words used in the game.

## Example Output
Attempt 1/6: ABUSE
<span style="background-color: green"> A </span><span style="background-color: green"> B </span><span style="background-color: yellow"> u </span><span style="background-color: grey"> S </span><span style="background-color: grey"> E </span>

Attempt 2/6: ABOUT
<span style="background-color: green"> A </span><span style="background-color: green"> B </span><span style="background-color: green"> O </span><span style="background-color: green"> U </span><span style="background-color: green"> T </span>
Congratulations! You guessed it right on attempt 2.
