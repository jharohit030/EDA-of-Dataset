#!/usr/bin/env python
# coding: utf-8

# In[164]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[118]:


df = pd.read_excel('flight_price.xlsx')


# In[119]:


df.head()


# In[120]:


df.info()


# In[121]:


df.describe()


# In[122]:


df.head(2)


# In[123]:


type(df['Date_of_Journey'].str.split('/').str[0][0])


# In[124]:


df['Day'] = df['Date_of_Journey'].str.split('/').str[0]
df['Month']=df['Date_of_Journey'].str.split('/').str[1]
df['Year']=df['Date_of_Journey'].str.split('/').str[2]


# In[125]:


df


# In[126]:


df['Day'] = df['Day'].astype(int)
df['Month'] = df['Month'].astype(int)
df['Year'] = df['Year'].astype(int)


# In[127]:


df.head()


# In[128]:


df.info()


# In[129]:


df.drop('Date_of_Journey', axis = 1, inplace = True)


# In[130]:


df.head()


# In[131]:


df['Arrival_Time'].str.split(' ').str[0]


# In[132]:


df['Arrival_hours']=df['Arrival_Time'].str.split(' ').str[0].str.split(':').str[0]
df['Arrival_min']=df['Arrival_Time'].str.split(' ').str[0].str.split(':').str[1]


# In[133]:


df.head()


# In[134]:


df.drop('Arrival_Time', axis = 1, inplace = True)


# In[135]:


df['Arrival_hours']= df['Arrival_hours'].astype(int)
df['Arrival_min']= df['Arrival_min'].astype(int)


# In[136]:


df.info()


# In[137]:


df['Dep_hours']=df['Dep_Time'].str.split(' ').str[0].str.split(':').str[0]
df['Dep_min']=df['Dep_Time'].str.split(' ').str[0].str.split(':').str[1]
df['Dep_hours']= df['Dep_hours'].astype(int)
df['Dep_min']= df['Dep_min'].astype(int)


# In[138]:


df.info()


# In[139]:


df.drop('Dep_Time', axis = 1, inplace = True)


# In[140]:


df.head()


# In[141]:


df.drop('Route', axis = 1, inplace = True)


# In[142]:


df.head(2)


# In[143]:


df['Duration_hours']= df['Duration'].str.split(' ').str[0].str.split('h').str[0]
df['Duration_min']= df['Duration'].str.split(' ').str[1].str.split('m').str[0]
#df.drop(index = 6474, inplace = True, axis = 0)
# df['Duration_hours']= df['Duration_hours'].astype(int)
# df['Duration_min']= df['Duration_min'].astype(int)


# In[147]:


df['Duration'].value_counts()


# In[148]:


df['Duration_hours']


# In[152]:


df['Duration_min'].fillna(0, inplace = True)


# In[153]:


df['Duration_min']


# In[166]:


df.drop(index = 6474, axis = 0, inplace = True)


# In[156]:


df


# In[169]:


#df['Duration_hours']= df['Duration_hours'].astype(int64)
#df['Duration_min']= df['Duration_min'].astype(in
df['Duration_hours'] = df['Duration_hours'].astype(int)
df['Duration_min'] = df['Duration_min'].astype(int)


# In[170]:


df.info()


# In[171]:


df.head(2)


# In[172]:


df.drop('Duration', axis = 1, inplace= True)


# In[173]:


df['Total_Stops'].unique()


# In[174]:


df['Total_Stops'].mode()


# In[175]:


df['Total_Stops']=df['Total_Stops'].map({'non-stop':0, '1 stop':1,'2 stops':2, '3 stops':3, '4 stops':4, np.nan:1})


# In[176]:


df['Total_Stops'].isnull().sum()


# In[177]:


df.head()


# In[178]:


df['Airline'].unique()


# In[179]:


df['Source'].unique()


# In[180]:


df['Destination'].unique()


# In[181]:


from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()


# In[182]:


encoder.fit_transform(df[['Airline','Source','Destination']]).toarray()


# In[194]:


df1 = pd.DataFrame(encoder.fit_transform(df[['Airline','Source','Destination']]).toarray(), columns = encoder.get_feature_names_out())


# In[196]:


df1


# In[197]:


df1.head(2)


# In[187]:


df.drop('Additional_Info', axis = 1, inplace = True)


# In[188]:


df.head()


# In[198]:


df2= pd.concat([df, df1], axis = 1)


# In[201]:


df2.columns


# In[202]:


df2.head()


# In[207]:


df2.drop('Destination', axis = 1, inplace = True)


# In[208]:


df2.info()


# In[209]:


df2


# In[210]:


df2.columns


# In[211]:


df2.head(10)


# In[ ]:




