# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 20:51:56 2017

@author: Administrator
"""

# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    i = 0
    table = []
    while i < nbuckets:
        table.append([])
        i = i + 1
    return table

# for 结合range，比while的加1好
def make_hashtable2(nbuckets):
    table = []
    for v in range(0, nbuckets):
        table.append([])
    return table

# wrong
def make_hashtablewrong(nbuckets):
    return [[]]*nbuckets

#print make_hashtable(3)
#print make_hashtablewrong(3)
table = make_hashtablewrong(3)
table[1].append(['ud', ['http:']])
print table[1]
print table[0]
print table