# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:32:02 2017

@author: Administrator
"""

# Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.


def bigger(a,b):
    if a < b :
        a=b
    return a
    




print bigger(2,7)
#>>> 7

print bigger(3,2)
#>>> 3

print bigger(3,3)
#>>> 3