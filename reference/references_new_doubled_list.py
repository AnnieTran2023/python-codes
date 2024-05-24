def new_doubled_list(list):
    new_list = list.copy()
    for index in range(len(new_list)):
        new_list[index] *= 2
    return new_list

def main():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)
    print(first_list)
    print(second_list)

main()
