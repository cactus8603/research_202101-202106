import csv
from tqdm import tqdm, trange
import pandas as pd
import numpy as np
import os
year = 2017

total_stock = []
AF_Actual = []
predict_stock = []

with open('./Result/'+ str(year) + '/' + str(year) + '_刪除無分析師預測後剩餘股吧名單.csv', newline='', encoding="utf-8", errors='ignore') as stock:
    rows = csv.reader(stock)

    header = next(rows)
    total_stock.append(header)
    print(header[8])
    for row in rows:
        total_stock.append(row)

with open("./" + str(year) + "/分析師預測" + str(year) +  ".csv", newline='', encoding="utf-8", errors='ignore') as predict:
    rows = csv.reader(predict)

    for row in rows:
        predict_stock.append(row)


with open('./'+ str(year) + '/AF_Actual' + str(year) + '.csv', newline='', encoding="utf-8", errors='ignore') as AF:
    rows = csv.reader(AF)

    header = next(rows)
    AF_Actual.append(header)

    for row in rows:
        AF_Actual.append(row)





predict_stock_start = 1
# AF_start = 1
# 股票代號、分析師預測.csv起始行數、季度
stkcd_index = [[0,0,0]]
stkcd_list = [0,]
# len(total_stock)
for i in range(1, 100):
    temp = float(total_stock[i][8])
    stkcd = 0
    if (temp >= 2.5):
        stkcd =  int(total_stock[i][1])
        date = total_stock[i][0]
        # month = 0
        if (date[6] == '-'):
            month = int(date[5])
        elif (date[7] == '-'):
            month = int(date[5:7])
        season = int((month-1)/3) + 1

        # 在"分析師預測year.csv"檔案中，找到相同股票代號
        
        # if (stkcd not in stkcd_list):
        # print(stkcd)
        if (stkcd not in stkcd_list):
            stkcd_list.append(stkcd)
        # 在分析師預測year.csv中，設定起始點
        if (stkcd_index[len(stkcd_index)-1][1] != 0):
            predict_stock_start = stkcd_index[len(stkcd_index)-1][1]
        else: predict_stock_start = 1

        # 紀錄相同股票代號在分析師預測year.csv中的範圍
        # len(predict_stock)
        for j in range(predict_stock_start, len(predict_stock)):
            temp_stkcd = int(predict_stock[j][0])
            if (temp_stkcd == stkcd):
                # print(temp, j, stkcd)
                temp = 0
                for k in range(len(stkcd_index)-1, 1, -1):
                    if(stkcd_index[k][0] == temp_stkcd and stkcd_index[k][2] == season):
                        temp = k
                        break;
                if(stkcd_index[temp][0] == temp_stkcd and stkcd_index[temp][2] == season):
                    break;
                stkcd_index.append([temp_stkcd, j, season])
                break;

                    
print(stkcd_index)
print(stkcd_list)
"""
# len(total_stock)
for i in trange(1000, 0, -1):
    stkcd = stkcd_list[len(stkcd_list)-1]
    if (stkcd == int(total_stock[i][1])):
        stkcd_index.append([0, i+1])
        break;
"""

# 

# 

# print(stkcd_index)

predicter_list_Q1 = []
predicter_list_Q2 = []
predicter_list_Q3 = []
predicter_list_Q4 = []

for i in range(1, len(stkcd_list)):
    stkcd = int(stkcd_list[i])


    predict_stock_start = stkcd_index[i][1]
    # print(stkcd)
    # print(stkcd_index[i][1], stkcd_index[i+1][1])
    
    # 找相同的分析師
    for j in range(stkcd_index[i][1], len(predict_stock)):
        if (stkcd == int(predict_stock[j][0])):
            # 紀錄
            date = predict_stock[j][1]
            AnanmID = predict_stock[j][3]
            ReportID = predict_stock[j][5]
            InstitutionID = predict_stock[j][6]
            Brokern = predict_stock[j][7]
            Feps = predict_stock[j][8]


            # 計算季度
            if (date[6] == '/'):
                    month = int(date[5])
            elif (date[7] == '/'):
                month = int(date[5:7])
            season = int((month-1)/3) + 1
            
            
            # 記錄到各個季度中
            if (season == 1):
                predicter_list_Q1.append([stkcd, AnanmID, ReportID, InstitutionID, Feps])
            elif (season == 2):
                predicter_list_Q2.append([stkcd, AnanmID, ReportID, InstitutionID, Feps])
            elif (season == 3):
                predicter_list_Q3.append([stkcd, AnanmID, ReportID, InstitutionID, Feps])
            elif (season == 4):
                predicter_list_Q4.append([stkcd, AnanmID, ReportID, InstitutionID, Feps])
        elif (stkcd != int(predict_stock[j][0])): break;


# print(predicter_list_Q1)
# print(predicter_list)

# 找前後一季都有相同的分析師
influential_predicter = [['stkcd', 'season', 'AnanmID']]
influential_predicter_and_value = [['stkcd', 'front', 'next', 'AnanmID', 'InstitutionID', 'Brokern']]
calculate_value = [['FE1', 'FE2', 'FE3', 'FE4']]

for i in range(1, len(stkcd_index)):
    # 取得股票代號
    stkcd = int(stkcd_index[i][0])
    # print("stkcd:", stkcd)
    # print("stkcd_index", stkcd_index[i][1])

    # 
    
    for j in range(stkcd_index[i][1], len(predict_stock)):
        # 檢查股票代號
        if (stkcd == int(predict_stock[j][0])):

            season = int(stkcd_index[i][2])
            # print(stkcd == int(predict_stock[j][0]))
            
            # print("season", season)
            
            if (season == 1):
                if (year == 2017): break;
                print("season1 finish")
                # elif:
            """
            elif (season == 2):
                front_season_predicter = []
                front_predicter =  []
                # front_season_predicter_and_feps = []
                # 紀錄前一季的資料
                for k in range(len(predicter_list_Q1)):
                    # 檢查下一項資料是否相同，若相同則以新資料為主
                    if (k < len(predicter_list_Q1)-1):
                        temp = k + 1
                        if (predicter_list_Q1[k][1] == predicter_list_Q1[temp][1]):
                            # print(predicter_list_Q1[k][1], predicter_list_Q1[temp][1])
                            continue;

                    # 相同股票代碼
                    if (int(predicter_list_Q1[k][0]) == stkcd):
                        # 紀錄 predicterID, Feps

                        front_season_predicter.append([
                            predicter_list_Q1[k][1], 
                            predicter_list_Q1[k][6]
                        ])
                        front_predicter.append([
                            predicter_list_Q1[k][1]
                        ])

                # 比較後一季的資料

                for k in range(len(predicter_list_Q3)):
                    # 檢查一下一項資料，若相同則以新資料為主
                    if (k < len(predicter_list_Q1)-1):
                        temp = k + 1
                        if (predicter_list_Q1[k][1] == predicter_list_Q1[temp][1]):
                            continue;
                    
                    # 相同股票代碼
                    if (int(predicter_list_Q3[k][0]) == stkcd):
                        # for l in range(len(front_season_predicter)-1):
                        
                        # 前後一季predicterID比較
                        if (predicter_list_Q3[k][1] in front_predicter):
                            break;
                            # 紀錄 股票代號、季度、分析師
                            influential_predicter.append([
                                stkcd, 
                                2, 
                                predicter_list_Q3[k][1]
                                ])
                            # 紀錄 股票代號、分析師、前一季feps，後一季feps，分析師代碼、證券商ID，證券商
                            influential_predicter_and_value.append([
                                stkcd, 
                                predicter_list_Q3[k][1], 
                                front_season_predicter[1], 
                                predicter_list_Q3[k][6], 
                                predicter_list_Q3[k][2],
                                predicter_list_Q3[k][4],
                                predicter_list_Q3[k][5]
                                ])
                            print("seson2 finish")
            """
            if (season == 3):
                
                front_season_predicter = []
                front_predicter = []
                # front_season_predicter_and_feps = []
                # 紀錄前一季的資料
                for k in range(len(predicter_list_Q2)):
                    # print("Season3 in")
                    # 檢查下一項資料是否相同，若相同則以新資料為主
                    if (k < len(predicter_list_Q2)-1):
                        temp = k + 1
                        if (predicter_list_Q2[k][1] == predicter_list_Q2[temp][1]):
                            # print(predicter_list_Q1[k][1], predicter_list_Q1[temp][1])
                            continue;

                    # 相同股票代碼
                    if (int(predicter_list_Q2[k][0]) == stkcd):
                        # 紀錄 predicterID, Feps
                        front_season_predicter.append([
                            predicter_list_Q2[k][1], 
                            predicter_list_Q2[k][4]
                            ])
                        front_predicter.append([
                            predicter_list_Q2[k][1]
                        ])

                # 比較後一季的資料
                
                for k in range(len(predicter_list_Q4)):
                    # 檢查一下一項資料，若相同則以新資料為主
                    
                    if (k < len(predicter_list_Q2)-1):
                        temp = k + 1
                        if (predicter_list_Q2[k][1] == predicter_list_Q2[temp][1]):
                            continue;
                    # print(int(predicter_list_Q4[k][0]), stkcd)
                    # input()
                    # break;
                    # 相同股票代碼
                    if (int(predicter_list_Q4[k][0]) == stkcd):
                        # for l in range(len(front_season_predicter)-1):
                        # 前後一季predicterID比較
                        print( type(predicter_list_Q4[k][1]))
                        if (predicter_list_Q4[k][1] in front_predicter):
                            print("next")
                            # print(predicter_list_Q4[k][1] in front_predicter)
                            
                            # 紀錄 股票代號、季度、分析師
                            influential_predicter.append([
                                stkcd, 
                                3, 
                                predicter_list_Q4[k][1]
                                ])
                            # 紀錄 股票代號、分析師ID、前一季feps，後一季feps、證券商ID
                            influential_predicter_and_value.append([
                                stkcd, 
                                predicter_list_Q4[k][1], 
                                front_season_predicter[1], 
                                predicter_list_Q4[k][4], 
                                predicter_list_Q4[k][3]
                                ])
                            print("season3 finish")
                """
                    # print("ok season4")
                print(front_predicter)
                print(len(front_predicter))
            # elif (season == 4):



# print()

print(influential_predicter)
print(influential_predicter_and_value)

"""

with open('./Result/' + str(year) + '/' + str(year) + '_具有影響力之分析師.csv','w', newline='', encoding="utf-8") as f:
    writeCsv = csv.writer(f)
    writeCsv.writerows(influential_predicter)

# print(stkcd_list)

"""
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

"""