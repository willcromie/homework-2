>>> from graphics import *
>>> def main():
...     win = GraphWin('change scene', 200, 150) 
...     win.yUp() 
...     head = Circle(Point(40,100), 25) 
...     head.setFill("yellow")
...     head.draw(win)
...     eye1 = Line(Point(30, 105), Point(40, 105))
...     eye1.setWidth(3)
...     eye1.draw(win)
...     eye2 = Line(Point(45, 105), Point(55, 105)) 
...     eye2.setWidth(3)
...     eye2.draw(win)
...     mouth = Oval(Point(30, 90), Point(50, 85)) 
...     mouth.setFill("red")
...     mouth.draw(win)
...     win.getMouse()
...     eye3 = Circle(Point(30, 105), 5)
...     eye3.setFill('black')
...     eye3.draw(win)
...     eye4 = Circle(Point(45, 105), 5)
...     eye4.setFill('black')
...     eye4.draw(win)
... 
...     
>>> main()









