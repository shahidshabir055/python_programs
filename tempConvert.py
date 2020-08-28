# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 08:41:00 2019

@author: eshah
"""

#goal of this tryout is to create a function from scratch and invoke it for the given problem
def convertTemp(t,tp):
    tempInC=0.0
    tempInF=0.0
    if(tp=='F'):
        tempInC=(t-32)*(5/9)
        return tempInC
    elif(tp=='c'):
        tempInF=t*(9/5)+32
        return tempInF
a=float(input("enter the temperature"))
b=str(input("enter the scale of temperature(c/F)"))
result=convertTemp(a,b)
print(result)