import csv
from tqdm import tqdm, trange
import pandas as pd

total_stock = []
delete_stock = []
remain_stock = []
"""
# 2018
with open('2018/20181股吧.csv', newline='') as stock:
    rows = csv.reader(stock)
    
    for row in rows:
        total_stock.append(row)

with open('2018/20182股吧.csv', newline='') as stock:
    rows = csv.reader(stock)
    headers = next(rows)

    for row in rows:
        total_stock.append(row)

with open('2018股吧.csv','w', newline='') as f:
    writeCsv = csv.writer(f)
    writeCsv.writerows(total_stock)

print("finish")
"""
zero = 0
# 2020
with open('2020/2020股吧1.csv', newline='') as stock:
    rows = csv.reader(stock)
    for row in rows:
        if (row[2] != '0'):
            total_stock.append(row)

stock.close()

with open('2020/2020股吧2.csv', newline='') as stock:
    rows = csv.reader(stock)
    headers = next(rows)

    for row in rows:
        if (row[2] != '0'):
            total_stock.append(row)
stock.close()

with open('2020/2020股吧3.csv', newline='') as stock:
    rows = csv.reader(stock)
    headers = next(rows)

    for row in rows:
        if (row[2] != '0'):
            total_stock.append(row)
stock.close()

with open('Result/2020/2020股吧K.csv','w', newline='') as f:
    writeCsv = csv.writer(f)
    writeCsv.writerows(total_stock)
f.close()

print('finish')
