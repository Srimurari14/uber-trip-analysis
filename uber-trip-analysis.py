#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("...\\Desktop\\\uber-raw-data-sep14.csv")

df.shape

df.head()

df.tail()

df.info()

df.describe()

df.isnull().sum()/df.shape[0]*100         #percent of nullvalues

df['Date/Time'].value_counts()

df.iloc[:,1:3].value_counts()

plt.scatter(df['Lon'],df['Lat'])
plt.show()                      #rides per location

df['Base'].value_counts()

plt.hist(df.Base,width= 0.25,bins=30)
plt.show()

df['Date/Time']= pd.to_datetime(df['Date/Time'])

df['Date/Time'].head()

df["Day"]=df["Date/Time"].apply(lambda x: x.day)
df["Hour"]=df["Date/Time"].apply(lambda x: x.hour)
df["Weekday"]=df["Date/Time"].apply(lambda x: x.weekday())

df.head()

df['Day'].value_counts()

plt.hist(df.Day,width= 0.6, bins= 30)
plt.show()                        #rides per day

df['Weekday'].value_counts() 

plt.hist(df.Weekday,width= 0.6, bins= 30)
plt.show()                                #rides by day in a week

df['Hour'].value_counts()

plt.hist(df.Hour,width= 0.6, bins= 30)
plt.show()                         #rides by hour

