from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    user_choise = input(f"What would you like? ({menu.get_items()}): ")

    if user_choise == "off":
        is_on = False
    elif user_choise == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(user_choise) == None:
            print("Enter a valid option!")
            user_choise = input("What would you like? (espresso/latte/cappuccino): ")
    else:
        user_choise = menu.find_drink(user_choise)
        if coffee_maker.is_resource_sufficient(user_choise) and money_machine.make_payment(user_choise.cost):
            coffee_maker.make_coffee(user_choise)