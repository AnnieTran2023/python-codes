number = input('Enter a weekday number: ')
try:
	number = int(number)
	if number >= 1 and number <=7:
		print("OK")
	else:
		print('Please enter an integer between 1 and 7')
except:
	print('Please enter an integer between 1 and 7')
