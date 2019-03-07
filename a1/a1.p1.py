"""
350112
a1 1.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

x=int(input("Enter the start value: "))
y=int(input("Enter the end value: "))
step=int(input("Enter the step value: "))

print("inch\tcm")
while x<=y:
    print("{:.1f}\t{:.1f}".format(x,x*2.54))
    x+=step
