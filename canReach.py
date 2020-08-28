# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:41:54 2020

@author: eshah
"""

def canreach(A):
    curPos = 0
    lastPos = len(A)-1
    i = 0
    steps = []
    while i <= curPos and curPos < lastPos:
        curPos = max(curPos, A[i]+i)
        i += 1
        print(curPos)
        steps.append(curPos)
    return curPos >= lastPos
A=[3,3,0,2,0,0,1]
#A=[2,4,1,1,0,2,3]
print(canreach(A))