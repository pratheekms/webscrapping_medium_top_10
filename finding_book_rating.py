# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:08:36 2020

@author: pratms
"""
import time
start = time.time()
import bs4,requests
import openpyxl
path=r"C:\Users\pratms\pythonprojects\webscrapping\webscrapping_medium_top_10\excel_doc.xlsx"

wb_obj=openpyxl.load_workbook(path)
sheet_obj=wb_obj.active
m_row=sheet_obj.max_row