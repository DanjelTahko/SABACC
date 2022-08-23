import random
import pygame
from card import Card
from settings import *
from deck import Deck
from ui import UI
from winner import *

class Level:

    def __init__(self) -> None:

        self.surface = pygame.display.get_surface()

        self.card_group = pygame.sprite.Group()

        self.cursor_img = pygame.image.load("graphic/mouse.png").convert_alpha()
        self.cursor_rec = self.cursor_img.get_rect().inflate(-34, -36)

        # Background Setup
        bg_table_path = pygame.image.load("graphic/table.jpeg").convert_alpha()
        self.bg_table = pygame.transform.scale(bg_table_path, [1280, 720])

        self.my_cards = []
        self.discard_pile = []
        self.your_turn = True
        self.discard = False
        self.discard_state = None
        self.time = 0

        self.rounds = 0
        self.rounds_before = 0

        self.new_game = True

        self.deck = Deck()
        self.cards = []

        self.ui = UI()

        self.first_dice_index = 1
        self.second_dice_index = 6


    def start_new_game(self):
        for i in range(len(self.my_cards)):
            self.my_cards.pop()
        self.cards = self.deck.create_deck()
        self.draw_card()
        self.draw_card()
        self.discard_pile.append(self.cards.pop())

    def draw_card(self):
        self.my_cards.append(self.cards.pop())

    
    def inputs(self):

        current_time = pygame.time.get_ticks()

        if (current_time - self.time >= 200):

            mouse = pygame.mouse.get_pressed()

            if mouse[0]:
                
                # Draw
                if (self.cursor_rec.colliderect(self.ui.button_1) and len(self.my_cards) < 5): 
        
                    self.draw_card()
                    self.time = current_time
                    self.rounds_before = self.rounds
                    self.rounds += 1

                # Discard & Draw
                if (self.cursor_rec.colliderect(self.ui.button_2)):

                    self.discard = True
                    self.discard_state = "draw"
                    self.time = current_time
                    

                # Swap
                if (self.cursor_rec.colliderect(self.ui.button_3)):

                    self.discard = True
                    self.discard_state = "swap"
                    self.time = current_time
                    

                # Stand
                if (self.cursor_rec.colliderect(self.ui.button_4)):

                   self.time = current_time
                   self.rounds_before = self.rounds
                   self.rounds += 1

                # Junk
                if (self.cursor_rec.colliderect(self.ui.button_5)):

                   self.junk_cards()
                   self.time = current_time
                   self.rounds_before = self.rounds
                   self.rounds += 1


    def junk_cards(self):
        
        cards_amount = len(self.my_cards)

        for i in range(cards_amount):
            self.discard_pile.append(self.my_cards.pop())

        for i in range(cards_amount):
            self.draw_card()

    def discard_card(self):

        mouse = pygame.mouse.get_pressed()

        # MY cards
        x = 640 - (60 * len(self.my_cards))
        for i in range(len(self.my_cards)):
            my_card = self.my_cards[i].return_card()
            self.my_cards[i].rect = my_card.get_rect(center = (x,400))
            self.surface.blit(my_card, self.my_cards[i].rect)
            x += 150

            if (mouse[0] and self.my_cards[i].rect.colliderect(self.cursor_rec) and self.discard_state == "draw"):
                self.discard_pile.append(self.my_cards[i])
                self.my_cards[i] = self.cards.pop()
                self.discard = False
                self.rounds_before = self.rounds
                self.rounds += 1

            elif (mouse[0] and self.my_cards[i].rect.colliderect(self.cursor_rec) and self.discard_state == "swap"):
                temp = self.discard_pile.pop()
                self.discard_pile.append(self.my_cards[i])
                self.my_cards[i] = temp
                self.discard = False
                self.rounds_before = self.rounds
                self.rounds += 1

        # Cursor
        self.cursor_rec.topleft = pygame.mouse.get_pos()
        self.surface.blit(self.cursor_img, self.cursor_rec)

            
        
    def draw_surface(self):

        # MY cards
        x = 640 - (60 * len(self.my_cards))
        for i in range(len(self.my_cards)):
            my_card = self.my_cards[i].return_card()
            self.my_cards[i].rect = my_card.get_rect(center = (x,600))
            self.surface.blit(my_card, self.my_cards[i].rect)
            x += 150

        # Upside down deck
        upsidedown_deck = pygame.image.load("graphic/CARDS/card_back.png")
        upsidedown_rect = upsidedown_deck.get_rect(center = (800, 300))
        self.surface.blit(upsidedown_deck, upsidedown_rect)

        # Discard pile
        discarded_cards = self.discard_pile[-1].return_card()
        created = discarded_cards.get_rect(center = (600,300))
        self.surface.blit(discarded_cards, created)

        # Displays menu
        self.ui.display()

        # Rounds played 
        font = pygame.font.SysFont('arial', 20)
        rounds_box = pygame.Rect(25, 650, 50, 50)
        rounds_text = font.render(str(self.rounds), False, 'black')
        pygame.draw.rect(self.surface, 'grey', rounds_box)
        self.surface.blit(rounds_text, (30, 655))

        # Rolling dices
        dice_1 = pygame.image.load(f"graphic/DICE/{self.first_dice_index}.png")
        dice_2 = pygame.image.load(f"graphic/DICE/{self.second_dice_index}.png")
        self.surface.blit(dice_1, (275, 300))
        self.surface.blit(dice_2, (300, 310))

        # ATM points
        rounds_box_v = pygame.Rect(1000, 650, 50, 50)
        rounds_text_v = font.render(str(calculate(self.my_cards)), False, 'black')
        pygame.draw.rect(self.surface, 'grey', rounds_box_v)
        self.surface.blit(rounds_text_v, (1010, 660))


        # Cursor
        self.cursor_rec.topleft = pygame.mouse.get_pos()
        self.surface.blit(self.cursor_img, self.cursor_rec)

    def run(self):

        self.surface.blit(self.bg_table, (0,0))
        current_time = pygame.time.get_ticks()

        if (self.new_game):
            self.start_new_game()
            self.new_game = False

        if (self.discard == False):
            self.inputs()
            self.draw_surface()
        else:
            self.discard_card()

        if (self.rounds_before != self.rounds):
            self.first_dice_index = random.randint(1,6)
            self.first_dice_index = random.randint(1,6)
            if (self.first_dice_index == self.second_dice_index):
                self.junk_cards()
            self.rounds_before += 1
            if (self.rounds_before == 3):
                print("game done, calculationg winner")
                print(calculate(self.my_cards))
                if current_time - self.time <= 2000:
                    self.new_game = True
                    self.rounds = 0
                    self.rounds_before = 0
      

        

