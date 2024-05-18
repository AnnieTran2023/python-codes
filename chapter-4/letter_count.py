s = input("Enter a string: ").lower()
if s == "":
    print("\nNo input")
else:
    characters = []

    for char in s:
        if char.isalpha():
            characters.append(char)

    distinct_characters = list(set(characters))

    distinct_characters.sort()

    if len(distinct_characters) == 0:
        print("\nNo letters")
    else:
        print()
        print(*distinct_characters, sep=" ")
