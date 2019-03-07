# 350112
# a4 1.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from graphics import *

def main():
    win = GraphWin()
    
    for i in range(10):
            shape = Rectangle(Point(30, 30), Point(70, 70))
            shape.setOutline("red")
            shape.setFill("red")
            shape.draw(win)
            p = win.getMouse()
            c = shape.getCenter()
            dx = p.getX() - c.getX()
            dy = p.getY() - c.getY()
            shape.move(dx, dy)
    win.close()

main()
