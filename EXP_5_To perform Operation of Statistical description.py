#!/usr/bin/env python
# coding: utf-8

# In[37]:


#Exp :- 5


# In[38]:


#Aim: To perform Operation of Statistical description


# In[39]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:-07-2006


# In[40]:


import pandas as pd


# In[1]:


import os


# In[2]:


os.getcwd()


# In[3]:


os.chdir("C:\\Users\\USER\\Desktop")


# In[86]:


data=pd.read_csv("Heart.csv")


# In[87]:


data.head()


# In[88]:


data.tail()


# In[89]:


data.info()


# In[90]:


data.describe()


# In[91]:


data.mean()


# In[92]:


data.median()


# In[93]:


data.std()


# In[94]:


data.var()


# In[ ]:





# In[ ]:





# In[ ]:




