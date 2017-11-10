# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 20:13:47 2017

@author: Administrator
"""

# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url) # 没有判断是否重复！
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    co = content.split()
    for c in co:
        add_to_index(index, c, url)
    
def lookup(index,keyword):
    for i in index:
        if i[0] == keyword:
            return i[1]
    return []



add_page_to_index(index,'fake.text',"This is a test is")
add_page_to_index(index,'real.text',"This is a not test")
#print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]

print lookup(index, 'is')
