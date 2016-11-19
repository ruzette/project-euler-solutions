'''

Project Euler Problem 16 

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

Link : https://projecteuler.net/problem=16

'''

def power_digit_sum(base=1, exp=1):

	# Get exponential number 
	product = base**exp

	# Convert to product list
	product_list = [int(x) for x in list(str(product))]

	return sum(product_list)


def main():
	print power_digit_sum(2, 15)
	print power_digit_sum(2, 1000)

if __name__ == "__main__":
	main()