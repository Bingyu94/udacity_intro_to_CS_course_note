# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:56:07 2017

@author: Administrator
"""

# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    mul = 1
    for e in list_of_numbers:
        mul = mul * e
    return mul

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1