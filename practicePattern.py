# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:25:53 2020

@author: eshah
"""
"""
def pattern(n):
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
    k=2*n-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k=k-1
        for j in range(0,i+2):
            print("*",end=" ")
        print("\r")
pattern(10)
"""

def pattern(n):
    k=2*n-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k=k-1
        for i in range(0,i+2):
            print("*",end=" ")
        print("\r")
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
pattern(10)