#!/usr/bin/env python
# coding: utf-8

# In[1]:


#EXP :- 2


# In[2]:


# Aim :To perform Operation of Exploratory Data Analysis (EDA).


# In[1]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:31-07-2026


# In[1]:


import pandas as pd


# In[2]:


import os


# In[3]:


os.getcwd()                                      # Get current working directory 


# In[4]:


os.chdir("C:\\Users\\USER\\Desktop")


# In[5]:


data=pd.read_csv("heart.csv")      


# In[6]:


data.head()                                      # first 5


# In[7]:


data.tail()                                       # last 5 


# In[8]:


data.shape                                        # here (cloumns , rows)


# In[9]:


data.columns


# In[10]:


data.info   


# In[11]:


data.dtypes 


# In[12]:


data.size                                         # Row * columns


# In[13]:


data.ndim                                         # no. of dimension 


# In[14]:


data.describe()


# In[ ]:





# In[ ]:




