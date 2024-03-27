logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os

def clear_console():
    os.system('clear')

print(logo)
print("=== Welcome to the secret auction program ===")

bidders = {}

user_name = input("\nWhat is your name?: ")
try:
    bid = int(input("What's your bid?: $"))
    bidders[user_name] = bid
except Exception as e:
    print("Please enter a valid integer")

is_more = input("\nAre there any other bidders? Type 'yes' or 'no' ")

while is_more == "yes":
    clear_console()
    user_name = input("\nWhat is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[user_name] = bid
    is_more = input("\nAre there any other bidders? Type 'yes' or 'no' ")

max_bid = 0;
winner = "";

for name in bidders:
    if bidders[name] > max_bid:
        max_bid = bidders[name]
        winner = name

print(f"\nThe winner is {winner} with a bid of ${max_bid}")
