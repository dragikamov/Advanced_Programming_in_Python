# 350112
# a3 1.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from student import Student


name1=input("Enter the first student's name: ")
name2=input("Enter the second student's name: ")
s1=Student(name1,2)
s2=Student(name2,3)
print("Checking for not being equal")

if s1!=s2:
    print("The students names are not equal")
else s1==s2:
    print("The students names are the same")

if s1<s2:
    print("Student 1's name is smaller than Student 2's name")
elif s1>s2:
    print("Student 1's name is larger than Student 2's name")
