#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv(r'C:\Users\ASUS\OneDrive\Desktop\Project_DataAnalyst\Python project\Python_ForestFire_Analysis\amazon_forestfire.CSV')


# In[3]:


data


# # 1. Display Top 5 Rows of The Dataset

# In[4]:


data.head(5)


# # 2. Check Last 5 Rows

# In[5]:


data.tail(5)


# # 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)

# In[8]:


data.shape


# # 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement

# In[9]:


data.info()


# # 5. Check For Duplicate Data and Drop Them
# 

# In[14]:


data[data.duplicated()]


# # 6. Check Null Values In The Dataset

# In[16]:


data.isnull().sum()


# # 7. Get Overall Statistics About The Dataframe

# In[17]:


data.describe()


# # 8. Rename Month Names To English

# In[18]:


data.columns


# In[23]:


data['new_month']=data['month'].map
({
    'Janeiro': 'Jan',
    'Fevereiro': 'Feb',
    'Março': 'Mar',
    'Abril': 'Apr',
    'Maio': 'May',
    'Junho': 'Jun',
    'Julho': 'Jul',
    'Agosto': 'Aug',
    'Setembro': 'Sep',
    'Outubro': 'Oct',
    'Novembro': 'Nov',
    'Dezembro': 'Dec'
})


# In[22]:


data.head(1)


# # 9. Total Number of Fires Registered

# In[26]:


data.value_counts('number')


# # 10. In Which Month Maximum Number of Forest Fires Were Reported?

# In[27]:


data.columns


# In[28]:


data.groupby('month')['number'].max()


# # 11. In Which Year Maximum Number of Forest Fires Was Reported?

# In[29]:


data.columns


# In[32]:


data.groupby('year')['number'].max()


# # 12. In Which State Maximum Number of Forest Fires Was Reported?
# 

# In[34]:


data.groupby('state')['number'].max()


# # 13. Find Total Number of Fires Were Reported In Amazonas

# In[35]:


data.columns


# In[43]:


data[data['state']=='Amazonas']['number'].sum()


# # 14. Display Number of Fires Were Reported In Amazonas (Year-Wise)

# In[57]:


data1=data[data['state']=='Amazonas']
data2= data1.groupby('year')['number'].sum().reset_index()
data2


# # 15. Display Number of Fires Were Reported In Amazonas (Day-Wise)

# In[58]:


data.columns


# In[64]:


data3=data[data['state']=='Amazonas']
data4= data3.groupby('date')['number'].sum().reset_index()
data4


# # 16. Find Total Number of Fires  Were Reported In 2015 And Visualize Data Based on Each ‘Month’

# In[65]:


data.columns


# In[76]:


data[data['year']==2015]['number'].sum()


# In[89]:


sns.barplot(x='month',y='number',data=data)
plt.figure(figsize=(85,55))


# # 17. Find Average Number of Fires Were Reported From Highest to Lowest (State-Wise)
# 

# In[80]:


data.columns


# In[93]:


data.groupby('state')['number'].mean().sort_values(ascending = False).reset_index()


# # 18.  To Find The State Names Where Fires Were Reported In 'dec' Month

# In[95]:


data.columns


# In[96]:


data.head(1)


# In[106]:


data[data['month']=='Dezembro']['state'].reset_index()


# In[ ]:




