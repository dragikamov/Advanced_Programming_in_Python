# 350112
# a4 3.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from graphics import *

win = GraphWin(200,200)

def draw_archery(tupple):
    colors=['yellow','red','blue','black','white']
    i=4
    circ1=Circle(Point(tupple[i][0],tupple[i][1]),tupple[i][2])
    circ1.setOutline(colors[i])
    circ1.setFill(colors[i])
    circ1.draw(win)
    i-=1
    
    circ2=Circle(Point(tupple[i][0],tupple[i][1]),tupple[i][2])
    circ2.setOutline(colors[i])
    circ2.setFill(colors[i])
    circ2.draw(win)
    i-=1
    
    circ3=Circle(Point(tupple[i][0],tupple[i][1]),tupple[i][2])
    circ3.setOutline(colors[i])
    circ3.setFill(colors[i])
    circ3.draw(win)
    i-=1
    
    circ4=Circle(Point(tupple[i][0],tupple[i][1]),tupple[i][2])
    circ4.setOutline(colors[i])
    circ4.setFill(colors[i])
    circ4.draw(win)
    i-=1
    
    circ5=Circle(Point(tupple[i][0],tupple[i][1]),tupple[i][2])
    circ5.setOutline(colors[i])
    circ5.setFill(colors[i])
    circ5.draw(win)
    i-=1
    

def main():
    
    draw_archery([(100, 100, 15), (100, 100, 30),(100, 100, 45), (100, 100, 60), (100, 100, 75)])
    p = win.getMouse()
    win.close()

main()
