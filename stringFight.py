# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 14:26:50 2020

@author: eshah
"""

try:
    t=int(input())
    while(t):
        def stringFight(str):
            str=list(str)
            if(str[0]=='(' and str[-1]!=')'):
                str.append(')')
            elif(str[0]==')' and str[-1]=='('):
                str.append(')')
                str.insert(0,'(')
            elif(str[0]==')' and str[-1]==')'):
                str.insert(0,'(')
            str1 = ""  
            return (str1.join(str))
        t-=1
    str=input()
    print(stringFight(str))
except EOFError as e : pass