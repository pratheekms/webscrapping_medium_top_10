# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:08:36 2020

@author: pratms
"""
import time
start = time.time()
import bs4,requests
import openpyxl
path=r"C:\Users\pratms\pythonprojects\webscrapping\webscrapping_medium_top_10\excel_doc1.xlsx"

wb_obj=openpyxl.load_workbook(path)
sheet_obj=wb_obj.active
m_row=sheet_obj.max_row
print("rows="+str(m_row))
for i in range(1,m_row+1):
    cell_obj=sheet_obj.cell(row=i,column=1)
    cell_value=cell_obj.value
    print(cell_value)
    

print("kjhsdh")
print("sfsdfasfdsdfsad")
    
end = time.time()
print("time taken by program is:"+str(end - start)) 