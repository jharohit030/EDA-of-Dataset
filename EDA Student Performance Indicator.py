#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv('StudentsPerformance.csv')


# In[4]:


df.head()


# In[6]:


df.shape


# In[ ]:


#Data check to perfrom
1. check Missing values
2. check Duplicates
3. check Data types
4. check the number of unique values of each column
5. check statistics of data set
6. check various categories present in the different categorical column


# In[7]:


#check missing values

df.isnull().sum()


# In[8]:


df.isna().sum() #same output to previous one


# In[10]:


#check duplicate
df.duplicated()


# In[11]:


#check data type
df.info()


# In[13]:


#unique values
df.nunique()


# In[14]:


#check the statistical of data
df.describe()


# In[15]:


df.tail() # last 5 records


# In[16]:


df.tail(50) #last 50 data


# In[21]:


#fetch the categorical features
[feature for feature in df.columns if df[feature].dtype== 'O']


# In[25]:


#segregate numerical and categorical features
numerical_feature = [feature for feature in df.columns if df[feature].dtype!= 'O']
categorical_feature = [feature for feature in df.columns if df[feature].dtype=='O']


# In[26]:


numerical_feature


# In[27]:


categorical_feature


# In[28]:


df['gender'].value_counts()


# In[30]:


df['race/ethnicity'].value_counts()


# In[33]:


#Agregate the total score with mean

df['total_score']= (df['math score']+df['reading score']+df['writing score'])
df['average'] = df['total_score']/3
df.head()


# In[37]:


## Exploring more visualization

fig, axis = plt.subplots(1,2, figsize=(15,7))
plt.subplot(121) #121 means 1row and 2 col ka 1st box
sns.histplot(data = df, x = 'average', bins = 30, kde = True, color='Green')
plt.subplot(122) #122 means 1row and 2 col ka 2nd box
sns.histplot(data = df,x = 'average', bins = 30 , kde = True, hue = 'gender')


# In[ ]:


#insights from data

Female  students tend to perform well than Male students


# In[43]:


plt.subplots(1,3, figsize=(25,6))
plt.subplot(141) #1st row, 4th col ka 1st box
sns.histplot(data = df, x = 'average', kde = True, hue = 'lunch')
plt.subplot(142)
sns.histplot(data = df[df.gender=='female'], x = 'average', kde = True, hue = 'lunch')
plt.subplot(143)
sns.histplot(data = df[df.gender=='male'], x = 'average', kde = True, hue = 'lunch')


# In[ ]:


#insights from data

standard lunch help students perform well in exam
standard lunch help perform well in exams be it a male and female


# In[45]:


plt.subplots(1,3, figsize=(25,6))
plt.subplot(141) #1st row, 4th col ka 1st box
sns.histplot(data = df, x = 'average', kde = True, hue = 'parental level of education')
plt.subplot(142)
sns.histplot(data = df[df.gender=='female'], x = 'average', kde = True, hue = 'parental level of education')
plt.subplot(143)
sns.histplot(data = df[df.gender=='male'], x = 'average', kde = True, hue = 'parental level of education')


# In[ ]:


Insights

1.In general parents education don't help student perform well in exam
2.2nd plot we can see there is no effect of parents education on female students
3.3rd plot shows that parents whose education is of associate's degree or master degree their male child tend to perform


# In[47]:


plt.subplots(1,3, figsize=(25,6))
plt.subplot(141) #1st row, 4th col ka 1st box
sns.histplot(data = df, x = 'average', kde = True, hue = 'race/ethnicity')
plt.subplot(142)
sns.histplot(data = df[df.gender=='female'], x = 'average', kde = True, hue = 'race/ethnicity')
plt.subplot(143)
sns.histplot(data = df[df.gender=='male'], x = 'average', kde = True, hue = 'race/ethnicity')


# In[ ]:


Insights

1. Student of group A and B tends to perform poorly in exam
2. Student of group A and B tends to perform poorly in exam irrespective of whether they are male or female


# In[48]:


sns.heatmap(df.corr(), annot = True)


# In[ ]:




