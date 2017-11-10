# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 15:41:55 2017

@author: Administrator
"""

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai':17.8, 'Istanbul':13.3, 'Karachi':13.0,
              'Mumbai':12.5}
print 'Istanbul' in population

population['haha'] = 33
print population