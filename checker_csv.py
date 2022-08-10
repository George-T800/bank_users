import os
from unittest import result
import pandas as pd
import glob

def checker_csv_result_file():
    df1 = pd.read_csv('result.csv', on_bad_lines='skip')
    
    new_header = df1.iloc[0] 
    df1 = df1[0:] 
    df1.columns = new_header 
    result = pd.concat([df1], axis=0)
    # result.set_index('bank_name')
    print (result)
    

checker_csv_result_file()

