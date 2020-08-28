# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:35:43 2019

@author: eshah
"""

class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    def __repr__(self):
        return '<tree node representation>'