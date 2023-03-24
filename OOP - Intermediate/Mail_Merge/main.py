PLACEHOLDER = "[name]"

#Read and store in a list each line from the file
with open("./Input/Names/invited_names.txt") as file:
    raw_names = file.readlines()

#Read and store the letter template
with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

#Create a file for each name in the list
for i in raw_names:
    formatted_names = i.strip()
    with open(f"./Output/ReadyToSend./letter_for_{formatted_names}.txt", "w") as file:
        file.write(letter.replace(PLACEHOLDER,formatted_names))