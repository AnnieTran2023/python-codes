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

def main():
    sudoku = [
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
    print(row_ok(sudoku, row_index=0)) 
    print(row_ok(sudoku, row_index=1)) 
    print(row_ok(sudoku, row_index=8)) 

if __name__ == "__main__":
    main()



