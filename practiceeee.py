import pandas as pd 
import numpy as np
dict={
    'column a':['john','musk','empire','wiky','elon','bargarder','hicky'],
    'column b':[1,2,np.nan,5,np.nan,8.4,np.nan] ,
    'column c':[78,54,23,89,12,43,56],
    'column d':['londan','kingdam','Uk',np.nan,'londan','kingdam',np.nan],
    'column f':[np.nan,True,np.nan,False,np.nan,True,True]
}

df=pd.DataFrame(dict)
#df.columns=['name ','points ','age ','location ','liked ']
df.index=['1st','2nd','3rd','4th','5th','6th','7th']
print(df)

print(df.isna().sum())   #to check how much NAN values in a column

df.columns=df.columns.str.replace(' ','_')
# print(df.fillna(axis=0,method='ffill')) #ffill mean it fill the colums forword means it assign below value in the above 
# print(df.fillna(axis=0,method='bfill'))
# a=df['column_b'].mean()
# print(a)
# print(df['column_b'].fillna(a))
# for index,row in df.iterrows():  #print all data row by row means it print all colums of first row and than print all colums of second row

#     print(index,row)
print(df.loc[df.column_d=='londan'])  #print the terget value/string
print(df.fillna(axis=0,method='ffill').reset_index(drop=True).sort_values(['column_c'])) #sort the values 