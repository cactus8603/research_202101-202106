import os
from datetime import datetime
import pandas as pd 
import numpy as np
from tqdm import *

if __name__ == '__main__':


    
    moreOrLess = '小'
    record = '前本下'

    path = './Result/Stdrank/影響力' + str(moreOrLess) +  '於2.5(' + str(record) + ').xlsx'
    data = pd.read_excel(path, engine='openpyxl').assign(Diff='.')
    
    # data_value = data.values

    # output = pd.read_excel(path, engine='openpyxl').assign(Diff=0)
    output = data.values.tolist()


    # print(data_value[0][0])

    # len(output)
    for index in trange(1,len(output)-1): # 前本下：trange(1,len(output)-1)
        stkcd = int(output[index][0])
        year = int(output[index][1])
        season = int(output[index][2])
        lastRow = index-1
        nextRow = index+1
        """
        # for all：本-前
        # if stkcd is same for all：本-前
        
        if (stkcd == output[lastRow][0]):
            
            # if year is same
            if (year == output[lastRow][1]):
                # if is next season
                if (season == output[lastRow][2]):
                    output[index][4] = output[index][3] - output[lastRow][3]
                    # print(output[index][4])
                    
            # if this year is next year
            elif (year == output[lastRow][1]+1):
                # if is next season
                if (season == output[lastRow][2]-3):
                    output[index][4] = output[index][3] - output[lastRow][3]
        """
        """
        # if stkcd is same for 前下：下-前
        if (stkcd == output[index-2][0]):
            # if the year of index-2 row is the same
            if (year == output[index-2][1]):
                if (season == output[index-2][2]+2):
                    output[index][4] = output[index][3] - output[index-2][3]
            
            # if the year of index-2 row is not the same
            elif (year == output[index-2][1]+1):
                if (season == output[index-2][2]-2):
                    output[index][4] = output[index][3]-output[index-2][3]
        """
        
        # if stkcd is same for 前本下：下-前
        if (output[index-1][0] == output[index+1][0]): # if the stkcd of lastrow and nextrow is the same, the stkcd of this row is the same
            # the year of lastRow and nextRow is the same
            if (output[index-1][1] == output[index+1][1]):
                if (output[index+1][2] == output[index-1][2]+2):
                    output[index][4] = output[index+1][3] - output[index-1][3]

            # the year of lastRow and nextRow is not the same
            elif (output[index-1][1] == output[index+1][1]-1):
                if (output[index+1][2] == output[index-1][2]-2):
                    output[index][4] = output[index+1][3] - output[index-1][3]
        



    
    outputPath = './Result/Stdrank/Step7/影響力' + str(moreOrLess) +  '於2.5(' + str(record) + ').xlsx'
    output = pd.DataFrame(data=output, columns=['stkcd', 'year', 'season', 'AverageStdrank', 'Diff'])
    output.to_excel(outputPath, index=False)