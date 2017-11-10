# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 16:22:51 2017

@author: Administrator
"""

# Question 1: Pick One

# Define a procedure, pick_one, that takes three inputs: a Boolean 
# and two other values. If the first input is True, it should return 
# the second input. If the first input is False, it should return the 
# third input.

# For example, pick_one(True, 37, 'hello') should return 37, and
# pick_one(False, 37, 'hello') should return 'hello'.

def pick_one(ch, a, b):
    if ch:
        return a
    else:
        return b


print pick_one(True, 37, 'hello')
#>>> 37

print pick_one(False, 37, 'hello')
#>>> hello

print pick_one(True, 'red pill', 'blue pill')
#>>> red pill

print pick_one(False, 'sunny', 'rainy')
#>>> rainy