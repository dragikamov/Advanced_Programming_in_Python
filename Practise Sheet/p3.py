#Problem 3

file=input("Enter file name:\n")
try:
    f=open(file,'r')
    for line in f:
        print(line,end="")
    f.close()
except IOError:
    print('Could not open "{}"'.format(file))
