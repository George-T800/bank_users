import os
import pandas as pd

def main_read_csv_files():
    file_path = "/home/crypton/Desktop/epam/csv_files" # << read from path, I use linux os and read files this way >>
    #list all the files from the directory
    file_list = os.listdir(file_path) # << read file one by one >>
    # print (file_list)
    # print ("------------------------------------------------------------------------------")
    filenames = ["csv1.csv", "csv2.csv", "csv3.csv"] # << in task was mention, we have 3 csv file and as guess needs to marge in one csv file >>
    sep = ";"
    # print ("------------------------------------------------------------------------------")
    def check_data(data):
    
        return True # << True if data should be written into target file, else False >>

    with open("/home/crypton/Desktop/epam/result.csv", "a+") as targetfile:
        for filename in filenames :
            with open("/home/crypton/Desktop/epam/"+filename, "r") as f:
                next(f) # << only if the first line contains headers >>
                for line in f:
                    data = line.split(sep)
                    if check_data(data):
                        targetfile.write(line)
        
            # mask_month = result.loc[:, 'Month'] # in task was Octomber
            # result.loc[:, mask_month]
    
    return True


    
main_read_csv_files()
