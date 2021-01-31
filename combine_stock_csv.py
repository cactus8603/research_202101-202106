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

# 2019
"""
with open('2019/20191股吧.csv', newline='') as stock:
    rows = csv.reader(stock)
    for row in rows:
        total_stock.append(row)
stock.close()

with open('2019/20192股吧.csv', newline='') as stock:
    rows = csv.reader(stock)
    headers = next(rows)

    for row in rows:
        total_stock.append(row)
stock.close()

with open('2019/20193股吧.csv', newline='') as stock:
    rows = csv.reader(stock)
    headers = next(rows)

    for row in rows:
        total_stock.append(row)
stock.close()

with open('2019股吧.csv','w', newline='') as f:
    writeCsv = csv.writer(f)
    writeCsv.writerows(total_stock)
f.close()


print('finish')
