# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:15:32 2020

@author: eshah
"""

import mysql.connector
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="prepaidmobile"
        )
mycursor=mydb.cursor()
#mycursor.execute("create database prepaidMobile")
#mycursor.execute("show databases")
#for x in mycursor:
#    print(x)
#mycursor.execute("create table customers(name varchar(20), mobileNo int, address varchar(20))")
mycursor.execute("show tables")
for x in mycursor:
    print(x)
