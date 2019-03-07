"""
350112
a1 3.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def in2cm_table(x,y,step,ch,f):
    if ch=='s':
        print("inch\tcm")
        while x<=y:
            print("{:.1f}\t{:.1f}".format(x,x*2.54))
            x+=step
    else:
        f.write("inch &nbsp cm</p>")
        while x<=y:
            f.write("{:.1f} &nbsp {:.1f}</p>".format(x,x*2.54))
            x+=step
