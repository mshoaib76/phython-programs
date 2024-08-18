import pandas as pd  #it will print the first  5 rows and all columns and than print 5 rows and all colums and so on 
import numpy as np
for df in pd.read_csv('top_intelligent_people_in_the_world_5000.csv',chunksize=5):
    print('Dataframe')
    print(df)
    