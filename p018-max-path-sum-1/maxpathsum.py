#!/usr/bin/env python
"""
Problem 18 - Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)

"""
import os
from pprint import pprint

class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def get_data():
    data_file = os.path.dirname('__file__')
    data_file = os.path.join(data_file, 'data', 'p018_path.txt')

    infile_data = []

    with open(data_file, 'r') as infile:
        infile_data = infile.readlines()
        infile_data = [ x.strip() for x in infile_data if x.strip()]
    return infile_data

def build_tree_path(data_lines):
    tree_path = []
    for idx, line in enumerate(data_lines):
        tree_str = ' ' * (2*(len(data_lines)-(idx))) + '%s' % line
        tree_path.append(tree_str)
    return tree_path

def normalize_tree_path(data_lines, tree_path):
    tree_list = []
    for idx, line in enumerate(data_lines):
        tree_node_list = []
        path_nums = line.split('  ')

        for p in path_nums:
            node_pos = tree_path[idx].index(p)
            left_node, right_node = (None, None)
            if (idx+1) != len(data_lines):
                left_node = tree_path[idx+1][node_pos-2:node_pos]
                right_node = tree_path[idx+1][node_pos+2:node_pos+4] 

            data = {'node' : p, 'left' : left_node, 'right' : right_node}
            tree_node_list.append(data)

        tree_list.append(tree_node_list)
    return tree_list

def create_node(index, tree_list, node_data=None):
    node = Node()

    if index == len(tree_list):
        return node

    index_tree_list = tree_list[index]
    index_node_dict = {}
    for tree_node_dict in index_tree_list:
        if tree_node_dict['node'] == node_data:
            index_node_dict = tree_node_dict
            break


    if not index_node_dict:
        return node
    
    node.data = node_data
    node.left = create_node(index+1, tree_list, index_node_dict['left'])
    node.right = create_node(index+1, tree_list, index_node_dict['right'])

    return node


def preorder(node):
    if not node:
        return None
    
    left_data = preorder(node.left)
    right_data = preorder(node.right)

    left_num, right_num = (0, 0)

    if left_data:
        left_num = left_data

    if right_data:
        right_num = right_data

    if left_num >= right_num and node.data:
        return int(node.data) + left_num
    elif left_num < right_num and node.data:
        return int(node.data) + right_num

    return node.data

if __name__ == '__main__':
    data_lines = get_data()
    tree_path = build_tree_path(data_lines)
    tree_list = normalize_tree_path(data_lines, tree_path)
    tree_node = create_node(0, tree_list, tree_list[0][0]['node'])    
    max_sum_path = preorder(tree_node)
    print max_sum_path
