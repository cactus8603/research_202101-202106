import pandas as pd
import openpyxl 

years = [2017, 2018, 2019]

for year in years:
    print(year)
    stock = openpyxl.load_workbook("./" + str(year) + "/" + str(year) + "股吧.xlsx")
    stock_sheet = stock['工作表1']
    print(int(stock_sheet.cell(row=2 , column=2).value))
    # print(year)
"""
stock = openpyxl.load_workbook("./" + str(years[0]) + "/" + str(years[0]) + "股吧.xlsx")
stock_sheet = stock['工作表1']

print(int(stock_sheet.cell(row=2 , column=2).value))
"""