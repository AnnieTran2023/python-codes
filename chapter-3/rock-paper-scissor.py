import random

scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''
rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''
paper = '''
          ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
'''
print("=== Rock - Paper - Scissors ===")
print("Winning give you one point and losing minus one point")
score = 0
while True:
    answer = input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors, or "exit" to end: ')

    if answer.lower() == "exit":
        break

    try:
        answer_number = int(answer)

        if answer_number not in [0, 1, 2]:
            print("Invalid choice. Please choose 0, 1, or 2.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")
        continue

    game = [rock, paper, scissors]
    random_int = random.randint(0, 2)

    print("You chose: ")
    print(game[answer_number])

    print("Computer chose: ")
    print(game[random_int])
    

    if answer_number == random_int:
        print("It's a draw!")
    elif (answer_number == 0 and random_int == 2):
        score += 1
        print("You win!")
    elif answer_number == 2 and random_int == 0:
        score = 0 if score <= 0 else score - 1
        print("You lose!")
    elif answer_number > random_int:
        score +=1
        print("You win!")
    else:
        score = 0 if score <= 0 else score - 1
        print("You lose!")
    print(f"Your current score: {score}")
print (f"Your final score : {score}")
print("Game exit!")
