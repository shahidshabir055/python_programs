# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:50:49 2019

@author: eshah
"""

#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years=[]
    while(len(list_of_leap_years)<16):
        given_year=given_year+1
        if((given_year%4==0 and given_year%100!=0 and given_year%400!=0) or given_year%400==0):
            list_of_leap_years.append(given_year)
    return list_of_leap_years
list_of_leap_years=find_leap_years(1000)
print(list_of_leap_years)