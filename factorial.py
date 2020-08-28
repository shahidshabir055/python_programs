# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:02:44 2020

@author: eshah
"""

num=int(input("enter the number:"))
factorial=1
if num<0:
    print("number should be positive:")
elif num==0:
    print("factorial = 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
l=[int(x) for x in str(factorial)]
zeroes=l.count(0)
print(factorial)
print(zeroes)