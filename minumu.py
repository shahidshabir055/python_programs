# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:00:28 2019

@author: eshah
"""

a=[2,1,3]
print(a)
b=[]
b=sorted(a)
print(b)
count=0

for i in range(0,len(a)):
    if(a[i]!=b[i]):
        a[i]=b[0]
        count=count+1
        print("Iteration {}".format(i+1))
        print(a)
        print(b)
    b.remove(b[0])


        

print(a)
print(b)
print(count)
          