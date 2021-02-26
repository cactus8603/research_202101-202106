import csv
from tqdm import tqdm, trange
import pandas as pd

year = 2017

total_stock = []
AF_Actual = []
predict_stock = []


# 先篩選在"刪除無分析師預測後剩餘股吧名單.csv"檔案中，AvgUserInfluIndex大於等於2.5的項目
with open('./Result/'+ str(year) + '/' + str(year) + '_刪除無分析師預測後剩餘股吧名單.csv', newline='', encoding="utf-8") as stock:
    rows = csv.reader(stock)

    header = next(rows)
    total_stock.append(header)
    for row in rows:
        total_stock.append(row)
        

with open('./'+ str(year) + '/AF_Actual' + str(year) + '.csv', newline='', encoding="utf-8") as AF:
    rows = csv.reader(AF)

    header = next(rows)
    AF_Actual.append(header)

    for row in rows:
        AF_Actual.append(row)

with open("./" + str(year) + "/分析師預測" + str(year) +  ".csv", newline='', encoding="utf-8") as predict:
    rows = csv.reader(predict)

    for row in rows:
        predict_stock.append(row)



# 在"分析師預測year.csv"檔案中，依序尋找 1.相同股票代號 2.前後一季都有相同分析師預測 的項目
stkcd_temp_row = 1
predict_temp_row = 1
# len(total_stock)
for i in range(1, 10):
    for j in range(stkcd_temp_row, len(total_stock)):
        if (float(total_stock[i][8]) >= 2.5):
            stkcd = int(total_stock[i][1])
            # print(stkcd)

    for k in range(stkcd_temp_row, len(predict_stock)):
        if (stkcd == int(predict_stock[k][0])):
            print(k)



# 在"AF_Actualyear.csv"檔案中尋找該股票代號和AEPS

