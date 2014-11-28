# Project Euler Problem 7 
#
# 
# 
# Link : 
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
	
	while (len(primes) <= n):
		if ( isPrime(i, primes) == True ) : 
			primes.append(i)
		i = i + 1
	
	prime = primes[(len(primes)-1)] 
	return prime

print find_prime_nth(10001)
	
