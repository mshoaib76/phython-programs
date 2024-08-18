import pandas as pd 
import numpy as np
df=pd.read_json('1mb.json')
print(df)
pd.option_context('display.max_rows',6113)
print(df)
df.columns=df.columns.str.replace('name','Fullname')
print(df)
print(df.drop([1,2,3,4,5]))
df.reset_index(drop=True)
print(df)

