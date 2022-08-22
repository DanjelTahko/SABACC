import pygame

from settings import *

class Card(pygame.sprite.Sprite):

    def __init__(self, number, symbol, status) -> None:
        super().__init__()
        self.number = number 
        self.symbol = symbol
        self.status = status

        self.image = pygame.Surface((140,200))
        self.image_rect = self.image.get_rect()
        self.font = pygame.font.SysFont("arial", 20)

    def create_card(self):

        number = None 
        border_color = None
        full_path = f"graphic/CARDS/{self.status}_{self.symbol}.png"
        symbol = pygame.image.load(full_path).convert_alpha()
        symbol_rect = symbol.get_rect(center = (50, 100))
        
        if (self.status == 'negative'):
            number = self.font.render(f"-{self.number}", False, 'white')
            border_color = 'red'
        elif (self.status == 'positive'):
            number = self.font.render(f"{self.number}", False, 'white')
            border_color = 'green'
        else:
            number = self.font.render(f"{self.number}", False, 'white')
            border_color = 'black'

        self.image.fill(CARD_BG)
        self.image.blit(number, (65, 10))
        self.image.blit(symbol, symbol_rect)
        pygame.draw.rect(self.image, border_color, self.image_rect, 3)

        return self.image

    def get_card_value(self):
        return {
            'number': self.number,
            'symbol': self.symbol,
            'status': self.status
        }


    