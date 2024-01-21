import random
from hangman_art import logo, stages, word_list

print(logo)

word = random.choice(word_list)

# print(word)
word_length = len(word)

answer = []
wrong_answer = [] 

while len(answer) < word_length:
    answer.append("_")
print(f"\nYou word has {word_length} characters : {' '.join(answer)}")

lives = 6

while "_" in answer:
    if lives > 0:
            
        user_guess = input("\nGuess a letter: ").lower()

        found = False

        if user_guess in answer or user_guess in wrong_answer:
                print(f"Try another letter! You have already guessed letter {user_guess}")

        for index in range (0,word_length):

            if word[index] == user_guess:
                answer[index] = user_guess
                found = True

        if not found:
            wrong_answer.append(user_guess)
            lives -=1 
            print(stages[lives])
            print("\nYou lose a life")
            print(f"Your remaining lives: {lives}")
        
        print(' '.join(answer))

    else:
        print("You ran out of lives! GAME OVER!")
        print(f"The word is {word}")
        break

if not "_" in answer:
    print("\nCongratulations! You are correct.")
    print(f"The word is {word}")
