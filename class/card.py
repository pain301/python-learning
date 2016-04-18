class Card:
	suitList = ['Clubs','Diamonds','Hearts','Spades']
	rankList = ['narf','Ace','2','3','4','5','6','7','8','9','10',
			'Jack','Queen','King']
	def __init__(self,suit = 0,rank = 2):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return self.rankList[self.rank]+' of '+self.suitList[self.suit]
	def __cmp__(self,other):
		if self.suit>other.suit:
			return 1
		if self.suit<other.suit:
			return -1
		if self.rank>other.rank:
			return 1
		if self.rank<other.rank:
			return -1
		return 0

class Deck:
	def __init__(self):
		self.cards = []	
		for suit in range(4):
			for rank in range(1,14):
				self.cards.append(Card(suit,rank))	
	def printDeck(self):
		for card in self.cards:
			print card

	def __str__(self):
		s = ""
		for i in range(len(self.cards)):
			s = s + " "*(i % len(Card.rankList))+str(self.cards[i])+'\n'
		return s
	def shuffle(self):
		import random
		nCards = len(self.cards)
		for i in range(nCards):
			j = random.randrange(i,nCards)
			self.cards[i],self.cards[j] = self.cards[j],self.cards[i]
	def removeCard(self,card):
		if card in self.cards:
			self.cards.remove(card)	
			return True
		else:
			return False
	def popCard(self):
		return self.cards.pop()

	def isEmpty(self):
		return (len(self.cards)==0)

card1 = Card(2,11)
card2 = Card(3,10)
print card1
print card2
print card1<card2

deck = Deck()
deck.printDeck()
print '-------------------------'
deck.shuffle()
deck.printDeck()

print deck.removeCard(Card(0,13))

while not deck.isEmpty():
	print deck.popCard()
