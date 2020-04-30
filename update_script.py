#!/usr/bin/env python
# ------
# Author: Rahul Raj (c) MIT License 2020
# Website: https://randomwalk.in
# ------

import os
from datetime import datetime
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/coder-amey/COVID-19-India_Data/master/time-series/India_regional_aggregated.csv')

# For the bubble chart
# --------------------
def format_date(date):
    l = date.split('-')
    l = reversed(l)
    return ''.join(l)

df['Date']=df.Date.apply(format_date)
cols = ['Region', 'Date', 'Confirmed', 'Recovered/Migrated', 'Deceased']
df_ind=df.reindex(columns=cols)
df_ind.drop(index=df_ind[df_ind['Region']=='National Total'].index, inplace=True)

# backup the old data and update new datasource for the bubble chart
dtg = str(datetime.now())
dtg = dtg.split()[0]
cmd = f'mv ./bubble/data/complete_modified_date.csv ./bubble/data/complete_modified_date_{dtg}.csv'
os.system(cmd)
df_ind.to_csv('./bubble/data/complete_modified_date.csv', index=False)
print('Bubble chart data updated')

# For the Rank Chart, we use the same data made for Bubble Chart
# --------------------
cmd = f'mv ./ranking/data/complete_modified_date.csv ./ranking/data/complete_modified_date_{dtg}.csv'
os.system(cmd)
cmd = f'cp ./bubble/data/complete_modified_date.csv ./ranking/data/complete_modified_date.csv'
os.system(cmd)
print('Rank chart data updated')

# For the line chart
# --------------------
def format_date(date):
    l = date.split('-')
    l = reversed(l)
    return ''.join(l)

df['Date']=df.Date.apply(format_date)
cols = ['Region', 'Date', 'Confirmed', 'Recovered/Migrated', 'Deceased']
df_ind=df.reindex(columns=cols)
# df_ind.drop(index=df_ind[df_ind['Region']=='National Total'].index, inplace=True)

# backup the old data and update new datasource for the line chart
cmd = f'mv ./line/data/complete_modified_date.csv ./line/data/complete_modified_date_{dtg}.csv'
os.system(cmd)
df_ind.to_csv('./line/data/complete_modified_date.csv', index=False)
print('Line chart data updated')

print('Completed successfully')

