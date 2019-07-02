class Deck:

    def __init__(self):
        self.deck = []
        for i in range(1, 5):
            for j in range(2, 15):
                self.deck.append(Card(j, i))

    def dealCard():
        if len(deck) > 0:    
            return deck.remove(0)
        return None

    def addCard(card):
        deck.append(card)

    def __str__():
        for i in range (0, 52):
            print(deck[i], end=" ")
    

        
        