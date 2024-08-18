import numpy as np
import  pandas as pd

df=pd.read_csv('heart-disease.csv')
print(df)
print(df.describe(include='all'))
print(df['sex'].value_counts())
#df[(df['age']>30)&(df['age']<50)['sex']].value_counts()
#print(df['sex'].iloc[30:50].value_counts())
print(df[(df['age']>30) & (df['age']<50) & (df['chol']>200)]['sex'].value_counts())
print(df[(df['age']>30) & (df['age']<50)]['sex'].value_counts())
print(df[(df['age']>30) & (df['age']<50)]['sex'].value_counts())



