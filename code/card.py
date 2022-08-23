import pygame

from settings import *

class Card(pygame.sprite.Sprite):

    def __init__(self, number, symbol, status) -> None:
        super().__init__()
        self.number = number 
        self.symbol = symbol
        self.status = status

        self.value = None
        if (self.status == "negative"):
            self.value = int(f"-{self.number}")
        else:
            self.value = int(self.number)

        # what does this do?
        self.rect = None

    def card_graphic(self):

        PATH = f"graphic/CARDS/{self.number}_{self.symbol}_{self.status}.png"
        card = pygame.image.load(PATH).convert_alpha()

        return card

    def get_card_value(self):

        num = None
        if (self.status == "negative"):
            num = int(f"-{self.number}")
        else:
            num = int(self.number)

        return {
            'number': num,
            'symbol': self.symbol,
            'status': self.status
        }


    