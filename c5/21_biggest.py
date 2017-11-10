# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:34:22 2017

@author: Administrator
"""

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

def biggest(a,b,c):
    if a > b :
        max = a
    else:
        max = b
    if max < c : 
        max = c
    return max



print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9