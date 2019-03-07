# 350112
# a4 2.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from graphics import *

def main():
    win = GraphWin("Face", 200, 200)

    lista=[Point(100,80),Point(95,95),Point(105,95)]
    
    face=Circle(Point(100,80),40)
    face.setFill('blue')
    face.setOutline('black')
    face.draw(win)

    leftEye = Circle(Point(90,70), 5)
    leftEye.setFill('yellow')
    leftEye.setOutline('red')
    rightEye = leftEye.clone()
    rightEye.move(20,0)
    leftEye.draw(win)
    rightEye.draw(win)

    nose=Polygon(lista)
    nose.setFill('yellow')
    nose.setOutline('red')
    nose.draw(win)

    mouth=Oval(Point(80,100),Point(120,105))
    mouth.setFill('red')
    mouth.setOutline('red')
    mouth.draw(win)

    Leftear=Circle(Point(60,75),7)
    Leftear.setFill('yellow')
    Leftear.setOutline('red')
    Rightear=Leftear.clone()
    Rightear.move(80,0)
    Leftear.draw(win)
    Rightear.draw(win)

    #The drawing is closing when the mouse is clicked
    p=win.getMouse()

    win.close()

main()
