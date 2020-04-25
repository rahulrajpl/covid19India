#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/coder-amey/COVID-19-India_Data/master/time-series/India_regional_aggregated.csv')


# In[2]:


def format_date(date):
    l = date.split('-')
    l = reversed(l)
    return ''.join(l)

df['Date']=df.Date.apply(format_date)

cols = ['Region', 'Date', 'Confirmed', 'Recovered/Migrated', 'Deceased']

df_ind=df.reindex(columns=cols)
df_ind.drop(index=df_ind[df_ind['Region']=='National Total'].index, inplace=True)
df_ind.to_csv('complete_modified_date.csv', index=False)


# In[3]:


get_ipython().system('mv ../covid19India/bubble/data/complete_modified_date.csv ../covid19India/bubble/data/complete_modified_date_0423.csv')


# In[4]:


get_ipython().system('cp ./complete_modified_date.csv ../covid19India/bubble/data/complete_modified_date.csv')


# In[5]:


def format_date(date):
    l = date.split('-')
    l = reversed(l)
    return ''.join(l)

df['Date']=df.Date.apply(format_date)

cols = ['Region', 'Date', 'Confirmed', 'Recovered/Migrated', 'Deceased']

df_ind=df.reindex(columns=cols)
# df_ind.drop(index=df_ind[df_ind['Region']=='National Total'].index, inplace=True)
df_ind.to_csv('complete_modified_date.csv', index=False)


# In[6]:


get_ipython().system('mv ../covid19India/line/data/complete_modified_date.csv ../covid19India/line/data/complete_modified_date_0423.csv')


# In[7]:


get_ipython().system('cp ./complete_modified_date.csv ../covid19India/line/data/complete_modified_date.csv')


# In[ ]:




