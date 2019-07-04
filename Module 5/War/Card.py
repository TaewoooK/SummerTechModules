class Card:

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def getValue(self):
		return self.value
	
	def getSuit(self):
		return self.suit

	def __str__(self):
		if self.suit == 1:
			if self.value == 11:
				return "Jack of Clovers"
			if self.value == 12:
				return "Queen of Clovers"
			if self.value == 13:
				return "King of Clovers"
			if self.value == 14:
				return "Ace of Clovers"
			else:
				return str(self.value) + " of Clovers"

		elif self.suit == 2:
			if self.value == 11:
				return "Jack of Hearts"
			if self.value == 12:
				return "Queen of Hearts"
			if self.value == 13:
				return "King of Hearts"
			if self.value == 14:
				return "Ace of Hearts"
			else:
				return str(self.value) + " of Hearts"
				
		elif self.suit == 3:
			if self.value == 11:
				return "Jack of Diamonds"
			if self.value == 12:
				return "Queen of Diamonds"
			if self.value == 13:
				return "King of Diamonds"
			if self.value == 14:
				return "Ace of Diamonds"
			else:
				return str(self.value) + " of Diamonds"
		else:
			if self.value == 11:
				return "Jack of Spades"
			if self.value == 12:
				return "Queen of Spades"
			if self.value == 13:
				return "King of Spades"
			if self.value == 14:
				return "Ace of Spades"
			else:
				return str(self.value) + " of Spades"

