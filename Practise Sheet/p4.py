# Problem 4

stack=[]

def push(a):
    stack.append(a)

def pop():
    return stack.pop()

def is_empty():
    if stack==[]:
        return True
    else:
        return False

def empty():
    while(is_empty()==False):
        stack.pop()

def main():
    while(True):
        c=input()
        if(c=='s'):
            x=int(input())
            push(x)
        elif(c=='p'):
            print("Popping",pop())
        elif(c=='e'):
            empty()
        elif(c=='c'):
            if(is_empty()):
                print("The stack is empty")
            else:
                print("The stack is not empty")
        elif(c=='q'):
            break
        else:
            print("Wrong input")
main()
