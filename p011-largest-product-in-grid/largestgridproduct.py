#!/usr/bin/env python
"""
Problem 11 - Largest product in a grid

In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.

What is the greatest product of four adjacent numbers 
in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?

"""
import os
from pprint import pprint

def get_data():
    data_file = os.path.dirname('__file__')
    data_file = os.path.join(data_file, 'data', 'p011_grid.txt')

    digits_data = []
    with open(data_file, 'r') as infile:
        digits_data = infile.readlines()
        digits_data = [ x.strip().split(' ') for x in digits_data if x.strip() ]
    return digits_data

def get_product(digits_list):
    product = 1

    for idx, val in enumerate(digits_list):
        product *= int(val)
    return product

def get_horizontal_product_list(digits_list, max_adjacent_num = 4):
    row_products = []

    for ridx, row_list in enumerate(digits_list):
        for cidx, cell_value in enumerate(row_list):
            if cidx >= (len(row_list) - max_adjacent_num + 1):
                continue
            product = get_product(row_list[cidx:(cidx+max_adjacent_num)])
            row_products.append(product)

    return row_products

def get_vertical_product_list(digits_list, max_adjacent_num=4):
    col_products = []
    col_length = len(digits_list[0])
    row_length = len(digits_list)

    for cidx in range(col_length):
        for ridx in range(row_length - max_adjacent_num + 1):
            digits = [ row[cidx] for row in digits_list[ridx:(ridx+max_adjacent_num)]]
            product = get_product(digits)
            col_products.append(product)

    return col_products

def get_diagonal_product_list(digits_list, reverse=False, max_adjacent_num=4):
    diagonal_products = []
    col_length = len(digits_list[0]) - max_adjacent_num + 1
    row_length = len(digits_list) - max_adjacent_num + 1
    new_digits_list = digits_list[:]

    if reverse:
        for idx in range(len(new_digits_list)):
            new_digits_list[idx].reverse()

    for ridx in range(row_length):
        for cidx in range(col_length):
            digits = [new_digits_list[ridx+x][cidx+x] for x in range(0, max_adjacent_num)]
            product = get_product(digits)
            diagonal_products.append(product)

    return diagonal_products

def large_grid_product():
    digits_list = get_data()
    horizontal_product_list = get_horizontal_product_list(digits_list)
    vertical_product_list = get_vertical_product_list(digits_list)
    right_diagonal_product_list = get_diagonal_product_list(digits_list)
    left_diagonal_product_list = get_diagonal_product_list(digits_list,reverse = True)
    max_product_list = [    max(horizontal_product_list), max(vertical_product_list), 
                            max(right_diagonal_product_list), max(left_diagonal_product_list) ]

    print max(max_product_list)

if __name__ == '__main__':
    large_grid_product()