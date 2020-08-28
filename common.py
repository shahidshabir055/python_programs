# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:53:27 2019

@author: eshah
"""

a=int(input())
b=int(input())
count=0
k=min(a,b)
for i in range(1,k+1):
    if(a%i==0 and b%i==0):
        count=count+1
print(count)