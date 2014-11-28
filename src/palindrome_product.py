# Project Euler Problem 4
#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def get_largest_palindrome_product():
	max = 1000
	palindrome = 0

	for i in reversed(range(1, max)):

		for j in reversed(range(1, max)):
			product = i*j

			prodListStr = list(str(product))

			isMaxProduct = check_palindrome(prodListStr)

			if (isMaxProduct and palindrome < product):
				palindrome = product
	return palindrome

def check_palindrome(prodListStr):
	for i in range(0, len(prodListStr)/2):
		if (prodListStr[i] != prodListStr[len(prodListStr)-1-i]):
			return False 
	return True

i = get_largest_palindrome_product()
print i
