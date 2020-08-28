# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:43:40 2020

@author: eshah
"""
t=int(input())
while (t):
    l=int(input())
    r=int(input())
    s=int(input())
    count=0
    if s==1:
        print(l,r)
    else:
        for i in range(1,l+1):
            k=i*s
            if k in range(l,r+1):
                print(i,end="")
    t-=1