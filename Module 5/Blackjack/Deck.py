from Card import Card
class Deck:

    def __init__(self):
        self.deck = []
        for i in range(1, 5):
            for j in range(2, 15):
                self.deck.append(Card(j, i, j))

    def dealCard(self):
        if len(self.deck) > 0:    
            return list.pop(self.deck)
        return None

    def addCard(self, card):
        self.deck.append(card)

    def __str__(self):
        if len(self.deck) <= 0:
            return "Empty"
        all = ""
        for i in range(0, len(self.deck)):
            all += str(self.deck[i]) + ", "
        return all
    
        