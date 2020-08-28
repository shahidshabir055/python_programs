# -*- coding: utf-8 -*-N
"""
Created on Sun Mar  8 11:25:40 2020

@author: eshah
"""


class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
	def __init__(self): 
		self.head = None
	def insertAtStart(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print (temp.data, end =" ") 
			temp = temp.next


	def detectLoop(self): 
		s = set() 
		temp = self.head 
		while (temp): 
			if (temp in s): 
				return True 
			s.add(temp) 
			temp = temp.next
		return False
llist = LinkedList() 
llist.insertAtStart(20) 
llist.insertAtStart(4) 
llist.insertAtStart(15) 
llist.insertAtStart(10) 
print("orginal list")
llist.printList()

# Create a loop for testing 
llist.head.next.next.next.next = llist.head; 
#print("list after loop")
#llist.printList()
if( llist.detectLoop()): 
	print ("Loop found") 
else : 
	print ("No Loop ") 

