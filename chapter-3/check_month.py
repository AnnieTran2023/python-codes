while True:
    number = input('Enter a month number: ')

    try:
        number = int(number)
        if 1 <= number <= 12:
            print("OK")
            break  
        else:
            print(f"{number} is not a valid month number\n")
    except ValueError:
        print(f"'{number}' is not a valid month number\n")
