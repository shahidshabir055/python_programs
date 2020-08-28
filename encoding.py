# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:00:33 2019

@author: eshah
"""

#PF-Assgn-30
#PF-Assgn-30
def encode(message):
    #Remove pass and write your logic here
    x=0
    encoded_message=[]
    '''
    for i in range(0,len(message)-1):
        letter = message[i]
        if(message[i]!=message[i+1]):
            x=1
            if(str(x)+letter not in encoded_message):
                 encoded_message.append(str(x)+letter)
            x=0
        elif(message[i]==message[i+1]):
            x=x+1
            encoded_message.append(str(x)+letter)
    '''
    count=1;
    if(len(message)==1):
            encoded_message.append(str(1)+message[0])
    for i in range(1,len(message)):
        if(message[i]!=message[i-1]):
            encoded_message.append(str(count)+message[i-1])
            count=1
        else:
            count+=1
        if(i==len(message)-1):
            encoded_message.append(str(count)+message[i])
        
    return encoded_message

#Provide different values for message and test your program
encoded_message=encode("M")
#print(encoded_message)
print( ''.join(i for i in encoded_message))

#output: 1A4B8C1A1B