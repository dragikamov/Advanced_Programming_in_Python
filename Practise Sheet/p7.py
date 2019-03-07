#Problem 7

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
        return "Name: " + self.first + "\nLast: " + self.last \
               + "\nMajor: " + self.major + "\n"
    def __eq__(self,other):
        if(self.first==other.first and self.last==other.last
           and self.major==other.major):
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
    f1=input("Enter the first student's first name:\n")
    l1=input("Enter the first student's last name:\n")
    m1=input("Enter the first student's major:\n")

    f2=input("Enter the second student's first name:\n")
    l2=input("Enter the second student's last name:\n")
    m2=input("Enter the second student's major:\n")
    
    s1=Student(f1,l1,m1)
    print(s1)
    s2=Student(f2,l2,m2)
    print(s2)
    if(s1==s2):
        print("The two students are the same")
    else:
        print("The two students are not the same")
    if(s1>s2):
        print("Student 1 is alphabeticaly greater than Student 2")
    elif(s1<s2):
        print("Student 1 is alphabeticaly smaller than Student 2")
    

main()
