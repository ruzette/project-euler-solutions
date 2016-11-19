#!/usr/bin/env python
"""
Problem 22 - Names Sources

Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical 
value for each name, multiply this value by its alphabetical position in the 
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is 
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

"""
import os
from pprint import pprint

def get_data():
    data_file = os.path.dirname('__file__')
    data_file = os.path.join(data_file, 'data', 'p022_names.txt')

    names_data = []

    with open(data_file, 'r') as infile:
        names_data = infile.read().strip()
        names_data = names_data.split(',') 
        names_data = [ x.strip('\"') for x in names_data if x.strip()]
    return names_data

def get_sum_list(sorted_names_list):
    names_score_list = []
    for idx, name in enumerate(sorted_names_list):
        name_sum = 0
        for letter in name:
            name_sum += ord(letter) - 64
        names_score_list.append(name_sum)
    return names_score_list

def get_total_score(names_score_list):
    total_names_scores = 0
    for idx, score in enumerate(names_score_list):
        total_names_scores += (idx+1) * score

    return total_names_scores

def names_sources():
    names_list  = get_data()
    sorted_names_list = sorted(names_list)
    names_score_list = get_sum_list(sorted_names_list)
    total_names_scores = get_total_score(names_score_list)
    pprint(total_names_scores)



if __name__ == '__main__':
    names_sources()