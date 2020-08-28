# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:19:49 2019

@author: eshah
"""

a=[1,1,-1,0,-1]
c0=0.000000
c1=0.000000
c2=0.000000
for i in range(0,len(a)):
    if(a[i]==0):
        c0+=1
    if(a[i]>0):
        c1+=1
    else:
        c2+=1
k0=c0/len(a)
k1=c1/len(a)       
k2=c2/len(a)
print(format(k0),".6f")
print(k1)
print(k2)
        