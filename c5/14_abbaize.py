# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:29:27 2017

@author: Administrator
"""

# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.



def abbaize(a,b):
    return a + b + b + a





print abbaize('a','b')
#>>> 'abba'

print abbaize('dog','cat')
#>>> 'dogcatcatdog'