def strings_surnames():

    number = int(input("How many surnames? "))

    surnames = []

    for i in range(number):

        surname = input("Enter a surname: ").lower()
        new_surname = surname[0].upper() + surname[1:]
        if not new_surname in surnames:
            surnames.append(new_surname)
    
    print()
    surnames.sort()
    print(*surnames)

strings_surnames()
        
