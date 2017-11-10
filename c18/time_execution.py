# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 17:31:57 2017

@author: Administrator
"""

import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1
    
print time_execution('spin_loop(10 ** 5)')
print time_execution('1+1')