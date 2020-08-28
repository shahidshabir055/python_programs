# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:11:06 2020

@author: eshah
"""
import os
f = open(r'E:\adil\DataSET\FruitImages\scabbed.txt','w')
for i in range(0,337):
    f.write("scabbedApple\n")
    
f.close()

#open and read the file after the appending:
#f = open("demofile2.txt", "r")
#print(f.read())