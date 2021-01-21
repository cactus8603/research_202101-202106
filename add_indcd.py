import pandas as pd
from tqdm import tqdm, trange
import openpyxl 

years = ["2017", "2018", "2019"]

for year in years:
    # 讀取股吧內容
    stock = openpyxl.load_workbook("./" + str(year) + "/" + str(year) + "股吧.xlsx")
    stock_sheet = stock['工作表1']

    # 讀取產業代碼
    industrial_code = openpyxl.load_workbook("./" + str(year) + "/產業代碼2017.xlsx")
    industrial_code_sheet = industrial_code['FI_T10']

    # 欲刪除產業代碼
    industrial_code_to_delete = ["J66", "J67", "J68", "J69"]

    # 建立刪除股票名單
    delete_stock = openpyxl.Workbook()
    delete_stock_sheet = delete_stock['Sheet']

    # 建立剩餘股票名單
    new_stock = openpyxl.Workbook()
    new_stock_sheet = new_stock['Sheet']

    # 寫入第一列資訊
    title = ["PostDate", "Stkcd", "TotalPosts", "AvgReadings", "AvgComments", "AvgNetComments", "AvgThumbUps", "AvgUserBarAge", "AvgUserInfluIndex", "AvgUserPosts", "AvgUserComments", "Indcd"]
    for i in range(1, stock_sheet.max_column+1):
        new_stock_sheet.cell(row=1, column=i, value=title[i-1])
        delete_stock_sheet.cell(row=1, column=i, value=title[i-1])


    # 第二列開始讀入資料
    row_temp = 2
    for i in trange(2, stock_sheet.max_row+1):

        # 取得stkcd
        stock_stkcd = int(stock_sheet.cell(row=i, column=2).value)
        industrial_code_stkcd = int(industrial_code_sheet.cell(row=row_temp, column=1).value)

        # 使stkcd相等
        for k in range(row_temp, industrial_code_sheet.max_row+1):
            industrial_code_stkcd = int(industrial_code_sheet.cell(row=row_temp, column=1).value)
            if (industrial_code_stkcd < stock_stkcd):  
                k = k+1
                row_temp = k
            else: break

        # 更新到該年最新的產業代碼
        for j in range(row_temp, industrial_code_sheet.max_row+1):
            if (industrial_code_sheet.cell(row=j, column=1).value != industrial_code_sheet.cell(row=j+1, column=1).value): 
                row_temp = j
                break

        # 取出產業代碼中的stkcd
        industrial_code_stkcd = int(industrial_code_sheet.cell(row=row_temp, column=1).value)

        # 寫入stkcd
        if(stock_stkcd==industrial_code_stkcd):

            # 取出indcd
            industrial_code_indcd = industrial_code_sheet.cell(row=row_temp, column=3).value
            
            # 複製原始檔案並寫入indcd
            stock_sheet.cell(row=i, column=12, value=industrial_code_indcd)
            
            # 確認列數
            delete_row = delete_stock_sheet.max_row+1
            new_row = new_stock_sheet.max_row+1

            # 寫入indcd
            if(industrial_code_indcd in industrial_code_to_delete):
                # 要刪除的
                for l in range(1, stock_sheet.max_column+1):
                    delete_stock_sheet.cell(row=delete_row, column=l, value=stock_sheet.cell(row=i, column=l).value)
            else:
                # 不刪除的
                for l in range(1, stock_sheet.max_column+1):
                    new_stock_sheet.cell(row=new_row, column=l, value=stock_sheet.cell(row=i, column=l).value)

    # 計算刪除筆數
    delete_stock_sheet.cell(row=1, column=delete_stock_sheet.max_column+2, value="刪除筆數")
    delete_stock_sheet.cell(row=2, column=delete_stock_sheet.max_column, value=delete_stock_sheet.max_row-1)

    # 存檔
    stock.save(r'./Result/' + str(year) + '/' + str(year) + '_加入產業代碼股吧.xlsx')
    delete_stock.save(r'./Result/' + str(year) + '/' + str(year) + '_金融產業股吧名單.xlsx')
    new_stock.save(r'./Result/' + str(year) + '/' + str(year) + '_刪除金融產業後剩餘股吧名單.xlsx')
