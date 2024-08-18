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
