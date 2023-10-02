#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df_tracks=pd.read_csv("C:\\Users\\ELCOT\\Downloads\\QP0183J\\tracks.csv")
df_tracks.head()


# In[4]:


# checking the null value

pd.isnull(df_tracks).sum()


# In[5]:


df_tracks.info()


# In[6]:


#Top 10 least popular songs

sorted = df_tracks.sort_values('popularity', ascending=True).head(10)
sorted


# In[7]:


#descerptive statistics of data

df_tracks.describe()


# In[8]:


most_popular = df_tracks.query('popularity<=100',inplace=False).sort_values('popularity', ascending = False)
most_popular[:10]


# In[9]:


df_tracks.set_index('release_date',inplace=True)
df_tracks.index=pd.to_datetime(df_tracks.index)
df_tracks.head()


# In[43]:


# Fetching data from particular row

df_tracks[['artists','name']].iloc[20]


# In[10]:


#coverting ms to s

df_tracks['duration_ms'] = df_tracks['duration_ms']/1000


# In[42]:


df_tracks.rename(columns={'duration_ms':'duration_s'}, inplace=True)
df_tracks.head()


# In[12]:


#Heatmap

corr_df = df_tracks.corr(method='pearson')
plt.figure(figsize=(14,6))
heatmap=sns.heatmap(corr_df,annot=True, fmt=".1g", vmin=-1,vmax=1,center=0,cmap='inferno',linewidths=1,linecolor='Black')
heatmap.set_title('Correlation between variables')


# In[16]:


#Creating sample data

sample_df = df_tracks.sample(int(0.005*len(df_tracks)))
print(len(sample_df))


# In[17]:


#regression plot
plt.figure(figsize=(10,5))
sns.regplot(data=sample_df, y='loudness',x='energy',color='c').set(title='Loudness Vs Energy Regression plot')


# In[18]:


plt.figure(figsize=(10,5))
sns.regplot(data=sample_df, y='popularity',x='acousticness',color='r').set(title='Popularity Vs acousticness Regression plot')


# In[19]:


df_tracks['dates']=df_tracks.index.get_level_values('release_date')
df_tracks.dates=pd.to_datetime(df_tracks.dates)
years=df_tracks.dates.dt.year


# In[20]:


sns.displot(years,discrete=True,aspect=2,height=5,kind='hist').set(title='Number of songs released per year')


# In[21]:


total_dr=df_tracks.duration_ms
sns.set_style(style='whitegrid')
fig,ax=plt.subplots(figsize=(10,5))
fig=sns.lineplot(x=years, y=total_dr,ax=ax).set(title='year vs duration')
plt.xticks(rotation=60)


# In[23]:


df_genre=pd.read_csv("C:\\Users\\ELCOT\\Downloads\\QP0183J\\SpotifyFeatures.csv")
df_genre.head()


# In[40]:


plt.figure(figsize=(10,5))
sns.color_palette('rocket', as_cmap=True)
plot=sns.barplot(y='duration_ms', x='genre', data=df_genre).set(title='Duration of songs in different genre')




# In[39]:


sns.set_style(style='darkgrid')
plt.figure(figsize=(10,5))
famous=df_genre.sort_values('popularity', ascending=False).head(10)
sns.barplot(y='genre',x='popularity', data=famous).set(title='Top 5 genre')


# In[ ]:




