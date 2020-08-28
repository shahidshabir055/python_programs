# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:13:10 2020

@author: eshah
"""

try:
    t=int(input())
    while(t>0):
        s=input()
        k=list(s)
        l=[]
        ink=[]
        count=0
        for i in range(0,len(k)-1):
            for j in range(1,len(k)):
                if k[i]==k[j]:
                    l=k[i+1:j]
                    ink.append(len(l))
        ink=sorted(ink)
        print(ink)
        print(ink[-1])
except EOFError as e : pass