import pandas as pd 
import numpy as np
df=pd.read_csv('online_course_engagement_data.csv',sep='|',index_col='users')
print(df)