# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 11:34:52 2017

@author: Administrator
"""

# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    n = ord('a')  + (ord(letter) - ord('a') + 1) % (ord('z') - ord('a')+1)
    return chr(n)

be = ord('a')
for i in range(0,26):
    print shift(chr(be + i))

# =============================================================================
# print shift('a')
# #>>> b
# print shift('n')
# #>>> o
# print shift('z')
# #>>> a
# =============================================================================
