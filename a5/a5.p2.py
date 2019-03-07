# 350112
# a5 2.py
# Dragi Kamov
# d.kamov@jacobs-university.de

import ppmview

f=open("ascteapot.ppm",'w')
f.write("P3\n")
f.write("400 200\n")
f.write("255\n")

for i in range(200):
    for j in range(400):
        if i<50:
            f.write("255 0 0 ")
        elif i<100:
            f.write("0 0 255 ")
        elif i<150:
            f.write("255 255 0 ")
        elif i<200:
            f.write("0 255 0 ")
    f.write("\n")
f.close()
