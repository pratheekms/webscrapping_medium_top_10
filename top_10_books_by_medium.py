# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:38:56 2020

@author: pratms
"""
import bs4,requests
finalResult={}

    
    url='https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5'
    res=requests.get(urlName,verify=False)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'lxml')
    value=soup.find_all("em",attrs={"class":"jb"})
    print(value)