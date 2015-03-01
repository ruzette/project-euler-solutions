'''

Project Euler Problem 20 

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Link : https://projecteuler.net/problem=20

'''

def factorial_digit_sum(n=1):

	factorial = 1

	# Get factorial product 
	for i in range(1, n):
		factorial = factorial * i

	# Convert to factorial list
	factorial_list = [int(x) for x in list(str(factorial))]

	return sum(factorial_list)

def main():
	print factorial_digit_sum(10)
	print factorial_digit_sum(100)

if __name__ == "__main__":
	main()