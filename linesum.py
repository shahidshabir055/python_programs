# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 12:49:03 2020

@author: eshah
"""

import math
a=[5,2,7]
sum=0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        k=a[i]+a[j]
        l=a[i]-a[j]
        dist=(math.sin(k))*(math.cos(l))
        sum=sum+dist
print(round(sum,2))
    