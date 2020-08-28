# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:07:17 2020

@author: eshah
"""

def countNum(x):
    num_bits=0
    while(x):
        num_bits+=x & 1
        x>>=1
    return num_bits
x=12
print(countNum(x))
        