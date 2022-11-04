# -*- coding: utf-8 -*-
"""FilterTaxiDB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fj4JUNEYXps1wuTmFrviIBVso2rbfphN

Import database and drop nan values
"""

import pandas as pd 
df = pd.read_csv(r'/content/drive/MyDrive/Taxi_Trips.csv').dropna()

df.head()

"""Creation of a dataset with year,month and day and filter for year 2021 with final grouping by month 

"""

import pandas as pd 
df = pd.read_csv(r'/content/drive/MyDrive/Taxi_Trips.csv')
year = [int(el.split('/')[2].split(' ')[0]) for el in df['Trip Start Timestamp']]
df['Year'] = year
month = [el.split('/')[0] for el in df['Trip Start Timestamp']]
df['Month'] = month 
day = [el.split('/')[1] for el in df['Trip Start Timestamp']]
df['Day'] = day
df3 = df[df['Year']==2021]

import numpy as np
ones = np.ones(len(df3['Month']))
df3['n_taxi'] = ones
df_third = df3.groupby(['Month','Day'])['n_taxi'].sum()

"""creation of the new csv"""

df_third.to_csv('df_multilines2.csv', index = True)