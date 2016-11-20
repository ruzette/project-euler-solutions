#!/usr/bin/env python
"""
Problem 19 - Counting Sundays

You are given the following information, 
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, 
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during 
the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import os
import datetime
from pprint import pprint


def total_first_month_sundays():
    first_sunday_counter = 0
    for idx_year in range(1901, 2001):
        for idx_month in range(1, 13):
            day_of_week = datetime.date(year=idx_year, month=idx_month, day=1)
            if day_of_week.strftime('%A') == 'Sunday':
                first_sunday_counter += 1
    print first_sunday_counter

if __name__ == '__main__':
    total_first_month_sundays()