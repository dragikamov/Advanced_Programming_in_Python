# 350112
# a5 3.py
# Dragi Kamov
# d.kamov@jacobs-university.de

import ppmview
import struct

f=open("ascteapot.ppm",'w')
f.write("P6\n")
f.write("498 300\n")
f.write("255\n")
f.close()

f=open("ascteapot.ppm",'ab')

for i in range(300):
    for j in range(498):
        if j//166==0:
            red=0
            green=255
            blue=0
            data=struct.pack("<3B",0,255,0)
            f.write(data)
        elif j//166==1:
            red=0
            green=0
            blue=0
            data=struct.pack("<3B",0,0,0)
            f.write(data)
        elif j//166==2:
            red=255
            green=0
            blue=0
            data=struct.pack("<3B",255,0,0)
            f.write(data)
f.close()
