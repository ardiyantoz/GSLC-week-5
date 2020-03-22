#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np
import seaborn as sb
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# In[12]:


listData = pd.read_csv("listings.csv")
print(listData.dtypes)
print(listData.isna().values.any())


# In[22]:


newcontinuousData = listData[["latitude","longitude","price","number_of_reviews","reviews_per_month","calculated_host_listings_count","availability_365"]]
newdiscreteData = listData[["minimum_nights"]]

print("{}".format(newdiscreteData.head()))
print("{}".format(newcontinuousData.head()))
                            


# In[32]:


print("Continuous: \nmean :\n{}".format(newcontinuousData.mean()))
print("\nvariants :\n{}\n".format(np.var(newcontinuousData)))

print("Discrete : \nmean :\n{}".format(newdiscreteData.mean()))
print("\nvariants :\n{}\n".format(np.var(newdiscreteData)))


# In[ ]:




