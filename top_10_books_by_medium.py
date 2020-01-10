# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:38:56 2020

@author: pratheek m s
"""
import time
start = time.time()
import bs4,requests
import openpyxl
import random

GlobalPath=r"C:\Users\pratms\pythonprojects\webscrapping\webscrapping_medium_top_10"
path=GlobalPath+r"\excel_doc1.xlsx"
#open excel file code start
wb_objex = openpyxl.Workbook()
sheet_objex = wb_objex.active
sheet_objex.cell(row=1,column=1).value='Sl. No'
sheet_objex.cell(row=1,column=2).value='Book Name'
sheet_objex.cell(row=1,column=3).value='Book Author'
sheet_objex.cell(row=1,column=4).value='Rating'

finalResult=[]
bookdict={}
bookcount=1
    
url="https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
res=requests.get(url,verify=False)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'lxml')
#slno=soup.find_all("a",attrs={"class":"fi cn hx hy hz ia"})
bookAndAuthors=soup.find_all("strong",attrs={"class":"id ke"})

for i in range(0,len(bookAndAuthors)-4):
    if len(bookAndAuthors[i].getText())>2:
        finalResult.append(bookAndAuthors[i].getText())
        print(bookAndAuthors[i].getText())

for i in finalResult:
    print("book "+str(bookcount)+i)
    print(len(finalResult[bookcount-1]))
    bookdict.update({bookcount:{'name':i.split(' by ')[0],'author':i.split(' by ')[1]}})
    bookcount+=1

for bn,ba in bookdict.items():
    print("book num",bn)
    booknum=bn
    for key in ba:
        print(key+":",ba[key])
        bookname=ba['name']
        bookauthor=ba['author']
    f = open(GlobalPath+r"\top100BokksByMedium.txt", "a")
    f.write(str(booknum)+'\t'+str(bookname)+'\t'+bookauthor+'\n')
    f.close()
    sheet_objex.cell(row=booknum+1,column=1).value=str(booknum)
    sheet_objex.cell(row=booknum+1,column=2).value=str(bookname)
    sheet_objex.cell(row=booknum+1,column=3).value=str(bookauthor)
    #sheet_objex.cell(row=booknum+1,column=4).value='Rating'

wb_objex.save(GlobalPath+r"\top100BokksByMedium.xlsx")
#book name and book author details are saved to an excel file
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 


pathForRating=GlobalPath+r"\top100BokksByMedium.xlsx"

wb_obj=openpyxl.load_workbook(pathForRating)
sheet_obj=wb_obj.active
m_row=sheet_obj.max_row
print("rows="+str(m_row))
for i in range(1,m_row+1):
    bookname=sheet_obj.cell(row=i,column=2).value
    bookauthor=sheet_obj.cell(row=i,column=3).value
    searchPhrase=bookname+" by "+bookauthor+" goodreads"
    #searchPhrase="Catch-22 by Joseph Heller in good reads"
    print(searchPhrase)
#searchPhrase="1984 by George Orwell in goodreads" 
    print(searchPhrase) 
    for j in search(searchPhrase, tld="com", num=10, stop=1, pause=random.randint(1,20)): 
        goodreadsurl=j
    print(goodreadsurl)
    print("bs4 starting")
    res=requests.get(goodreadsurl,verify=False)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'lxml')
    ratingObj=soup.find("span", itemprop="ratingValue")
    rating=ratingObj.getText()
    print("ratinng of",bookname,bookauthor, rating)
    sheet_obj.cell(row=i,column=4).value=str(rating)
    print("rating write complete")
wb_obj.save(pathForRating)
print("excel saved")


   
wb_objex.save(r"C:\Users\pratms\pythonprojects\webscrapping\webscrapping_medium_top_10\top100BokksByMedium.xlsx")
   
end = time.time()
print("time taken by program is:"+str(end - start)) 