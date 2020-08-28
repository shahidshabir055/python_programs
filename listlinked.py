# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 06:25:04 2020

@author: eshah
"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print ("[",printval.dataval,"]->" ,end=" ")
            printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode
    def is_cycle(self):
        slow=self.headval
        fast=self.headval
        while fast and fast.nextval and fast.nextval.nextval:
            slow, fast = slow.nextval , fast.nextval.nextval
            if slow is fast:
                slow=slow.dataval
            while slow is not fast:
                slow,fast=slow.nextval,fast.nextval
            return slow
        return None
list = SLinkedList()
list.headval = Node("sun")
e2 = Node("Mon")
e3=Node("tue")
e4 = Node("fri")
e5 = Node("Wed")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval=e4
e4.nextval=e5
list.AtBegining("fri")
list.listprint()
#list.is_cycle()