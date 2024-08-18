import re

import pandas as pd
import numpy as np
df=pd.read_csv('online_course_engagement_data.csv')
print(df)
print(df.drop([1,2,3,4,5,6,7,8,9]))
print(df.loc[[10,11,12,13,14,15],['CourseCategory','DeviceType']])
print(df.sort_values(['UserID'],ascending=False))
#df['SUm']=df['DeviceType']+df['CourseCompletion']
#print(df.head(5))
print(df.drop(columns=['UserID'],inplace=False))
print(df.loc[df['UserID']=='khn'])
#it works for only one but we can can this syntex for two values find
# in two colums (below syntex)
#print(df.loc[(df['CourseCategory']=='Arts')&(df['DeviceType']==1)])
#print(df(['TimeSpentOnCourse'] >9850))
#find the word
print(df.loc[df['CourseCategory'].str.contains('Arts',regex=True)])
#find the two words and also we use small words by using (flags=re.I) if the word is capital
print(df.loc[df['CourseCategory'].str.contains('programming|arts',flags=re.I,regex=True)])
#find one word if we use small word
print(df.loc[df['CourseCategory'].str.contains('programming',flags=re.I,regex=True)])
#find the word with startind,endind,and in between  * means 0 to any other word
print(df.loc[df['CourseCategory'].str.contains('r[a-z]*',flags=re.I,regex=True)])
#print(df.loc[df(['TimeSpentOnCourse'] >9850)])
#change the specific word
df=df.loc[df['CourseCategory']=='Science ','CourseCategory']='OOP'
print(df)