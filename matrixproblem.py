# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:57:17 2020

@author: eshah
"""
cols=int(input("enter the array"))
rows=3
arr = [[i for i in range(cols)]  for j in range(rows)] 
print(arr)
temp=0
count=0
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        temp=arr[i][j]
        arr[i][j]=arr[i+1][j+1]
if temp==arr[3][cols]:
    count+=1
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        temp=arr[i][j]
        arr[i][j]=arr[i+1][j-1]
if temp==arr[3][cols]:
    count+=1
print(count)