# Project Euler Problem 7 
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?
# 
# Link : https://projecteuler.net/problem=7 
# 

def isPrime(n, prime_list):
	for i in prime_list: 
		if ( n % i == 0 ): 
			return False
	return True

# Finds the nth prime number
def find_prime_nth(n):
	primes = []
	i = 2
	
	while (len(primes) < n):
		if ( isPrime(i, primes) == True ) : 
			primes.append(i)
		i = i + 1
	
	prime = primes[(len(primes)-1)] 
	return prime

print find_prime_nth(10001)
	
