#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from warnings import filterwarnings
filterwarnings('ignore')


# In[12]:


df = pd.read_csv('forest.csv', header =1)


# In[13]:


df


# In[14]:


df.columns


# In[15]:


df.head()


# In[18]:


#convert dataframe into Dictionary as mongoDb stores data in records/ documents
data = df.to_dict(orient = 'records')


# In[19]:


data


# In[21]:


df.info()


# In[22]:


#columns which has null values
df[df.isnull().any(axis = 1)]


# In[23]:


df.isnull().sum()


# In[24]:


#Remove null or na values row
df= df.dropna().reset_index(drop = True)


# In[25]:


df


# In[26]:


df.shape


# In[27]:


#columns which have string
df.iloc[[122]]


# In[28]:


#remove 122th column
df = df.drop(122).reset_index(drop = True)


# In[29]:


df


# In[30]:


df.columns


# In[32]:


df.column = df.columns.str.strip()


# In[33]:


df.column


# In[36]:


df.describe()


# In[37]:


df.describe().T


# In[47]:


df.Classes.value_counts()


# In[ ]:




