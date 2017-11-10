# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 16:19:24 2017

@author: Administrator
"""

# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction(time, dis):
    return (dis*2*1000) / time / speed_of_light



print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?

print speed_fraction(16, 20)