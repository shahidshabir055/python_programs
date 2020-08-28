# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 20:00:58 2020

@author: eshah
"""

def findsetbit(n):
    cnt=0
    for i in range(1,n+1):
        x=bin(i)
        x=str(x)
        for j in range(0,len(x)):
            if(x[j]=='1'):
                cnt+=1
    return cnt
n=5
print(findsetbit(n))
        