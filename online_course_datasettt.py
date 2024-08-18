import pandas as pd
import numpy as np
df=pd.read_csv('online_course_engagement_data.csv')
print(df)
print(df['CourseCategory'].head(100))
 
#print(df.iloc[0:5])
print(df.drop([1,2,3,4,5]))
print(df.loc[df['Education']])