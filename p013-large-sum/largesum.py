#!/usr/bin/env python
"""
Problem 13 - Large Sum

Work out the first ten digits of the sum of the 
following one-hundred 50-digit numbers.

"""
import os
from pprint import pprint

def get_data():
    data_file = os.path.dirname('__file__')
    data_file = os.path.join(data_file, 'data', 'p013_digits.txt')

    digits_data = []
    with open(data_file, 'r') as infile:
        digits_data = infile.readlines()
        digits_data = [ x.strip() for x in digits_data if x.strip() ]

    return digits_data

def large_sum():
    digits_list = get_data()
    int_digits_list = [int(x) for x in digits_list]
    sum_digits = sum(int_digits_list)
    first_ten_digits = str(sum_digits)[:10]
    pprint(first_ten_digits)


if __name__ == '__main__':
    large_sum()