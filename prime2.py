# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:41:30 2020

@author: eshah
"""

for i in range(1,18):
    if i == 1:
        continue
    flag = 1
    for j in range(2,(i//2)+1):
        if(i%j==0):
            flag=0
            break
    if flag == 1:
        print(i,end=" ")