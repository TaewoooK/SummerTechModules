class Card:

	def __init__(self, value, suit, cardNum):
		self.value = value
		self.suit = suit
		self.cardNum = cardNum

	def getValue(self):
		return self.value
		
	def setValue(self, value):
		self.value = value
	
	def getSuit(self):
		return self.suit

	def __str__(self):
		if self.suit == 1:
			if self.cardNum == 11:
				return "Jack of Clovers"
			if self.cardNum == 12:
				return "Queen of Clovers"
			if self.cardNum == 13:
				return "King of Clovers"
			if self.cardNum == 14:
				return "Ace of Clovers"
			else:
				return str(self.value) + " of Clovers"

		elif self.suit == 2:
			if self.cardNum == 11:
				return "Jack of Hearts"
			if self.cardNum == 12:
				return "Queen of Hearts"
			if self.cardNum == 13:
				return "King of Hearts"
			if self.cardNum == 14:
				return "Ace of Hearts"
			else:
				return str(self.value) + " of Hearts"
				
		elif self.suit == 3:
			if self.cardNum == 11:
				return "Jack of Diamonds"
			if self.cardNum == 12:
				return "Queen of Diamonds"
			if self.cardNum == 13:
				return "King of Diamonds"
			if self.cardNum == 14:
				return "Ace of Diamonds"
			else:
				return str(self.value) + " of Diamonds"
		else:
			if self.cardNum == 11:
				return "Jack of Spades"
			if self.cardNum == 12:
				return "Queen of Spades"
			if self.cardNum == 13:
				return "King of Spades"
			if self.cardNum == 14:
				return "Ace of Spades"
			else:
				return str(self.value) + " of Spades"

