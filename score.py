# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def findMinimumScore (A, N):
    # Write your code here
    for i in range(N-1,1,-1):
        A[i-1]=A[i-1]+1+(max(A[i-1],A[-1]))
        output=A[i-1]
        A.remove(A[-1])
    return output
        
    

N = int(input())

A = [0]*(N-1)
for i in range(0,N-1):
    A[i] = int(input())

out_ = findMinimumScore(A, N)
print (out_)