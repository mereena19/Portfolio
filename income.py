#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[22]:


from sklearn.model_selection import train_test_split


# In[23]:


from sklearn.linear_model import LogisticRegression


# In[24]:


from sklearn.metrics import accuracy_score,confusion_matrix


# In[26]:


os.listdir()


# In[27]:


income_df=pd.read_csv("income.csv")


# In[4]:


income_df


# In[6]:


df=income_df.copy()


# In[7]:


df


# In[8]:


df.info()


# In[11]:


df.isnull().sum()


# In[13]:


df.dropna(inplace=True)


# In[14]:


df.isnull().sum()


# In[15]:


Total=df.describe()
Total


# In[30]:


totalcat=df.describe(include='O')


# In[31]:


totalcat


# In[33]:


df['workclass'].value_counts()


# In[34]:


df['occupation'].value_counts()


# # Relationship between Independent variable

# In[36]:


correlation=df.corr()
correlation


# # Gender proportion
# 

# In[40]:


gender=pd.crosstab( index=df['sex'],
               columns='count',
               normalize=True)


# In[41]:


gender


# In[ ]:


Here Male count is larger.


# # Sex vs Income>50k

# In[46]:


sex_Income=pd.crosstab(index=df['sex'],
                       columns=df['income >50K'],
                       margins=True,
                       normalize='index')


# In[48]:


sex_Income


# In[55]:


sns.displot(df['age'],bins=10,kde=False)


# In[61]:


sns.boxplot(x="income >50K",
                y="age",
                data=df)


# In[63]:


df.groupby('income >50K')['age'].median()


# # workclass vs income >50K

# In[66]:


df.groupby('workclass')['income >50K'].median()


# In[68]:


sns.barplot(x='workclass',y='income >50K',data=df)


# # Education vs income >50K

# In[69]:


df.groupby('education')['income >50K'].median()


# In[73]:


sns.barplot(x='education',y='income >50K',data=df)


# In[ ]:




