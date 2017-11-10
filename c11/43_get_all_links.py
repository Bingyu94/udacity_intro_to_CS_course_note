# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:42:08 2017

@author: Administrator
"""

#Finish crawl web

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1 :
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote
    
def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)

# deepth search
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled
            

# https://en.wikipedia.org/wiki/Ada
html = get_page('http://shanchuantian.com/')
#html = get_page('https://classroom.udacity.com/courses/cs101/lessons/48713769/concepts/487275590923')
#print get_all_links(html)
print crawl_web('http://shanchuantian.com/')
