"""
350112
a1 2.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

def in2cm_table(x,y,step):
    print("inch\tcm")
    while x<=y:
        print("{:.1f}\t{:.1f}".format(x,x*2.54))
        x+=step
    
