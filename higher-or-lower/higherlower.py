from art import logo, vs
from data import data
import random

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

score = 0
result = True
again = "N"

while (result == True) or (result == False and again == "Y"):

    random_person1 = data[random.randint(1,len(data)-1)]
    random_person2 = data[random.randint(1,len(data)-1)]
    if random_person1 == random_person2:
        random_person2 = data[random.randint(1,len(data)-1)]

    print(f"Compare A: {random_person1["name"]}, a {random_person1["description"]}, from {random_person1["country"]}.")

    print(vs)

    print(f"Against B: {random_person2["name"]}, a {random_person2["description"]}, from {random_person2["country"]}.")
    response = input("Who has more followers on Instagram? Type 'A' or 'B': ")

    clear_console()
    print(logo)

    if (response == "A" and random_person1["follower_count"] > random_person2["follower_count"]) or (response == "B" and random_person2["follower_count"] > random_person1["follower_count"]):
        score += 1
        print(f"You are right 🎉! Current score: {score}.")
    else:
        result = False
        print(f"Sorry! That's wrong 🥲. Final score: {score}")
        again = input("\nWould you like to play again? Type 'Y' or 'N': ")

print("\nBye bye!")





