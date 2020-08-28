# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:37:25 2020
@author: eshah
"""

#creating a node class
class Node:
    def __init__(self,val):
        self.childLeft=None
        self.childRight=None
        self.NodeData=val
root=Node(1)
root.childLeft=Node(2)
root.childRight=Node(3)
root.childLeft.childLeft=Node(4)
root.childLeft.childRight=Node(5)
def InOrd(root):
    if root:
        InOrd(root.childLeft)
        print(root.NodeData)
        InOrd(root.childRight)
InOrd(root)
print("the pre-order traversal is:")
def preOrd(root):
    
    if root:
        print(root.NodeData)
        preOrd(root.childLeft)
        preOrd(root.childRight)
preOrd(root)
print("the post-order traversal is:")
def postOrd(root):
    if root:
        postOrd(root.childLeft)
        postOrd(root.childRight)
        print(root.NodeData)
postOrd(root) 