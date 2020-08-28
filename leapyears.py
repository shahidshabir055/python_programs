# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:35:39 2019

@author: eshah
"""

def find_leap_years(given_year):

    # Write your logic here
    leap=[]
    while(len(leap)<=15):
        if((given_year%4==0 and given_year%100!=0) or given_year%400==0):
            leap.append(given_year)
            given_year=given_year+4
    return leap
list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)