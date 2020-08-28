# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 06:23:22 2020
@author: eshah
"""
def matrix_in_spiral_order(sqmt):
    SHIFT=((0,1),(1,0),(0,-1),(-1,0))
    direction =x=y=0
    spiral_ordering=[]
    for i in range(len(sqmt)**2):
        spiral_ordering.append(sqmt[x][y])
        sqmt[x][y]=0
        next_x,next_y=x+SHIFT[direction][0],y+SHIFT[direction][1]
        if next_x not in range(len(sqmt)) or next_y not in range(len(sqmt)) or sqmt[next_x][next_y]==0:
            direction =(direction+1) & 3
            next_x,next_y=x+SHIFT[direction][0],y+SHIFT[direction][1]
        x,y=next_x,next_y
    return spiral_ordering
sqmt=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(matrix_in_spiral_order(sqmt))