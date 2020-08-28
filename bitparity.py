# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:07:14 2020

@author: eshah
"""

def getParity(x):
    result=0
    while x:
        result=~result
        x = x&(x-1)
    return result
 

def getParityBrute(x):
    result=0
    while(x):
        result=(result^(x&1))
        x=x>>1
    return result

x=7


print(getParity(x))