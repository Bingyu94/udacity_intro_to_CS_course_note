# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:35:54 2017

@author: Administrator
"""

# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    tot = 1
    while n >= 1:
        tot = tot * n
        n = n-1
    return tot



print factorial(4)
#>>> 24
print factorial(5)
#>>> 120
print factorial(6)
#>>> 720

