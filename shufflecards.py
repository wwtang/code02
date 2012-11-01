from random import *


values = range(1,11) + "J Q K".split()
suits = "Spades Hearts Clubs Diamonds".split()

deck = ['%s %s'%(v,s) for v in values for s in suits]

shuffle(deck)

while deck:
    raw_input(deck.pop())


