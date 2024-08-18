import pandas as pd 
import numpy as np
df=pd.read_csv('ecommerce_sales_analysis.csv')

print(df)
print(df.sales_month_8.nlargest(1))
#lambda :
"""
  lambda ara a way to define function without actullly defining them
  it means we can use condtions and adjust values own our choice 
"""
def checkfun(x):
    if x<300:
        return 'lessthan300'
    elif x<500:
        return 'lessthan500'
    elif x<800:
        return 'lessthan800'
    elif x< 1200:
        return "lessthan1200"
    else:
        return 'Not a value' 
    
df['sales_month_8']=df['sales_month_8'].apply(lambda x:checkfun(x))
print(df)

