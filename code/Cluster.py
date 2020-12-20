#!/usr/bin/env python
# coding: utf-8

# In[3]:

#libraries need for the code
import numpy as np
import pandas as pd
from scipy import stats
import random


# In[4]:

#reading file
df = pd.read_csv("agaricus-lepiota.data", sep=',', header=None)


# In[5]:

#Checking for null values
print(df.isna().sum())
df.describe()


# In[6]:

#checking unique values according to dataset discription
for colname in df[[11]]:
    print("{} = {}".format(colname, len(df[colname].unique())))


# In[7]:


#to deal with '?' we replace it with NaN 
df = df.replace({'?':np.NaN})
print(df.isna().sum())


# In[8]:

#count no. of unique values in column 11
print(df[11].value_counts())


# In[9]:


#Now to deal with NaN we create a column to keep track of imputed variables and impute the variables with the mode of the values    

#add new column and replace it with binary variables if null then 1 else 0
df["11_imputed"] =   np.where(df[11].isnull(),1,0)

#Take mode in that vairable
Mode = df[11].mode()[0]

#Replace NaN values with mode in actual vairable
df[11].fillna(Mode,inplace=True)

    


# In[10]:

#again check for null values
print(df.isna().sum())


# In[11]:

#check for the changes
print(df[11].value_counts())


# In[12]:


#lets drop the class label as it should not be used in unsupervised learning algorithms
#lets drop the last column for now as we dont need it for our k-mode clustering
df2 = df.drop(columns=[0,'11_imputed'])
df2


# In[15]:

#Calculate Hamming Distance
def get_distance(x,c):
    return np.sum(np.array(x) != np.array(c), axis = 0)


# In[19]:

#Return Index for the random clusters
def random_clusters(k,n):
    dup = np.array([])
    while 1:
        ranIndex = np.random.randint(low=0, high=n, size=k)
        u, c = np.unique(ranIndex, return_counts=True)
        dup = u[c > 1]
        if dup.size == 0:
            break
    return ranIndex


# In[90]:


def kmodes(dataset, NumberOfClusters):
    #converting the df to numpy array for faster clustering
    n = len(dataset)
    d = len(dataset.columns)
    df_temp = dataset.to_numpy()
    addZeros = np.zeros((n, 1))
    df_temp = np.append(df_temp, addZeros, axis=1)
    
    #initializing cluster centres
    cluster = df_temp[random_clusters(NumberOfClusters,n)]
    print("\n The initial cluster centers: \n", cluster , "\n\n")
    
    #initializing empty array
    cluster2 = []
    
    #Assignment of observations to a cluster 
    for i in range(n):
        minDist = 9999999
        for j in range(NumberOfClusters):
            dist = get_distance(cluster[j,0:d],df_temp[i,0:d])
            if(dist < minDist):
                minDist = dist
                clusterNumber = j
                df_temp[i,d] = clusterNumber
                cluster[j,d] = clusterNumber
     
    #Compute new centroids by calculating the modes
    for j in range(NumberOfClusters):
        result =  np.where(df_temp[:,d] == j)
        mode = stats.mode(df_temp[result])
        cluster[j] = np.reshape(mode[0],(d+1)) 
    
    #Terminating criteria for iterations - if old modes != to new modes, we will keep finding clusters 
    while(cluster != cluster2):
        #Assign old modes with new modes
        cluster2 = cluster
        for i in range(n):
            minDist = 9999999
            for j in range(NumberOfClusters):
                dist = get_distance(cluster[j,0:d],df_temp[i,0:d])
                if(dist < minDist):
                    minDist = dist
                    clusterNumber = j
                    df_temp[i,d] = clusterNumber
                    cluster[j,d] = clusterNumber
                    
        for j in range(NumberOfClusters):
            result =  np.where(df_temp[:,d] == j)
            mode = stats.mode(df_temp[result])
            cluster[j] = np.reshape(mode[0],(d+1))
        
        #Stopping crieteria for the loop. if old modes = new modes, the break and stop,
        if np.array_equal(cluster,cluster2):
            break
            
    #convert back to pandas data frame        
    dataset3 = pd.DataFrame(df_temp)
    
    
    return dataset3


# In[97]:

#call kmodes clustering algorithm
cluster = kmodes(df2,20)


# In[98]:

#rename the last column for clusters
cluster = cluster.rename(columns ={22: "Cluster"} )

print("\n The final clusters: \n", cluster , "\n\n")


# In[99]:

#Export to dataframe to a csv file
cluster.to_csv("cluster.csv",index=False)
