"""
350112
a2 5.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

import student

s1=student.Student("John",3,25)
s1.setScore(1,100)
s1.setScore(2,95)
s1.setScore(3,50)

print("Before change:\n",s1,sep="")
s1.setName("Jack")
s1.setAge(30)
print("\nAfter change:\n",s1,sep="")
