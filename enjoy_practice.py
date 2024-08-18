#pip install openpyxl
import  numpy as np
import  pandas as pd
khan=pd.DataFrame(np.random.rand(200,5))
print(khan.info())#info means it tell us the all information about the file
#print(khan)
#print(khan.loc[(khan[1]<0.3)])
bb=khan.drop([0,1,2,3,4,5])
#print(bb)
print(bb.reset_index(drop=True)) #if we we to reset the index it show another indexing value instead of setting the original index that's why we use the drop=True

cc=bb.head(3)
cc.columns=['first','second','third','fourth','fifth']
print(cc.loc[:,['first']])=='khan'
cc.index=['phela','dosra','tisra']
print(cc)

df=pd.read_excel('world_population_excel_workbook.xlsx')
print(df['Rank'].value_counts(dropna=False))  #it counts the all values we use dropna it mean it ignore all duplicate values

df.index=np.arange(10,244)
ss=df.loc[200]=='Country'
print(ss)
print(df)
#df.columns=list('ABCDFGTREWQYUIOPM') _---->17 colums
#print(df)
print(df.drop_duplicates(subset=[1],keep=False))
#print(df.loc[[100 ,65],['Rank ','World Population']])
#print(df.head(50))
df=pd.set_option('display.max_rows',50)
#print(df)