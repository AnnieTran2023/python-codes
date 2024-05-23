def count_occurrences(nestedList, number):
    count = 0
    for list in nestedList:
        for num in list:
            if num == number:
                count +=1
    return count

def main():
 	m = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 2, 1]]
 	print(count_occurrences(m, 1))
 	print(count_occurrences(m, 2))
 	print(count_occurrences(m, 5))
	
main()
