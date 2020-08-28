# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:41:03 2020

@author: eshah
"""
from collections import defaultdict
try:
    t = input()
    n,m = map(int,input().split())
    f = list(map(int,input().split()))
    p = list(map(int,input().split()))
    temp = defaultdict(list)
    for c, i in zip(f, p):
        temp[c].append(i)
    s = ({k:sum(v) for k,v in temp.items()})
    key_min = min(s.keys(), key=(lambda k: s[k]))
    print(s[key_min])
except EOFError as e : pass