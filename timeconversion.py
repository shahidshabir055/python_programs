# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:19:32 2019

@author: eshah
"""

#!/bin/python3

# Complete the timeConversion function below.
#
def timeConversion(s):
    if(s[-2]=='P' and (s[0:2])!=str(12)):
        k=(s[0:2])
        k=int(k)+12
        if(int(k)==24):
            k='00'
        return(str(k)+s[2:-2])
    elif(s[-2]=='A' and (s[0:2])==str(12)):
        k='00'
        return(str(k)+s[2:-2])
    elif(s[-2]=='P' and (s[0:2])==str(12)):
        return(s[0:-2])
    else:
        return(s[0:-2])

s="10:40:45PM"
print(timeConversion(s))
"""
    count = 0
    
    while head and count<101:
        count += 1
        head = head.next
        
    return count>100
"""