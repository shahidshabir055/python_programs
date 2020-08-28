# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:12:20 2020

@author: eshah
"""

# Python 3.x code to demonstrate star pattern 

# Function to demonstrate printing pattern triangle 
def triangle(n): 
	k = 2*n - 2
	for i in range(0, n):  
		for j in range(0, k): 
			print(end=" ") 
		k = k - 1
		for j in range(0, i+1): 
			print("* ", end="") 
		print("\r")  
n = 5
triangle(n) 
