import numpy as np
import  pandas as pd
df=pd.DataFrame(np.random.rand(324,5))
print(df)
# df.columns=list("ABCDF")
# print(df)
# print(df.loc[[1,2],['C','D']])  #print 1 and 2 row and C and D colums ----for loc[]<--must use this
# print(df.loc[(df['A']<0.2) & (df['C']>0.5)]) #print all rows which values less than 0.2
# print(df.iloc[[1,2],[2,3]]) #iloc means we can target the index if the name change of the values
# df.head(3)
# print(df.drop(['A','B'],axis=1,inplace=True)) #drop mean ignore if we use inplace word than it permently drop the values
# print(df.drop([1,3],axis=0,inplace=True))
# print(df.reset_index(drop=True,inplace=True)) #reset the unset index (dropna mean it drop all NAL data)
# #print(df['D'].isnull())   #isnull means it check if any value is zero
# #print(df.loc[:,['B']]==32)
# #print(df['D']==None)

print(df.to_csv('friends.csv'))
Noted=pd.read_csv("Noted.csv")
Noted.columns=list(['first ''second' ' third'])
Noted.index=['A','B','C']
print(Noted)
#print(Noted.isnull())
#print(Noted.drop(['first'],axis=1,inplace=True))







