# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:41:32 2017

@author: Administrator
"""

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def median(a,b,c):
    small = 0
    big = 0
    if a < b:
        small = a
        big = b
    else:
        small = b
        big = a
    if c < small:
        return small
    if c > big:
        return big
    return c
    


print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7







