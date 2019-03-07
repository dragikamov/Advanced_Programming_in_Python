#Problem 1

start=int(input("Enter a start length: "))
end=int(input("Enter a end length: "))
step=int(input("Enter a step size: "))

print("mile\tm")
while(start<=end):
    print("{0:.1f}\t{1:.1f}".format(start,start*1609.344))
    start+=step
