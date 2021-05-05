import os
from datetime import datetime
import pandas as pd 
import numpy as np
from tqdm import *

def replace():
    for year in range(2016, 2021):
        path = './recommend/分析師股票推薦' + str(year) + '.xlsx'

        data = pd.read_excel(path, engine='openpyxl')
        data_value = data.values

        for index in trange(len(data_value)):
            if (data_value[index][9] == '买入'): data_value[index][9] = 5
            elif (data_value[index][9] == '增持'): data_value[index][9] = 4
            elif (data_value[index][9] == '中性'): data_value[index][9] = 3
            elif (data_value[index][9] == '减持'): data_value[index][9] = 2
            elif (data_value[index][9] == '卖出'): data_value[index][9] = 1
        
        output = pd.DataFrame(data=data_value)
        output.columns = ['stkcd', 'ReportID', 'Accper', 'Rptdt', 'Fenddt', 'AnanmID', 'Ananm', 'InstitutionID', 'Brokern', 'Stdrank', 'Rankchg']
        output_path = './recommend/Result/分析師股票推薦' + str(year) + '.xlsx'
        output.to_excel(output_path, index=False)


if __name__ == '__main__':
    # replace()

    # Already Done: less (aB, aBc, aC), more (aB, aBc, aC)
    # Prepare to start: less (), more (aBc)

    year = 2017
    moreOrLess = 'more'
    record = 'aBc'
    path = './Result/significance_' + str(moreOrLess) +  '_' + str(record) + '.xlsx'
    data = pd.read_excel(path, engine='openpyxl')
    data_value = data.values

    path2017 = './recommend/Result/分析師股票推薦2017.xlsx'
    search2017 = pd.read_excel(path2017, engine='openpyxl')
    search2017_value = search2017.values

    path2018 = './recommend/Result/分析師股票推薦2018.xlsx'
    search2018 = pd.read_excel(path2018, engine='openpyxl')
    search2018_value = search2018.values

    path2019 = './recommend/Result/分析師股票推薦2019.xlsx'
    search2019 = pd.read_excel(path2019, engine='openpyxl')
    search2019_value = search2019.values
    
    index2017 = 0
    index2018 = 0
    index2019 = 0

    output = []
    dataToSearch = []

    # len(data_value)
    for index in trange(len(data_value)):

        stkcd = int(data_value[index][1])
        time = str(data_value[index][2])
        year = int(time[:4])
        DataSeason = int(time[5:])
        # print(year, DataSeason)
        IDs = str(data_value[index][3])
        dash = '-'
        try:
            index_dash = IDs.index(dash)
        except ValueError:
            continue
        Institution = int(IDs[:index_dash])
        AnanmID = str(IDs[(index_dash+1):])

        dataToSearch.append([stkcd, year, DataSeason, Institution, AnanmID])
        # dataToSearch.append([stkcd, year, Institution, AnanmID])
        # print(data_value[index+1][1])
        if (index+1 >= len(data_value) or int(data_value[index+1][1]) > stkcd):
            # print(dataToSearch)
            # print(stkcd)

            # 2017
            Std2017 = []
            exist = []

            for i in range(index2017, len(search2017_value)):
                stkcd2017 =  int(search2017_value[i][0])
                if (stkcd2017 > stkcd):
                    index2017 = stkcd2017
                    break
                
                if (stkcd2017 == stkcd):
                    Rptdt = str(search2017_value[i][3])
                    dash = '-'
                    year = int(Rptdt[:Rptdt.index(dash)])
                    month = int (Rptdt[Rptdt.index(dash)+1:Rptdt.index(dash,6)])
                    season = int((month-1)/3) + 1
                    AnanmID = str(search2017_value[i][5])
                    InstitutionID = int(search2017_value[i][7])
                    Stdrank = int(search2017_value[i][9])

                    # print(AnanmID)
                    string = AnanmID.split(',')
                    string.sort()
                    ID = "-".join(string)
                    # if (string != None): 
                    # print("string ", ID)

                    searchData2017 = [stkcd2017, year, season, InstitutionID, ID]
                    # searchData2017 = [stkcd2017, year, InstitutionID, ID]
                    recordData = [stkcd2017, year, season, InstitutionID, ID, Stdrank]

                    if (searchData2017 in dataToSearch and searchData2017 not in exist): 
                        # print("Find ",searchData2017)
                        exist.append(recordData)
                        Std2017.append(recordData)
                    
            # print(Std2017)
            Std2017Season = pd.DataFrame(Std2017, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Stdrank']).groupby('season', as_index=False)
            # print(Std2017)

            for season in range(1,5):
                try:
                    data = np.array(Std2017Season.get_group(season))
                    sum_ = np.sum(data, axis=0)[5]
                    output.append([data[0][0], data[0][1], data[0][2], sum_/len(data)]) # stkcd, year, season AverageStdrank 
                    # print(output)

                except KeyError:
                    pass

            # 2018
            Std2018 = []
            exist = []

            for i in range(index2018, len(search2018_value)):
                stkcd2018 =  int(search2018_value[i][0])
                if (stkcd2018 > stkcd):
                    index2018 = stkcd2018
                    break
                
                if (stkcd2018 == stkcd):
                    Rptdt = str(search2018_value[i][3])
                    dash = '-'
                    year = int(Rptdt[:Rptdt.index(dash)])
                    month = int (Rptdt[Rptdt.index(dash)+1:Rptdt.index(dash,6)])
                    season = int((month-1)/3) + 1
                    AnanmID = str(search2018_value[i][5])
                    InstitutionID = int(search2018_value[i][7])
                    Stdrank = int(search2018_value[i][9])

                    # print(AnanmID)
                    string = AnanmID.split(',')
                    string.sort()
                    ID = "-".join(string)
                    # if (string != None): 
                    # print("string ", ID)

                    searchData2018 = [stkcd2018, year, season, InstitutionID, ID]
                    # searchData2018 = [stkcd2018, year, InstitutionID, ID]
                    recordData = [stkcd2018, year, season, InstitutionID, ID, Stdrank]

                    if (searchData2018 in dataToSearch and searchData2018 not in exist): 
                        # print("Find ",searchData2018)
                        exist.append(recordData)
                        Std2018.append(recordData)
                    
            # print(Std2018)
            Std2018Season = pd.DataFrame(Std2018, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Stdrank']).groupby('season', as_index=False)
            # print(Std2018)

            for season in range(1,5):
                try:
                    data = np.array(Std2018Season.get_group(season))
                    sum_ = np.sum(data, axis=0)[5]
                    output.append([data[0][0], data[0][1], data[0][2], sum_/len(data)]) # stkcd, year, season AverageStdrank 
                    # print(output)

                except KeyError:
                    pass
            
            # 2019
            Std2019 = []
            exist = []

            for i in range(index2019, len(search2019_value)):
                stkcd2019 =  int(search2019_value[i][0])
                if (stkcd2019 > stkcd):
                    index2019 = stkcd2019
                    break
                
                if (stkcd2019 == stkcd):
                    Rptdt = str(search2019_value[i][3])
                    dash = '-'
                    year = int(Rptdt[:Rptdt.index(dash)])
                    month = int (Rptdt[Rptdt.index(dash)+1:Rptdt.index(dash,6)])
                    season = int((month-1)/3) + 1
                    AnanmID = str(search2019_value[i][5])
                    InstitutionID = int(search2019_value[i][7])
                    Stdrank = int(search2019_value[i][9])

                    # print(AnanmID)
                    string = AnanmID.split(',')
                    string.sort()
                    ID = "-".join(string)
                    # if (string != None): 
                    # print("string ", ID)

                    searchData2019 = [stkcd2019, year, season, InstitutionID, ID]
                    # searchData2019 = [stkcd2019, year, InstitutionID, ID]
                    recordData = [stkcd2019, year, season, InstitutionID, ID, Stdrank]

                    if (searchData2019 in dataToSearch and searchData2019 not in exist): 
                        # print("Find ",searchData2019)
                        exist.append(recordData)
                        Std2019.append(recordData)
                    
            # print(Std2019)
            Std2019Season = pd.DataFrame(Std2019, columns=['stkcd', 'year', 'season', 'InstitutionID', 'AnanmID', 'Stdrank']).groupby('season', as_index=False)
            # print(Std2019)

            for season in range(1,5):
                try:
                    data = np.array(Std2019Season.get_group(season))
                    sum_ = np.sum(data, axis=0)[5]
                    output.append([data[0][0], data[0][1], data[0][2], sum_/len(data)]) # stkcd, year, season AverageStdrank 
                    # print(output)

                except KeyError:
                    pass


            # clear search data
            dataToSearch = []

    output = pd.DataFrame(data=output, columns=['stkcd', 'year', 'season', 'AverageStdrank'])

    recordSeason = ''
    if (record == 'aBc'): recordSeason = '(前本下)'
    elif (record == 'aB'): recordSeason = '(前本)'
    elif (record == 'aC'): recordSeason = '(前下)'

    recordMoreOrLess = ''
    if (moreOrLess == 'more'): recordMoreOrLess = '影響力大於2.5'
    elif (moreOrLess == 'less'): recordMoreOrLess = '影響力小於2.5'
    
    OutputPath = './Result/Stdrank/' + recordMoreOrLess + recordSeason + '.xlsx'

    output.to_excel(OutputPath, index=False)


    # print(data_value[0]) # 0	2	201704	10101837-30000000000000028242-30359892-30374843-30376736
    # print(search_value[0]) # 1	10118463	2017-12-31	2017-02-02	2016-12-31	30360744	刘晨明	104384	天风证券股份有限公司	5	首次



