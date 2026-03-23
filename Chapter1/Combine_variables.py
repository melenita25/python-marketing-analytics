#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import copy


# In[2]:


sales = pd.read_csv("sales.csv")


# In[3]:


sales.head(5)


# In[4]:


sales.dtypes


# In[5]:


sales.info()


# In[6]:


sales['Product line'] = sales['Product'] + ' ' + sales['line']
sales = sales.drop(columns=['Product','line'])
sales.head(5)


# In[7]:


sales.groupby(['Product.1','type'])['Year'].count()


# In[9]:


sales['Product type'] = sales['Product.1'] + ' ' + sales['type']
sales = sales.drop(columns=['Product.1','type'])
sales.head(5)


# In[10]:


sales['Product'] = sales['Product.2'] + ' ' + sales['Order'] + ' ' + sales['method']
sales = sales.drop(columns=['Product.2','Order', 'method'])
sales.head(5)


# In[11]:


sales.groupby('type.1')['Year'].count()


# In[13]:


sales = sales.rename(columns = {'type.1':'Order method'})
sales.head(5)


# In[14]:


sales = sales.fillna('')


# In[17]:


sales['Retailer country']=sales['Retailer']+' '+sales['country']
sales = sales.drop(columns = ['Retailer', 'country'])
sales.head()


# In[ ]:





# In[ ]:





# In[ ]:




