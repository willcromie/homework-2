Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from graphics import *
import time
def moveAll(shapeList, dx, dy):
    for shape in shapeList: 
        shape.move(dx, dy)

        
def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)

        
def makeFace(center, win):
    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1Center = center.clone() 
    eye1Center.move(-10, 5)
    eye1 = Circle(eye1Center, 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2End1 = eye1Center.clone()
    eye2End1.move(15, 0)
    eye2End2 = eye2End1.clone()
    eye2End2.move(10, 0)
    
    eye2 = Line(eye2End1, eye2End2)
    eye2.setWidth(3)
    eye2.draw(win)

    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)
     
    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)

    nose1 = center.clone()
    nose1.move(-4,-4)
    nose2 = center.clone()
    nose2.move(4,-4)
    nose3 = center.clone()
    nose3.move(0,0)
    vertices = [nose1, nose2, nose3]

    nose = Polygon(vertices)
    nose.setFill(red)
    nose.draw(win)
    
 
    return [head, eye1, eye2, mouth, nose]
 
>>> def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.yUp() 

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)
    
    faceList = makeFace(Point(40, 100), win)
    faceList2 = makeFace(Point(150,125), win)
 
    stepsAcross = 46
    dx = 5
    dy = 3
    wait = .05
    for i in range(3):
        moveAllOnLine(faceList, dx, 0, stepsAcross, wait)
        moveAllOnLine(faceList, -dx, dy, stepsAcross//2, wait)
        moveAllOnLine(faceList, -dx, -dy, stepsAcross//2, wait)
 
    win.promptClose(win.getWidth()/2, 20)
 
     
>>> main()
