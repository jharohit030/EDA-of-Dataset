#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')


# In[4]:


df.head(2)


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.shape


# In[8]:


df['Reviews'].str.isnumeric().sum()


# In[9]:


df[~df['Reviews'].str.isnumeric()]


# In[10]:


df_copy = df.copy()


# In[11]:


df_copy.drop(index = 10472, axis = 0, inplace = True)


# In[13]:


df_copy[~df_copy['Reviews'].str.isnumeric()]


# In[14]:


df_copy['Reviews'] = df_copy['Reviews'].astype(int)


# In[15]:


df_copy.info()


# In[16]:


df_copy['Size'].unique()


# In[17]:


df_copy['Size'] = df_copy['Size'].str.replace('M','000')
df_copy['Size'] = df_copy['Size'].str.replace('k','')
df_copy['Size'] = df_copy['Size'].replace('Varies with device',np.nan)


# In[18]:


df_copy['Size'] = df_copy['Size'].astype(float)


# In[19]:


df_copy.info()


# In[20]:


df_copy['Installs'].unique()


# In[21]:


df_copy['Price'].unique()


# In[22]:


chars_to_remove = ['+',',','$']
cols_to_clean = ['Installs','Price']
for item in chars_to_remove:
    for cols in cols_to_clean:
        df_copy[cols] = df_copy[cols].str.replace(item,'')


# In[23]:


df_copy['Installs'].unique()


# In[24]:


df_copy['Installs'] = df_copy['Installs'].astype(int)
df_copy['Price'] = df_copy['Price'].astype(float)


# In[25]:


df_copy.info()


# In[26]:


df.head(2)


# In[28]:


df_copy['Last Updated'] = pd.to_datetime(df_copy['Last Updated'])
df_copy['Day'] = df_copy['Last Updated'].dt.day
df_copy['Month'] = df_copy['Last Updated'].dt.month
df_copy['Year'] = df_copy['Last Updated'].dt.year


# In[29]:


df_copy.info()


# In[30]:


df_copy['Content Rating'].value_counts()


# In[33]:


df_copy[df_copy.duplicated('App')]


# In[ ]:


#observation: the dataset has duplicate records


# In[34]:


df_copy= df_copy.drop_duplicates(subset = ['App'], keep = 'first')


# In[35]:


df_copy.shape


# In[36]:


numeric_feature = [feature for feature in df_copy.columns if df_copy[feature].dtype!= 'O']
categorical_feature = [feature for feature in df_copy.columns if df_copy[feature].dtype== 'O']

print('We have {} numerical features : {}'.format(len(numeric_feature), numeric_feature))
print('We have {} categorical features : {}'.format(len(categorical_feature), categorical_feature))


# In[41]:


#visualization diagram

plt.figure(figsize = (15,15))
plt.suptitle('Univariate Analysis of Numerical Feature', fontsize = 20, fontweight = 'bold', alpha = 0.8, y = 1.)

for i in range(0, len(numeric_feature)):
    plt.subplot(5,3,i+1)
    sns.kdeplot(x = df_copy[numeric_feature[i]], shade = True, color = 'r')
    plt.xlabel(numeric_feature[i])
    plt.tight_layout()


# In[ ]:


#Rating and Year is left skwed adn Reviews, size, INstalls ans preice are right skwed


# In[43]:


#categorical column

plt.figure(figsize = (20,15))
plt.suptitle('Univariate Analysis of Categorical feature', fontsize = 20, fontweight = 'bold', alpha = 0.8, y =1.)
category = ['Type', 'Content Rating']
for i in range(0, len(category)):
    plt.subplot(2,2,i+1)
    sns.countplot(x = df[category[i]], palette = 'Set2')
    plt.xlabel(category[i])
    plt.xticks(rotation = 45)
    plt.tight_layout()


# In[44]:


## which is most popular app category
df_copy.head(2)


# In[45]:


df_copy['Category'].value_counts().plot.pie(y = df_copy['Category'], figsize = (15,16), autopct = "%1.1f")


# In[ ]:


#most papular are family and less is beauty


# In[46]:


## top 10 app category

category = pd.DataFrame(df_copy['Category'].value_counts())
category.rename(columns = {'Category':'count'}, inplace = True)


# In[47]:


category


# In[49]:


plt.figure(figsize=(15,6))
sns.barplot(x = category.index[:10], y = 'count', data = category[:10], palette = 'hls')
plt.title('Top 10 App Category')
plt.xticks(rotation = 90)
plt.show()


# In[ ]:




