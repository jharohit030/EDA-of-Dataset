#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[9]:


df = pd.read_csv('wine.csv',sep=";")


# In[10]:


df.head()


# In[23]:


df


# In[11]:


df.info()


# In[12]:


df.describe() #descriptive summary of dataset


# In[13]:


## shape of dataset
df.shape


# In[14]:


#list down all columns
df.columns


# In[15]:


df['quality'].unique()


# In[16]:


#conclusion -> Imbalanced dataset
df['quality'].value_counts()


# In[18]:


## Missing Values
df.isnull().sum() #here no missing values present


# In[20]:


# TO duplicate records
df[df.duplicated()]


# In[21]:


#removing duplicate records
df.drop_duplicates(inplace = True)


# In[24]:


df.shape


# In[25]:


#correlation
df.corr()


# In[26]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize = (10,20))
sns.heatmap(df.corr(), annot = True) #annot used in seaborn for showing the values


# In[28]:


df.quality.value_counts().plot(kind ='bar')


# In[30]:


sns.distplot(df['fixed acidity'])


# In[32]:


sns.histplot(df['fixed acidity'], kde =True)


# In[33]:


for i in df.columns:
    sns.histplot(df[i], kde = True)


# In[34]:


#categorical plots
sns.catplot(x = 'quality', y = 'alcohol', data = df, kind = 'box')


# In[35]:


sns.scatterplot(x='alcohol', y = 'pH', hue = 'quality', data = df)


# In[ ]:




