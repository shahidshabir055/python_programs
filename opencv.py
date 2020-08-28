# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:42:23 2020

@author: eshah
"""

import cv2,time
import pandas
from datetime import datetime
"""
#reading the image
img=cv2.imread("E:\study material\shahid.jpg",1)
resize=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
face_cascade = cv2.CascadeClassifier("E:\study material\haarcascade_frontalface_default.xml")
grey_img=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grey_img,scaleFactor=1.05,minNeighbors=5)
for x,y,w,h in faces:
    img=cv2.rectangle(resize,(x,y),(x+w,y+h),(10,25,300),2)
print(grey_img)
print(type(grey_img))
print(grey_img.shape)
cv2.imshow("shahid",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
"""
#capturing the videos
video=cv2.VideoCapture(0)
a=1
while True:
    check,frame=video.read()
    #print(check)
    print(frame)
    #time.sleep(3)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing',gray)
    key= cv2.waitKey(1)
    if key== ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows()
"""
#detecting the motions
first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["start","End"])
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)
    (cnts,_)=cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour)<1000:
            continue
        status=1
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)
    status_list=status_list[-2:]
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==1 and status_list[-2]==1:
        times.append(datetime.now())
    cv2.imshow('frame',frame)
    cv2.imshow('Capturing',gray)
    cv2.imshow('delta',delta_frame)
    cv2.imshow('thresh',thresh_delta)
    key= cv2.waitKey(1)
    if key== ord('q'):
        break
print(status_list)
print(times)
for i in range(0,len(times),2):
    df=df.append({"start":times[i],"End":times[i+1]},ignore_index=True)
df.to_csv("times.csv")
video.release()
cv2.destroyAllWindows()