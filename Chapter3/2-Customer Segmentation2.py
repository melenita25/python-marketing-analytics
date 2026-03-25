#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("Mall_Customers.csv")
data.head(5)


# In[3]:


data.info()


# In[4]:


data = data.rename(columns = {'Annual Income (k$)':'Income','Spending Score (1-100)':'Spend_score'})
data


# In[5]:


data.describe()


# ## Traditional Segmentation of Mall Customers

# In[6]:


data.head(3)


# In[8]:


data['Income'].plot.hist()
plt.xlabel('Income')
plt.show()


# Create a new column ‘Cluster’ to have the values ‘Low Income’, ‘Moderate Income’, ‘High earners’ for customers with income in the ranges < 50, 50 – 90, and >= 90 respectively, using the code below.

# In[10]:


data['Cluster'] = np.where(data['Income']>=90,"High earners",np.where(data['Income']<50,"Low Income","Moderate Income"))
data.head(5)


# In[11]:


data.groupby('Cluster')['Income'].describe()


# ## Standardizing Customer Data

# In[12]:


from sklearn.preprocessing import StandardScaler


# In[13]:


scaler = StandardScaler()
cols_to_scale = ['Age', 'Income', 'Spend_score']
data_scaled = data.copy()
data_scaled[cols_to_scale] = scaler.fit_transform(data_scaled[cols_to_scale])
data_scaled[cols_to_scale].describe()


# ## Calculating distance between customers

# In[14]:


sel_cols = ['Income', 'Spend_score']
cust3 = data_scaled[sel_cols].head(3)
cust3


# In[15]:


from scipy.spatial.distance import cdist


# In[16]:


cdist(cust3, cust3, metric='euclidean')


# In[17]:


np.sqrt((-1.739+1.739)**2 + (-0.4348-1.1957)**2)


# ## k-means Clustering on Mall Customers

# In[20]:


cluster_cols = ['Income', 'Spend_score']
sns.scatterplot(data=data_scaled,x='Income',y='Spend_score')


# In[21]:


from sklearn.cluster import KMeans


# In[22]:


model = KMeans(n_clusters=5,random_state=42)
model.fit(data_scaled[cluster_cols])
data_scaled['Cluster'] = model.predict(data_scaled[cluster_cols])
data_scaled.head(5)


# In[23]:


sns.scatterplot(data=data_scaled, x='Income',y='Spend_score', hue='Cluster')
plt.show()


# ## Dealing with High-Dimensional Data

# In[24]:


cluster_cols = ['Age', 'Income', 'Spend_score']
model = KMeans(n_clusters=4, random_state=42)
model.fit(data_scaled[cluster_cols])
data_scaled['Cluster'] = model.predict(data_scaled[cluster_cols])


# In[25]:


from sklearn import decomposition


# In[26]:


pca = decomposition.PCA(n_components = 2)
pca_res = pca.fit_transform(data_scaled[cluster_cols])
data_scaled['pc1']=pca_res[:,0]
data_scaled['pc2']=pca_res[:,1]


# In[28]:


sns.scatterplot(data=data_scaled, x='pc1',y='pc2',hue='Cluster')
plt.show()


# In[29]:


data['Cluster'] = data_scaled.Cluster
data


# In[30]:


data.groupby('Cluster')[['Age', 'Income', 'Spend_score']].mean()


# In[31]:


data.groupby('Cluster')[['Age', 'Income', 'Spend_score']].mean().plot.bar()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




