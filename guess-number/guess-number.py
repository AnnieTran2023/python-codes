import random

logo = """"
                           ('-.    .-')     .-')              .-') _             _   .-')   .-. .-')    ('-.  _  .-')   
                         _(  OO)  ( OO ).  ( OO ).           ( OO ) )           ( '.( OO )_ \  ( OO ) _(  OO)( \( -O )  
  ,----.    ,--. ,--.   (,------.(_)---\_)(_)---\_)      ,--./ ,--,' ,--. ,--.   ,--.   ,--.);-----.\(,------.,------.  
 '  .-./-') |  | |  |    |  .---'/    _ | /    _ |       |   \ |  |\ |  | |  |   |   `.'   | | .-.  | |  .---'|   /`. ' 
 |  |_( O- )|  | | .-')  |  |    \  :` `. \  :` `.       |    \|  | )|  | | .-') |         | | '-' /_)|  |    |  /  | | 
 |  | .--, \|  |_|( OO )(|  '--.  '..`''.) '..`''.)      |  .     |/ |  |_|( OO )|  |'.'|  | | .-. `.(|  '--. |  |_.' | 
(|  | '. (_/|  | | `-' / |  .--' .-._)   \.-._)   \      |  |\    |  |  | | `-' /|  |   |  | | |  \  ||  .--' |  .  '.' 
 |  '--'  |('  '-'(_.-'  |  `---.\       /\       /      |  | \   | ('  '-'(_.-' |  |   |  | | '--'  /|  `---.|  |\  \  
  `------'   `-----'     `------' `-----'  `-----'       `--'  `--'   `-----'    `--'   `--' `------' `------'`--' '--' 
  """
print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

random_number = random.randint(1,100)

attempts = 0

if level == "easy":
    attempts = 10
    print("\nYou have 10 attempts to guess the number")
elif level == "hard":
    attempts = 5
    print("\nYou have 5 attempts to guess the number")

while attempts > 0:
    guess = int(input("\nMake a guess: "))

    if guess == random_number:
        print("\nCongratulations! You got it right!")
        break
    elif guess > random_number:
        attempts -= 1
        print("Too high")
        print(f"You have {attempts} attempts remaining to guess the number")
    elif guess < random_number:
        attempts -= 1
        print("Too low")
        print(f"You have {attempts} attempts remaining to guess the number")
    
    if attempts == 0:
        print("You run out of guesses, you lose 🥲")



