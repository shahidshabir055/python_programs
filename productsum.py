# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:55:54 2020

@author: eshah
"""
import math as mt 
def kFactors(n, k): 
	
	a = list()  
	while n % 2 == 0: 
		a.append(2) 
		n = n // 2
	for i in range(3, mt.ceil(mt.sqrt(n)), 2): 
		while n % i == 0: 
			n = n / i; 
			a.append(i) 
 
	if n > 2: 
		a.append(n) 
	if len(a) < k: 
		print("-1") 
		return
	for i in range(k - 1): 
		print(a[i], end = ", ") 
	product = 1
	
	for i in range(k - 1, len(a)): 
		product *= a[i] 
	print(product) 
n, k = 48, 3
kFactors(n, k)
