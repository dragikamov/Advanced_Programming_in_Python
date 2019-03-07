# 350112
# a4 4.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from graphics import *

def main():
    win = GraphWin(1000,1000)
    p = win.getMouse()
    q = win.getMouse()
    dx1 = p.getX()
    dy1 = p.getY()
    dx2 = q.getX()
    dy2 = q.getY()
    shape = Rectangle(Point(dx1, dy1), Point(dx2, dy2))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    length=abs(dx1-dx2)
    width=abs(dy1-dy2)

    print("x1={:} y1={:}\nx2={:} y2={:}".format(dx1,dy1,dx2,dy2))
    print("The perimeter is",2*(length+width))
    print("The area is",length*width)
    r = win.getMouse()
    win.close()

main()
