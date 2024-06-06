from decimal import Decimal, getcontext

def compute_discount(price, discount_percent):
	discounted = price * (1-discount_percent/100)
	return discounted

def main():
	price = Decimal(input('Enter price: '))
	discount_percent = Decimal(input('Enter discount percentage: '))
	discounted_price = price - compute_discount(price, discount_percent)
	print(f"The discount is {discounted_price:.2f} euros")
	
main()
