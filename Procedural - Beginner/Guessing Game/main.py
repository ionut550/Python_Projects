import art
import random
import os
clear = lambda: os.system('cls')

def difficulty_chooser(word):
    """Take as input 'easy' or 'hard'."""
    if word == "easy":
        return 10
    elif word == "hard":
        return 5

def guess_verifier(guess):
    """Takes the value and tests if it can be cast to an integer.
    Return -1 if the value cannot be casted."""
    try:
        guess = int(guess)
        return guess
    except ValueError:
        guess = -1
        return guess

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = ""
    switch = False
    while not (difficulty == "easy" or difficulty == "hard"):
        if switch:
            print("Enter a valid option!")
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        else:
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
            switch = True
    
    number = random.randint(1,100)
    lives = difficulty_chooser(difficulty)
    switch2 = False

    while lives > 0:
        guess = ""
        
        while not guess in range(1,101):
            if switch2:
                print("Enter a valid option!")
                guess = guess_verifier(input("Make a guess :"))  
            else: 
                guess = guess_verifier(input("Make a guess :")) 
                switch2 = True         
        
        if guess == number:
            lives = 0 
            print("You guessed right")
        elif guess > number:
            lives -= 1
            print("Too high")
            print(f"Lives left: {lives}")
        else:
            lives -= 1
            print("Too low")
            print(f"Lives left: {lives}")

def start_game():
    game = ""
    switch = False
    while not (game == "y" or game == "n"):
        if switch:
            print("Enter a valid option!")
            game =input("Do you want to play a game of Guessing the number? Type 'y' or 'n': ").lower()
        else:
            game =input("Do you want to play a game of Guessing the number? Type 'y' or 'n': ").lower()
            switch = True
    return game    

while start_game() == "y":
    clear()
    play_game()