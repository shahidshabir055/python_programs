# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:29:16 2019

@author: eshah
"""

def find_more_than_average():
    sum=0
    avg=0.0
    for i in range(0,len(list_of_marks)):
        sum+=i
    avg=sum/(len(list_of_marks)+1)
    count=0
    for i in range(0,len(list_of_marks)):
        if(list_of_marks[i]>avg):
            count=count+1
    return moreThanAvg=(count/len(list_of_marks)*100
list_of_marks= (12,18,25,24,2,5,18,20,20,21)
print(find_more_than_average())