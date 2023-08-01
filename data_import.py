import pandas as pd
import os
import glob

# import the configuration
from config import STANDARD_MODEL_PATH

# relative directory where your Excel files are stored
data_dir = os.path.dirname(STANDARD_MODEL_PATH)

def import_data(data_dir):
    # get a list of all Excel files in the directory
    blockage_files = glob.glob(os.path.join(data_dir, '*.xlsx'))
    
    # create an empty list to hold the dataframes
    blockage_dataframes = []
    
    for file in blockage_files:
        # read the Excel file and add it to the list
        df = pd.read_excel(file)
        blockage_dataframes.append(df)
    
    # read standard file
    standard_df = pd.read_excel(STANDARD_MODEL_PATH)    
        
    return blockage_dataframes, standard_df

# use the function
blockage_dataframes, standard_df = import_data(data_dir)