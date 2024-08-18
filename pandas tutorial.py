import pandas as pd
import numpy as np
df=pd.read_csv('Noted.csv')
print(df)
df.loc[1,'train']=2432



