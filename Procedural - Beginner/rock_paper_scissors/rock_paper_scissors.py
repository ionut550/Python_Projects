import random 

list = ["Rock", "Paper", "Scissors"]
user_choise = int(input("Type 0 for Rock, 1 for Pape, 2 fro Scissors: "))
while(user_choise > 2 or user_choise < 0):
    print("Introduce a valid number!")
    user_choise = int(input("Type 0 for Rock, 1 for Pape, 2 fro Scissors: "))

computer_choise = random.randint(0,2)
print(computer_choise)
if (user_choise == 0):
    if(computer_choise == 1):
        print("You lose")
    elif(computer_choise == 2):
        print("You win")
    else: 
        print("It's a draw")
elif (user_choise == 1):
    if(computer_choise == 2):
        print("You lose")
    elif(computer_choise == 0):
        print("You win")
    else: 
        print("It's a draw")
elif(user_choise == 2):
    if(computer_choise == 0):
        print("You lose")
    elif(computer_choise == 1):
        print("You win")
    else: 
        print("It's a draw")