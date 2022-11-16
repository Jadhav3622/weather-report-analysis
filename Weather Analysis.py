#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


weather_df = pd.read_csv(r'C:\Users\Jadhav\Downloads\1. Weather Data.csv')
print(weather_df)


# In[3]:


weather_df.head(20)


# In[4]:


weather_df.shape


# In[5]:


weather_df.index


# In[6]:


weather_df.columns


# In[7]:


weather_df.dtypes


# In[8]:


weather_df['Weather'].unique()


# In[9]:


weather_df.nunique()


# In[10]:


weather_df.count()


# In[11]:


weather_df['Weather']. value_counts()


# In[12]:


weather_df.info()


# In[19]:


plt.figure(figsize = (20,9))
sns.barplot(weather_df['Rel Hum_%'], weather_df['Temp_C'])


# In[13]:


weather_df.describe()


# In[14]:


weather_df.transpose()


# In[15]:


weather_df['Wind Speed_km/h'].nunique()


# In[16]:


weather_df['Wind Speed_km/h'].unique()


# In[17]:


weather_df[weather_df.Weather == 'Clear']


# In[18]:


weather_df[weather_df['Wind Speed_km/h'] == 11]


# In[19]:


plt.figure(figsize = (18,9))
sns.barplot(x = 'Wind Speed_km/h', y = 'Visibility_km', data = weather_df, color = 'red')


# In[20]:


weather_df.isnull().sum()


# In[21]:


weather_df.rename(columns = {'Weather': 'Weather Condition'})


# In[24]:


weather_df.rename(columns = {'Weather': 'Weather Condition'}, inplace  = True)
weather_df.head(20)


# In[26]:


weather_df.Visibility_km.mean()


# In[29]:


weather_df.Press_kPa.mode()


# In[33]:


weather_df.Temp_C.median()


# In[36]:


weather_df.Press_kPa.std()


# In[38]:


weather_df['Rel Hum_%'].var()


# In[39]:


weather_df[weather_df['Weather Condition'].str.contains('Snow')].head(50)


# In[21]:


sns.distplot(weather_df['Dew Point Temp_C'])


# In[22]:


sns.jointplot(weather_df['Rel Hum_%'], weather_df['Wind Speed_km/h'], kind = 'hex')


# In[40]:


weather_df[weather_df['Weather Condition'].str.contains('Snow')].tail(50)


# In[41]:


weather_df[(weather_df['Wind Speed_km/h']>24) & (weather_df['Visibility_km'] == 25)]


# In[42]:


weather_df.groupby('Weather Condition').mean()


# In[43]:


weather_df.groupby('Weather Condition').min()


# In[44]:


weather_df.groupby('Weather Condition').max()


# In[49]:


weather_df[(weather_df['Weather Condition'] =='Clear') | (weather_df['Visibility_km']> 50)].head(20)


# In[56]:


weather_df[(weather_df['Weather Condition'] =='Rain') & (weather_df['Visibility_km']< 60)].head(5000)


# In[58]:


weather_df[(weather_df['Weather Condition'] == 'Clear') & (weather_df['Rel Hum_%'] >50) | (weather_df['Visibility_km'] >40)]


# In[26]:


plt.figure(figsize = (30,15))
sns.pairplot(weather_df[['Temp_C', 'Dew Point Temp_C']])


# In[ ]:




