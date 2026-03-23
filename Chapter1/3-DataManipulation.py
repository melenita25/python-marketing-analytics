#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df1 = pd.DataFrame() 
df2 = pd.DataFrame()


# In[3]:


df1['viewers'] = ["Sushmita", "Adam", "Benny", "Anurag"]
df2['users'] = ["Adam", "Anurag", "Benny", "Sushmita", "Apoorva"]


# In[4]:


df1


# In[5]:


df1 = df1.assign(views = [31.2,17.9,265.23,42.47]) 
df2 = df2.assign(cost = [20,np.nan, 15, 2, 7])


# In[6]:


df1


# In[7]:


df2


# In[8]:


df = df1.merge(df2, how = 'left', left_on='viewers', right_on = 'users')
df


# In[11]:


df = df.fillna(df['cost'].mean())
df


# In[12]:


df['Gender'] = ["Female", "Male", "Male", "Female"]
df.head()


# In[13]:


df['Gender'] = df['Gender'].map({'Female':'F', 'Male':'M'})
df


# In[15]:


df.groupby('Gender')['cost'].sum()


# In[16]:


df.set_index(['viewers'],inplace=True)


# In[17]:


df


# In[18]:


df.loc[['Adam','Anurag'],['cost','views']]


# In[19]:


df=pd.DataFrame({'Currency': pd.Series(['USD','EUR','GBP']),'ValueInINR': pd.Series([70, 89, 99])})

df.head()


# In[20]:


df1 = df.copy()
df1.head(5)


# In[ ]:




