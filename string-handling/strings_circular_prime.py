def is_prime(number):
    is_prime = True
    if number <= 1:
        is_prime = False
        return is_prime
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
    return is_prime

def is_circular_prime(number):

    if is_prime(number) == False:
        return False
    else: 
        num_str = str(number)
        circular_numbers = []
    
        # Generate all possible circulars
        for i in range(len(num_str)):
            rotated_num_str = num_str[i:] + num_str[:i]
            circular_numbers.append(int(rotated_num_str))
    
        is_circular_prime = True

        for number in circular_numbers:
            if is_prime(number) == False:
                is_circular_prime = False
    
        return is_circular_prime

def main():
    number = int(input("Enter a positive integer: "))
    result = is_circular_prime(number)
    if result == True:
        print(f"{number} is a circular prime")
    else:
        print(f"{number} is not a circular prime")

main()



