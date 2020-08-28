# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:40:23 2019

@author: eshah
"""

lt = [['a',5],['b',2],['c',3]]
print(lt)
for x in lt:
    print(x)
print("_____________")
for x in range(0,len(lt)):
    print(lt[x])
print("-------------------")
for x in lt:
    print(x[1])
mylist=[0]*5
for i in range(1,5):
    mylist[i]=(i-1)*10
print(mylist)
