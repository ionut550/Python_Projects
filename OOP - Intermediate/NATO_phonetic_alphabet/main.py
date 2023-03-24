import pandas

raw_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_letters = {code.letter:code.code for (index,code) in raw_data.iterrows()}

user_input = input("Enter the name: ").upper()

print([nato_letters[letter] for letter in user_input])