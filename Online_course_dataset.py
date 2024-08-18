import pandas as pd
import numpy as np
df=pd.read_csv('online_course_engagement_data.csv')
print(df)
print(df['CourseCategory'].head(100))
df=pd.set_option('display.max_rows',9000)
print(df)
#print(df.sort_values('NumberOfVideosWatched'))
print(df.loc[:,'UserID'])
print(df.loc[[10,12],['UserID','NumberOfVideosWatched']])
print(df.isnull())