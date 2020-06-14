# Pythonic Card Deck Example.

import collections

Card = collections.namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(rank) for rank in range(2,11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit
                                         for rank in self.ranks]
                                         
    def __len__(self):
        return len(self._cards)
        
    def __getitem__(self, position):
        return self._cards[position]

    def __contains__(self, item):
        if item in self._cards:
            return True
        return False

    def __str__(self):
        return "Card Deck with {} cards from {} * {}".format(len(self), self.ranks, self.suit)
        
Deck = FrenchDeck()
print ("Total Cards in French Deck : {}".format(len(Deck)))

# Get An Elements from the class.
print("Second Card is : {}".format(Deck[2-1]))
print("Twenty Second Card is : {}".format(Deck[22-1]))

# Get a random Card. Use random.choice as FrenchDeck is a sequence.
from random import choice
print ("Random Card {}".format(choice(Deck)))

# Slicing.
print(Deck[:3])
print(Deck[11:14])
print(Deck[12::13])

# presence check.
card = Card('Q','hearts')
print ("Card is :", card)
print("Whether card in Deck: ",card in Deck)

print (Deck)

import random
class ShuffledDeck(FrenchDeck):
    def __init__(self):
        self.sequence = list(range(52))
        random.shuffle(self.sequence)
        super(FrenchDeck, self).__init__()

    def __getitem__(self, item):
        return super(FrenchDeck, self).__getitem__(self.sequence[item])

ShuffleDeck = ShuffledDeck()

print ("First Card {}".format(ShuffleDeck[0]))
print ("Last Card {}".format(ShuffleDeck[51]))
#  nsharma@nsharma-mbps ~/Documents/GitHub/RandomCodes $ python3 Cards.py
# Total Cards in French Deck : 52
# Second Card is : Card(rank='3', suit='spades')
# Twenty Second Card is : Card(rank='10', suit='diamonds')
# Random Card Card(rank='Q', suit='hearts')
# [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
# [Card(rank='K', suit='spades'), Card(rank='A', suit='spades'), Card(rank='2', suit='diamonds')]
# [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
# Card is : Card(rank='Q', suit='hearts')
# Whether card in Deck:  True
# Card Deck with 52 cards from ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * ['spades', 'diamonds', 'clubs', 'hearts']
#  nsharma@nsharma-mbps ~/Documents/GitHub/RandomCodes $
