# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:14:21 2020

@author: eshah
"""
import math
import operator
#calculating the distance for nearest neighbor
def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)
"""
data1=[2,2,2,'a']
data2=[4,4,4,'b']
distance=euclideanDistance(data1,data2,3)
print('distance:'+repr(distance))
"""
#finding the nearest neighbor
def getNeighbors(trainingSet,testSet,k):
    distances=[]
    length=len(testInstance)-1
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
#demo
"""
trainSet=[[2,2,2,'a'],[4,4,4,'b'],[3,3,3,'b']]
testInstance=[5,5,5]
k=1
neighbors=getNeighbors(trainSet,testInstance,k)
print(neighbors)
"""
#predicting the response by allowing the neighbors to vote and take the majority
def getResponse(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedVotes=sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]
#demo
"""
neighbors=[[1,1,1,'a'],[2,2,2,'b'],[3,3,3,'a']]
response=getResponse(neighbors)
print(response)
"""
#calculating accuracy
def getAccuracy(testSet,predictions):
    correct=0
    for x in range(len(testSet)):
        if(testSet[x][-1] is predictions[x]):
            correct+=1
    return(correct/float(len(testSet)))*100
#demo
"""
testSet=[[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
predictions=['a','a','a']
print(getAccuracy(testSet,predictions))
"""
 