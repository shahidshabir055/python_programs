# -*- coding: utf-8 -*-
"""
Created on Sun May 31 15:20:07 2020

@author: eshah
"""

# Pythono3 code to rename multiple 
# files in a directory or folder 

# importing os module 
import os 

# Function to rename multiple files 
def main(): 

	for count, filename in enumerate(os.listdir("E:\dil\DataSET\FruitImages\healthy_Fruit_Test/")):
        
		dst ="healthyApple" + str(count) + ".jpg"
		src ='E:\dil\DataSET\FruitImages\healthy_Fruit_Test/'+ filename
		dst ='E:\dil\DataSET\FruitImages\healthy_Fruit_Test/' + dst		
		# rename() function will 
		# rename all the files 
		os.rename(src, dst) 
# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 
