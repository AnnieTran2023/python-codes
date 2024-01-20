print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("--------Welcome to our treasure game--------")
direction = input("You are at a crossroad. Which direction do you choose? left or right: ").lower()
if direction == "left":
    print("Game Over!!! You fell into a hole...")
elif direction == "right":
    swim_wait = input("You've come to a lake. Do you want to swim or wait for a boat? ").lower()
    if swim_wait == "swim":
        print("There is a crocodile in the lake and it just ate you. Game over!!!")
    elif swim_wait == "wait":
        print("A boat has taken you safely across the lake")
        door = input("There are three different doors in front of you. Which color you choose? red yellow or blue: ").lower()
        if door == "yellow":
            print("Congratulations!!! You have found the treasure!...")
        else:
            print("This room is full of fire and you are dead! Game over!!!")
