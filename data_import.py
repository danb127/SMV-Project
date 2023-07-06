import pandas as pd
import os
import glob

# relative directory where your Excel files are stored
data_dir = './Pull Complaint Valve Data Pat M'

def import_data(data_dir):
    # get a list of all Excel files in the directory
    files = glob.glob(os.path.join(data_dir, '*.xlsx'))
    
    # create an empty list to hold the dataframes
    dataframes = []
    
    for file in files:
        # read the Excel file and add it to the list
        df = pd.read_excel(file)
        dataframes.append(df)
        
        # print the first few rows of the dataframe
        print(df.head())
        
        
    return dataframes

# use the function
dataframes = import_data(data_dir)
