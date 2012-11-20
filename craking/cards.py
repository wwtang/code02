"""
cards class
"""

class card(object):
	def __init__(self, rank =2,suit = 0):
		self.suit = suit
		self.rank = rank
	rank_name = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']
	suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

	def __str__(self):
		return "%s of %s"%(card.rank_name[self.rank], card.suit_name[self.suit])

	# def __cmp__(self, ohter):
	# 	if self.suit > other.suit: return 1
	# 	if self.suit < other.suit: return -1

	# 	if self.rank > other.rank: return 1
	# 	if self.rank < other.rank: return -1


	# 	return 0

	def __cmp__(self, other):
		t1= self.suit, self.rank
		t2 = other.suit, other.rank
		return cmp(t1, t2)
		
class deck(object):
	def __init__(self):
		self.cards=[]
		for s in range(4):
			for r in range(1,14):
				c = card(r,s)
				self.cards.append(c)

	def __str__(self):
		res = []
		for c in self.cards:
			res.append(str(c))
		return '\n'.join(res)
