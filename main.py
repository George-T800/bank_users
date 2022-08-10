from unittest import result
from pip import main
from reader_csv import main_read_csv_files
from checker_csv import checker_csv_result_file, result

def main ():
    print ("########### Main ###################")
    main_read_csv_files()
    checker_csv_result_file()
    return True
main()

