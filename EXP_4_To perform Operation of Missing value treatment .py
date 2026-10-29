#!/usr/bin/env python
# coding: utf-8

# In[20]:


#EXP :- 4


# In[21]:


# Aim :To perform Operation of Missing value treatment.


# In[1]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:31-07-2026


# In[23]:


import pandas as pd


# In[24]:


import os


# In[25]:


os.getcwd()                                      # Get current working directory 


# In[26]:


os.chdir("C:\\Users\\USER\\Desktop")


# In[27]:


data=pd.read_csv("titanic.csv")      


# In[28]:


data.head()                                      # first 5


# In[29]:


data.tail()                                       # last 5 


# In[30]:


data.shape                                        # here (cloumns , rows)


# In[31]:


data.columns


# In[32]:


data.info   


# In[33]:


data.dtypes 


# In[34]:


data.size


# In[35]:


data.ndim                                         # no. of dimension 


# In[36]:


data.describe()


# In[37]:


data.isna()


# In[38]:


data.isna().any()                                ## Checks column contains any missing values


# In[39]:


data.isnull().sum()                               # Identify the missing values from each column


# In[40]:


data.isnull().sum().sum()                        # Counts total missing values in the dataset


# In[41]:


df2 = data["Age"].fillna(30.272590)             # Replace missing Age values in the dataset


# In[42]:


df2.isna().sum()


# In[45]:


df2.isna().any()


# In[46]:


df2.isna()


# In[48]:


df2.isnull().sum()


# In[ ]:




