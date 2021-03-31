import os
from datetime import datetime
import pandas as pd 
import numpy as np
from tqdm import *

year = 2017

stock_path = './'+ str(year) + '/' + str(year) + '_刪除無分析師預測後剩餘股吧名單.xlsx'
stock = pd.read_excel(stock_path, engine='openpyxl')
stock_value = stock.values

predict_stock2017_path = "./2017/分析師預測2017.xlsx"
predict_stock2017 = pd.read_excel(predict_stock2017_path, engine='openpyxl')
predict_stock2017_value = predict_stock2017.values

predict_stock2018_path = "./2018/分析師預測2018.xlsx"
predict_stock2018 = pd.read_excel(predict_stock2018_path, engine='openpyxl')
predict_stock2018_value = predict_stock2018.values

predict_stock2019_path = "./2019/分析師預測2019.xlsx"
predict_stock2019 = pd.read_excel(predict_stock2019_path, engine='openpyxl')
predict_stock2019_value = predict_stock2019.values

AF_Actual_path = './'+ str(year) + '/AF_Actual' + str(year) + '.xlsx'
AF_Actual = pd.read_excel(AF_Actual_path, engine='openpyxl')
AF_value = AF_Actual.values

# test area #

# test area #

# search stkcd and its season #

predict_stock_start = 1
stkcd_list = []
# season_list = []

# len(stock)

for i in range(len(stock)):
    
    InfluIndex = stock_value[i][8]

    if (InfluIndex < 2.5):
        continue;
    else :
        stkcd = stock_value[i][1]
        date = str(stock_value[i][0])
        # print(date)

        # calculate season
        if (date[6] == '-'):
            month = int(date[5])
        elif (date[7] == '-'):
            month = int(date[5:7])
        season = int((month-1)/3) + 1

        # renew stkcd_list
        if ([stkcd,season] not in stkcd_list):
            stkcd_list.append([stkcd, season])
            # season_list.append(season)
        
        

# print(stkcd_list)
# print(season_list)

# search stkcd and its season #

# record the data of each season #

predicter_list_Q0 = []
predicter_list_Q1 = []
predicter_list_Q2 = []
predicter_list_Q3 = []
predicter_list_Q4 = []
predicter_list_Q5 = []

for i in trange(len(stkcd_list)):

    stkcd = stkcd_list[i][0]

    if( year == 2017):
        for j in range(len(predict_stock2017_value)):
            if (stkcd == predict_stock2017_value[j][0]):
                date = str(predict_stock2017_value[j][1])

                # calculate season
                if (date[6] == '-'):
                    month = int(date[5])
                elif (date[7] == '-'):
                    month = int(date[5:7])
                season = int((month-1)/3) + 1

                if (season == 1):
                    predicter_list_Q1.append(predict_stock2017_value[j])
                elif (season == 2):
                    predicter_list_Q2.append(predict_stock2017_value[j])
                elif (season == 3):
                    predicter_list_Q3.append(predict_stock2017_value[j])
                elif (season == 4):
                    predicter_list_Q4.append(predict_stock2017_value[j])

            elif (stkcd < predict_stock2017_value[j][0]): break;
        
        for j in range(len(predict_stock2018_value)):
            if (stkcd == predict_stock2018_value[j][0]):
                date = str(predict_stock2018_value[j][1])

                # calculate season
                if (date[6] == '-'):
                    month = int(date[5])
                elif (date[7] == '-'):
                    month = int(date[5:7])
                season = int((month-1)/3) + 1

                if (season == 1):
                    predicter_list_Q5.append(predict_stock2018_value[j])

            elif (stkcd < predict_stock2018_value[j][0]): break;


# print(len(predicter_list_Q1), len(predicter_list_Q2), len(predicter_list_Q3), len(predicter_list_Q4))
# print(len(predicter_list_Q5))
# temp = np.array(predicter_list_Q4)
# print(temp[:,3])

# too slow
influential_predicter = []
file1 = [['Stkcd', 'season', 'AnanmID', 'Ananm']]
exist_data = []
pop_times = 0
temp_list_row = [0,0,0,0]
# len(stkcd_list)
for i in trange(len(stkcd_list)):
    stkcd = stkcd_list[i][0]
    season = stkcd_list[i][1]
    temp_data = []
    if (season == 1):
        if (year == 2017):
            # print("No data")
            continue;
        """
        else :
            for j in range(len(predicter_list_Q0)):
                if (predicter_list_Q0[j][3] in predicter_list_Q2[:][3]):
                    temp = predicter_list_Q2[:][3]
                    index = predicter_list_Q2[:][3].index(predicter_list_Q0[j][3])
                    influential_predicter.append([predicter_list_Q0[j], predicter_list_Q2[index][8]])
        """
        
    elif (season == 2):
        temp_list = np.array(predicter_list_Q3)

        # predicterID list
        temp = temp_list[:,3]
        
        predicter = []
        # find in front season
        for j in range(temp_list_row[1], len(predicter_list_Q1)):

            # stkcd in temp_list
            stkcd_temp = predicter_list_Q1[j][0]
            
            if (predicter_list_Q1[j][3] in temp):
                # predicter.append(predicter_list_Q1[j][3])
                # influential_predicter.append(predicter_list_Q1[j])
                # write File1
                data = [stkcd, season, predicter_list_Q1[j][3], predicter_list_Q1[j][4]]
                temp_data.append(data)
            elif (stkcd_temp > stkcd): 
                temp_list_row[1] = j 
                break
            
        """
        # find in next season
        for j in range(len(predicter_list_Q3)):
            if (predicter_list_Q3 in predicter):
                influential_predicter.append(predicter_list_Q3[j])
        """

    elif (season == 3):
        temp_list = np.array(predicter_list_Q4)
        # predicterID list
        temp = temp_list[:,3]
        predicter = []
        # find in front season
        for j in range(temp_list_row[2], len(predicter_list_Q2)):

            # stkcd in temp_list
            stkcd_temp = predicter_list_Q2[j][0]

            if (predicter_list_Q2[j][3] in temp):
                # predicter.append(predicter_list_Q1[j][3])
                # influential_predicter.append(predicter_list_Q2[j])
                # write File1
                data = [stkcd, season, predicter_list_Q1[j][3], predicter_list_Q1[j][4]]
                temp_data.append(data)
            elif (stkcd_temp > stkcd): 
                temp_list_row[2] = j 
                break
        """
        # find in next season
        for j in range(len(predicter_list_Q4)):
            if (predicter_list_Q4 in predicter):
                influential_predicter.append(predicter_list_Q4[j])
        """
    elif (season == 4):
        temp_list = np.array(predicter_list_Q5)
        # predicterID list
        temp = temp_list[:,3]
        predicter = []
        # find in front season
        for j in range(temp_list_row[2], len(predicter_list_Q3)):

            # stkcd in temp_list
            stkcd_temp = predicter_list_Q3[j][0]

            if (predicter_list_Q3[j][3] in temp):
                # predicter.append(predicter_list_Q1[j][3])
                # influential_predicter.append(predicter_list_Q3[j])
                # write File1
                data = [stkcd, season, predicter_list_Q1[j][3], predicter_list_Q1[j][4]]
                temp_data.append(data)
            elif (stkcd_temp > stkcd): 
                temp_list_row[3] = j 
                break;
        """
        # find in next season
        for j in range(len(predicter_list_Q5)):
            if (predicter_list_Q5 in predicter):
                influential_predicter.append(predicter_list_Q5[j])
        """
    # file1.append(data)
    for rows in range(len(temp_data)):
        # write file
        if (temp_data[rows] not in exist_data):
            file1.append(temp_data[rows])
            exist_data.append(temp_data[rows])
        
        if (len(exist_data) >= 250):
            exist_data.pop(0)
            pop_times += 1
    # print(data)
    

# print(file1[:10])
print("poptimes:" , pop_times)
print("len:" , len(exist_data))


# print(influential_predicter)
output = pd.DataFrame(data=file1)
"""
exist_data = []
drop_list = []
for i in trange(1, len(file1)):
    if (file1[i] in exist_data):
        drop_list.append(i)
    else :
        exist_data.append(file1[i])
    
output = output.drop(drop_list, axis=0)
"""        
# print(file1[1])
# print(drop_list)

output.to_excel('./Result/' + str(year) + '/' + str(year) + '_具有影響力分析師.xlsx')
        


