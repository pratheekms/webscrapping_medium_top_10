# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 19:05:37 2020

@author: pratms
"""
import bs4,requests
#import lxml
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
searchPhrase="1984 by George Orwell in goodreads" 
print(searchPhrase) 
for j in search(searchPhrase, tld="com", num=10, stop=1, pause=3): 
    goodreadsurl=j
    print(goodreadsurl)
print("bs4 starting")
res=requests.get(goodreadsurl,verify=False)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'lxml')
#rating=soup.find_all("span",attrs={"itemprop":"ratingValue"})
ratingObj=soup.find("span", itemprop="ratingValue")
rating=ratingObj.getText()
print(rating)