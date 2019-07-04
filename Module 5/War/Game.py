from Deck import Deck
import random

def p1CheckForWin(Deck):
    if len(Deck.deck) == 0:
        print("Player 2 Wins!")
        return True
    return False

def p2CheckForWin(Deck):
    if len(Deck.deck) == 0:
        print("Player 1 Wins!")
        return True
    return False

mainDeck = Deck()

print("Welcome to War!")

p1Deck = Deck()
p1DealDeck = Deck()
p2Deck = Deck()
p2DealDeck = Deck()

#shuffle Deck
random.shuffle(mainDeck.deck)

#Empty out player decks
for i in range(0, 52):
    p1Deck.dealCard()

for i in range(0, 52):
    p2Deck.dealCard()

for i in range(0, 52):
    p1DealDeck.dealCard()

for i in range(0, 52):
    p2DealDeck.dealCard()

#Put cards in each Deck
for i in range(0, 26):
    p1Deck.addCard(mainDeck.dealCard())

for i in range(0, 26):
    p2Deck.addCard(mainDeck.dealCard())

print("The deck has been shuffled and distributed evenly")
print("==================================================")

end = False

while end == False:
    enter = input("Press \"ENTER\" to deal card")

    p1DealDeck.addCard(p1Deck.dealCard())
    p2DealDeck.addCard(p2Deck.dealCard())

    print(p1DealDeck)
    print(p2DealDeck)

    onCard = 0
    loop = True

    while loop == True:
        if p1DealDeck.deck[len(p1DealDeck.deck)-1].getValue() > p2DealDeck.deck[len(p2DealDeck.deck)-1].getValue():
            print("Player 1 has a larger hand")
            for i in range(len(p1DealDeck.deck)):
                p1Deck.addCard(p1DealDeck.dealCard())
                p1Deck.addCard(p2DealDeck.dealCard())
            loop = False
            end = p1CheckForWin(p1Deck)
            if end != True:
                end = p2CheckForWin(p2Deck)
        elif p1DealDeck.deck[len(p1DealDeck.deck)-1].getValue() < p2DealDeck.deck[len(p2DealDeck.deck)-1].getValue():
            print("Player 2 has a larger hand")
            for i in range(len(p2DealDeck.deck)):
                p2Deck.addCard(p1DealDeck.dealCard())
                p2Deck.addCard(p2DealDeck.dealCard())
            loop = False
            end = p1CheckForWin(p1Deck)
            if end != True:
                end = p2CheckForWin(p2Deck)
        else:
            print("Each player has the same hand")
            print("Three cards are put down")
            
            if len(p1Deck.deck) < 3:
                for i in range (len(p1Deck.deck)):
                    p1DealDeck.addCard(p1Deck.dealCard())
                    print(p1DealDeck)
            else:
                for i in range (3):
                    p1DealDeck.addCard(p1Deck.dealCard())
                    print(p1DealDeck)
            if len(p2Deck.deck) < 3:
                for i in range (len(p2Deck.deck)):  
                    p2DealDeck.addCard(p2Deck.dealCard())
                    print(p2DealDeck)
            else:
                for i in range (3):  
                    p2DealDeck.addCard(p2Deck.dealCard())
                    print(p2DealDeck)
                
        