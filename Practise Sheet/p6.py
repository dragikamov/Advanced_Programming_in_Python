#Problem 6

class Student:
    def __init__(self,first,last,major):
        self.first=first
        self.last=last
        self.major=major
    def setFirst(self,first):
        self.first=first
    def setLast(self,last):
        self.last=last
    def setMajor(self,major):
        self.major=major
    def getFirst(self):
        return self.first
    def getLast(self):
        return self.last
    def getMajor(self):
        return self.major
    def __str__(self):
        return "Name:" + self.first + "\nLast:" + self.last

def main():
    s1=Student("Ana","Banana","BCCB")
    print(s1)

main()
