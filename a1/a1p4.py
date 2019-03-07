"""
350112
a1 4.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

stack=[]

def isEmpty():
    if stack==[]:
        return True
    else:
        return False

def empty():
    while isEmpty()==False:
            stack.pop()

def push(i):
    stack.append(i)

def pop():
    return stack.pop()

while True:
    ch=input()
    if ch=='s':
        i=int(input())
        push(i)
        print("Pushing",i)
    elif ch=='p':
        if isEmpty()==True:
            print("Stack underflow")
        else:
            print("Popping element {:}".format(pop()))
    elif ch=='e':
        empty()
        print("Emptying stack")
    elif ch=='q':
        print("Good Bye!")
        break
        
