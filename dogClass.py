# -*- coding: utf-8 -*-
"""
Created on Mon May 11 09:52:54 2020

@author: eshah
"""

class dog:
    def __init__(self,name,month,day,year,speakText):
        self.name=name
        self.month=month
        self.day=day
        self.year=year
        self.speakText=speakText
    def speaktext(self):
        return self.speakText
    def birthday(self):
        return str(self.day)+"/"+str(self.month)+"/"+str(self.year)
def main():
    boyDog=dog("shepherd","oct",10,1997,"barking")
    print(boyDog.birthday())
    print(boyDog.speaktext())
if __name__=="__main__":
    main()