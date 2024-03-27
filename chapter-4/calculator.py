logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add (n1, n2):
    return n1+n2

def subtract (n1,n2):
    return n1-n2

def multiply (n1,n2):
    return n1 * n2

def divide (n1,n2):
    return n1 / n2

math_operations = {"+" : add, "-": subtract, "*": multiply, "/" : divide}

is_continue = True 

while is_continue == True:
    first_number = int(input("Enter first number: "))
    operator = input ("Enter the operator: ")
    second_number = int(input("Enter second number: "))

    for key in math_operations:
        if operator == key:
            result = math_operations[key](first_number, second_number)
            print(f"{first_number} {operator} {second_number} = {result}")
    
    ask = input("\nWould you to continue? 'yes' or 'no' ")

    if ask == "no":
        is_continue = False

print(" === Bye === ")

