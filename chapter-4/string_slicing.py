def print_output(s):
    for i in range(-1, -(len(s))-1, -1):
        print(s[i::])


def main():
    number = input("Enter a positive integer: ")

    while number != "quit":
        if number == "":
            print("No input")
        else:
            try:
                number_int = int((number))
                if number_int == 0:
                    print("0 is not a positive integer")
                else:
                    print_output(number)
            except:
                print(f"{number} is not a positive integer")

        number = input("\nEnter a positive integer: ")
    print("Bye!")


main()
