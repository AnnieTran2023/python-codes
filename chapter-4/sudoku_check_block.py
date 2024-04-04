def block_ok(nestedList, row_index, column_index):

    block = []

    if row_index % 3 !=0 or column_index % 3 !=0:
        return False

    for index in range(row_index, row_index+3):
        for i in range(column_index, column_index+3):
            block.append(nestedList[index][i])

    result = set()

    for number in block:
        if number != 0:
            if number in result:
                return False
            else:
                result.add(number)
    return True
    
def main():
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 6],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(block_ok(sudoku, row_index=0, column_index=0)) # False
    print(block_ok(sudoku, row_index=3, column_index=6)) # False
    print(block_ok(sudoku, row_index=6, column_index=3)) # True

    print(block_ok(sudoku, row_index=0, column_index=4)) # False


if __name__ == "__main__":
    main()
