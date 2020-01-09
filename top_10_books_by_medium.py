# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 16:38:56 2020

@author: pratms
"""
import bs4,requests
finalResult={}

    
    #url='http://www.moneycontrol.com/nifty/nse/nifty-live'
    res=requests.get(urlName,verify=False)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'lxml')
    value=soup.find_all(tagName,attrs={"class":className})
    sensex=value[0].getText()