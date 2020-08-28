# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:23:03 2020

@author: eshah
"""

def msort(mylist,left,right):
    if(right-left>1):
        middle=(left+right)//2
        msort(mylist,left,middle)
        msort(mylist,middle,right)
        mlist(mylist,left,middle,right)
def mlist(mylist,left,middle,right):
    leftList=mylist[left:middle]
    rightList=mylist[middle:right]
    k=left
    i=0
    j=0
    while(left+i<middle and middle+j < right):
        if(leftList[i]<=rightList[j]):
            mylist[k]=leftList[i]
            i=i+1
        else:
            mylist[k]=rightList[j]
            j=j+1
        k=k+1
        if(left+i<middle):
            while(k<=right):
                mylist[k]=leftList[i]
                i=i+1
        else:
            while(k<right):
                mylist[k]=rightList[j]
                j=j+1
        k=k+1
mylist=input("enter the elemnts").split()
mylist=[int(x) for x in mylist]
msort(mylist,0,len(mylist))
print("the sorted list is")
print(mylist)