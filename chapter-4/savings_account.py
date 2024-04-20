from decimal import Decimal, getcontext

rate = Decimal(input('Enter interest rate: '))/100
tax = Decimal(input('Enter capital income tax rate: '))/100
deposit = Decimal(input('Enter initial deposit: '))
years = int(input('Enter number of years: '))
print()

for year in range(years):
	interest = deposit * rate * (1-tax)
	deposit += interest
	print(f"Year {year+1}: {deposit:.2f}")
