#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('conversion_rates.csv')
data


# In[3]:


converted_df = data.groupby('group').sum()


# In[4]:


converted_df


# In[6]:


viewed_df = data.groupby('group').count().rename({'converted':'viewed'},axis=1)
viewed_df


# In[7]:


stats = converted_df.merge(viewed_df,on='group')
stats


# In[8]:


stats['convertion_rate'] = stats['converted'] / stats['viewed']
stats


# In[9]:


df = stats.stack()
df


# In[11]:


df['A']['convertion_rate']


# In[12]:


stats.unstack()


# In[13]:


stats.unstack().unstack()


# In[ ]:





# In[ ]:




