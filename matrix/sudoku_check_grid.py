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

def row_ok(nestedList, row_index):
    row = nestedList[row_index]
    result = set()
    for num in row:
        if num != 0:
            if num in result:
                return False
            else:
                result.add(num)
    return True

def column_ok(nestedList, column_index):

    column = []

    for list in nestedList:
        column.append(list[column_index])
    result = set()

    for number in column:
        if number != 0:
            if number in result:
                return False
            else:
                result.add(number)
    return True

def grid_ok(grid):

    # check rows and columns
    for i in range(9):
      
        if row_ok(grid, i) == False or column_ok(grid, i) == False:
            return False
    
    # check blocks
    for column_index in range(0,9,3):
        for row_index in range(0,9,3):
            if block_ok(grid, row_index, column_index) == False:
                return False
    return True

def main():
    sudoku_1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    sudoku_2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(grid_ok(sudoku_1)) # False
    print(grid_ok(sudoku_2)) # True

if __name__ == "__main__":
    main()
