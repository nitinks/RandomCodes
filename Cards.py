# Pythonic Card Deck Example.

import collections

Cards = collections.namedtuple('Card',['rank', 'suit'])

class FrenchDeck:
    ranks = [str(rank) for rank in range(2,11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [ Card(rank, suit) for suit in self.suit 
                                         for rank in self.rank]
                                         
    def __len__(self):
        return len(self._cards)
        
    def __getitem__(self, position):
        return self._cards[position]
        
Deck = FrenchDeck()
print ("Total Cards in French Deck : {}.format(len(Deck)))
