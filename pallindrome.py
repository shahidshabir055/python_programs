# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:35:31 2019

@author: eshah
"""

class tree(object):
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
root=tree()
root.data="Root"
root.left=tree()
root.left.data="child1"
root.right=tree()
root.left.data="child2"

root.left.left=tree()
root.left.left.data="child3"
root.left.right=tree()
root.left.right.data="child5"
root.right.right=tree()
root.right.right.data="child4"

