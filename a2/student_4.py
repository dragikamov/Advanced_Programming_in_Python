"""
350112
a2 4.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number, age):
        """All scores are initially 0."""
        print("Constructor being called")
        self._name = name
        self._scores = []
        self._age=age
        for count in range(number):
            self._scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self._name

    def setName(self,name):
        self._name=name

    def setAge(self,age):
        self._age=age

    def getAge(self):
        return self._age
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self._scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self._scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self._scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self._scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self._name  + "\nScores: " + \
             " ".join(map(str, self._scores)) + "\nAge: " + \
             str(self._age)

