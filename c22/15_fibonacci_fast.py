# -*- coding: utf-8 -*-
"""
Created on Mon Nov 06 15:52:00 2017

@author: Administrator
"""

#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    record = [0] * (n+1)
    record[0] = 0
    record[1] = 1
    i = 2
    while i <= n:
        record[i] = record[i-1] + record[i-2]
        i = i + 1
    return record[n]

# 官方答案 更快
def fibonacci2(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current



print fibonacci(36)
#>>> 14930352

print time_execution('fibonacci(36)')
print time_execution('fibonacci2(36)')