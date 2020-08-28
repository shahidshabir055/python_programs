# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:33:43 2020

@author: eshah
"""

n=int(input())
count=0
cnt=0
for i in range(1,n):
    if n%i==0:
        count+=1
    for i in range(0,n):
        if count==2**2(i):
            print(n)
        