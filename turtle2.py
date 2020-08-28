# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:17:45 2020

@author: eshah
"""
import turtle
def main():
 # This line reads a line of input from the user.
    filename = input("Please enter drawing filename: ")

 # Create a Turtle Graphics window to draw in.
    t = turtle.TurtleScreen()
# The screen is used at the end of the program.
    screen = t.getscreen()

    file = open(filename, "r")
    for line in file:
        text = line.strip()

        commandList = text.split(",")

        command = commandList[0]
        if command == "goto":
            
    
             x = float(commandList[1])
             y = float(commandList[2])
             width = float(commandList[3])
             color = commandList[4].strip()
             t.width(width)
             t.pencolor(color)
             t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
                t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file:",command)

    file.close()

    t.ht()

    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()