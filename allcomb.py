# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:55:04 2020

@author: eshah
"""
#print all the combinations of a string
def allcombinations(string, i=0):
    if(i == len(string)):
        print("".join(string))
    for k in range(i, len(string)):
        s = [n for n in string]
        s[i], s[k] = s[k], s[i]
        allcombinations(s, i+1)
print(allcombinations("hello"))