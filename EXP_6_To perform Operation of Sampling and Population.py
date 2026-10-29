#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Exp :- 6


# In[17]:


#Aim: To perform Operation of Sampling and Population


# In[18]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:-07-08-2026


# In[19]:


import pandas as pd


# In[20]:


import os


# In[21]:


os.getcwd()


# In[22]:


os.chdir("C:\\Users\\USER\\Desktop")


# In[23]:


data=pd.read_csv("heart.csv")


# In[24]:


data.head()


# In[25]:


data.tail()


# In[26]:


data.describe()


# In[27]:


data.info()


# In[28]:


data.columns


# In[29]:


list(data.columns)


# In[30]:


age_above_60=data[data["age"]>60]
print(age_above_60)


# In[31]:


print(len(age_above_60))


# In[ ]:





# In[ ]:




