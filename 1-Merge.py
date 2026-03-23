#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


products = {'CampaignYear': [2015, 2016, 2017, 2018, 2019 , 2020, 2021],
        'ProductPrice': [199, 199, 199, 299, 299, 349, 349 ],
        'ProductVersion': ['v1', 'v1', 'v1', 'v2', 'v2', 'v2', 'v3']
        }
products


# In[3]:


df_products = pd.DataFrame(products)
df_products


# In[5]:


revenue = {'CampaignYear': [ 2016, 2017, 2018, 2019 , 2020, 2021],
           'Revenue': [9473, 8422, 9987, 7994, 9530, 9444 ]}
revenue


# In[6]:


df_revenue = pd.DataFrame(revenue)
df_revenue


# In[7]:


df_combined = pd.merge(df_products, df_revenue, on='CampaignYear')
df_combined


# In[8]:


df_combined_outer = pd.merge(df_products, df_revenue, how = 'outer')
df_combined_outer


# In[9]:


df_combined_inner = pd.merge(df_products, df_revenue, how = 'inner')
df_combined_inner


# In[10]:


df_combined_left = pd.merge(df_products, df_revenue, how = 'left')
df_combined_left


# In[11]:


df_combined_right = pd.merge(df_products, df_revenue, how = 'right')
df_combined_right


# In[ ]:




