# Project Euler Problem 6
#
# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.
#
# Link : https://projecteuler.net/problem=6
#

import math

def sum_of_squares(max):
	sum = 0
	for i in range(1, max+1):
		sum += math.pow(i, 2)
	return sum

def square_of_sum(max):
	sum = 0
	for i in range (1, max+1):
		sum += i
	square = math.pow(sum,2)
	return square

sum = sum_of_squares(100)
square = square_of_sum(100)
difference = square - sum

print difference	
