# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:45:53 2019

@author: eshah
"""

def countSwaps(a):
    count = 0
    print(a)
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                count = count+1
    print("Array is sorted in "+str(count)+" swaps.")
    print("First Element: ", a[0] )
    print("Last Element: ", a[-1])
    print(a)
a = [4,2,3,1,11,5,9]
countSwaps(a)