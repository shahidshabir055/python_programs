# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 11:36:22 2020

@author: eshah
"""
import math 
def isPerfectSquareCube(x): 
    for i in range(x,1,-1):
        sr= math.sqrt(i)
        cb=i**(1./3.)
        #cb=729**(1/3)
        #if((sr - math.floor(sr)) == 0 and round(cb)**3==i ):
        if(round(sr)**2==i and round(cb)**3==i):
           return i
x = 751
print(isPerfectSquareCube(x))