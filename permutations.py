# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 21:09:59 2024

@author: Shoaib Baloch
"""
"""import itertools as it
l=('abc')
for i in it.permutations(l):
    print(list(i))"""
result=[]
def per(data,i,n):
    if n==i:
        result.append("".join(data))
    for j in range(i,n+1):     
        data[i],data[j]=data[j],data[i]
        per(data,i+1,n)
        data[i],data[j]=data[j],data[i]
        
l="ABC"
i=0
n=len(l)-1
per(list(l),i,n)
print(result)