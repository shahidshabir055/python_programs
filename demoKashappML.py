# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:30:08 2020

@author: eshah
"""

class BSTNode:
    def __inint__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    def search_bst(tree,key):
        return(tree
               if not tree or tree.data==key else search_bst(tree.left,key)
               if key<tree.data else search_bst(tree.right,key))
Bst=BSTNode()
