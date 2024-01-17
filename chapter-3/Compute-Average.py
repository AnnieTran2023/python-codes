from decimal import Decimal, getcontext

number_array = []
sum = 0

number1 = Decimal(input('Enter first number: '))
number_array.append(number1)
sum += number1
if number1 == 0:
	print('Nothing to be calculated')
else: 
	while number1 != 0:
		number_loop = Decimal(input('Enter next number: '))
		if number_loop != 0:
			number_array.append(number_loop)
			sum += number_loop
		number1 = number_loop

	total_numbers = len(number_array)
	average = sum / total_numbers
	print('The average is ' + "{:.2f}".format(average))
