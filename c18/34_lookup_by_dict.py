# -*- coding: utf-8 -*-
"""
Created on Sun Nov 05 11:25:24 2017

@author: Administrator
"""

# Change the lookup procedure
# to now work with dictionaries.

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None
    
# =============================================================================
#     for entry in index:
#         if entry[0] == keyword:
#             return entry[1]
#     return None
# =============================================================================
