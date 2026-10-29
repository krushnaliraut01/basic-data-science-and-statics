#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exp :- 10


# In[2]:


# Aim : To perform Operation Simple Linear Regression for Salary Data(SLR)


# In[3]:


#Name:Himanshu Gulhane
#Roll:21
#sec:C
#subject:DSS
#Date:


# In[71]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[72]:


import os


# In[73]:


os.getcwd()


# In[74]:


os.chdir("C:\\Users\\USER\\Desktop")


# In[75]:


data=pd.read_csv("Salary.csv")


# In[76]:


data.head()


# In[77]:


data.tail()


# In[78]:


data.head(30)


# In[79]:


data.info()


# In[80]:


data.describe()


# In[81]:


data.shape


# In[82]:


data.size


# In[83]:


data.ndim


# In[84]:


data.isnull().sum()


# In[85]:


#Independent and Dependent Variables
#x = data['YearsExperience']
#y = data['Salary']


# # Independent and Dependent Variables

# In[86]:


X=data.drop('Salary',axis=1)


# In[87]:


X.head()


# In[88]:


y=data.Salary


# In[89]:


y.head()


# In[90]:


from sklearn.model_selection import train_test_split


# In[91]:


X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.30)


# In[92]:


print(X_train.shape)


# In[93]:


X_test.shape


# In[ ]:





# # Model Fitting

# In[94]:


from sklearn.linear_model import LinearRegression
LR=LinearRegression()
LR.fit(X_train,y_train)


# In[95]:


#Assigning Coefficient (slope) to m
m = LR.coef_


# In[96]:


print("Coefficient  :" , m)


# In[97]:


#Assigning Y-intercept to a
c = LR.intercept_


# In[98]:


print("Intercept : ", c)


# # y=mx+c

# # Prediction

# In[99]:


y_pred=LR.predict(X_test)


# In[100]:


y_pred


# In[101]:


y_test


# # Evaluation metrics

# In[102]:


from sklearn import metrics


# Accuracy

# In[103]:


Accuracy = LR.score(X_test, y_test)
Accuracy


# MAE

# In[104]:


print(metrics.mean_absolute_error(y_test,y_pred))


# MSE

# In[105]:


print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))


# RMSE

# In[106]:


rmse = np.sqrt(metrics.mean_squared_error(y_test,y_pred))
print("RMSE:", rmse)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




