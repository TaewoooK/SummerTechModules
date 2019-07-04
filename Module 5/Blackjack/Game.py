from Deck import Deck
import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

def changeValue(Deck):
    for i in range(len(Deck.deck)):
        if Deck.deck[i].getValue() == 11 or Deck.deck[i].getValue() == 12 or Deck.deck[i].getValue() == 13:
            Deck.deck[i].setValue(10)
        if Deck.deck[i].getValue() == 14:
            Deck.deck[i].setValue(11)
    return Deck

mainDeck = Deck()
mainDeck = changeValue(mainDeck)

print("Welcome to Blackjack")

p1Deck = Deck()
p2Deck = Deck()

#shuffle Deck
random.shuffle(mainDeck.deck)

#Empty out player decks
for i in range(0, 52):
    p1Deck.dealCard()

for i in range(0, 52):
    p2Deck.dealCard()

for i in range(2):
    p1Deck.addCard(mainDeck.dealCard())
    p2Deck.addCard(mainDeck.dealCard())

print("The deck has been shuffled")
print("Each player has two cards")
print("==========================")

print("Player 1's cards")
value = 0
for i in range (len(p1Deck.deck)):
    value += p1Deck.deck[i].getValue()
print(p1Deck)
print("The total value:", value)
print("==========================")
print("Player 2's top card")
print(p2Deck.deck[0])

ans = False
again = True

#Player 1 Done
while again == True:
    ans = False
    while ans == False:
        print("==========================")
        option = int(input("Type \"1\" to hit, Type \"2\" to pass "))
        if option == 1:
            p1Deck.addCard(mainDeck.dealCard())
            value = 0
            for i in range (len(p1Deck.deck)):
                value += p1Deck.deck[i].getValue()

            print(p1Deck)
            print("The total value:", value)

            for i in range (len(p1Deck.deck)):
                if p1Deck.deck[i].getValue() == 11:
                    print("==========================")
                    ace = input("Do you want to change the value of Ace? (y/n) ")
                    if ace == "y":
                        if p1Deck.deck[i].getValue() == 11:
                            p1Deck.deck[i].setValue(1)
                            value = 0
                            for i in range (len(p1Deck.deck)):
                                value += p1Deck.deck[i].getValue()
                            print(p1Deck)
                            print("The total value:", value)
                        else:
                            p1Deck.deck[i].setValue(11)

            ans = True
        elif option == 2:
            print("Passed")
            ans = True
            again = False
        else:
            print("Invalid Input")

if value > 21:
    print("==========================")
    print("Player 1 is over 21")

#Player 2 Computer Start...
p2 = True
while p2 == True:
    p2Value = 0
    for i in range (len(p2Deck.deck)):
        p2Value += p2Deck.deck[i].getValue()

    if p2Value <= 13:
        p2Deck.addCard(mainDeck.dealCard())
    else:
        p2 = False

    for i in range (len(p1Deck.deck)):
        if p1Deck.deck[i].getValue() == 11:
            if p2Value > 20:
                p2Deck.deck[i].setValue(1)

    p2Value = 0
    for i in range (len(p2Deck.deck)):
        p2Value += p2Deck.deck[i].getValue()

print("Player 2's value:", end=" ")
print(p2Value)

if p2Value > 21:
    print("Player 2 is over 21")

#Win statements
print("==========================")
if value > 21 and p2Value > 21:
    print("Both lose")
elif p2Value > 21:
    print("Player 1 Wins!")
elif value > 21:
    print("Player 2 Wins!")
elif value > p2Value:
    print("Player 1 Wins!")
elif p2Value > value:
    print("Player 2 Wins!")
else:
    print("There is a tie!")

