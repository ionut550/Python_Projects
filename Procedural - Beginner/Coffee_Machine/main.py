import recipe

MACHINE_MONEY = 0

def user_choice():
    choice = input("What would you like ? (espresso/latte/cappuccino): ").lower()
    valid_entry = True
    valid_words = ["espresso", "latte", "cappuccino", "off", "report"]
    while valid_entry:
        if choice in valid_words:
            valid_entry = False
        else:
            print("Enter a valid option!")
            choice = input("What would you like ? (espresso/latte/cappuccino): ").lower()
    return choice


def correct_value(value, coin):
        try:
            return float(value)
        except ValueError:
            print("Enter a valid option!")
            value = correct_value(input(f"How many {coin}?: "), coin)
            return value


def report():
    money = MACHINE_MONEY
    for index in recipe.resources:
        if index == "water" or index == "milk":
            print (f"{index}: {recipe.resources[index]}ml")
        else:
            print(f"{index}: {recipe.resources[index]}g")
    print(f"Money: ${money}")


def enough_resources(coffee):
    if recipe.MENU[coffee]["ingredients"]["water"] <= recipe.resources["water"]:
        recipe.resources["water"] -= recipe.MENU[coffee]["ingredients"]["water"]
    else:
        print("Sorry there is not enough water!")
        return False

    if recipe.MENU[coffee]["ingredients"]["coffee"] <= recipe.resources["coffee"]:
        recipe.resources["coffee"] -= recipe.MENU[coffee]["ingredients"]["coffee"]
    else:
        print("Sorry there is not enough coffee!")
        return False
    try:
        if recipe.MENU[coffee]["ingredients"]["milk"] <= recipe.resources["milk"]:
            recipe.resources["milk"] -= recipe.MENU[coffee]["ingredients"]["milk"]
        else:
            print("Sorry there is not enough milk!")
            return False
    except Exception:
        return True
    return True

def coin_counter():
    print("Please insert coins")
    quarters = correct_value(input("How many quarters?: "), "quarters")
    dimes = correct_value(input("How many dimes?: "), "dimes")
    nickles = correct_value(input("How many nickles?: "), "nickles")
    pennies = correct_value(input("How many pennies?: "), "pennies")
    return round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)


def enough_balance(balance, coffee):
    if balance >= recipe.MENU[coffee]["cost"]:
        print(f'Here is $ {balance - recipe.MENU[coffee]["cost"]} in change.')
        return recipe.MENU[coffee]["cost"]
    else:
        print(f"Sorry not enough balance. Here is your change {balance}.")
        return 0

is_on = True


while is_on :
    choise = user_choice()
    if choise == "report":
        report()
    elif choise == "off":
        is_on = False
    else:
        balance = enough_balance(coin_counter(),choise)
        if balance != 0 and enough_resources(choise):
            MACHINE_MONEY += balance
            print(f"Here is your {choise}. Enjoy!")
