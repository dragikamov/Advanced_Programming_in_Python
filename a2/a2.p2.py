"""
350112
a2 2.py
Dragi Kamov
d.kamov@jacobs-university.de
"""

from craps import (Player,playOneGame,playManyGames)
from die import Die

string=input("Enter how many games you want to play ")
while True:
    string=string.lower()
    if string=="one" or string=="1":
        playOneGame()
    else:
        playManyGames()
    ask=input("Do you wish to continue?\n")
    ask=ask.lower()
    if ask=="yes":
        string=input("Enter how many games you want to play ")
    else:
        break
