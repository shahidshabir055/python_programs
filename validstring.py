# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:30:09 2020

@author: eshah
"""

def iswellformed (s) :
    left_chars = []
    lookup= {'(': ')', '{': '}', '[': ']' }
   # a="yes"
    #b="no"
    for c in s:
        if c in lookup:
            left_chars. append(c)
        elif(lookup[left_chars.pop()]!=c):
            return False
    if(left_chars == []):
        return True
    else:
        return False
s=input()
print(iswellformed(s))