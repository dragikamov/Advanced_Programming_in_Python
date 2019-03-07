#Problem 8

from random import shuffle

class Student:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        #self.major=major
    def setFirst(self,first):
        self.first=first
    def setLast(self,last):
        self.last=last
    #def setMajor(self,major):
        #self.major=major
    def getFirst(self):
        return self.first
    def getLast(self):
        return self.last
    #def getMajor(self):
        #return self.major
    def __str__(self):
        return "Name: " + self.first + "\nLast: " + self.last + "\n"
    def __eq__(self,other):
        if(self.first==other.first and self.last==other.last):
           return True
        else:
           return False
    def __gt__(self,other):
        if(self.first>other.first):
            return True
        else:
            return False
    def __lt__(self,other):
        if(self.first<other.first):
            return True
        else:
            return False

def main():
    first=["John","Lara","Mark","Rebekka","Dushan","Jovana","Ana","Irma","Emily","Roa"]
    shuffle(first)
    last=["Smith","Kroft","Ali","Terzikj","Gjorgjioska","Krstevska","Doe","Brr","GAAA","NOO"]
    shuffle(last)
    l1=[]
    for i in range(10):
        l1.append(Student(first[i],last[i]))
    print("Shuffled:\n")
    for i in range(10):
        print(l1[i])
    l1.sort()
    print("Sorted:\n")
    for i in range(10):
        print(l1[i])
    

main()
