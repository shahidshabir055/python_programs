# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 18:17:11 2019

@author: eshah
"""

#PF-Assgn-28

def find_max(num1, num2):
    # Write your logic here
    num=[]
    if(num1>num2 or num1 > 99 or num2 >99 or num1<10 or num2<10):
        return -1
    else:
        for k in range(num1,num2+1):
               sum=0
               if(k%5==0):
                   temp_num=k
                   while(temp_num!=0):
                       sum=sum+temp_num%10
                       temp_num=temp_num//10
                   if(sum%3==0):
                       num.append(k)
        if(num==[]):
            return -1
        else:
            num.sort(reverse=True)
            max_num=num[0]
            return max_num
#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,99)
print(max_num)