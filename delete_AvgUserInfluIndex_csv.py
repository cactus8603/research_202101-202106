import csv
from tqdm import tqdm, trange
import pandas as pd
# year = 2017
# year = 2018
year = 2019

total_stock = []
delete_stock = []
remain_stock = []
predict_stock = []
not_delete_list = []

with open("./Result/" + str(year) + "/" + str(year) + "_刪除無分析師預測後剩餘股吧名單.csv", newline='', encoding="utf-8") as stock:
    rows = csv.reader(stock)

    header = next(rows)
    total_stock.append(header)
    delete_stock.append(header)
    remain_stock.append(header)

    for row in rows:
        total_stock.append(row)

for i in trange(1, len(total_stock)):

    if (float(total_stock[i][8]) < 2.5):
        delete_stock.append(total_stock[i])
    elif(float(total_stock[i][8]) >= 2.5):
        remain_stock.append(total_stock[i])


with open('./Result/' + str(year) + '/' + str(year) + '_樣本小於2.5股吧名單.csv','w', newline='', encoding="utf-8") as f:
    writeCsv = csv.writer(f)
    delete_stock[1][12] = len(delete_stock) -1 
    # delete_stock[1][13] = len()

    writeCsv.writerows(delete_stock)
    # print(delete_stock[2][1])


with open('./Result/' + str(year) + '/' + str(year) + '_刪除樣本小於2.5後股吧名單.csv','w', newline='', encoding="utf-8") as f:
    writeCsv = csv.writer(f)
    remain_stock[0][12] = ''
    remain_stock[0][13] = ''
    writeCsv.writerows(remain_stock)

# print("delete", remain_stock)

print("finish")

