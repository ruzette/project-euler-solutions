#!/usr/bin/env python
"""
Problem 14 - Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import os
import sys
from pprint import pprint

def get_sequence(index):
    chain_list = [ index ]
    while index != 1:
        if index % 2 == 0:
            index = index / 2
        else:
            index = (3*index) + 1
        chain_list.append(index)

    return chain_list

def get_sequence_list_by_counter(max_count):
    collatz_chain_list = []

    for index in range(1, max_count):
        chain_list = get_sequence(index)
        collatz_chain_list.append(chain_list)
        print "Index : ", index, " Length : ", len(chain_list)
    
    return collatz_chain_list

def get_collatz_sequence():
    max_count = 1000000
    collatz_chain_list = get_sequence_list_by_counter(max_count)
    max_collatz_chain = max(collatz_chain_list, key=len)
    collatz_index = collatz_chain_list.index(max_collatz_chain) + 1 
    print "Collatz Sequence Index : ", collatz_index



if __name__ == '__main__':
    get_collatz_sequence()