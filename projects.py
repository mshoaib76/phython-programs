import numpy as np
import pandas as pd
#import matplotlib as mt 
users=pd.read_csv('online_course_engagement_data.user.csv')
print(users)
print(users.head(25))
print(users.tail(10))
print(users.shape[1])
print(users.columns)
print(users.shape[0])
users.index=np.arange(100, 9100)
print(users)
print(users.dtypes)
print(users['CourseCategory'])
print(users.CourseCategory.value_counts())
print(users.describe())
print(users.describe(include='all'))
print(users.CourseCategory.describe())
print(users.NumberOfVideosWatched.mean())
print(users.NumberOfVideosWatched.value_counts().tail())
data_array=users['NumberOfVideosWatched']
mean=np.mean(data_array)
median=np.median(data_array)
STD=np.std(data_array)
print("Mean is :",mean)
print("Median is ",median)
print('Standard Deviation is :',STD)
print(users.NumberOfVideosWatched.max())
print(users.NumberOfVideosWatched.min())
#extra steps
print(users.loc[users['CourseCategory']=='Science'])
#print(users[users['CourseCategory'].isin(['Health','Arts'])])
users.loc[users['CourseCategory']=='Science','CourseCategory']='OOP'
print(users.head(30))
ss=users['TimeSpentOnCourse'].nlargest(3)
print(ss)
dataset=users[users['CourseCategory'].isin(['Health','Arts'])]
print(dataset)
dataset2=users[~users['CourseCategory'].isin(['Health','Arts'])]
print(dataset2) 
print(dataset['NumberOfVideosWatched'].hist())



