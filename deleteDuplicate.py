# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:17:17 2020

@author: eshah
"""

def deleteDuplicate(A):
    if not A:
        return 0
    k=1
    for i in range(1,len(A)):
        if(A[k-1]!=A[i]):
            A[k]=A[i]
            k+=1
    return k
A=[1,2,3,5,1,2,6,7,3]
print(deleteDuplicate(A))