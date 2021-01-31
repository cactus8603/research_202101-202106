import csv
from tqdm import tqdm, trange
import pandas as pd


total_stock = []
delete_stock = []
remain_stock = []
industrial_code = []
# 欲刪除產業代碼
industrial_code_to_delete = ["J66", "J67", "J68", "J69"]
delete_total_kinds = []
# year = 2017
year = 2019

with open(str(year) + '/' + str(year) + '股吧.csv', newline='') as stock:
    rows = csv.reader(stock)

    header = next(rows)
    total_stock.append(header)
    delete_stock.append(header)
    remain_stock.append(header)

    for row in rows:
        total_stock.append(row)

with open(str(year) + '/' + '產業代碼' + str(year) + '.csv', newline='') as stock:
    rows = csv.reader(stock)
    
    for row in rows:
        industrial_code.append(row)
"""
print(total_stock[2][1])
print(len(total_stock))
print(industrial_code[2][2])
delete_stock.append(total_stock[1])
delete_stock[1][11] = industrial_code[2][2]
print(delete_stock)
"""
row_temp = 1
# len(total_stock)
for i in trange(1, len(total_stock)):
    # 取得stkcd
    stock_stkcd = int(total_stock[i][1])
    industrial_code_stkcd = int(industrial_code[row_temp][0])
    # print(row_temp, industrial_code_stkcd, stock_stkcd)
    # print(industrial_code_stkcd == stock_stkcd)

    # 使stkcd相等
    for k in range(row_temp, len(industrial_code)+1):
        industrial_code_stkcd = int(industrial_code[row_temp][0])
        if (industrial_code_stkcd < stock_stkcd): 
            k = k + 1
            row_temp = k
        else: 
            break
    
    # print(row_temp, industrial_code_stkcd, stock_stkcd)
    # print(k)
    # 更新到該年最新的產業代碼
    for j in range(row_temp, len(industrial_code)+1):
        if (industrial_code[j][0] != industrial_code[j+1][0]): 
            row_temp = j
            # print(row_temp)
            break

    # 取出產業代碼中的stkcd
    industrial_code_stkcd = int(industrial_code[row_temp][0])

    temp = int( int(stock_stkcd) / (10**(len(str(stock_stkcd))-1)))

    if(stock_stkcd==industrial_code_stkcd):
        # print(stock_stkcd, industrial_code_stkcd)
        # 取出產業代碼
        industrial_code_indcd = industrial_code[row_temp][2]

        total_stock[i][11] = industrial_code_indcd

        # 寫入indcd
        if(industrial_code_indcd in industrial_code_to_delete):
            # 要刪除的
            delete_stock.append(total_stock[i])
            delete_stock[len(delete_stock)-1][11] = industrial_code_indcd
            if (stock_stkcd not in delete_total_kinds):
                delete_total_kinds.append(stock_stkcd)
        elif( temp == 2 or temp == 9 ):
            # 要刪除的
            delete_stock.append(total_stock[i])
            delete_stock[len(delete_stock)-1][11] = industrial_code_indcd
            if (stock_stkcd not in delete_total_kinds):
                delete_total_kinds.append(stock_stkcd)
        else:
            # 不刪除的
            remain_stock.append(total_stock[i])
            remain_stock[len(remain_stock)-1][11] = industrial_code_indcd

    # print(industrial_code_stkcd, stock_stkcd)
    

with open('./Result/' + str(year) + '/' + str(year) + '_加入產業代碼股吧.csv','w', newline='') as f:
    writeCsv = csv.writer(f)
    total_stock[0][12] = ''
    total_stock[0][13] = ''
    writeCsv.writerows(total_stock)


with open('./Result/' + str(year) + '/' + str(year) + '_金融產業股吧名單.csv','w', newline='') as f:
    writeCsv = csv.writer(f)
    delete_stock[1][12] = len(delete_stock) -1 
    delete_stock[1][13] = len(delete_total_kinds)

    writeCsv.writerows(delete_stock)


with open('./Result/' + str(year) + '/' + str(year) + '_刪除金融產業後剩餘股吧名單.csv','w', newline='') as f:
    writeCsv = csv.writer(f)
    remain_stock[0][12] = ''
    remain_stock[0][13] = ''
    writeCsv.writerows(remain_stock)

print("finish")
