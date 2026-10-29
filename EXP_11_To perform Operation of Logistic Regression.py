#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exp :- 11


# In[2]:


# Aim : To perform Operation of Logistic Regression


# In[3]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:


# In[4]:


import pandas as pd                        # Importing the Libraries
import numpy as np 


# In[5]:


import os                                   # Data acquisitionuing Pandas


# In[6]:


os.getcwd()


# In[7]:


os.chdir("C:\\Users\\USER\\Desktop")


# In[8]:


data=pd.read_csv("heart.csv")  


# In[9]:


data.head()


# In[10]:


data.tail()


# In[11]:


data.info()


# In[12]:


data.describe()


# In[13]:


data.shape


# In[14]:


data.size


# In[15]:


data.ndim


# In[16]:


data.isna()


# In[17]:


data.isna().any()                # Data preprocessing _ data cleaning _ missing value treatment


# In[18]:


data.isna().sum()


# In[19]:


x=data.drop("target", axis=1)   #Independent and Dependent Variables
y=data["target"]


# In[20]:


from sklearn.model_selection import train_test_split                                     #splitting the data into training and testing data sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=42)


# In[21]:


from sklearn.linear_model import LogisticRegression              #Logistic Regression


# In[22]:


log = LogisticRegression()
log.fit(x_train, y_train)


# In[26]:


y_pred = log.predict(x_test)


# In[27]:


from sklearn.metrics import accuracy_score 


# In[28]:


accuracy_score (y_test,y_pred)


# In[ ]:





# In[ ]:





# In[ ]:




