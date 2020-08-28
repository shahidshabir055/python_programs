# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:23:54 2020

@author: eshah
"""

def multiply(num1,num2):
    sign = -1 if(num1[0] < 0 ^ num2[0]<0) else 1
    num1[0],num2[0]=abs(num1[0]),abs(num2[0])
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1),-1):
        for j in range(len(num2),-1):
            result[i+j+1] += num1[i] * num2[j]
            result[i+j+1] +=(result[i+j+1])//10
            result[i+j+1]%=10
    #result = result[next((i for i, x in enumerate(result)if x !=0),len(result)):] or [0]
    return [sign * result[0]]+ result[1:]
num1=[1,9,3,7,0,7,7,2,1]
num2=[-7,6,1,8,3,8,2,5,7,2,8,7]
print(multiply(num1,num2))