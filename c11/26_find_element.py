# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:57:49 2017

@author: Administrator
"""

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

# =============================================================================
# def find_element(p, v):
#     i = 0
#     for e in p:
#         if e == v:
#             return i
#         i = i + 1
#     return -1
# =============================================================================

# =============================================================================
# def find_element(p, v):
#     for e in p:
#         if e == v:
#             return p.index(e)
#     return -1
# =============================================================================

# =============================================================================
# def find_element(p, v):
#     if v in p:
#         return p.index(v)
#     return -1
# =============================================================================

def find_element(p, v):
    if v not in p:
        return -1
    return p.index(v)
    

print find_element([1,2,3], 3)
print find_element(['alpha', 'beta'], 'gamma') 