# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:36:02 2019

@author: eshah
"""

def bubbleSort(nlist):
    count=0
    for i in range(len(nlist)-1,0,-1):
        for j in range(i):
            if nlist[j]>nlist[j+1]:
                temp = nlist[i]
                nlist[j] = nlist[j+1]
                nlist[j+1] = temp
                count=count+1
    print(count)
    print(nlist[0],nlist[-1])
nlist = [14,46,43,27,57,41,45,21,70]
bubbleSort(nlist)
print(nlist)
#print "My name is %s and weight is %d kg!" % ('Zara', 21)
#print "my name is %s and my age is %a!" % ('shahid',20)