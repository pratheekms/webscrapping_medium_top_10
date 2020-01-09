# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:38:56 2020

@author: pratms
"""
import time
start = time.time()
import bs4,requests
finalResult=[]
bookcount=1
    
url="https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
res=requests.get(url,verify=False)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'lxml')
slno=soup.find_all("a",attrs={"class":"fi cn hx hy hz ia"})
bookAndAuthors=soup.find_all("strong",attrs={"class":"id ke"})
#print("slno----------------")
#print(str(slno)+"\n")
#print("bookauthor----------------")
#print(str(bookAndAuthors)+"\n")

for i in range(0,len(bookAndAuthors)-4):
    finalResult.append(bookAndAuthors[i].getText())
    print(bookAndAuthors[i].getText())
    
    
print("aa----------------")

for i in finalResult:
    print("book "+str(bookcount)+"--"+i)
    bookcount=+1

#print("\n"+"\n")

    
end = time.time()
print("time taken by program is:"+str(end - start)) 