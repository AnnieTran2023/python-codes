def print_matrix_sum(nestedList1, nestedList2):

    for i in range(len(nestedList1)):
        for index in range(len(nestedList1[i])):
           sum = nestedList1[i][index] + nestedList2[i][index]
           print(sum , end=" ")
        print()


def main():
    m1 = [[1, 2, 0], [2, 3, 4]]
    m2 = [[3, 2, 5], [6, 4, 3]]
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]]
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]
    print_matrix_sum(m1, m2)
    print()
    print_matrix_sum(m3, m4)

main()
