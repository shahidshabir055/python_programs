# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:11:08 2019

@author: eshah
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
'''
def rotLeft(a, d):
    n=0
    while(n<d):
        temp=a[0]
        for i in range(0,len(a)-1):
            #temp=a[0]
            a[i]=a[i+1]
        a[-1]=temp 
        print(a)
        n=n+1
    return(a)
'''
def rotLeft(a,d):
    index=d%len(a)
    newar=[]
    for i in range(d,len(a)):
        newar.append(a[i])
        print(newar)
    for i in range(0,d):
        newar.append(a[i])
        print(newar)
    return newar
k=[1,2,3,4,5]
d=4
print(rotLeft(k,d))
