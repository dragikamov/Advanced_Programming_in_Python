# 350112
# a3 2.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from student import Student
import random

students=[]
names=["Mark","Hendrik","Roa","Cheeku","Theo","Lina","Emily","Nadia","Jasmine","Antonia","Scott","Andrei","Joseph"]

random.shuffle(names)
for n in names:
    students.append(Student(n,2))

print("Original list:")
for s in students:
    print(s.getName())

random.shuffle(students)
print("\nShuffled list:")
for s in students:
    print(s.getName())

students.sort()
print("\nSorted:")
for s in students:
    print(s.getName())
