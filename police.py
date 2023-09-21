#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


police_df=pd.read_csv('police.csv')
police_df


# In[4]:


df=police_df.copy()


# In[5]:


df


# In[6]:


df.info()


# In[8]:


df.isnull().sum()


# In[10]:


df.drop(columns='country_name',inplace=True)


# In[11]:


df


# # For speeding,where men and women stops more often

# In[12]:


df.head()


# In[28]:


df[df.violation=='Speeding'].driver_gender.value_counts()


# # Does gender affect who get searched during a stop?

# In[29]:


df.groupby('driver_gender').search_conducted.sum()


# # mean stop duration

# In[31]:


df.stop_duration.value_counts()


# In[33]:


df['stop_duration']=df.stop_duration.map({'0-15 Min':7.5,'16-30 Min':24,'30+ Min':45})


# In[34]:


df


# In[35]:


df['stop_duration'].mean()


# # age distribution for each violations

# In[38]:


df.groupby('violation').driver_age.describe()


# In[ ]:




