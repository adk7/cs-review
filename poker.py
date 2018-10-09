# -*- coding: utf-8 -*-
from itertools import product
from random import shuffle

class Poker(object):
    
    def __init__(self):
        self.suites = ['♥', '♦', '♣', '♠']
        self.ranks = ['A', 'K', 'Q', 'J', 10, 9, 8 ,7, 6, 5, 4, 3, 2]
        
    def deal(self):
        
        cards = list(product(self.suites, self.ranks))
        shuffle(cards)
        cards = (card for card in cards)
        return cards
    
    
