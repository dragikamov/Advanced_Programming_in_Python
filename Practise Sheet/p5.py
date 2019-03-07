# Problem 5

queue=[]

def push(a):
    queue.append(a)

def pop():
    return queue.pop(0)

def is_empty():
    if queue==[]:
        return True
    else:
        return False

def empty():
    while(is_empty()==False):
        queue.pop()

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
                print("The queue is empty")
            else:
                print("The queue is not empty")
        elif(c=='q'):
            break
        else:
            print("Wrong input")
main()
