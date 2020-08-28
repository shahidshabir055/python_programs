# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:55:50 2020

@author: eshah
"""

#inverted pyramid
"""
def pattern(n):
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k = k+1
        for i in range(0,i+1):
            print("*",end=" ")
        print("\r")
pattern(10)
"""
def pattern(n):
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for i in range(0,i+1):
            print("*",end=" ")
        print("\r")
pattern(10)