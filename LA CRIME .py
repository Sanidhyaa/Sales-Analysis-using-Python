#!/usr/bin/env python
# coding: utf-8

# In[106]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud,STOPWORDS


# In[6]:


df=pd.read_csv(r'C:\Users\Welcome\Desktop\abcd.csv')


# In[7]:


df.head(2)


# # DATA CLEANING 

# In[8]:


df=df.fillna({"Cross Street":"unknown"})


# In[9]:


df=df.drop(["Crm Cd 2","Crm Cd 3","Crm Cd 4"],axis=1)


# In[10]:


df.head(2)


# In[11]:


df.isnull().sum()


# # Pandas Profiling

# In[12]:


import ydata_profiling as prf


# In[13]:


data_report=prf.ProfileReport(df)


# In[131]:


data_report


# In[14]:


df.head(5)


# In[16]:


f1=sns.countplot(x="AREA NAME",data=df,palette="Set1")
sns.set(rc={"figure.figsize":(20,5)})
sns.set_style("whitegrid",{"axes.grid":"False"})
for bar in f1.containers:
    f1.bar_label(bar)
plt.show()


# In[17]:


top_10_crimes=df["Crime Code Description"].value_counts()[0:10]


# In[31]:


plt.figure(figsize=(6,6))
f2=plt.barh(list(df["Crime Code Description"].value_counts()[0:10].keys()),list(df["Crime Code Description"].value_counts()[0:10]),color="r")
plt.xlabel("COUNT")
plt.ylabel("Crime Description")
plt.title("TOP 10 Most Crime Occurence")
plt.grid(False)
plt.show()


# In[37]:


df["Weapon Desc"].value_counts()[0:5]


# In[67]:


f3=sns.barplot(x=list(df["Weapon Desc"].value_counts().keys()[0:5]),y=list(df["Weapon Desc"].value_counts()[0:5]))
sns.set(rc={"figure.figsize":(25,10)})
sns.set_style("whitegrid")
for i in f3.containers:
    f3.bar_label(i)
plt.show()


# In[71]:


#Lets See most crimes that have occured in the Central Region because central region is ont= the top of Criminal City list.
d1=df[df["AREA NAME"]=="Central"]


# In[74]:


d1["Crime Code Description"].value_counts()[0:5]


# In[83]:


plt.figure(figsize=(10,5))
plt.barh(list(d1["Crime Code Description"].value_counts()[0:5].keys()),list(d1["Crime Code Description"].value_counts()[0:5]),color="g")
plt.xlabel("Count")
plt.ylabel("Crimes")
plt.title("Top Crimes in Central Region")
plt.show()


# In[86]:


df.columns


# In[139]:


word_cloud = WordCloud(
       width=3000,
       height=2000,
       random_state=1,
       background_color="salmon",
       colormap="Pastel1",
       collocations=False,
       stopwords=STOPWORDS,
       ).generate(str(df["Premis Desc"].str.split()))


# In[140]:


plt.imshow(word_cloud)
plt.axis("off")
plt.show()


# In[137]:


df["Premis Desc"].str.split()


# In[143]:


df["Premis Desc"].value_counts()[0:5] # MOST CRIMES HAVE BEEN OCCURED ON THE STREETS OF LA


# In[104]:





# In[93]:


df["Vict Age"].value_counts()[1:6] #MOST VICTIMS LIE IN THE AGE GROUP OF 25-35 


# In[ ]:


CONCLUSION
FROM THE ABOVE ANAYLSIS IT IS CLEAR THAT MOST OCCURENCES HAVE OCCURED ON THE STREET WHICH CAN ALSO BE SEEN THROUGH THE
CRIMES OCCURED CHART THAT HIGHEST OCCURED CRIME IS VEHICLE STOLEN AND MOST USED WEAPON IS FIST WHICH IS NEEDED FOR THIS.

