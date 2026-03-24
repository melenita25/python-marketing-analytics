#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib as mlt


# In[2]:


ads = pd.read_csv('Advertising.csv', index_col = 'Date')
ads.head(5)


# In[3]:


ads.info()


# In[4]:


ads.describe()


# In[6]:


ads['Products'].unique()


# In[8]:


ads['Products'].value_counts()


# In[11]:


ads.groupby('Products')[['Web', 'Newspaper', 'Radio', 'TV']].sum()


# In[13]:


ads.groupby('Products').sum().plot(kind='bar', y='TV')


# In[17]:


ads.groupby('Products').sum().plot(kind='bar', y='Web', color = 'Green')


# In[19]:


sns.pairplot(ads)


# In[ ]:





# In[ ]:





# In[ ]:




