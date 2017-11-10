# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:43:15 2017

@author: Administrator
"""

# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(s,t):
    pos = s.find(t)
    if pos == -1:
        return -1
    while pos != -1:
        lastpos = pos
        pos = s.find(t, pos+1)
    return lastpos



print find_last('aaasa', 's')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0




