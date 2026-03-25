#!/usr/bin/env python
# coding: utf-8

# ## Bank Customer Segmentation for Loan Campaign

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# In[2]:


bank0 = pd.read_csv("Bank_Personal_Loan_Modelling-1.csv")
bank0.head(5)


# In[3]:


bank0.info()


# In[4]:


scaler = StandardScaler()
bank0[['Income Scaled','CCAvg Scaled']] = scaler.fit_transform(bank0[['Income','CCAvg']])
bank0[['Income Scaled','CCAvg Scaled']].describe()


# In[5]:


model = KMeans(n_clusters = 3, random_state = 42)
cluster_cols = ['Income Scaled', 'CCAvg Scaled']
model.fit(bank0[cluster_cols])
bank0['Cluster'] = model.predict(bank0[cluster_cols])


# In[7]:


sns.scatterplot(data=bank0, x='Income', y='CCAvg', hue='Cluster')
plt.show()


# In[12]:


bank0.groupby('Cluster')[['Income', 'CCAvg']].mean()


# In[17]:


bank0.groupby('Cluster')[['Income Scaled', 'CCAvg Scaled']].mean().plot(kind='bar',color = ['blue','green'])
plt.show()


# In[18]:


sel_cols = ['Income', 'CCAvg', 'Age', 'Mortgage', 'Family', 'CreditCard', 'Online', 'Personal Loan']
bank0.groupby('Cluster')[sel_cols].mean()


# ## Bank Customer Segmentation with Multiple Features

# In[19]:


bank_scaled = bank0.copy()
bank_scaled.columns


# In[20]:


cluster_cols = ['Income','CCAvg','Age','Experience','Mortgage']
bank_scaled[cluster_cols] = scaler.fit_transform(bank_scaled[cluster_cols])
bank_scaled


# In[21]:


bank_scaled[cluster_cols].describe()


# In[23]:


model = KMeans(n_clusters = 3, random_state = 42)
model.fit(bank_scaled[cluster_cols])
bank_scaled['Cluster'] = model.predict(bank_scaled[cluster_cols])


# In[25]:


from sklearn import decomposition

pca = decomposition.PCA(n_components=2)
pca_res = pca.fit_transform(bank_scaled[cluster_cols])

bank_scaled['pc1'] = pca_res[:,0]
bank_scaled['pc2'] = pca_res[:,1]


# In[30]:


sns.scatterplot(data=bank_scaled, x='pc1', y='pc2', hue='Cluster')
plt.show()


# In[31]:


bank0['Cluster'] = bank_scaled.Cluster
bank0.groupby('Cluster')[cluster_cols].mean()


# In[32]:


sel_cols = ['Income', 'CCAvg', 'Age', 'Experience', 'Mortgage', \
            'Family', 'CreditCard', 'Online', 'Personal Loan']

bank0.groupby('Cluster')[sel_cols].mean()


# In[ ]:




