# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:07:24 2020

@author: eshah
"""

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Atbeginning(self,newData):
        temp=node(newData)
        temp.next=self.head
        self.head=temp
    def displayList(self):
        display=self.head
        while display is not None:
            print(display.data)
            display.next=next
list = LinkedList()
list.head = node("Mon")
e2 = node("Tue")
e3 = node("Wed")

list.head.next = e2
e2.nextval = e3

list.Atbeginning("Sun")

list.displayList()
