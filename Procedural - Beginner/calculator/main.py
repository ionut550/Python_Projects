import art
import os

clear = lambda: os.system('cls')
def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

while True:
    print(art.logo)
    first_number = float(input("What's the first number?  "))
    for symbol in operation:
        print(symbol)
    operation_symbol = input("Pick an operation:  ")
    second_number = float(input("What's the next number?  "))
    calculation_operation = operation[operation_symbol]
    result = calculation_operation(first_number,second_number)
    print(f"{first_number} {operation_symbol} {second_number} = {result}")
 
    new_screen = True
    while new_screen :
        if (input("Do you want to continue to calculate? (Y or N)").lower()) == "y":
            operation_symbol = input("Pick an operation:  ")
            second_number = float(input("What's the next number?  "))
            calculation_operation = operation[operation_symbol]
            first_number = result
            result = calculation_operation(result,second_number)
            print(f"{first_number} {operation_symbol} {second_number} = {result}")
        else: 
            new_screen = False
    
    clear()