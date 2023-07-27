import pandas as pd
import numpy as np

## clean data in Olympic_Data.csv and Population.csv (from Kaggle)
#
# Usage: 
# $ python clean.py data/Olympic_Data.csv and data/Population.csv results/clean.csv

import pandas as pd
import numpy as np
import select as sql   

# Read in Data files
P1_df = pd.read_csv('data/Olympic_Data.csv')
P2_df = pd.read_csv('data/Population.csv')

# drop unneeded columns
P2_df=P2_df.drop(['Rank', 'Country/Territory', 'Capital', 'Continent'], axis =1)
P1_df=P1_df.drop(['ID', 'Games','Height', 'Weight', 'Team'], axis =1)

# drop olympians that didnt medal
P1_df.dropna(subset = ['Medal'], inplace=True)

# rename columns
P2_df.rename(columns = {'CCA3':'NOC'}, inplace = True)

# merge data sets

output4 = pd.merge(P1_df, P2_df,
                   on= 'NOC',
                   how='outer')

# drop countries that have never won a medal
output4.dropna(subset = ['Medal'], inplace=True)

output4.tail(10)

output4.to_csv('results/clean.csv')