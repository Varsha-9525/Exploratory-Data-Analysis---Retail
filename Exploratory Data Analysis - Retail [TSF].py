#!/usr/bin/env python
# coding: utf-8

# # Name - Varsha Dhamdhere
# 
# # Data Science and Business Analytics Intern @ The Sparks Foundation 
# 
# ## Task-3: Exploratory Data Analysis - Retail
# 
# 

# 
# #### Problem Statement -:
# - Perform "Exploratory Data Analysis" on the dataset "SuperStore"
# - As a business manager,try to find out the weak areas where you can work to make more profit.
# - What all business problems you can derive by exploring the data?
# - #### Dataset- [ https://bit.ly/3i4rbWl ]
# 
# 

# In[91]:


# Importing Libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[49]:


# Importing Dataset
df = pd.read_csv("C:\\Users\\H\\Downloads\\SampleSuperstore.csv")
df.head()


# In[50]:


df.tail()


# In[51]:


# shape for dimension of dataset
df.shape


# In[52]:


# Description
df.describe()


# In[53]:


# Check if there is any missing value/null value
df.isnull().sum()


# In[54]:


print('Total no. of null values -',df.isnull().sum().sum())


# In[55]:


# Check datatype in dataset
df.dtypes


# In[56]:


df.columns


# In[57]:


# Checking the dataset for any duplicate value. If any duplicate value is present we'll drop it.
df.duplicated().sum()


# In[58]:


# Drop duplicate values
df.drop_duplicates()


# In[59]:


# New shape
df.shape


# #### Feature Selection

# - Removing unnecessary variables
# 

# In[60]:


# Deleting column 'Postal Code'
df.drop(columns='Postal Code', axis=1, inplace= True)


# In[61]:


df.info()


# ## Data Visualization

# In[62]:


plt.figure(figsize=(19,8))
plt.bar('Sub-Category','Category',data=df)
plt.show()


# In[63]:


print(df['State'].value_counts())


# In[64]:


import seaborn as sns

plt.figure(figsize=(16,8))
sns.countplot(x= df['State'])
plt.xticks(rotation= 90)
plt.show()


# In[65]:


print(df['Sub-Category'].value_counts())


# In[66]:


plt.figure(figsize=(16,8))
sns.countplot(x= df['Sub-Category'])
plt.xticks(rotation=90)
plt.show()


# In[67]:


# Correlation of dataset
df.corr()


# In[68]:


df.cov()


# In[69]:


# Heatmap to check Collinearity between sales,quantity,discount,profit
plt.figure(figsize=(15,7))
sns.heatmap(df.corr(),annot=True)
plt.show()


# In[70]:


sns.countplot(x=df['Segment'])


# In[71]:


sns.countplot(x=df['Region'])


# In[72]:


sns.countplot(x=df['Category'], data=df)


# In[73]:


plt.figure(figsize=(20,10))
sns.countplot(x=df['Sub-Category'],data=df)
plt.show()


# In[74]:


plt.figure(figsize=(20,10))
sns.barplot(x=df['Sub-Category'],y=df['Profit'])


# In[75]:


plt.figure(figsize=(15,7))
sns.lineplot('Discount','Profit', data=df, color='g', label='Discount')
plt.legend()


# In[76]:


df.hist(bins=40,figsize=(20,15))
plt.show()


# In[77]:


figsize=(20,10)
sns.pairplot(df, hue='Sub-Category')


# In[78]:


figsize=(20,10)
sns.pairplot(df, hue='Category')


# In[79]:


figsize=(20,10)
sns.pairplot(df, hue='Region')


# In[80]:


figsize=(20,10)
sns.pairplot(df, hue='Segment')


# In[81]:


# Sum the sales,profit,discount,quantity according to every state of region and also according to Sub-Categories sales
grouped=pd.DataFrame(df.groupby(['Ship Mode','Segment','Category','Sub-Category','State','Region'])['Quantity','Discount','Sales','Profit'].sum().reset_index())
grouped


# In[82]:


# sum, mean, min, max, count,median, standard deviation, variance of each states of Profit
df.groupby("State").Profit.agg(["sum","mean","min","max","count","median","std","var"])


# In[83]:


sales_profit = df.groupby("State")["Profit"].sum()
sales_profit


# In[84]:


# State wise Profit
plt.figure(figsize=(20,10))
sns.barplot(x=sales_profit.index, y=sales_profit.values)
plt.ylabel("Profit")
plt.xticks(rotation=90)
plt.show()


# In[85]:


# State wise Sales
sales = df.groupby("State")["Sales"].sum()
sales.plot.bar(figsize=(20,10))


# In[86]:


# Sales and Profit Category wise

category = df.groupby("Category")["Profit", "Sales"].sum()
category.plot.bar(figsize=(20,10))


# In[87]:


# Sales and Profit Sub-Category wise

category = df.groupby("Sub-Category")["Profit", "Sales"].sum()
category.plot.bar(figsize=(20,10))


# In[88]:


# Sales and Profit Sub-Category wise

category = df.groupby("State")["Profit", "Sales"].sum()
category.plot.bar(figsize=(20,10))


# In[89]:


# Category vs Region

plt.figure(figsize=(20,10))
sns.countplot(x="Category", hue= "Region", data=df)
plt.xticks(rotation="vertical")
plt.plot()


# In[90]:


# Sub-Category vs. Region

plt.figure(figsize=(20,10))
sns.countplot(x="Sub-Category", hue= "Region", data=df)
plt.xticks(rotation="vertical")
plt.plot()


# ### Conclusion :
# - Profits and sales are highly correlated.
# 
# - There is no correlation between quantity and profit.
# 
# - In category, Furniture has large no. of sales but instead of making profit, it makes loss. So, there is need to limit the sales of Furniture.
# 
# - In sub-category, Tables has has large no. of sales but instead of making profit, it makes loss. So, there is need to limit the sales of Tables.
# 
# - States like Texas, Ohio has huge sales but it makes big loss. So, there is need to reduce the sales in these states.
# 
# - States like Michigan, Indiana, Virginia, Georgia makes good profit. So, sales can be increased in these states

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




