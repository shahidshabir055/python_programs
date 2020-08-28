# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:46:31 2020

@author: eshah
"""

def mulmatrix(A,B):
    result=[[0  for x in range(len(A))] for y in range(len(B))]
    print(result)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j]=A[i][k]*B[k][j]
    return result
a=[[3,5,3],[2,6,8],[6,4,1]]
b=[[6,5,2],[7,3,9],[8,5,2]]
print(mulmatrix(a,b))