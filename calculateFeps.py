import os
from datetime import datetime
import pandas as pd 
import numpy as np
from tqdm import *

# read files
# more_path = './Result/significance_more.xlsx' 
more_path = './Result/significance_more_aC.xlsx' 
# more_path = './Result/significance_less_aC.xlsx'
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

# print(AF2017_value[2][2])

"""
index = 828
# print(predict_stock2017_value[index])
predict_stkcd = int(predict_stock2019_value[index][0])
predict_date = str(predict_stock2019_value[index][1])
dash = '-'
index_dash = predict_date.index(dash,1)
predict_year = int(predict_date[:predict_date.index(dash)])
predict_month = int(predict_date[predict_date.index(dash)+1:predict_date.index(dash,6)])
predict_season = int((predict_month-1)/3) + 1

predict_AnanmID = str(predict_stock2019_value[index][3])

string = predict_AnanmID.split(',')
print(string)
string.sort(reverse=True)
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

for index in trange(len(more_value)):
    # get data
    stkcd = more_value[index][1]
    time = str(more_value[index][2])
    year = int(time[:4])
    season = int(time[5:])

    IDs = str(more_value[index][3])
    dash = '-'
    try:
        index_dash = IDs.index(dash)
    except ValueError:
        continue
    Institution = IDs[:index_dash]
    AnanmID = IDs[(index_dash+1):]
    target_stkcd_data.append([stkcd, year, season, Institution, AnanmID])
    # target_stkcd_data = np.concatenate((target_stkcd_data, [[stkcd, year, season, Institution, AnanmID]]), axis=0)

    
    # print(len(target_stkcd_data), index)
    # print(target_stkcd_data)
    # print(target_stkcd_data[len(target_stkcd_data)-1], index, len(target_stkcd_data)-1)
    # search in predict file
    len_target = len(target_stkcd_data)
    if (len_target>=1 and stkcd > int(target_stkcd_data[len_target-2][0])):
        
        # print(stkcd, target_stkcd_data[len_target-2][0], len_target, index+1)
        # print("00")
        # print(len(target_stkcd_data))
        target_stkcd = target_stkcd_data[len_target-2][0]
        # print(target_stkcd_data)
        # print(len(target_stkcd_data))
        # print("----------")
        # print(index, " stkcd target_stkcd ", stkcd, target_stkcd)
        # print("total target ", len_target-1)
        # print(target_stkcd_data)
        for i in range(AF2017_index, len(AF2017_value)):
            AF2017_stkcd = int(AF2017_value[i][0])
            # print(AF2017_stkcd)

            if (AF2017_stkcd == target_stkcd):
                AF2017_eps = float(AF2017_value[i][2])
                # print("2017: ", target_stkcd, AF2017_eps)
                AF2017_index = i-1
                break

        for i in range(AF2018_index, len(AF2018_value)):
            AF2018_stkcd = int(AF2018_value[i][0])

            if (AF2018_stkcd == target_stkcd):
                AF2018_eps = float(AF2018_value[i][2])
                # print("2018: ", target_stkcd, AF2018_eps)
                AF2018_index = i-1
                break
        
        for i in range(AF2019_index, len(AF2019_value)):
            AF2019_stkcd = int(AF2019_value[i][0])

            if (AF2019_stkcd == target_stkcd):
                AF2019_eps = float(AF2019_value[i][2])
                # print("2018: ", target_stkcd, AF2019_eps)
                AF2019_index = i-1
                break
        # print('over')
        

        # data in predict
        need_data = []
        exist_data = []
        # exist_data_sort = []
        # 2017
        for i in range(index_in_predict_2017, len(predict_stock2017_value)):

            predict_stkcd = int(predict_stock2017_value[i][0])
            if (predict_stkcd > int(target_stkcd_data[len_target-2][0])):
                index_in_predict_2017 = i-1
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

            # To deal with sort
            string = predict_AnanmID.split(',')
            string.sort()
            temp = ''
            for i in range(len(string)):
                temp = temp + str(string[i]) 
                if (i != len(string)-1):
                    temp += '-'

            predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]]
            if (predict_mod in target_stkcd_data and predict_mod not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0], Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]])
                # print(predict_mod)
            """
            if (predict in target_stkcd_data and predict not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID]) 
            
            else :
                # To deal with sort
                string = predict_AnanmID.split(',')
                string.sort()
                temp = ''
                for i in range(len(string)):
                    temp = temp + str(string[i]) 
                    if (i != len(string)-1):
                        temp += '-'

                predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]]

                if (predict_mod in target_stkcd_data and predict_mod not in exist_data):
                    need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0], Feps])
                    exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]])
                    print(predict_mod)
                    # print("sort")
                    # print(predict_mod)
                """
            
         
        # print("2017 ", len(need_data), index_in_predict_2017)

        exist_data = []
        # exist_data_sort = []
        # 2018
        
        for i in range(index_in_predict_2018, len(predict_stock2018_value)):
    
            predict_stkcd = int(predict_stock2018_value[i][0])
            if (predict_stkcd > int(target_stkcd_data[len_target-2][0])):
                index_in_predict_2018 = i-1
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

            # To deal with sort
            string = predict_AnanmID.split(',')
            string.sort()
            temp = ''
            for i in range(len(string)):
                temp = temp + str(string[i]) 
                if (i != len(string)-1):
                    temp += '-'
        
            predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]]


            if (predict_mod in target_stkcd_data and predict_mod not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0], Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]])
                # print(temp)
                # print(predict_mod)
            """
            if (predict in target_stkcd_data and predict not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID])
            
            else:
                string = predict_AnanmID.split(',')
                string.sort()
                temp = ''
                for i in range(len(string)):
                    temp = temp + str(string[i]) 
                    if (i != len(string)-1):
                        temp += '-'

                predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]]
                if (predict_mod in target_stkcd_data and predict_mod not in exist_data):
                    need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0], Feps])
                    exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]])
                    print(predict_mod)
                    # print("sort")
                    # print(predict_mod)
                """
                
        # print("2018 ", len(need_data), index_in_predict_2018)
        
        # exist_data = []
        # exist_data_sort = []
        # 2019
        for i in range(index_in_predict_2019, len(predict_stock2019_value)):
        
            predict_stkcd = int(predict_stock2019_value[i][0])
            if (predict_stkcd > int(target_stkcd_data[len_target-2][0])):
                index_in_predict_2019 = i-1
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

            # To deal with sort
            string = predict_AnanmID.split(',')
            string.sort()
            temp = ''
            for i in range(len(string)):
                temp = temp + str(string[i]) 
                if (i != len(string)-1):
                    temp += '-'

            predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]]
            if (predict_mod in target_stkcd_data and predict_mod not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0], Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]])
                # print(predict_mod)
        # print("2019 ", len(need_data))
            """
            if (predict in target_stkcd_data and predict not in exist_data):
                need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID, Feps])
                exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, predict_AnanmID])
            
            else:
                # To deal with sort
                string = predict_AnanmID.split(',')
                string.sort()
                temp = ''
                for i in range(len(string)):
                    temp = temp + str(string[i]) 
                    if (i != len(string)-1):
                        temp += '-'
                print(string)
                
                predict_mod = [predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]]
                if (predict_mod in target_stkcd_data and predict_mod not in exist_data):
                    need_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0], Feps])
                    exist_data.append([predict_stkcd, predict_year, predict_season, predict_InstitutionID, string[0]])
                    # print("sort")
                    print(predict_mod)
            """
        # print("2019 ", len(need_data), len(exist_data))

        # need_data = np.array(need_data)
        # need_data = need_data[np.lexsort((need_data[:,2], need_data[:,1]))]

        # print(exist_data)
        # print(len(exist_data))

        # print(need_data)
        # print(len(need_data))
        
        # sort by year
        data = pd.DataFrame(need_data, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Feps']).groupby('year', as_index=False)
        # data2017 = data[data['year'] == 2017]
        # print(data.items())
        data2017 = []
        data2018 = []
        data2019 = []
        try: 
            data2017 = data.get_group(2017) 
            data2018 = data.get_group(2018)
            data2019 = data.get_group(2019)
        except KeyError:
            pass
        """
        # s_sum = 0.0
        s_sum = data['year'].sum()
        print("sum ", s_sum)
        try:
            s_sum = float(data['year'].sum())
            print("sum ", s_sum)
        except TypeError:
            pass
        """
        length = len(data)
        # print("year len", length)
        if (length == 1):
            # print(length)
            temp_year = int(need_data[0][1])
            # print("temp ", temp_year)
            # print(average_sum)
            if (temp_year == 2017):
                data2017 = np.array(need_data)
            elif (temp_year == 2018):
                data2018 = np.array(need_data)
            elif (temp_year == 2019):
                data2019 = np.array(need_data)

        # print(data2017)
        # print(data2018)
        # print(data2019)
        # 2017
        data2017season = pd.DataFrame(data2017, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Feps']).groupby('season', as_index=False)
        # print(data2017season.items())

        
        # print(float(data2017[:, 2].sum()/len(data2017)))
        # get each season in 2017
        data2017s2 = [] 
        data2017s3 = [] 
        data2017s4 = []
        
        try:
            data2017s2 = np.array(data2017season.get_group(2))
            data2017s3 = np.array(data2017season.get_group(3))
            # data2017s3 = data2017season.get_group(3)
            data2017s4 = np.array(data2017season.get_group(4))
        except KeyError:
            pass
        
        # data2017s2 = np.array(data2017season.get_group(2))
        # data2017s3 = np.array(data2017season.get_group(3))
        # data2017s4 = np.array(data2017season.get_group(4))
        # print(data2017s2)
        # print(data2017s3)
        # print(data2017s4)
        
        """
        try:
            s_sum = float(data2017['season'].sum())
        except TypeError:
            pass
        """
        # print("sum ", s_sum)
        
        length = len(data2017season)
        if (length == 1):
            season = 0
            try:
                season = int(data2017[0][2])
            except KeyError:
                pass
            if (season == 3):
                data2017s3 = np.array(data2017)
            elif (season == 2):
                data2017s2 = np.array(data2017)
            elif (season == 4):
                data2017s4 = np.array(data2017)
        
        # print(data2017s2)
        # print(data2017s3)
        # print(data2017s4)

        # write data [stkcd, year, season, AF, FE1, FE2, BIAS1, BIAS2]
        # s2
        # data2017s2 = np.array(data2017season.get_group(2))
        # print("2017 s2 ", target_stkcd)
        # print(data2017s2)
        if (len(data2017s2) >= 1):

            feps = data2017s2[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2017s2)

            abs_sum = 0.0
            sum_ = 0.0
            # print("AF", type(AF2017_eps))
            # print("aver", type(average))
            for eps in range(len(feps)):
                abs_sum += abs(AF2017_eps - feps[eps])
                sum_ += AF2017_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2017_eps - average)
            FE2 = (abs_sum) / (len(data2017s2))
            BIAS1 = float(AF2017_eps - average)
            BIAS2 = float(sum_ / (len(data2017s2)))
            # print()
            result = [data2017s2[0][0], data2017s2[0][1], data2017s2[0][2], AF2017_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print("2017s2 ", result)
        # else:
            # print("2017 s2 no data")
            # continue
        
        # s3
        # data2017s3 = np.array(data2017season.get_group(3))
        # print("2017 s3")
        # print(data2017s3)
        # print("len ", len(data2017s3))
        if (len(data2017s3) >= 1):
            feps = data2017s3[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2017s3)
            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2017_eps - feps[eps])
                sum_ += AF2017_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2017_eps - average)
            FE2 = (abs_sum) / (len(data2017s3))
            BIAS1 = float(AF2017_eps - average)
            BIAS2 = float(sum_ / (len(data2017s3)))

            result = [data2017s3[0][0], data2017s3[0][1], data2017s3[0][2], AF2017_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print("2017s3 ", result)
        # else:
            # print("2017 s3 no data")
            # continue

        # s4
        # data2017s4 = np.array(data2017season.get_group(2))
        # print("2017 s4")
        # print(data2017s4)
        if (len(data2017s4) >= 1):
            feps = data2017s4[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2017s4)
            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2017_eps - feps[eps])
                sum_ += AF2017_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2017_eps - average)
            FE2 = (abs_sum) / (len(data2017s4))
            BIAS1 = float(AF2017_eps - average)
            BIAS2 = float(sum_ / (len(data2017s4)))

            result = [data2017s4[0][0], data2017s4[0][1], data2017s4[0][2], AF2017_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print("2017s4 ", result)
        # else:
            # print("2017 s4 no data")
            # continue

        
        # 2018
        data2018season = pd.DataFrame(data2018, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Feps']).groupby('season', as_index=False)
        data2018s1 = []
        data2018s2 = []
        data2018s3 = []
        data2018s4 = []
        try:
            data2018s1 = np.array(data2018season.get_group(1))
            data2018s2 = np.array(data2018season.get_group(2))
            data2018s3 = np.array(data2018season.get_group(3))
            data2018s4 = np.array(data2018season.get_group(4))
        except KeyError:
            pass

        # if groupby not work
        """
        try:
            s_sum = float(data2018['season'].sum())
        except TypeError:
            pass
        # print("sum ", s_sum)
        """
        # print("2018data")
        # print(data2018)
        length = len(data2018season)
        # print("2018 len ", length)
        if (length == 1):
            season = 0
            try:
                season = int(data2018[0][2])
            except KeyError:
                pass
            # average_sum = s_sum/length
            # print("2018ave ", average_sum)
            # print(average_sum)
            if (season == 3):
                data2018s3 = np.array(data2018)
            elif (season == 2):
                data2018s2 = np.array(data2018)
            elif (season == 4):
                data2018s4 = np.array(data2018)
            elif (season == 1):
                data2018s1 = np.array(data2018)
        

        # s1
        # data2018s1 = data2018season.get_group(1)
        # print("2018 s1")
        # print(data2018s1)
        if (len(data2018s1) >= 1):
            feps = data2018s1[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2018s1)
            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2018_eps - feps[eps])
                sum_ += AF2018_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2018_eps - average)
            FE2 = (abs_sum) / (len(data2018s1))
            BIAS1 = float(AF2018_eps - average)
            BIAS2 = float(sum_ / (len(data2018s1)))

            result = [data2018s1[0][0], data2018s1[0][1], data2018s1[0][2], AF2018_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)

            # print("2018s1", result)
        # else:
            # print("2018 s1 no data")
            # continue
        
        
        # s2
        # data2018s2 = data2018season.get_group(2)
        # print("2018 s2")
        # print(data2018s2)
        if (len(data2018s2) >= 1):
            feps = data2018s2[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2018s2)
            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2018_eps - feps[eps])
                sum_ += AF2018_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2018_eps - average)
            FE2 = (abs_sum) / (len(data2018s2))
            BIAS1 = float(AF2018_eps - average)
            BIAS2 = float(sum_ / (len(data2018s2)))

            result = [data2018s2[0][0], data2018s2[0][1], data2018s2[0][2], AF2018_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print("2018s2 ", result)
        # else:
            # print("2018 s2 no data")
            # continue

        # s3
        # data2018s3 = data2018season.get_group(3)
        # print("2018 s3")
        # print(data2018s3)
        if (len(data2018s3) >= 1):
            feps = data2018s3[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2018s3)
            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2018_eps - feps[eps])
                sum_ += AF2018_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2018_eps - average)
            FE2 = (abs_sum) / (len(data2018s3))
            BIAS1 = float(AF2018_eps - average)
            BIAS2 = float(sum_ / (len(data2018s3)))

            result = [data2018s3[0][0], data2018s3[0][1], data2018s3[0][2], AF2018_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print("2018s3", result)
        # else:
            # print("2018 s3 no data")
            # continue

        # s4
        # data2018s4 = data2018season.get_group(4)
        # print("2018 s4")
        # print(data2018s4)
        if (len(data2018s4) >= 1):
            feps = data2018s4[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2018s4)
            
            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2018_eps - feps[eps])
                sum_ += AF2018_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2018_eps - average)
            FE2 = (abs_sum) / (len(data2018s4))
            BIAS1 = float(AF2018_eps - average)
            BIAS2 = float(sum_ / (len(data2018s4)))

            result = [data2018s4[0][0], data2018s4[0][1], data2018s4[0][2], AF2018_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print("2018s4", result)
        # else :
            # print("2018 s4 no data")  
            # continue
    

        # 2019
        data2019season = pd.DataFrame(data2019, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Feps']).groupby('season', as_index=False)
        # data2019season.columns = data2019season.columns.str.strip()
        data2019s1 = []
        data2019s2 = []
        data2019s3 = []
        data2019s4 = []
        try:
            data2019s1 = np.array(data2019season.get_group(1))
            data2019s2 = np.array(data2019season.get_group(2))
            data2019s3 = np.array(data2019season.get_group(3))
            data2019s4 = np.array(data2019season.get_group(4))
        except KeyError:
            pass
        """
        # if groupby not work
        try:
            s_sum = float(data2019['season'].sum())
        except TypeError:
            pass
        # print("sum ", s_sum)
        """
        # print(data2019season)
        length = len(data2019season)
        if (length == 1):
            # print(length)
            season = 0
            try:
                season = int(data2019[0][2])
            except KeyError:
                pass
            # print(season)
            # print(type(season))
            # average_sum = s_sum/length
            # print(average_sum)
            if (season == 3):
                data2019s3 = np.array(data2019)
            elif (season == 2):
                data2019s2 = np.array(data2019)
            elif (season == 4):
                data2019s4 = np.array(data2019)
            elif (season == 1):
                data2019s1 = np.array(data2019)


        # s1
        # data2019s1 = data2019season.get_group(1)
        # print("2019 s1")
        # print(data2019s1)
        if (len(data2019s1) >= 1):
            feps = data2019s1[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2019s1)
            
            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2019_eps - feps[eps])
                sum_ += AF2019_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2019_eps - average)
            FE2 = (abs_sum) / (len(data2019s1))
            BIAS1 = float(AF2019_eps - average)
            BIAS2 = float(sum_ / (len(data2019s1)))

            result = [data2019s1[0][0], data2019s1[0][1], data2019s1[0][2], AF2019_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print("2019s1", result)
        # else:
            # print("2019 s1 no data")
            # continue

        # s2
        # data2019s2 = data2019season.get_group(2)
        # print("2019 s2")
        # print(data2019s2)
        if (len(data2019s2) >= 2):
            feps = data2019s2[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2019s2)

            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2019_eps - feps[eps])
                sum_ += AF2019_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2019_eps - average)
            FE2 = (abs_sum) / (len(data2019s2))
            BIAS1 = float(AF2019_eps - average)
            BIAS2 = float(sum_ / (len(data2019s2)))

            result = [data2019s2[0][0], data2019s2[0][1], data2019s2[0][2], AF2019_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print("2019s2 ", result)
        # else:
            # print("2019 s2 no data")
            # continue

        # s3
        # data2019s3 = data2019season.get_group(3)
        # print("2019 s3")
        # print(data2019s3)
        if (len(data2019s3) >= 1):

            feps = data2019s3[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2019s3)

            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2019_eps - feps[eps])
                sum_ += AF2019_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2019_eps - average)
            FE2 = (abs_sum) / (len(data2019s3))
            BIAS1 = float(AF2019_eps - average)
            BIAS2 = float(sum_ / (len(data2019s3)))

            result = [data2019s3[0][0], data2019s3[0][1], data2019s3[0][2], AF2019_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print(result)
        # else:
            # print("2019 s3 no data")
            # continue

        # s4
        # data2019s4 = data2019season.get_group(4)
        # print("2019 s4")
        # print(data2019s4)
        if (len(data2019s4) >= 1):
            feps = data2019s4[:,5]
            feps = feps.astype(np.float)
            average = feps.sum(axis=0)/len(data2019s4)

            abs_sum = 0.0
            sum_ = 0.0
            for eps in range(len(feps)):
                abs_sum += abs(AF2019_eps - feps[eps])
                sum_ += AF2019_eps - feps[eps]

            # calculate FE1, FE2, BIAS1, BIAS2
            FE1 = abs(AF2019_eps - average)
            FE2 = (abs_sum) / (len(data2019s4))
            BIAS1 = float(AF2019_eps - average)
            BIAS2 = float(sum_ / (len(data2019s4)))

            result = [data2019s4[0][0], data2019s4[0][1], data2019s4[0][2], AF2019_eps, FE1, FE2, BIAS1, BIAS2]
            output.append(result)
            # print(result)
        # else:
            # print("2019 s4 no data")
            # continue
        
        # data2019 = need_data[need_data[:, 1] = 2019]
        # print(data2017)

        
        # avoid lower speed of append
        
        temp = []
        temp.append(target_stkcd_data[len(target_stkcd_data)-1])
        # print(temp)
        target_stkcd_data = []
        target_stkcd_data.append(temp[0])
        # print(target_stkcd_data)



    # temp = pd.DataFrame([[stkcd, year, season, Institution, AnanmID]], columns=['stkcd', 'year', 'season', 'Institution', 'AnanmID'])
    # print(temp)
# print("output is")
# print(output)
output = pd.DataFrame(data=output, columns=['stkcd', 'year', 'season', 'AF_Eps', 'FE1', 'FE2', 'BIAS1', 'BIAS2'])

output.to_excel('./Result/影響力大於2.5(前下).xlsx', index=False)
# output.to_excel('./Result/影響力小於2.5(前下).xlsx', index=False)
