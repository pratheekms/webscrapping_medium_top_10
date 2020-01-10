# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:03:34 2020

@author: pratms
"""

import openpyxl

path=r"C:\Users\pratms\pythonprojects\webscrapping\webscrapping_medium_top_10\excel_doc1.xlsx"

wb_obj=openpyxl.load_workbook(path)
sheet_obj=wb_obj.active
m_row=sheet_obj.max_row
print("rows="+str(m_row))
for i in range(1,m_row+1):
    bookname=sheet_obj.cell(row=i,column=2).value
    bookauthor=sheet_obj.cell(row=i,column=3).value
    searchPhrase=bookname+" by "+bookauthor+" goodreads"
    #searchPhrase="Catch-22 by Joseph Heller in good reads"
    print(searchPhrase)
    rating=9
    sheet_obj.cell(row=i,column=4).value=str(rating)
    print("rating write complete")
wb_obj.save(r"C:\Users\pratms\pythonprojects\webscrapping\webscrapping_medium_top_10\excel_doc1.xlsx")