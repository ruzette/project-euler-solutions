# Project Euler Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Link : https://projecteuler.net/problem=10
#

def is_prime(n, prime_list):
	for i in prime_list:
		if ( n % i == 0): 
			return False
		return True



def find_prime_list(n):
	primes = []
	i = 2

	while (i < n):
		if (is_prime(i, primes) == True):
			primes.append(i)
		i = i + 1
		print i
	print primes
	return primes

def get_prime_sum(n):
	primes = find_prime_list(n)
	return sum(primes)

print get_prime_sum(2000000)
