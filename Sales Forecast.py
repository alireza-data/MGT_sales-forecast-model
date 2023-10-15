#!/usr/bin/env python
# coding: utf-8

# In[48]:


#Sales analysis & Forcast
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk(r'C:\Users\engra\Desktop\Python training\sales.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
    


# In[49]:


import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[50]:


df = pd.read_csv(r'C:\Users\engra\Desktop\Python training\sales.csv')
df.head()


# In[51]:


X = df.iloc[:, :-1].values    # Features => Time => Independent Variable
y = df.iloc[:, -1].values     # Target => Sales => Dependent Variable

X


# In[52]:


y


# In[55]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)


# In[56]:


predictions = model.predict(X_test)
predictions


# In[57]:




y_test


# In[62]:


plt.scatter(X_train, y_train, color='red')
plt.xlabel('Time / Month')  # Replace 'X-axis label' with your desired x-axis label
plt.ylabel('Sales / Unit')  # Replace 'Y-axis label' with your desired y-axis label

plt.plot(X_train, model.predict(X_train))


# In[ ]:




