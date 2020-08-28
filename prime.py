# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 09:58:57 2020

@author: eshah
"""
a=int(input("enter a:"))
b=int(input("enetr b:"))
for i in range(a, b + 1):  
        if (i == 1): 
            continue
        flag = 1
        for j in range(2, i // 2 + 1): 
            if (i % j == 0): 
                flag = 0
                break
        if (flag == 1): 
            print(i, end = " ") 
            