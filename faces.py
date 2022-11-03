Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from graphics import *
>>> win = GraphWin('Faces',200,150)
>>> win.yUp()
>>> def main():
...     for i in range(6):
...         win.getMouse()
...         head = Circle(Point(40,100), 25)
...         head.setFill("yellow")
...         head.draw(win)
...         eye1 = Circle(Point(30, 105), 5)
...         eye1.setFill('blue')
...         eye1.draw(win)
...         eye2 = Line(Point(45, 105), Point(55, 105))
...         eye2.setWidth(3)
...         eye2.draw(win)
...         mouth = Oval(Point(30, 90), Point(50, 85))
...         mouth.setFill("red")
...         mouth.draw(win)
... 
>>> main()
