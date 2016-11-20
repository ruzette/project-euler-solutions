#!/usr/bin/env python
"""
Problem 10 - Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import os
from pprint import pprint

def prime_summation():
    max_number = 2000000
    prime_list = [2]
    for idx in range(3, max_number + 1):
        is_prime = all(idx % prime != 0 for prime in prime_list)
        if is_prime:
            prime_list.append(idx)

    print prime_list
    print sum(prime_list)

if __name__ == '__main__':
    prime_summation()