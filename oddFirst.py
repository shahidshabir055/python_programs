# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:37:10 2020

@author: eshah
"""

def odd_first(A):
    next_even=len(A)-1
    next_odd=0
    while next_odd<next_even:
        if A[next_odd]%2==1:
            next_odd+=1
        else:
            A[next_odd],A[next_even]=A[next_even],A[next_odd]
            next_even-=1
    return A
A=[12,55,677,3334,676,34]
print(odd_first(A))