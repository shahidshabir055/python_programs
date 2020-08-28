# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:52:06 2020

@author: eshah
"""

def weird_algorithm(n):
    while(n>1):
        print(n)
        if(n%2==0):
            n=n//2
        else:
            n=(n*3)+1
weird_algorithm(3)