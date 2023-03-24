import game_data
import random
import art
import os

clear = lambda: os.system('cls')

def get_name (person):
    """Take int and return the name from that position."""
    return person["name"]

def get_followers (person):
    """Take int and return the number of followers."""
    return person["follower_count"]

def get_description (person):
    """Take int and return the description."""
    return person["description"]

def get_country (person):
    """Take int and return the country"""
    return person["country"]

def comparation (guess, first_person, second_person):
    if guess == "a" and (get_followers(first_person) > get_followers(second_person)):
        return True
    elif guess == "a" and (get_followers(first_person) < get_followers(second_person)):
        return False
    elif guess == "b" and (get_followers(first_person) < get_followers(second_person)):
        return True
    elif guess == "b" and (get_followers(first_person) > get_followers(second_person)):
        return False


def game():
   
    first_person = game_data.data[random.randint(0,len(game_data.data)-1)]
    second_person = game_data.data[random.randint(0,len(game_data.data)-1)]
    game_running = True
    score = 0

    while game_running:
        same_person =True
        print(art.logo)
        if score != 0:
            print(f"You're right! Current score: {score}")
        while same_person:
            if first_person == second_person:
                second_person = game_data.data[random.randint(0,len(game_data.data)-1)]
            else:
                same_person =False
        
        print(f"Compare A: {get_name(first_person)}, {get_description(first_person)}, from {get_country(first_person)}")
        print(art.vs)
        print(f"Compare B: {get_name(second_person)}, {get_description(second_person)}, from {get_country(second_person)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        switch = True
        while switch:
            if guess == "a" or guess == "b":
                switch = False
            else:
                print("Enter a valid option!")
                guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if comparation(guess, first_person, second_person):
            score += 1
            first_person = second_person
            clear()
        else:
            game_running = False
            clear()
            print(art.logo)
            print(f"Sorry, that's  wrong. Final score: {score}")

playing = True

while playing:
    clear()
    game()
    
    switch = True
    while switch:
        user = input("Do you still wanna play ? Type 'y' or 'n'").lower()
        if user == "n":
            playing = False
            switch = False
        elif user == "y":
            switch = False
        else:
            print("Enter a valid option!")