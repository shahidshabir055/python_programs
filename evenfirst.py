# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:29:30 2020

@author: eshah
"""

def even_odd(A):
    next_even=0
    next_odd=len(A)-1
    while next_even < next_odd:
        if A[next_even]%2==0:
            next_even+=1
        else:
            A[next_even],A[next_odd]=A[next_odd],A[next_even]
            next_odd-=1
    return A
a=[6,1,3,4,2,9,11,56,77,66]
print(even_odd(a))
        