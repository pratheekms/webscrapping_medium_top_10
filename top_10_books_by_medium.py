# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:38:56 2020

@author: pratms
"""
import time
start = time.time()
import bs4,requests
finalResult={}

    
url="https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
res=requests.get(url,verify=False)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'lxml')
slno=soup.find_all("a",attrs={"class":"fi cn hx hy hz ia"})
bookAndAuthors=soup.find_all("em",attrs={"class":"jb"})
print(slno+"\n")
print(bookAndAuthors+"\n")
print("\n")

    
end = time.time()
print("time taken by program is:"+str(end - start)) 