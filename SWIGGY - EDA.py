#!/usr/bin/env python
# coding: utf-8

# # Problem statement

# The online food ordering market includes foods prepared by restaurants, prepared by
# independent people, and groceries being ordered online and then picked up or delivered. The
# first online food ordering service, World Wide Waiter (now known as Waiter.com), was
# founded in 1995. Online food ordering is the process of ordering food from a website or other
# application. The product can be either ready-to-eat food or food that has not been specially
# prepared for direct consumption.
# 

# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
from PIL import Image


# In[8]:


df = pd.read_csv("swiggy.csv")


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df.info()


# In[12]:


df.shape


# In[13]:


df.isnull().sum()


# In[14]:


sns.heatmap(df.isnull(),yticklabels=False ,cbar =False,cmap = 'Blues')


# In[15]:


plt.figure(figsize = (10,5))
sns.histplot(data = df,x = 'Rating',color = 'Red',bins = 5)
plt.title("Ratings")
plt.xlabel("Rating")
plt.ylabel("count")
plt.show()


# observation 
# 
# 1. we can conclude that maximum no of rating that is given is 4.1

# In[ ]:





# In[16]:


plt.figure(figsize = (20,10))
sns.histplot(data = df,x = 'Cost_for_Two',bins = 5,color = 'Green')
plt.title("Cost_for_Two")
plt.xlabel("Cost")
plt.ylabel("count")
plt.show()


# In[17]:


round(df['Cost_for_Two'].mean(),2)


# In[18]:


plt.figure(figsize = (10,5))
plt.hist(data = df,x = 'Cost_for_Two',color = 'orange',bins = 5)
plt.title("histogram of Fixed")
plt.xlabel("Cost")
plt.ylabel("count")
plt.vlines(df['Cost_for_Two'].mean(), ymin = 0, ymax = 50, colors='blue', label='Mean')
plt.show()


# we can conclude from the figure The average cost for two people is arond 320

# In[19]:


df[['Shop_Name','Cuisine']].value_counts().head()


# we can conclude that Italian,American has highest no of Cuisines 

# In[20]:


df.head()


# In[21]:


df.Cost_for_Two.unique()


# In[22]:


#shops that minimum cost and maximum rating


# In[23]:


df.sort_values(by = 'Rating',ascending = False).head()


# In[24]:


df.sort_values(by = 'Cost_for_Two').head()


# # observation

# 1. Most liked Foods is from Khicdi Experiment
# 2. Ice cream Business is more in Koramangala
# 3. Minumum cost for two is from Tandoori Merchant	

# # Area wise Analysis

# In[25]:


df.Location.unique()


# In[26]:


loc=[]
def dis():
    for i in df.Location:
        loc.append(i.split(",")[-1])
    return loc
l=dis()
l


# In[27]:


a = set(l)
len(a)


# In[28]:


a


# In[29]:


df["Area"] = l
df


# In[30]:


Koramangala = df[df["Area"] == ' Koramangala']


# In[31]:


Koramangala


# In[32]:


Koramangala.describe()


# In[33]:


sns.histplot(Koramangala['Cost_for_Two'],bins = 15)


# Area Jayanagar

# In[34]:


Jayanagar = df[df["Area"] == ' Jayanagar']
Jayanagar


#  Area  HSR

# In[35]:


HSR = df[df["Area"] == ' HSR']
HSR


# In[36]:


sns.histplot(HSR['Cost_for_Two'],bins = 10)


# In[37]:


BTM = df[df["Area"] == ' HSR']
BTM


# In[38]:


sns.histplot(BTM['Cost_for_Two'],bins= 10)


# In[ ]:





# # Revenue Area wise

# In[39]:


Revenue = {}
Revenue['BTM']=BTM['Cost_for_Two'].sum()
Revenue['HSR']=HSR['Cost_for_Two'].sum()
Revenue['Jayanagar']=Jayanagar['Cost_for_Two'].sum()
Revenue['Koramangala']=Koramangala['Cost_for_Two'].sum()

re = Revenue.values()
city = Revenue.keys()

Revenue = pd.DataFrame()
Revenue['Revenue']=re
Revenue['City']=city
Revenue


# In[40]:


sns.barplot(x = Revenue['City'], y = Revenue['Revenue'],data = Revenue)


# In[41]:


sns.countplot(df.Area)
plt.title("No of shops")


# Conclusion
# 
# 1. Area Koramangala has highest no of Revenue 
# 2. Area Koramangala has highest no of shops

# # Cuisine analysis 

# In[42]:


df.Cuisine


# In[43]:


C = df.Cuisine.unique()
C


# In[44]:


cui = []
for i in C :
    e = i.split(",")
    for j in e:
        if j[0]==" ":
            j=j[1:]
        if j not in cui:
            cui.append(j)
cui


# In[45]:


len(cui)


# In[46]:


dict_cuisine = {}
for i in df['Cuisine'].unique():
    Cuisines_Lists = i.split(',')
    for cuisine in Cuisines_Lists:
        cuisine = cuisine.lstrip(" ")
        if cuisine in dict_cuisine:
            dict_cuisine[cuisine] = dict_cuisine[cuisine]+1
        else:
            dict_cuisine[cuisine]=1
            
print(dict_cuisine)
print()        


# In[47]:


Cuisine = dict_cuisine.keys()
freq = dict_cuisine.values()


# In[48]:


df_cuisine = pd.DataFrame()


# In[49]:


df_cuisine['Cuisine'] = Cuisine
df_cuisine['count'] = freq


# In[50]:


df_cuisine


# In[51]:


plt.figure(figsize = (15,15))

sns.barplot(x = df_cuisine['Cuisine'],
            y = df_cuisine['count'] ,
           data = df_cuisine)

plt.xticks(rotation = 90,)
plt.title("Cuisines overall analysis(Bangalore)",fontweight = 'bold')
plt.xlabel('Cuisine')
plt.ylabel('Count')
plt.show()


# In[52]:


df_cuisine.sort = df_cuisine.sort_values(by = 'count',ascending  = False)


# In[53]:


df_cuisine.sort.head(10)


# In[54]:


plt.pie(df_cuisine.sort['count'],labels= df_cuisine.sort['Cuisine'],autopct = '%.2f%%')
plt.show()


# # Conclusion

# 1. As we see from the above analysis Chinese has Hiighest no of cuisines
# 2. we can also infer that People are fond of these Chinese

# # Cuisines Area Wise Analysis

# In[55]:


BTM_cuisine = BTM['Cuisine']


# In[56]:


BTM_dict = {}
for i in BTM_cuisine:
    k = i.split(',')
    for j in k:
        j = j.lstrip(" ")
        if j in BTM_dict:
            BTM_dict[j] = BTM_dict[j]+1
        else:
            BTM_dict[j]=1
            
print(BTM_dict)
print()        


# In[57]:


cuisine_BTM = BTM_dict.keys()
freq_BTM = BTM_dict.values()
dict_BTM = {
    "Cuisine" : cuisine_BTM,
    "Count" : freq_BTM
}


# In[58]:


BTM_cuisine = pd.DataFrame(dict_BTM)


# In[59]:


BTM_cuisine


# In[60]:


plt.figure(figsize = (15,15))

sns.barplot(x = BTM_cuisine['Cuisine'],
            y = BTM_cuisine['Count'] ,
           data = df_cuisine)

plt.xticks(rotation = 90,)
plt.title("Cuisines analysis(BTM)",fontweight = 'bold')
plt.xlabel('Cuisine')
plt.ylabel('Count')
plt.show()


# In[61]:


Cu_BTM = BTM_cuisine.sort_values(by= "Count",ascending  = False)


# In[62]:


Cu_BTM


# In[64]:


plt.savefig("cuisine_analysis.png")
plt.show()


# In[ ]:




