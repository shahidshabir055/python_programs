# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:11:11 2020

@author: eshah
"""

s=[0,1,1,0,0,1,1]
count=0
l=[]
for i in range(0,len(s)-1):
    l.append(s[i])
    if s[i]==0 and s[i] in l:
        l.remove(s[i])
        count+=1
        i+=1
    print(l)
    
print(count)