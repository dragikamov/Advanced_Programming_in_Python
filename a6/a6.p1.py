# 350112
# a6 1.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from random import random, randrange

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def getInputs():
    probA=float(input("What is the probability player A wins a serve?\n"))
    probB=float(input("What is the probability that player B wins a serve?\n"))
    n=int(input("How many games to simulate?\n"))
    return probA, probB, n

def simNGames(n, probA, probB):
    winsA=0
    winsB=0
    for i in range(n):
        scoreA,scoreB=simOneGame(probA,probB)
        if scoreA>scoreB:
            winsA=winsA+1
        else:
            winsB=winsB+1
    return winsA, winsB
        
def simOneGame(probA,probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    n = winsA + winsB
    print ("\nGames simulated:", n)
    print ("Wins for A:{0}({1:0.1%})".format(winsA, winsA / n))
    print ("Wins for B:{0}({1:0.1%})".format(winsB, winsB / n))

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()
