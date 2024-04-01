print("=== Creating a dictionary ===")

dictionary = {}

english_word = input("Enter english word (quit ends): ").lower()

while english_word != "quit":
    finnish_word = input("Enter finnish word: ").lower()
    dictionary[english_word] = finnish_word

    english_word = input("Enter english word (quit ends): ").lower()

print("\n=== Using a dictionary ===")
search_word = input("Enter english word (quit ends): ").lower()

while search_word != "quit":
    is_found = False
    
    for english in dictionary:
        if english == search_word:
            print(f"{dictionary[english]}")
            is_found = True
   
    if is_found == False:
        print("Unknown word")

    search_word = input("\nEnter english word (quit ends): ").lower()
