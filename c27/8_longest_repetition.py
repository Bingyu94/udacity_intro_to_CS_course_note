# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 17:43:47 2017

@author: Administrator
"""

# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

# bad idea
def longest_repetition2(p):
    if p == []:
        return None
    cur = p[0]
    oldpos = 0
    #newpos = 0
    maxlen = 1
    maxobj = p[0]
    for i in range(0,len(p)):
        if p[i] != cur:
            cur = p[i]
            if i - oldpos > maxlen:
                maxlen = i - oldpos
                maxobj = p[i-1]
                oldpos = i
    return maxobj

def longest_repetition(p):
    best = None
    length = 0
    current = None
    current_len = 0
    for e in p:
        if current != e:
            current = e
            current_len = 1
        else:
            current_len = current_len + 1
        if current_len > length:
            length = current_len
            best = current
    return best

#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

