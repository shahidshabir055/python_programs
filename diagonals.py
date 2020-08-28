# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 12:49:11 2020

@author: eshah
"""

def printDiag(s,n):
    for i in range(len(s)):
        print(s[i][i],end=" ")

def pintsec(s,n):
    for i in range(len(s)):
        print(s[i][n-i-1],end=" ")
n=4
s=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]
printDiag(s,n)
print()
pintsec(s,n)
            