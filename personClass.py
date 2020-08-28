# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:20:12 2020

@author: eshah
"""
class person():
    def __init__(self,name,age,height,grade):
        self.name=name
        self.age=age
        self.height=height
        self.grade=grade
    def isEligible(self):
        if(self.grade>7.5):
            return True
        else:
            return False
#shahid=person("shahid",21,6.2,7.8)
class student(person):
    def __init__(self,name,age,height,grade,rollno):
        super(student,self).__init__(name,age,height,grade)
        self.rollno=rollno
syed=student("shahid",45,6.4,7.9,"17bcs055")
print(syed.__dict__)
print(syed.isEligible())
    