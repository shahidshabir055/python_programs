# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:25:58 2020

@author: eshah
"""

t=int(input())
while(t):
    n=int(input())
    arr=input()
    arr=list(arr)
    sum=0
    for i in range(0,len(arr)-1):
        if((arr[i])>(arr[i+1])):
            arr[i]=arr[i+1]
    for i in range(0,len(arr)):
        sum+=int(arr[i])
    print(sum)
    t-=1