# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 12:19:03 2020

@author: eshah
"""

def numberOfPaths(m, n): 
	if(m == 1 or n == 1): 
		return 1
	return numberOfPaths(m-1, n) + numberOfPaths(m, n-1) 
m = 10
n = 10
print(numberOfPaths(m, n))
