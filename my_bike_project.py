import numpy as np
import pandas as pd
import time

df_chicago = pd.read_csv('chicago.csv')
df_new_york = pd.read_csv('new_york.csv')
df_washington = pd.read_csv('washington.csv')


print(df_chicago.dtypes)
df_chicago['Start Time'] = pd.to_datetime(df_chicago['Start Time'])
print(df_chicago.dtypes)

        
        

            
