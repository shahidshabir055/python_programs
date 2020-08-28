# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:23:04 2020

@author: eshah
"""
"""
def generate_pascal_triangle(n):
    result=[[1]*(i+1) for i in range(n)]
    for i in range(n):
        for j in range(1,i):
            result[i][j]=result[i-1][j-1]+result[i-1][j]
    print(result)
print(generate_pascal_triangle(5))
"""
"""
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j)," ",end="")
        print("\r")
    print()
def function(n,k):
    res=1
    if(k>n-k):
        k=n-k
    for i in range(0,k):
        res=res*(n-i)
        res=res//(i+1)
    return res
pattern(7)
"""
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j)," ",end="")
        print("\r")
    print()
def function(n,k):
    res=1
    if(k>n-k):
        k=n-k
    for i in range(0,k):
        res=res*(n-i)
        res=res//(i+1)
    return res
pattern(13)
        