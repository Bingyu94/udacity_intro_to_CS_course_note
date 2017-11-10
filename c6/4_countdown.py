# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:42:31 2017

@author: Administrator
"""

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).


def countdown(n):
    while n >=1 :
        print n
        n = n - 1
    print 'Blastoff!'



countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!


