# Project Euler Problem 3
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
#
# Link : https://projecteuler.net/problem=3
#

# Determine the largest prime factor of this number
number = 600851475143 

# Returns the largest prime factor, given n		
def get_largest_prime_factor(n): 
	
	# Finds the prime factors of a given number
	# and returns a list of those prime numbers
	prime_list = find_prime_list(n)

	# Reverses the list so that it's easier to access 
	# the largest prime factor 
	prime_list.reverse()

	return prime_list[0]

# Determines all the prime factors of a given number 
# and returns as a list. 
def find_prime_list ( n ): 
	print ("Finding Largest Prime Factor...")

	prime_list = []
	dividend = n
	i = 2	

	# To find the list of primes, perform a division loop 
	# until the quotient is equal to 1. The remainder should 
	# first be checked if the divisor is divisible to the dividend, 
	# else the divisor would keep incrementing. 
	#
	# If the quotient returns 1, it means all the prime factors
	# have been collected. If not, use the quotient as the new dividend
	# and find the other prime factors.

	while ( dividend > 1 ): 
		quotient = dividend / i 
		remainder = dividend % i 
		
		if ( remainder != 0 ): 
			i += 1 
			continue
		if ( quotient  == 1 ):
			prime_list.append(i)
			break
		else: 
			prime_list.append(i)
			dividend = quotient

	return prime_list 

x = get_largest_prime_factor(number)
print x		 
