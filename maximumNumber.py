# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 04:51:52 2020

@author: eshah
"""
l=[12,98,99,44]
k=[]
for i in range(0,len(l)):
    q=l[i]//10
    r=l[i]%10
    if q>r:
        k.append(q)
        k.append(r)
    else:
        k.append(r)
        k.append(q)
k=sorted(k)
k=[ele for ele in reversed(k)]
for i in k:
    print(i,end="")
    