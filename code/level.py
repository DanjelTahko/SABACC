import pygame
from card import Card
from settings import *
from deck import Deck

class Level:

    def __init__(self) -> None:

        self.surface = pygame.display.get_surface()

        card_group = pygame.sprite.Group()
        print(type(card_group))

        self.cursor_img = pygame.image.load("graphic/mouse.png").convert_alpha()
        self.cursor_rec = self.cursor_img.get_rect().inflate(-34, -36)

        bg_table_path = pygame.image.load("graphic/table.jpeg").convert_alpha()
        self.bg_table = pygame.transform.scale(bg_table_path, [1280, 720])

        self.my_cards = []
        self.discard_pile = []
        self.your_turn = True
        self.time = 0

        self.new_game = True

        #self.deck = Deck()
        #self.cards = []

    def modes(self):

        """
        1. Draw
        2. Discard & Draw
        3. Swap
        4. Stand
        5. Junk
        """

        pass 

    def start_new_game(self):
        self.cards = self.deck.create_deck()
        self.draw_card()
        self.draw_card()
        self.discard_card(self.cards.pop())
        print(self.discard_pile)
     

    def draw_card(self):
        self.my_cards.append(self.cards.pop())

    def discard_card(self, card):
        self.discard_pile.append(card)


    def inputs(self):

        current_time = pygame.time.get_ticks()

        if (current_time - self.time >= 200):

            mouse = pygame.mouse.get_pressed()

            if mouse[0]:
                
                self.draw_card()
                self.time = current_time

    def draw_surface(self):

        # Background
        self.surface.blit(self.bg_table, (0,0))

        card = pygame.image.load("graphic/CARDS/3_circle_positive.png")
        rect = card.get_rect(center = (300, 600))
        self.surface.blit(card, rect)

        # MY cards
        # Change this to sprites instead of image on surface..
        #x = 640 - (60 * len(self.my_cards))
        #for i in range(len(self.my_cards)):
        #    created_card = self.my_cards[i].create_card()
        #    created_card_rect = created_card.get_rect(center = (x,600))
        #    self.surface.blit(created_card, created_card_rect)
        #    x += 150
        # Thats why cursor will show black over symbol

        # Upside down deck
        upsidedown_deck = pygame.Surface((100,200))
        upsidedown_deck.fill(CARD_BG)
        upsidedown_rect = upsidedown_deck.get_rect(center = (800, 300))
        self.surface.blit(upsidedown_deck, upsidedown_rect)

        # Discard pile
        #discarded_cards = self.discard_pile[-1].create_card()
        #created = discarded_cards.get_rect(center = (600,300))
        #self.surface.blit(discarded_cards, created)

        # Cursor
        self.cursor_rec.topleft = pygame.mouse.get_pos()
        self.surface.blit(self.cursor_img, self.cursor_rec)

    def run(self):

        #if (self.new_game):
         #   self.start_new_game()
          #  self.new_game = False

        self.inputs()
        self.draw_surface()

        

