# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 14:08:40 2017

@author: Administrator
"""

# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    od = ord('a')  + (ord(letter) - ord('a') + n) % (ord('z') - ord('a')+1)
    return chr(od)


print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i