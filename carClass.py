# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:13:02 2020

@author: eshah
"""
class car():
    def __init__(self,name,mfd,price):
        self.Name=name
        self.mfd=mfd
        self.price=price
    def modifyPrice(self):
        self.price=(int(self.price * 1.5))
Honda=car("cruze",2019,20000)
print(Honda.__dict__)
Honda.modifyPrice()
print(Honda.price)

