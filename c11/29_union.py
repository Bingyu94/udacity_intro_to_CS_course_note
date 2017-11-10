# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:34:58 2017

@author: Administrator
"""

# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)

a = [1,2,3]
b = [2,4,6]
union(a, b)
print a
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]