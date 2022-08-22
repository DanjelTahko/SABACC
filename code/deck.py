from settings import *
from card import Card

import random

class Deck:

    def __init__(self) -> None:
        self.deck = []

    def create_deck(self):

        for number in CARD_CONFIG['numbers']:
            for symbol in CARD_CONFIG['symbols']:

                new_card_negative = Card(number, symbol, 'negative')
                new_card_positive = Card(number, symbol, 'positive')
                self.deck.append(new_card_negative)
                self.deck.append(new_card_positive)

        neutral_card = Card(0, 'zero', 'neutral')
        self.deck.append(neutral_card)
        self.deck.append(neutral_card)

        random.shuffle(self.deck)
        return self.deck



               