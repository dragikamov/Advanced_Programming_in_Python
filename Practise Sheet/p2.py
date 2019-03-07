#Problem 2

start=int(input("Enter a start length: "))
end=int(input("Enter a end length: "))
step=int(input("Enter a step size: "))
file=input("Name of file: ")

if file=="":
    print("mile\tm")
    while(start<=end):
        print("{0:.1f}\t{1:.1f}".format(start,start*1609.344))
        start+=step
else:
    f=open(file,'w')
    f.write("mile\tm\n")
    while(start<=end):
        f.write("{0:.1f}\t{1:.1f}\n".format(start,start*1609.344))
        start+=step
    f.close()
