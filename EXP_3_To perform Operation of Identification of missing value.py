#!/usr/bin/env python
# coding: utf-8

# In[1]:


#EXP :- 3


# In[2]:


# Aim :To perform Operation of Identification of missing value.


# In[1]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:31-07-2026


# In[4]:


import pandas as pd


# In[5]:


import os


# In[6]:


os.getcwd()                                      # Get current working directory 


# In[7]:


os.chdir("C:\\Users\\USER\\Desktop")      # change directory 


# In[8]:


data=pd.read_csv("titanic.csv")      


# In[9]:


data.head()                                      # first 5


# In[10]:


data.tail()                                       # last 5 


# In[11]:


data.shape                                        # here (cloumns , rows)


# In[12]:


data.columns


# In[13]:


data.info   


# In[14]:


data.dtypes 


# In[15]:


data.size


# In[16]:


data.ndim                                         # no. of dimension 


# In[17]:


data.describe()


# In[37]:


data.isna()


# In[18]:


data.isna().any()                                ## Checks column contains any missing values


# In[19]:


data.isnull().sum()                               # Identify the missing values from each column


# In[36]:


data.isnull().sum().sum()                        # Counts total missing values in the dataset


# In[ ]:




