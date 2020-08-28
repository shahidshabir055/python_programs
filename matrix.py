# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 20:54:52 2019

@author: eshah
"""
n=3
arr=[[1,2,3],
     [5,2,5],
     [8,5,1]]
sum=0
sum2=0
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if(i==j):
            sum+=arr[i][j]
        if(i+j==n-1):
            sum2+=arr[i][j]
            
print(sum)
print(sum2)
print(abs(sum-sum2))

    