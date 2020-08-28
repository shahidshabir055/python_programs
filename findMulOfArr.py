# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:48:32 2020

@author: eshah
"""

def findMul(arr,n):
    mul=1
    for i in range(0,len(arr)):
        mul=(mul*arr[i])%((10**9+7))
    return mul
n=int(input())
arr=list(map(int,input().split()))
print(findMul(arr,n))