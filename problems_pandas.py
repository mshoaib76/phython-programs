import pandas as pd 
import numpy as np
dict={
       'animal':['cat','cat','snake','dog','dog','cat','snake','dog','lion','lion'],
       'age':[2.5,3,0.5,np.nan,5,2,4.5,np.nan,7,3],
       'visits':[1,3,2,3,2,3,1,1,2,4],
       'priority':['yes','yes','no','yes','no','no','no','yes','yes','no'],   
}
labels=['a','b,','c','d','e','f','g','j','i','j']
df=pd.DataFrame(dict,index=labels)
df
      