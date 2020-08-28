# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:19:36 2020

@author: eshah
"""
def matchingStrings(strings, queries):
    result=[]
    c=0
    queries=set(queries)
    queries=list(queries)
    for i in range(0,len(queries)):
        if queries[i] in strings:
            c=strings.count(queries[0])
            result[i].append(c)
        else:
            result.append(0)
    return result
queries=['ab','abc','bc']
strings=['ab','ab','abc']
print(queries)
print(strings)
print(matchingStrings(strings,queries))
  #[1,5,2,3,4]
  
#[1,2,2,3,4]  
    