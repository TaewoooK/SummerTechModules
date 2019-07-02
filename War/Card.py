class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def getValue():
        return value
    
    def getSuit():
        return suit

    def __str__():
        if suit == 1:
			if value == 11:
				return "Jack of Clovers"
			if value == 12:
				return "Queen of Clovers"
			if value == 13:
				return "King of Clovers"
			if value == 14:
				return "Ace of Clovers"
			else:
				return value + " of Clovers"
	    
        elif suit == 2:
			if value == 11:
				return "Jack of Hearts"
			if value == 12:
				return "Queen of Hearts"
			if value == 13:
				return "King of Hearts"
			if value == 14:
				return "Ace of Hearts"
			else:
				return value + " of Hearts"
		    
        elif suit == 3:
			if value == 11:
				return "Jack of Diamonds"
			if value == 12:
				return "Queen of Diamonds"
			if value == 13:
				return "King of Diamonds"
			if value == 14:
				return "Ace of Diamonds"
			else:
				return value + " of Diamonds"
        
        else:
			if value == 11:
				return "Jack of Spades"
			if value == 12:
				return "Queen of Spades"
			if value == 13:
				return "King of Spades"
			if value == 14:
				return "Ace of Spades"
			else:
				return value + " of Spades"
		
