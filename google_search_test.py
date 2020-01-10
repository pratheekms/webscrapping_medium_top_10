# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:05:37 2020

@author: pratms
"""

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "The Unbearable Lightness of Being by Milan Kundera good reads"
  
for j in search(query, tld="com", num=10, stop=1, pause=3): 
    print(j)