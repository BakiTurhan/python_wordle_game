import random
from termcolor import colored


def load_words(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            return file.read().split("\n")
    except Exception as e: 
        print(colored(f"Error loading words: {e}", "red"))


def check_word(guess, game_word):
    for i, char in enumerate(guess):
        if game_word[i] == char:
            print(colored(f" {char} ",on_color="on_light_green"), end="")
        elif char in game_word:
            print(colored(f" {char} ", on_color="on_light_yellow"), end="")
        else:
            print(colored(f" {char} ", on_color="on_dark_grey"), end="")  
    print("")


word_list = load_words("words.txt")
game_word = random.choice(word_list)
attempt = 1
    

while True:
    guess = input(f"Attempt {attempt}/6: ").strip().upper()

    if len(guess) != 5:
        print(colored("The word must be 5 letters!", "red"))
        continue
    if guess not in word_list:
        print(colored("The word is not in the list!", "red"))
        continue

    check_word(guess, game_word)

    if guess == game_word:
        check_word(guess,game_word)
        print(colored(f"Congratulations! You guessed it right on attempt {attempt}", "green"))
        break
    
    
    attempt += 1

    if attempt > 6:
        print(colored(f"You failed! The correct word is: {game_word}", "cyan"))  
        break


  
