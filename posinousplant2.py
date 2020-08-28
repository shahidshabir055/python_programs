# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:23:10 2020

@author: eshah
"""

def pass_day(plants):
	stack = [plants[0]]
	last = plants[0]
	for i in range(1, len(plants)):
		x = plants[i]
		if x <= last:
			stack.append(x)
			last = x
		else:
			last = x
	return stack
plants=[6,5,8,4,7,10,9]
l = len(plants)
count = 1
while True:
	r = pass_day(plants)
	if len(r) == l:
		print(count)
		break
	else:
		count += 1
		l = len(r)
