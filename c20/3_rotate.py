# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 14:10:59 2017

@author: Administrator
"""

# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
    od = ord('a')  + (ord(letter) - ord('a') + n) % (ord('z') - ord('a')+1)
    return chr(od)

def rotate(s, n):
    # Your code here
    res = ''
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            res = res + shift_n_letters(i, n)
        else:
            res = res + i
    return res

print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???