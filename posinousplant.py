# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:19:49 2020

@author: eshah
"""
days=1
def finddays(p):
    i=0
    global days
    while i < len(p):
        if(p[i]>p[i-1]):
            p.remove(p[i])
            i=i+2
            days+=finddays(p)
        print(p)
        i=i+1
    return days
p=[6 ,5 ,8, 4, 7, 10, 9]
[6,5,4,10,9]
[6,5,4,9]
[6,5,4]
#p=[3,6,2,7,5]
print(finddays(p))