# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:04:22 2020

@author: eshah
"""



# Write your code here
t=int(input())
s=input()
count=0
for i in range(0,len(s)-1):
    for j in range(1,len(s)):
        if s[i]==s[j]:
            count+=1
if count>0:
    print(count)
else:
    print(1)
