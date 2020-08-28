# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 07:25:24 2020

@author: eshah
"""

class Node:
    def __init__(self,dataVal=None):
        self.dataVal=dataVal
        dataVal.nextval=None
class sLinkedList:
    def __init__(self):
        self.head=None
slist=sLinkedList()
slist.head=Node("mon")
n2=Node("tue")
slist.head.nextVal=n2
n3=Node("sun")
#n2.nextval=n3