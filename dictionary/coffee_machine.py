MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#TODO: 1.print report

user_choice = input("What would you like? (espresso/latte/cappuccino): ")

while user_choice != "off":
    if user_choice == "report":
        for item in resources:
            print(f"{item}: {resources[item]}ml")
        print(f"Money: ${profit}")
    elif user_choice not in MENU:
        print(f"We do not serve {user_choice} in this machine. Please choose again!")    
    else:
        chosen_drink = MENU[user_choice]["ingredients"]
        if chosen_drink["water"] > resources["water"]:
            print("Sorry there is not enough water!")
        elif chosen_drink["coffee"] > resources["coffee"]:
            print("Sorry there is not enough coffee!")
        elif "milk" in chosen_drink and chosen_drink["milk"] > resources["milk"]:
            print("Sorry there is not enough milk!")
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_money = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies*0.01)
            if total_money >= MENU[user_choice]["cost"]:
                change = total_money-MENU[user_choice]["cost"]
                print(f"Here is your ${change:.1f} change.")
                print(f"Enjoy your {user_choice} ☕️!")
                profit += MENU[user_choice]["cost"]
                for item in chosen_drink:
                    if item in resources:
                        resources[item] -= chosen_drink[item]
            else:
                print("Sorry! That's not enough money. Money refunded!")
    
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")

print("Thank you...Bye!")
