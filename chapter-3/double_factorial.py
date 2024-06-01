number = input('Enter a non-negative integer: ')

try:
	number = int(number)
	total = 1;
	for num in range(1,number+1):
		if num == 1: continue
		if number % 2 == num % 2:
			total = total * num
	print(f"{number}!! = {total}")
	
except:
	print('Please enter a non-negative integer')
