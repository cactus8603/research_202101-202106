import os
from datetime import datetime
import pandas as pd 
import numpy as np
from tqdm import *

# read files
more_path = './Result/significance_more.xlsx' 
more = pd.read_excel(more_path, engine='openpyxl')
more_value = more.values

predict_stock2017_path = "./2017/分析師預測2017.xlsx"
predict_stock2017 = pd.read_excel(predict_stock2017_path, engine='openpyxl')
predict_stock2017_value = predict_stock2017.values

predict_stock2018_path = "./2018/分析師預測2018.xlsx"
predict_stock2018 = pd.read_excel(predict_stock2018_path, engine='openpyxl')
predict_stock2018_value = predict_stock2018.values

predict_stock2019_path = "./2019/分析師預測2019.xlsx"
predict_stock2019 = pd.read_excel(predict_stock2019_path, engine='openpyxl')
predict_stock2019_value = predict_stock2019.values

AF2017_path = "./2017/AF_Actual2017.xlsx"
AF2017 = pd.read_excel(AF2017_path, engine='openpyxl')
AF2017_value = AF2017.values

AF2018_path = "./2018/AF_Actual2018.xlsx"
AF2018 = pd.read_excel(AF2018_path, engine='openpyxl')
AF2018_value = AF2018.values

AF2019_path = "./2019/AF_Actual2019.xlsx"
AF2019 = pd.read_excel(AF2019_path, engine='openpyxl')
AF2019_value = AF2019.values

print(AF2017_value[2][2])

"""
index = 224
print(predict_stock2017_value[index])
predict_stkcd = int(predict_stock2017_value[index][0])
predict_date = str(predict_stock2017_value[index][1])
dash = '-'
index_dash = predict_date.index(dash,1)
predict_year = int(predict_date[:predict_date.index(dash)])
predict_month = int(predict_date[predict_date.index(dash)+1:predict_date.index(dash,6)])
predict_season = int((predict_month-1)/3) + 1

predict_AnanmID = str(predict_stock2017_value[index][3])
string = predict_AnanmID.split(',')
string.sort()
temp = ''
for i in range(len(string)):
    temp = temp + str(string[i]) 
    if (i != len(string)-1):
        temp += '-'

print(string)
print(temp)


predict_InstitutionID = str(predict_stock2017_value[index][6])
Feps = predict_stock2017_value[index][7]

predict = [predict_stkcd, predict_year, predict_season, predict_AnanmID, predict_InstitutionID]
print(predict)
"""
# read files finish

output = []
# output = pd.DataFrame(data=output, columns=['stkcd', 'year', 'season', 'Institution', 'AnanmID'])

# ['stkcd', 'year', 'season', 'Institution', 'AnanmID']
index_in_predict_2017 = 0
index_in_predict_2018 = 0
index_in_predict_2019 = 0
AF2017_index = 2
AF2017_stkcd = 0
AF2017_eps = 0.0

AF2018_index = 2
AF2018_stkcd = 0
AF2018_eps = 0.0

AF2019_index = 2
AF2019_stkcd = 0
AF2019_eps = 0.0

target_stkcd_data = []
# len(more_value)
# search in significance_more file
for index in range(160):
    # get data
    stkcd = more_value[index][1]
    time = str(more_value[index][2])
    year = int(time[:4])
    season = int(time[5:])

    IDs = str(more_value[index][3])
    dash = '-'
    index_dash = IDs.index(dash)
    Institution = IDs[:index_dash]
    AnanmID = IDs[(index_dash+1):]
    target_stkcd_data.append([stkcd, year, season, Institution, AnanmID])
    # target_stkcd_data = np.concatenate((target_stkcd_data, [[stkcd, year, season, Institution, AnanmID]]), axis=0)

    
    # print(len(target_stkcd_data), index)
    # print(target_stkcd_data)
    # print(target_stkcd_data[len(target_stkcd_data)-1], index, len(target_stkcd_data)-1)
    # search in predict file
    len_target = len(target_stkcd_data)
    if (len_target>1 and stkcd > int(target_stkcd_data[len_target-2][0])):
        # print(stkcd, target_stkcd_data[len_target-2][0], len_target, index+1)
        # print("00")
        # print(len(target_stkcd_data))
        target_stkcd = target_stkcd_data[len_target-2][0]
        for i in range(AF2017_index, len(AF2017_value)):
            AF2017_stkcd = int(AF2017_value[i][0])
            # print(AF2017_stkcd)

            if (AF2017_stkcd == target_stkcd):
                AF2017_eps = float(AF2017_value[i][2])
                # print("2017: ", target_stkcd, AF2017_eps)
                AF2017_index = i
                break

        for i in range(AF2018_index, len(AF2018_value)):
            AF2018_stkcd = int(AF2018_value[i][0])

            if (AF2018_stkcd == target_stkcd):
                AF2018_eps = float(AF2018_value[i][2])
                # print("2018: ", target_stkcd, AF2018_eps)
                AF2018_index = i
                break
        
        for i in range(AF2019_index, len(AF2019_value)):
            AF2019_stkcd = int(AF2019_value[i][0])

            if (AF2019_stkcd == target_stkcd):
                AF2019_eps = float(AF2019_value[i][2])
                # print("2018: ", target_stkcd, AF2019_eps)
                AF2019_index = i
                break
        # print('over')
        

        # data in predict
        need_data = []
        exist_data = []
        # 2017
        for i in range(index_in_predict_2017, len(predict_stock2017_value)):

            predict_stkcd = int(predict_stock2017_value[i][0])
            if (predict_stkcd > int(target_stkcd_data[len_target-2][0])):
                index_in_predict_2017 = i
                break
            # print(predict_stkcd, int(target_stkcd_data[len_target-2][0]), index)
            predict_date = str(predict_stock2017_value[i][1])
            dash = '-'
            # index_dash = predict_date.index(dash,1)
            predict_year = int(predict_date[:predict_date.index(dash)])
            predict_month = int(predict_date[predict_date.index(dash)+1:predict_date.index(dash,6)])
            predict_season = int((predict_month-1)/3) + 1

            predict_AnanmID = str(predict_stock2017_value[i][3])
            predict_AnanmID = predict_AnanmID.replace(",", "-")

            predict_InstitutionID = str(predict_stock2017_value[i][6])
            Feps = predict_stock2017_value[i][8]

            predict = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID]
            # predict_feps = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps]
            # predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string]
            # predict_feps_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string, Feps]
            if (predict in target_stkcd_data and predict not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID])
                # print(predict)
            
            # if (predict_mod in target_stkcd_data and predict_feps_mod not in need_data):
                # need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string, Feps])
                # print(predict_mod)
            
         
        print("2017 ", len(need_data), index_in_predict_2017)
        exist_data = []
        # 2018
        for i in range(index_in_predict_2018, len(predict_stock2018_value)):
    
            predict_stkcd = int(predict_stock2018_value[i][0])
            if (predict_stkcd > int(target_stkcd_data[len_target-2][0])):
                index_in_predict_2018 = i
                break
            predict_date = str(predict_stock2018_value[i][1])
            dash = '-'
            # index_dash = predict_date.index(dash,1)
            predict_year = int(predict_date[:predict_date.index(dash)])
            predict_month = int(predict_date[predict_date.index(dash)+1:predict_date.index(dash,6)])
            predict_season = int((predict_month-1)/3) + 1

            predict_AnanmID = str(predict_stock2018_value[i][3])
            predict_AnanmID = predict_AnanmID.replace(",", "-")

            predict_InstitutionID = str(predict_stock2018_value[i][6])
            Feps = predict_stock2018_value[i][8]

            predict = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID]
            # predict_feps = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps]
            # predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string]
            # predict_feps_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string, Feps]
            if (predict in target_stkcd_data and predict not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID])
                # print(predict)
            
            # if (predict_mod in target_stkcd_data and predict_feps_mod not in need_data):
                # need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string, Feps])
                # print(predict_mod)
                
        print("2018 ", len(need_data), index_in_predict_2018)
        exist_data = []
        # 2019
        for i in range(index_in_predict_2019, len(predict_stock2019_value)):
        
            predict_stkcd = int(predict_stock2018_value[i][0])
            if (predict_stkcd > int(target_stkcd_data[len_target-2][0])):
                index_in_predict_2019 = i
                break
            predict_date = str(predict_stock2019_value[i][1])
            dash = '-'
            # index_dash = predict_date.index(dash,1)
            predict_year = int(predict_date[:predict_date.index(dash)])
            predict_month = int(predict_date[predict_date.index(dash)+1:predict_date.index(dash,6)])
            predict_season = int((predict_month-1)/3) + 1

            predict_AnanmID = str(predict_stock2019_value[i][3])
            predict_AnanmID = predict_AnanmID.replace(",", "-")

            predict_InstitutionID = str(predict_stock2019_value[i][6])
            Feps = predict_stock2019_value[i][8]

            predict = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID]
            # predict_feps = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps]
            # predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string]
            # predict_feps_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string, Feps]
            if (predict in target_stkcd_data and predict not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID])
            
            # if (predict_mod in target_stkcd_data and predict_feps_mod not in need_data):
                # need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string, Feps])
                # print(predict_mod)
        print("2019 ", len(need_data), index_in_predict_2019)
        
        # need_data = np.array(need_data)
        # need_data = need_data[np.lexsort((need_data[:,2], need_data[:,1]))]
        # print(need_data)
        # print(len(need_data))
        # print(need_data[:, 1])

        # sort by year
        data = pd.DataFrame(need_data, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Feps']).groupby('year', as_index=False)
        data2017 = data.get_group(2017)
        # data2018 = data.get_group(2018)
        # data2019 = data.get_group(2019)
        print(data2017)
        # sort by season
        # 2017
        data2017season = pd.DataFrame(data2017, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Feps']).groupby('season', as_index=False)
        # print(data2017season)
        
        # write data [stkcd, year, season, AF, FE1, FE2, BIAS1, BIAS2]
        # s2
        data2017s2 = np.array(data2017season.get_group(2))
        feps = data2017s2[:,5]
       
        average = round(feps.sum(axis=0) / len(data2017s2), 3)
        # print("average ", average)
        # print(feps)

        
        abs_sum = 0.0
        sum_ = 0.0
        # print("AF", type(AF2017_eps))
        # print("aver", type(average))
        for eps in range(len(feps)):
            abs_sum = abs(AF2017_eps - feps[eps])
            sum_ = AF2017_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2017_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2017s2)), 3)
        BIAS1 = round(float(AF2017_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2017s2))), 3)

        result = [data2017s2[0][0], data2017s2[0][1], data2017s2[0][2], AF2017_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)
        print("2017s2 ", result)

        # s3
        data2017s3 = np.array(data2017season.get_group(2))
        feps = data2017s3[:,5]
        average = round(feps.sum(axis=0) / len(data2017s3), 3)
        abs_sum = 0.0
        sum_ = 0.0
        for eps in range(len(feps)):
            abs_sum = abs(AF2017_eps - feps[eps])
            sum_ = AF2017_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2017_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2017s3)), 3)
        BIAS1 = round(float(AF2017_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2017s3))), 3)

        result = [data2017s3[0][0], data2017s3[0][1], data2017s3[0][2], AF2017_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)
        print("2017s3 ", result)

        # s4
        data2017s4 = np.array(data2017season.get_group(2))
        feps = data201743[:,5]
        average = round(feps.sum(axis=0) / len(data2017s4), 3)
        abs_sum = 0.0
        sum_ = 0.0
        for eps in range(len(feps)):
            abs_sum = abs(AF2017_eps - feps[eps])
            sum_ = AF2017_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2017_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2017s4)), 3)
        BIAS1 = round(float(AF2017_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2017s4))), 3)

        result = [data2017s4[0][0], data2017s4[0][1], data2017s4[0][2], AF2017_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)
        print("2017s4 ", result)

        """
        # 2018
        data2018season = pd.DataFrame(data2018).groupby(2, as_index=False)

        # s1
        data2018s1 = data2018season.get_group(1)
        average = data2018s1[:,5].sum(axis=0)/len(data2018s1)
        feps = data2018s1[:,5]
        abs_sum = 0
        sum_ = 0
        for eps in range(len(feps)):
            abs_sum = abs(AF2018_eps - feps[eps])
            sum_ = AF2018_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2018_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2018s1)), 3)
        BIAS1 = round(float(AF2018_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2018s1))), 3)

        result = [data2018s1[0][0], data2018s1[0][1], data2018s1[0][2], AF2018_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)

        
        # s2
        data2018s2 = data2018season.get_group(2)
        average = data2018s2[:,5].sum(axis=0)/len(data2018s2)
        feps = data2018s2[:,5]
        abs_sum = 0
        sum_ = 0
        for eps in range(len(feps)):
            abs_sum = abs(AF2018_eps - feps[eps])
            sum_ = AF2018_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2018_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2018s2)), 3)
        BIAS1 = round(float(AF2018_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2018s2))), 3)

        result = [data2018s2[0][0], data2018s2[0][1], data2018s2[0][2], AF2018_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)

        # s3
        data2018s3 = data2018season.get_group(3)
        average = data2018s3[:,5].sum(axis=0)/len(data2018s3)
        feps = data2018s3[:,5]
        abs_sum = 0
        sum_ = 0
        for eps in range(len(feps)):
            abs_sum = abs(AF2018_eps - feps[eps])
            sum_ = AF2018_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2018_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2018s3)), 3)
        BIAS1 = round(float(AF2018_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2018s3))), 3)

        result = [data2018s3[0][0], data2018s3[0][1], data2018s3[0][2], AF2018_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)

        # s4
        data2018s4 = data2018season.get_group(4)
        average = data2018s4[:,5].sum(axis=0)/len(data2018s4)
        feps = data2018s4[:,5]
        abs_sum = 0
        sum_ = 0
        for eps in range(len(feps)):
            abs_sum = abs(AF2018_eps - feps[eps])
            sum_ = AF2018_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2018_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2018s4)), 3)
        BIAS1 = round(float(AF2018_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2017s4))), 3)

        result = [data2018s4[0][0], data2018s4[0][1], data2018s4[0][2], AF2018_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)


        # 2019
        data2019season = pd.DataFrame(data2019).groupby(2, as_index=False)
        # s1
        data2019s1 = data2019season.get_group(1)
        average = data2019s1[:,5].sum(axis=0)/len(data2019s1)
        feps = data2019s1[:,5]
        abs_sum = 0
        sum_ = 0
        for eps in range(len(feps)):
            abs_sum = abs(AF2019_eps - feps[eps])
            sum_ = AF2019_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2019_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2019s1)), 3)
        BIAS1 = round(float(AF2019_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2019s1))), 3)

        result = [data2019s1[0][0], data2019s1[0][1], data2019s1[0][2], AF2019_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)

        # s2
        data2019s2 = data2019season.get_group(2)
        average = data2019s2[:,5].sum(axis=0)/len(data2019s2)
        feps = data2019s2[:,5]
        abs_sum = 0
        sum_ = 0
        for eps in range(len(feps)):
            abs_sum = abs(AF2019_eps - feps[eps])
            sum_ = AF2019_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2019_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2019s2)), 3)
        BIAS1 = round(float(AF2019_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2019s2))), 3)

        result = [data2019s2[0][0], data2019s2[0][1], data2019s2[0][2], AF2019_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)

        # s3
        data2019s3 = data2019season.get_group(3)
        average = data2019s3[:,5].sum(axis=0)/len(data2019s3)
        feps = data2019s3[:,5]
        abs_sum = 0
        sum_ = 0
        for eps in range(len(feps)):
            abs_sum = abs(AF2019_eps - feps[eps])
            sum_ = AF2019_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2019_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2019s3)), 3)
        BIAS1 = round(float(AF2019_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2019s3))), 3)

        result = [data2019s3[0][0], data2019s3[0][1], data2019s3[0][2], AF2019_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)

        # s4
        data2019s4 = data2019season.get_group(4)
        average = data2019s4[:,5].sum(axis=0)/len(data2019s4)
        feps = data2019s4[:,5]
        abs_sum = 0
        sum_ = 0
        for eps in range(len(feps)):
            abs_sum = abs(AF2019_eps - feps[eps])
            sum_ = AF2019_eps - feps[eps]

        # calculate FE1, FE2, BIAS1, BIAS2
        FE1 = round(abs(AF2019_eps - average), 3)
        FE2 = round((abs_sum) / (len(data2019s4)), 3)
        BIAS1 = round(float(AF2019_eps - average), 3)
        BIAS2 = round(float(sum_ / (len(data2019s4))), 3)

        result = [data2019s4[0][0], data2019s4[0][1], data2019s4[0][2], AF2019_eps, FE1, FE2, BIAS1, BIAS2]
        output.append(result)

        # data2019 = need_data[need_data[:, 1] = 2019]
        # print(data2017)
        """

        # avoid lower speed of append
        target_stkcd_data = []



    # temp = pd.DataFrame([[stkcd, year, season, Institution, AnanmID]], columns=['stkcd', 'year', 'season', 'Institution', 'AnanmID'])
    # print(temp)
print(output)
output = pd.DataFrame(data=output)

output.to_excel('./Result/影響力大於2.5.xlsx', index=False)
