number_list = []

number = input("Enter an integer: ")

if number == "":
    print("\nNo input")
else:
    while number != "":
        number_list.append(int(number))
        number = input("Enter an integer: ")

    number_list.sort()
    distinct_number_list = list(set(number_list))

    lower_limit = int(input("Enter lower limit: "))
    upper_limit = int(input("Enter upper limit: "))

    index_upper = 0
    index_lower = 0

    result = []
    
    for number in distinct_number_list:
        if number >= lower_limit and number <= upper_limit:
            result.append(number)
    
    result.sort()

    if len(result) == 0:
        print(f"\nThere are no values between {lower_limit} and {upper_limit}")
    else:
        print()
        print(*result, sep = ", ")

