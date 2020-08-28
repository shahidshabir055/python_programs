# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:08:32 2019

@author: eshah
"""

#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    #Remove pass and write your logic here
    pairs=0
    for i in range(0,len(num_list)-1):
        for j in range(i+1,len(num_list)):
            #print(num_list[i])
            #print(num_list[j])
            if(num_list[i]+num_list[j]==n):
                pairs=pairs+1
    if(pairs!=0):
        return pairs
    else:
        return 0
        

num_list=[1,2,3,4,5,6]
n=6
print(find_pairs_of_numbers(num_list,n))