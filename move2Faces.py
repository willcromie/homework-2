Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from graphics import *
import time
def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.yUp()


    cir1 = Circle(Point(40,100), 25)
    cir1.setFill("yellow")
    cir1.draw(win)
    eye1 = Circle(Point(30, 100), 5)
    eye1.setFill('black')
    eye1.draw(win)
    eye2 = Circle(Point(50, 100), 5)
    eye2.setFill('black')
    eye2.draw(win)
    mouth1 = Line(Point(30, 80), Point(50, 80))
    mouth1.setWidth(2)
    mouth1.draw(win)
    
... 
...     cir2 = Circle(Point(260,100), 25)
...     cir2.setFill("yellow")
...     cir2.draw(win)
...     eye3 = Circle(Point(250,100), 5)
...     eye3.setFill('black')
...     eye3.draw(win)
...     eye4 = Circle(Point(270,100), 5)
...     eye4.setFill('black')
...     eye4.draw(win)
...     mouth2 = Line(Point(250,80), Point(270,80))
...     mouth2.setWidth(2)
...     mouth2.draw(win)
...     
... 
...     for i in range(46):
...         cir1.move(5, 0)
...         eye1.move(5, 0)
...         eye2.move(5, 0)
...         mouth1.move(5, 0)
...         cir2.move(-5,0)
...         eye3.move(-5, 0)
...         eye4.move(-5, 0)
...         mouth2.move(-5,0)
...         time.sleep(.05)
... 
...     for i in range(46):
...         cir1.move(-5, 0)
...         eye1.move(-5, 0)
...         eye2.move(-5, 0)
...         mouth1.move(-5, 0)
...         cir2.move(5,0)
...         eye3.move(5, 0)
...         eye4.move(5, 0)
...         mouth2.move(5, 0)
...         time.sleep(.05)
... 
...         
>>> main()
