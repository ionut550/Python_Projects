import random
import hangman_art
import hangman_words
import os

clear = lambda: os.system('cls')
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
display = ["_"] * len(chosen_word)
end_of_game = False
lives = 6
used_letters = []
print(display)

while not end_of_game and lives > 0:
    one_letter = True

    while one_letter:     
        user_letter = input("Select a letter: ").lower()
        clear()
        
        if len(user_letter) == 1 and user_letter not in used_letters and user_letter not in ["1","2","3","4","5","6","7","8","9","0"]:
            one_letter = False
            used_letters.append(user_letter)
            print(f"Letter used: {used_letters}")
        else:
            print("Introduce one single letter that you didn't used before")
            print(f"Letter used: {used_letters}")
            print(display)
    counter = 0
    
    for i in range(len(chosen_word)):
        if user_letter == chosen_word[i]:
            display[i] = user_letter
            counter += 1
    
    if not counter :
        lives -= 1
    
    if "_" not in display:
        end_of_game = True
    print(display)
    print(hangman_art.stages[lives])

if lives > 0:
    print("You win")
else:
    print(f"You lose, the word was {chosen_word}")
    