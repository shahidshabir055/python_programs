# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:13:54 2019

@author: eshah
"""

def compareTriplets(a, b):
    Aearned=0
    Bearned=0
    earned=[]
    for i in range(0,len(a)):
        if(a[i]>b[i]):
            Aearned+=1
    for i in range(0,len(b)):
        if(b[i]>a[i]):
            Bearned+=1
    earned.append(Aearned)
    earned.append(Bearned)
    return earned
k=[5,6,3]
l=[4,1,6]
print(compareTriplets(k,l))