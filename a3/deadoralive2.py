# 350112
# a3 4.py
# Dragi Kamov
# d.kamov@jacobs-university.de

from cards import Deck, Card

class Player(object):

    def __init__(self, cards):
        self._cards = cards

    def __str__(self):
        result = str(self._cards.pop())
        return result

    def hit(self, card):
        self._cards.append(card)

    #gives me the current card
    def getCard(self):
        return self._cards.pop()

    def getPoints(self):
        count = 0
        for card in self._cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        
        for card in self._cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        """Dealt 21 or not."""
        return len(self._cards) == 2 and self.getPoints() == 21 


class Dealer(Player):
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        """Initial state: show one card only."""
        Player.__init__(self, cards)
        self._showOneCard = True

    def __str__(self):
        """Return just one card if not hit yet."""
        if self._showOneCard:
            return str(self._cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        """Add cards while points < 17,
        then allow all to be shown."""
        self._showOneCard = False
        while self.getPoints() < 17:
            self._cards.append(deck.deal())

class Deadoralive(object):
    def __init__(self):
        self._deck=Deck()
        self._deck.shuffle()
        self._player1=Player([])
        self._player2=Player([])

    def play(self):
        win1=0
        win2=0
        check=0
        for i in range(26):
            ch=input("Press [y] to continue or any other to quit: ")
            if ch=='Y' or ch=='y':
                self._player1.hit(self._deck.deal())
                self._player2.hit(self._deck.deal())
                card1=self._player1.getCard()
                card1a=card1.rank
                card2=self._player2.getCard()
                card2a=card2.rank
                print("Player 1:\n",card1a)
                print("Player 2:\n",card2a)
                if(card1a>card2a):
                    print("Player 1 won")
                    win1+=1
                elif(card2a>card1a):
                    print("Player 2 won")
                    win2+=1
                else:
                    check=1
                    elif card1.suit==card2.suit:
                        print("TIE")
                if i==25:
                    print("\nPlayer 1:",win1,"wins")
                    print("Player 2:",win2,"wins")
            else:
                print("Player 1:",win1,"wins")
                print("Player 2:",win2,"wins")
                if(max(win1,win2)==win1):
                    print("\nGrand winner is Player 1 with ",win1,"wins",end="")
                else:
                    print("\nGrand winner is Player 2 with ",win2,"wins",end="")
                if check==1:
                    print("and it counts as double.")
                break

class Blackjack(object):

    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._player = Player([self._deck.deal(), self._deck.deal()])
        self._dealer = Dealer([self._deck.deal(), self._deck.deal()])

    def play(self):
        print("Player:\n", self._player)
        print("Dealer:\n", self._dealer)
        while True:
            choice = input("Do you want a hit? [y/n]: ")
            if choice in ("Y", "y"):
                self._player.hit(self._deck.deal())
                points = self._player.getPoints()
                print("Player:\n", self._player)
                if points >= 21:
                    break
            else:
                break
        playerPoints = self._player.getPoints()
        if playerPoints > 21:
            print("You bust and lose")
        else:
            self._dealer.hit(self._deck)
            print("Dealer:\n", self._dealer)
            dealerPoints = self._dealer.getPoints()
            if dealerPoints > 21:
                print("Dealer busts and you win")
            elif dealerPoints > playerPoints:
                print("Dealer wins")
            elif dealerPoints < playerPoints and playerPoints <= 21:
                print("You win")
            elif dealerPoints == playerPoints:
                if self._player.hasBlackjack() and not self._dealer.hasBlackjack():
                    print("You win")
                elif not self._player.hasBlackjack() and self._dealer.hasBlackjack():
                    print("Dealer wins")
                else:
                    print("There is a tie")
        
def main():
    game = Deadoralive()
    game.play()

main()
  
