import pandas as pd
import openpyxl 

a = ["J66", "J67", "J68", "J69"]
b = "J66"
title = ["PostDate", "Stkcd", "TotalPosts", "AvgReadings", "AvgComments", "AvgNetComments", "AvgThumbUps", "AvgUserBarAge", "AvgUserInfluIndex", "AvgUserPosts", "AvgUserComments", "Indcd"]
stock = openpyxl.load_workbook("./Result/2017_code.xlsx")
stock_sheet = stock['工作表1']

delete_stock = openpyxl.Workbook()
delete_stock_sheet = delete_stock['Sheet']

for i in range(1, stock_sheet.max_column+1):
    delete_stock_sheet.cell(row=1, column=i, value=title[i-1])

row = delete_stock_sheet.max_row+1
for l in range(1, stock_sheet.max_column+1):
    delete_stock_sheet.cell(row=row, column=l, value=stock_sheet.cell(row=2, column=l).value)


delete_stock_sheet.cell(row=1, column=delete_stock_sheet.max_column+2, value="刪除筆數")
delete_stock_sheet.cell(row=2, column=delete_stock_sheet.max_column, value=delete_stock_sheet.max_row-1)


delete_stock.save(r'./Result/2017_delete_stock.xlsx')