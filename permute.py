# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:14:17 2020

@author: eshah
"""
"""
from collections import namedtuple
a=namedtuple('courses','name,technology')
#s=a('data science','python')
s=a._make(['data science', 'python'])
print(s)
            
""" 
from collections import Counter
a=[1,2,3,4,1,2,3,4,7,5,2,9,5,2,3]
s=Counter(a)
print(list(s.elements()))
print(s.most_common())
print(s)        