import numpy as np
import  pandas as pd
dict ={
    'name':['jim','mary','kakulo'],
    'age':[70,50,40],
    'city':['kolkata','dehli','england']
}
df=pd.DataFrame(dict)
print(df)
df.loc[1,'age']=23
print(df)
print(df.to_csv('data.csv',index=False))
print(df.head(2))  #print only first two rows
print(df.tail(2))   #print only last 2 rows
print(df.describe()) # static analycis of floating
Noted=pd.read_csv('Noted.csv')
print(Noted)
Noted.index=['first','second','third']   #to write own name of indexs
print(Noted)
#Noted['speed'][0]=45
#print(Noted)
ser=pd.Series(np.random.rand(34))
print(ser)
Data_frame=pd.DataFrame(np.random.rand(234,5),index=np.arange(234))
print(Data_frame)
Data_frame[0][0]='jim'   #placing string in floating values
print(Data_frame.head()) #print only 4 5 lines
print(Data_frame.dtypes) #print int into object by placing string
print(Data_frame.index)  #print the total index
print(Data_frame.columns) #print the index
print(Data_frame.to_numpy())  #convert pandas into numpy array
print(Data_frame.sort_index(axis=0,ascending=False)) #print the reversing index (asceding must write to reverse the numbers)
Data_frame.columns=list("ABCDE")   #replaceing the names with ABCDE
print(Data_frame.head(2))  #print the only first two rows


