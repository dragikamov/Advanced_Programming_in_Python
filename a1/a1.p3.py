"""
350112
a1 3.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

import mod_conversion2

x=int(input("Enter the start value: "))
y=int(input("Enter the end value: "))
step=int(input("Enter the step value: "))

ch=input("Enter a character: ")
f=open("in2cm.html",'w')
mod_conversion2.in2cm_table(x,y,step,ch,f)
f.close()
