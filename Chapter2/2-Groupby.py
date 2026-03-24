#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


sales = pd.read_csv('sales.csv')
sales.head(5)


# In[3]:


sales.columns


# In[4]:


sales['Year'].unique()


# In[5]:


sales['Product line'].unique()


# In[6]:


sales['Product type'].unique()


# In[7]:


sales['Product'].unique()


# In[8]:


sales['Order method type'].unique()


# In[9]:


sales['Retailer country'].unique()


# In[10]:


sales.describe()


# In[11]:


sales['Year'].value_counts()


# In[13]:


sales['Product line'].value_counts()


# In[14]:


sales['Product type'].value_counts()


# In[16]:


sales['Product'].value_counts()


# In[17]:


sales.columns


# In[18]:


sales['Order method type'].value_counts()


# In[19]:


sales['Retailer country'].value_counts()


# In[21]:


sales.groupby('Retailer country')[['Revenue','Planned revenue','Product cost','Quantity','Gross profit']].sum()


# In[23]:


sales.dropna().groupby('Retailer country')[['Revenue','Planned revenue','Product cost','Quantity',
                                            'Unit cost','Unit price','Gross profit','Unit sale price']].min()


# In[24]:


sales.groupby('Year')[['Revenue','Planned revenue','Product cost','Quantity',
                                            'Unit cost','Unit price','Gross profit','Unit sale price']].sum()


# In[26]:


sales.groupby('Product line')[['Revenue','Planned revenue','Product cost',
                               'Quantity','Unit cost','Unit price','Gross profit','Unit sale price']].sum()


# In[25]:


sales.columns


# In[ ]:




