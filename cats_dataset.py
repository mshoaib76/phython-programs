#import necessary libraries 
import pandas as pd
import numpy as np
#import data set, assign variable 'users ' and use the 'user id' as index
users=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|', index_col='user_id')
#print firsy 25 rows
print(users.head(25))
#print the last 10 rows
print(users.tail(10))
#number of observations in the dataset
print(users.shape[0])
#Total numbers of colums
print(users.shape[1])
#print the name of colums
print(users.columns)
#Total numbers of colums
print(users.shape[1])
#print(users.columns.value_counts().sum())
#How the dataset indexed 
users.index=[np.arange(100,1043)]
print(users)
#print the datatypes
print(users.dtypes)
#print only occupation colums 
print(users['occupation'])
#what is the most frequient occupation
print(users.occupation.value_counts())
#summerize the Dataset
print(users.describe())
#summerize all the colums
print(users.describe(include='all'))
#summerize occupation colums
print(users.occupation.describe())
#what is the maen age of the users
print(users.age.mean())
#what is the age with least occurence ?
print(users.age.value_counts())
#max values
print(users.age.max())
print(users.zip_code.max())
#min values
print(users.age.min())
print(users.zip_code.min())



