# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:00:40 2020

@author: eshah
"""
t=1
n=int(input())
arr=[]
while (n):
    elt=int(input())
    arr.append(elt)
    n-=1
sum=0
for i in range(0,len(arr)-1):
    if(arr[i]>arr[i+1]):
        arr[i]=arr[i+1]
for i in range(0,len(arr)):
    sum+=arr[i]
print(sum)
#1 5 2 3 4
# 1 2 2 3 4 5