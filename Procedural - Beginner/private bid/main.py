import os

clear = lambda: os.system('cls')
bider_left = True
bider_list ={}

while bider_left:
    name = input("What is your name? ")
    bid = int(input("How much do you bid? "))
    bider_list[name] = bid
    people = input("There are more biders ?(Yes or No) ").lower()
    if people == "no":
        bider_left = False
    clear()

highest_bider = ["", 0]

for i in bider_list:
    if bider_list[i] > highest_bider[1]:
        highest_bider[1] = bider_list[i]
        highest_bider[0] = i
print(f"Highest bider is {highest_bider[0]} with a bid of ${highest_bider[1]}.")