# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:18:07 2020

@author: eshah
"""
#factorial using recursion
num = input("Enter a number: ")
def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("NA")
    else:
        return n*recur_factorial(n-1)
print (recur_factorial(int(num)))