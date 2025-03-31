# Python Wordle Game

This Python application allows you to play the popular **Wordle** game in the terminal. The player attempts to guess a 5-letter word within 6 attempts. After each guess, the program highlights the correct letters and their positions using colors.

## Features

- The player is given 6 attempts to guess the correct word.
- After each guess:
  - Green indicates that the letter is correct and in the correct position.
  - Yellow indicates that the letter is correct but in the wrong position.
  - Gray indicates that the letter is not in the word.
- The word list is loaded from the `words.txt` file.
- The player can only guess 5-letter words.
- If the player guesses correctly, the program congratulates them. If they fail to guess the word in 6 attempts, the correct word is revealed.

## Requirements

- The `termcolor` library. You can install it via pip:

  ```bash
  pip install termcolor

## File Structure

- **wordle_game.py** - The main Python game file.
- **words.txt** - A text file containing the words used in the game.

## Example Output 

```bash
Attempt 1/6: ABUSE 
A(green) B(green) U(yellow) S(grey) E(grey)

Attempt 2/6: ABOUT
A(green) B(green) O(green) U(green) T(green)
Congratulations! You guessed it right on attempt 2.
