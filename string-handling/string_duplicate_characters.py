def strings_duplicate_characters():

    str = input("Enter a string: ")

    characters = set(str)
    if len(str) == len(characters):
        print("No duplicates")
    else:
        print("Contains duplicate(s)")

strings_duplicate_characters()
