class Card:
	suitList = ['Clubs','Diamonds','Hearts','Spades']
	rankList = ['narf','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
	def __init__(self,suit = 0,rank = 1):
		self.suit = suit
		self.rank = rank	
	def __cmp__(self,other):
		if(self.rank>other.rank):
			return 1
		if(self.rank<other.rank):
			return -1
		if(self.suit>other.suit):
			return 1
		if(self.suit<other.suit):
			return -1
		return 0;
	def __str__(self):
		return self.suitList[self.suit]+' of '+self.rankList[self.rank]

class Deck:
	cards = []	
	def __init__(self):
		for i in range(4):
			for j in range(1,14):
				self.cards.append(Card(i,j))	
	def printDeck(self):
		for i in self.cards:
			print i
	def __str__(self):
		nCards = len(self.cards)	
		s = ""
		for i in range(nCards):
			s = s+ i*' ' + str(self.cards[i])+'\n'
		return s
	def shuffle(self):
		import random
		nCards = len(self.cards)		
		for i in range(nCards):
			j = random.randrange(i,nCards)	
			self.cards[i],self.cards[j] = self.cards[j],self.cards[i]

	def remove(self,card):
		if card in self.cards:
			self.cards.remove(card)	
			return True
		else:
			return False
	def popCard(self):
		return self.cards.pop()	
	def isEmpty(self):
		return (len(self.cards)==0)

	def deal(self,hands,nCards = 999):
		nHands = len(hands)	
		for i in range(nCards):
			if self.isEmpty():
				break
			hands[i%nHands].addCard(self.popCard())

class Hand(Deck):
	def __init__(self,name = ''):
		self.cards = []
		self.name = name
	def __str__(self):
		s = 'hand ' + self.name	
		if self.isEmpty():
			return s+' is Empty\n'
		else:
			return s+ ' contains\n' + Deck.__str__(self)
	def addCard(self,card):
		self.cards.append(card);

class CardGame:
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()

class OldMaidHand(Hand):
	def removeMatches(self):
		count = 0
		copyCards = self.cards[:]		
		for card in copyCards:
			matchCard = Card(3-card.suit,card.rank)
			if matchCard in self.cards:
				self.cards.remove(card)
				self.cards.remove(matchCard)
				print 'hand %s:%s match %s'%(self.name,card,matchCard)
				count = count + 1
		return count

class OldMaidGame(CardGame):
	def play(self,names):
		self.deck.remove(Card(0,12))
		self.hands = []
		for name in names:
			self.hands.append(OldMaidHand(name))	
		self.deck.deal(self.hands)
		print '-----------------cards have been dealt'
		self.printHands()
		matches = self.removeAllMatches()	
		print matches
		print '----------------AllMathces discard'
		self.printHands()
		turn = 0
		nHands = len(self.hands)
		while matches<25:
			matches = matches + self.playOneTurn(turn)
			turn = (turn+1)%nHands
		print '--------------------Game is Over'
		self.printHands()
	def removeAllMatches(self):
		count = 0
		for hand in self.hands:
			count = count + hand.removeMatches()	
		return count
	def printHands(self):
		for hand in self.hands:
			print hand
	def playOneTurn(self,turn):
		if self.hands[turn].isEmpty():
			return 0		
		neighbor = self.findNeighbor(turn)
		pickedCard = self.hands[neighbor].popCard()
		self.hands[turn].addCard(pickedCard)
		print 'Hand',self.hands[turn].name,'picked',pickedCard
		count = self.hands[turn].removeMatches()
		self.hands[turn].shuffle()
		return count
	def findNeighbor(self,turn):
		nHands = len(self.hands)	
		for next in range(1,nHands):
			neighbor = (turn+next)%nHands
			if not self.hands[neighbor].isEmpty():
				return neighbor

game = OldMaidGame()
game.play(['Luffy','Sabo','Zoro'])
