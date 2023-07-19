import pandas as pd
import numpy as np

## clean data in Olympic_Data.csv and Population.csv (from Kaggle)
#
# Usage: 
# $ python clean.py data/Olympic_Data.csv and data/Population.csv results/clean.csv

# where:
# Olympic_Data.csv    = C:\Users\ahaas.SDDOMAIN\Desktop\Olympic_Data.csv\data
# data/Population     = C:\Users\ahaas.SDDOMAIN\Desktop\Population.csv\data

# Read in Data files
P1_df = pd.read_csv('data/Olympic_Data.csv')
P2_df = pd.read_csv('data/Population.csv')

# drop unneeded columns
P2_df.drop(P2_df.columns[0,2,3], axis =1, inplace=True)

# rename columns
fixed_columns = {
    'Country Code':'NOC',
}

P2_df.rename(columns=fixed_columns,inplace=True)
P2_df.columns

# converting to number
P2_df_int = {
     'Number': ':,',
}


## merge and clean data