# 350112
# a6 2.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from random import random, randrange

wins={'A' : 0, 'B' : 0 }
prob={'A' : 0, 'B' : 0 }
score={'A' : 0, 'B' : 0 }


def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def getInputs():
    prob['A']=float(input("What is the probability player A wins a serve?\n"))
    prob['B']=float(input("What is the probability that player B wins a serve?\n"))
    n=int(input("How many games to simulate?\n"))
    return n

def simNGames(n):
    for i in range(n):
        simOneGame()
        if score['A']>score['B']:
            wins['A']=wins['A']+1
        else:
            wins['B']=wins['B']+1
x=65
def serve(x):
    if x==65:
        x=66
        return 'B'
    else:
        x=65
        return 'A'
    
def simOneGame():
    score['A'] = 0
    score['B'] = 0
    serving = serve(x)
    while not gameOver():
        if random() < prob[serving]:
            score[serving]=score[serving]+1
        else:
            serving=serve(ord(serving))

def gameOver():
    return score['A'] == 15 or score['B'] == 15

def printSummary():
    n = wins['A'] + wins['B']
    print ("\nGames simulated:", n)
    print ("Wins for A:{0}({1:0.1%})".format(wins['A'], wins['A'] / n))
    print ("Wins for B:{0}({1:0.1%})".format(wins['B'], wins['B'] / n))

def main():
    printIntro()
    n = getInputs()
    simNGames(n)
    printSummary()

main()
