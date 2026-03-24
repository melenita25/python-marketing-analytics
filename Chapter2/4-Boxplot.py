#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


sales = pd.read_csv('sales.csv')
sales


# In[4]:


sales.columns


# In[8]:


sales.groupby('Order method type').sum().plot(kind='bar',y='Revenue', color ='grey')


# In[13]:


sales.groupby('Year')[['Revenue','Planned revenue','Gross profit']].plot(kind='box',color='blue')


# In[ ]:




