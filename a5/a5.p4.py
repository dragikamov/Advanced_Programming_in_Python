# 350112
# a5 4.py
# Dragi Kamov
# d.kamov@jacobs-university.de

f=open("mountains.csv",'r')
w=open("conv.html",'w')

w.write(str('<table style="width:100%">'))
for i in f:
    check=0
    check2=0
    w.write("<tr>")
    for j in i:
        if(j=='"' and check==0):
            w.write("<td>")
            check=1
        elif(j=='"' and check==1):
            w.write("</td>")
            check=0
        elif(check==0 and j>='0' and j<='9' and check2==0):
            w.write("<td>")
            w.write(j)
            check2=1
        elif(check2==1 and j==","):
            w.write("</td>")
            check2=0
        elif(check==0 and check2==0):
            continue
        else:
            w.write(j)
    w.write("</tr>")
w.write("</table>")
f.close()
w.close()
