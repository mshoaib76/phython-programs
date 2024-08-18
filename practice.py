#Read json file
import numpy as np
import pandas as pd 
df=pd.read_json('1mb.json')
print(df)
print(df.info())
print(df.drop([1,2,4,5,6,7],inplace=True)) 

df.reset_index(drop=True) #True mean it drop the values and don't show anyother index row
print(df)
print(df.loc[:,'name'])
print(df.loc[[10,12],['name','address']])
print(df['name'].value_counts(dropna=False))  #it counts the names and dropna mean it drop all NAN values
print(df.iloc[0:5])
df.loc[:,'name']='elon musk'
print(df.head())


 
