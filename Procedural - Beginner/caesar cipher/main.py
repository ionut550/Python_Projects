from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    
    for i in text:
        if i in alphabet:
            end_text += alphabet[alphabet.index(i)+(shift % 26)]
        else:
            end_text += i

    print(f"The {direction}d text is {end_text}") 

end_of_program = False
first_run = True
while not end_of_program:
    if first_run:
        print(logo)
        first_run = False
        user_choise = "yes"
    else:
        user_choise = input("Would you like to run again?(Yes or No) ").lower()
    
    if user_choise == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift,direction)
    else: 
        end_of_program = True