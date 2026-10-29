#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Exp :- 9


# In[ ]:


# Aim : To Perform the Operation to Find Central Tendency of measures Mean Median Mode


# In[ ]:


#Name:krushnali raut
#Roll:49
#sec:C
#subject:DSS
#Date:31-07-2026


# # Central Tendency of measures Mean Median Mode And Measures of Dispertion Std , Varience 

# In[2]:


age=[22,21,20,20,21,21,21,21,20,20,22,20,22,21,22,22,22,22,22]


# In[3]:


age


# In[4]:


import statistics


# In[5]:


Mean=statistics.mean(age)


# In[6]:


Mean


# In[7]:


Median =statistics.median (age)


# In[8]:


Median


# In[9]:


Mode= statistics.mode (age)


# In[10]:


Mode


# In[11]:


import numpy as np
x=np.array([1,2,3,4,5,6,7,2,6,2,1,4,2,2,6])


# In[12]:


x


# In[13]:


print(np.mean(x))


# In[14]:


print(np.median(x))


# In[1]:


print(np.mode(x))


# In[16]:


from scipy import stats


# In[17]:



print(stats.mode(x))


# In[18]:


print(np.std(x))


# In[19]:


print(np.var(x))


# In[ ]:




