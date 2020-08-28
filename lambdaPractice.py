# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:58:32 2020

@author: eshah
"""
"""
x=lambda a:a*a
i=int(input())
print(x(i))
"""

"""
def new(a):
    return a*a
x=map(new,[1,2,3,4])
print(x)
print(set(x))
"""
def new(A):
    s=[]
    for i in A:
       s.append(i**2) 
    return s
A=[1,2,3,4]
B=new(A)
print(B)
