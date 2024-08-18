import numpy as np
import pandas as pd
df=pd.read_csv('Flavors.csv')
print()
print(df)
df.columns=df.columns.str.replace(" ",'_')
print(df)
print(df.drop(columns=['Liked']))
print(f"Mean of Total_Rating: ",df['Total_Rating'].mean())
print(df['Total_Rating'][30:40].interpolate(method='index'))
print(df.notnull().sum())
ss=df.Flavor.unique()
print(ss)
print(df.describe())
