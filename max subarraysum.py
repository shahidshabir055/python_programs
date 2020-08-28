# -*- coding: utf-8 -*-
"""
Created on Sun May  3 21:05:43 2020

@author: eshah
"""
array=[-1,2,4,-3,5,2,-5,2]
n=len(array)
best=0
"""
#complexity=O(n^3)
for i in range(n):
    for j in range(i,n):
        sum=0
        for k in range(i,j):
            sum+=array[k]
        best=max(best,sum)
print(best)
"""
#complexity=o(n^2)
"""
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=array[j]
        best=max(best,sum)
print(best)
"""
sum=0
for i in range(n):
    sum=max(array[i],sum+array[i])
    best=max(best,sum)
print(best)
