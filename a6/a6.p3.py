# 350112
# a6 3.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from random import random, randrange

wins={'A' : 0, 'B' : 0 }
prob={'A' : 0, 'B' : 0 }
score={'A' : 0, 'B' : 0 }
check=0

def printIntro():
    print("This program simulates a volleyball game between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")

def getInputs():
    prob['A']=float(input("What is the probability player A wins a serve?\n"))
    prob['B']=float(input("What is the probability that player B wins a serve?\n"))
    n=int(input("How many games to simulate?\n"))
    check=int(input("Is the game sanctioned? [1/0]\n"))
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
            if check==1:
                score[ord(serving)]+=1

def gameOver():
    if check==0:
        return (score['A'] >= 15 and score['A']-score['B']>=2
                ) or (score['B']== 15 and score['B']-score['A']>=2)
    else:
        return (score['A'] >= 25 and score['A']-score['B']>=2
                ) or (score['B']== 25 and score['B']-score['A']>=2)

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
