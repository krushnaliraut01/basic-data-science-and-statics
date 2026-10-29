#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exp :- 8


# In[2]:


#Aim:-To perform Operation of Data Visualization


# In[3]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:03-09-2026


# In[4]:


import numpy as np
from matplotlib import pyplot as plt


# In[5]:


x=np.arange(1,11)


# In[6]:


x


# In[7]:


y=2*x


# In[8]:


y


# In[9]:


plt.plot(x,y)
plt.title("Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


# In[10]:


plt.bar(x,y)
plt.title("Bar Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


# In[11]:


plt.scatter(x,y)
plt.title("scatter Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


# In[12]:


1 - 12
2-15
3-10
4-9
5-7
6-12
7-11
8-15
9-14
10-3


# In[13]:


R=(1,2,3,4,5,6,7,8,9,10)
M=(12,15,10,9,7,12,11,15,14,3)
plt.scatter(R,M)
plt.title("Unit Test marks")
plt.xlabel("Roll no")
plt.ylabel("Marks")
plt.show()


# In[14]:


R=(1,2,3,4,5,6,7,8,9,10)
M=(12,15,10,9,7,12,11,15,14,3)
plt.bar(R,M)
plt.title("Unit Test marks")
plt.xlabel("Roll no")
plt.ylabel("Marks")
plt.show()


# In[15]:


R = (1,2,3,4,5,6,7,8,9,10)
M = (12,15,10,9,7,12,11,15,14,3)

# Below 10 → Red, 10 or above → Green
colors = ['red' if marks < 10 else 'green' for marks in M]

plt.bar(R, M, color=colors)

plt.title("Unit Test Marks")
plt.xlabel("Roll No")
plt.ylabel("Marks")
plt.show()


# In[ ]:





# In[ ]:




