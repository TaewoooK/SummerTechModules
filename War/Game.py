from Deck import Deck
import random

mainDeck = Deck()

print("Welcome to War!")
mainDeck = mainDeck.shuffle()

p1Deck = Deck()
p2Deck = Deck()

#Empty out player decks
for i in range(0, 52):
    p1Deck.dealCard()

for i in range(0, 52):
    p2Deck.dealCard()

#Put cards in each Deck
for i in range(0, 26):
    p1Deck.addCard(mainDeck.dealCard())

for i in range(0, 26):
    p2Deck.addCard(mainDeck.dealCard())

print("The deck has been shuffled and distributed evenly")

print(p1Deck)
print(p2Deck)
