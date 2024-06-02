from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user_choice = input("What would you like? (espresso/latte/cappuccino/): ")

while user_choice != "off":
    if user_choice == "report":
        menu = MenuItem()
        report = report()
        print(report)
    elif user_choice not in menu:
        print(f"We do not serve {user_choice} in this machine. Please choose again!")    
    else:
        
