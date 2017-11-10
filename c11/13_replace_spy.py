# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:27:44 2017

@author: Administrator
"""
# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

#replace_spy(spy)
#print spy
#>>> [0,0,8]

def replace_spy(spy):
    spy[2] = spy[2] + 1

spy = [0, 0, 7]
replace_spy(spy)
print spy

p = [1,2]
q = [3,4]
p.append(q)
print p
print len(p)
q[1] = 5
print p

