# Project Euler Problem 5
# 
# 2520 is the smallest number that can be divided by each of 
# the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?
#
# Link : https://projecteuler.net/problem=5
#

from collections import Counter

def find_primes(n):
	prime_list = []
	dividend = n
	i = 2

	while ( dividend > 1 ):
		quotient = dividend / i
		remainder = dividend % i

		if ( remainder != 0 ): 
			i += 1 
			continue
		if ( quotient  == 1 ):
			prime_list.append(i)
			break
 
		prime_list.append(i)
		dividend = quotient

	return prime_list

def find_smallest_multiple(n):
	smallest_product = 1

	for i in range (2, n+1):		
		prime_list = find_primes(i)
		prime_ctr = Counter(prime_list)
		
		#counts the occurrences of the smallest product
		product_list = find_primes(smallest_product)
		counter_list = Counter(product_list)
		
		# Iterates through the values in the current number's prime numbers 
		# and compares if they are the same.
		for key, value in prime_ctr.iteritems():
			multiple = counter_list.get(key, 0)
			
			if ( multiple < value ) :
				smallest_product *= key
	return smallest_product
#print find_smallest_multiple(10)
print find_smallest_multiple(20)
