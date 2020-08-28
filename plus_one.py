# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:02:24 2020
@author: eshah
"""
def plus_one(A):
    A[-1]+=1
    print(A)
    for i in reversed(range(1,len(A))):
        print(A)
        if A[i]!=10:
            break
        A[i]=0
        A[i-1]+=1
        print(A)
    if A[0]==10:
        A[0]=1
        A.append(0)
    return A
a=[10,2,1]
print(plus_one(a))