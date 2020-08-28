# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:11:46 2019

@author: eshah
"""

import numpy as np
a=np.array([1,23,7,45,6])
print(a.ndim)
b=np.arange(100)
print(b)
c=np.arange(10,100)
print(c)
print(c.ndim)
c.reshape(5,18)
print(c.ndim)