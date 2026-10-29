#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exp :- 12


# In[2]:


# Aim : To perform Operation of KNN classifiers 


# In[3]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:


# In[4]:


import pandas as pd                                                                # Importing the Libraries
import numpy as np 


# In[5]:


import os                                                                          # Data acquisitionuing Pandas


# In[6]:


os.getcwd()


# In[7]:


os.chdir("C:\\Users\\USER\\Desktop")


# In[32]:


data=pd.read_csv("Iris.csv")  


# In[33]:


data.head()


# In[34]:


data.tail()


# In[35]:


data.info()


# In[36]:


data.describe()


# In[37]:


data.shape


# In[38]:


data.size


# In[39]:


data.ndim


# In[40]:


data.isna()


# In[41]:


data.isna().any()                                                                        # Data preprocessing _ data cleaning _ missing value treatment


# In[42]:


data.isna().sum()


# In[50]:


x=data.drop("Species", axis=1)                                                           #Independent and Dependent Variables
y=data["Species"]


# In[51]:


from sklearn.model_selection import train_test_split                                     #splitting the data into training and testing data sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=42)


# In[52]:


from sklearn.neighbors import KNeighborsClassifier                                       # KNN Classifier
from sklearn.metrics import accuracy_score  


# In[53]:


knn=KNeighborsClassifier()


# In[54]:


knn.fit(x_train, y_train)


# In[55]:


y_pred2=knn.predict(x_test)


# In[56]:


accuracy = accuracy_score(y_test, y_pred2)


# In[57]:


accuracy


# In[ ]:





# In[ ]:




