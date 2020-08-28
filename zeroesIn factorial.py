# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:06:23 2020

@author: eshah
"""

n=int(input("enter n"))
def factorial(n):
    count=0
    x=1
    while(n//pow(5,x)>1):
        count+=n//(pow(5,x))
        x+=1
    return count
print(factorial(n))