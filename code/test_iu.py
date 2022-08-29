import pygame

from settings import *

class ui():

    def __init__(self) -> None:
        
        # General
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont(UI_FONT, UI_FONT_SIZE)

        # Play menu / choices
        self.button_draw  = pygame.Rect(25, 150, 200, 50)
        self.button_swap  = pygame.Rect(25, 210, 200, 50)
        self.button_stand = pygame.Rect(25, 270, 200, 50)
        self.button_junk  = pygame.Rect(25, 330, 200, 50)

        # Bet menu / choicess
        self.button_bet_check = pygame.Rect(25, 150, 200, 50)
        self.button_bet_bet   = pygame.Rect(25, 210, 200, 50)
        self.button_bet_call  = pygame.Rect(25, 270, 200, 50)
        self.button_bet_raise = pygame.Rect(25, 330, 200, 50)
        self.button_bet_junk  = pygame.Rect(25, 390, 200, 50)

        # Card rects
        self.card_1 = None
        self.card_2 = None
        self.card_3 = None
        self.card_4 = None
        self.card_5 = None

    def show_menu_play(self):

        #amount_cards = len(cards)

        # Render text
        text_draw  = self.font.render("DRAW", False, UI_FONT_COLOR)
        text_swap  = self.font.render("SWAP", False, UI_FONT_COLOR)
        text_stand = self.font.render("STAND", False, UI_FONT_COLOR)
        text_junk  = self.font.render("JUNK", False, UI_FONT_COLOR)

        # Cursor position
        pos = pygame.mouse.get_pos()

        # Draw rect & gold border if mouse over rect
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_draw)
        if (self.button_draw.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_draw, 3)

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_swap)
        if (self.button_swap.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_swap, 3)

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_stand)
        if (self.button_stand.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_stand, 3)

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_junk)
        if (self.button_junk.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_junk, 3)

        # Draw text on surface/rect
        self.display_surface.blit(text_draw, (30, 160))
        self.display_surface.blit(text_swap, (30, 220))
        self.display_surface.blit(text_stand, (30, 280))
        self.display_surface.blit(text_junk, (30, 340))

    def show_menu_bet(self):

        # Render text
        text_check = self.font.render("CHECK", False, UI_FONT_COLOR)
        text_bet   = self.font.render("BET", False, UI_FONT_COLOR)

        text_call  = self.font.render("CALL", False, UI_FONT_COLOR)
        text_raise = self.font.render("RAISE", False, UI_FONT_COLOR)
        text_junk  = self.font.render("JUNK", False, UI_FONT_COLOR)

        # Cursor position
        pos = pygame.mouse.get_pos()

        # Draw rect
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_bet_check)
        if (self.button_bet_check.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_bet_check, 3)

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_bet_bet)
        if (self.button_bet_bet.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_bet_bet, 3)

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_bet_call)
        if (self.button_bet_call.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_bet_call, 3)

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_bet_raise)
        if (self.button_bet_raise.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_bet_raise, 3)

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, self.button_bet_junk)
        if (self.button_bet_junk.collidepoint(pos[0], pos[1])):
            pygame.draw.rect(self.display_surface, 'gold', self.button_bet_junk, 3)

        # Draw text on surface/rect
        self.display_surface.blit(text_check, (30, 160))
        self.display_surface.blit(text_bet, (30, 220))
        self.display_surface.blit(text_call, (30, 280))
        self.display_surface.blit(text_raise, (30, 340))
        self.display_surface.blit(text_junk, (30, 400))

    def show_stats(self, player):

        # Credits 
        credits_stats      = pygame.Rect(25, 25, 200, 50)
        credits_stats_text = self.font.render(f"{player.credits} CREDITS", False, UI_FONT_COLOR)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, credits_stats)
        self.display_surface.blit(credits_stats_text, (30, 30))

        # Rounds
        rounds_stats      = pygame.Rect(25, 645, 50, 50)
        rounds_stats_text = self.font.render(str(player.rounds), False, UI_FONT_COLOR)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, rounds_stats)
        self.display_surface.blit(rounds_stats_text, (30, 650))

        # ATM points
        points_stats      = pygame.Rect(1205, 645, 50, 50)
        points_stats_text = self.font.render(str(player.card_values), False, UI_FONT_COLOR)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, points_stats)
        self.display_surface.blit(points_stats_text, (1210, 650))
 
    def show_cards(self, player):

        # Cursor position
        pos = pygame.mouse.get_pos()

        """
            [140] | 10 | [140]
            # middle = 640!!
        """

        if (len(player.cards) == 2):

            card_1 = player.cards[0].card_graphic()
            self.card_1 = card_1.get_rect(topleft = (495, 600))
            if (self.card_1.collidepoint(pos[0], pos[1])):
                self.card_1 = card_1.get_rect(topleft = (495, 495))

            card_2 = player.cards[1].card_graphic()
            self.card_2 = card_2.get_rect(topleft = (645, 600))
            if (self.card_2.collidepoint(pos[0], pos[1])):
                self.card_2 = card_2.get_rect(topleft = (645, 495))

            self.display_surface.blit(card_1, self.card_1)
            self.display_surface.blit(card_2, self.card_2)

        elif (len(player.cards) == 3):

            card_1 = player.cards[0].card_graphic()
            self.card_1 = card_1.get_rect(topleft = (420, 600))
            if (self.card_1.collidepoint(pos[0], pos[1])):
                self.card_1 = card_1.get_rect(topleft = (420, 495))

            card_2 = player.cards[1].card_graphic()
            self.card_2 = card_2.get_rect(topleft = (570, 600))
            if (self.card_2.collidepoint(pos[0], pos[1])):
                self.card_2 = card_2.get_rect(topleft = (570, 495))

            card_3 = player.cards[2].card_graphic()
            self.card_3 = card_3.get_rect(topleft = (720, 600))
            if (self.card_3.collidepoint(pos[0], pos[1])):
                self.card_3 = card_3.get_rect(topleft = (720, 495))

            self.display_surface.blit(card_1, self.card_1)
            self.display_surface.blit(card_2, self.card_2)
            self.display_surface.blit(card_3, self.card_3)

        elif (len(player.cards) == 4):

            card_1 = player.cards[0].card_graphic()
            self.card_1 = card_1.get_rect(topleft = (345, 600))
            if (self.card_1.collidepoint(pos[0], pos[1])):
                self.card_1 = card_1.get_rect(topleft = (345, 495))

            card_2 = player.cards[1].card_graphic()
            self.card_2 = card_2.get_rect(topleft = (495, 600))
            if (self.card_2.collidepoint(pos[0], pos[1])):
                self.card_2 = card_2.get_rect(topleft = (495, 495))

            card_3 = player.cards[2].card_graphic()
            self.card_3 = card_3.get_rect(topleft = (645, 600))
            if (self.card_3.collidepoint(pos[0], pos[1])):
                self.card_3 = card_3.get_rect(topleft = (645, 495))

            card_4 = player.cards[3].card_graphic()
            self.card_4 = card_4.get_rect(topleft = (795, 600))
            if (self.card_4.collidepoint(pos[0], pos[1])):
                self.card_4 = card_4.get_rect(topleft = (795, 495))

            self.display_surface.blit(card_1, self.card_1)
            self.display_surface.blit(card_2, self.card_2)
            self.display_surface.blit(card_3, self.card_3)
            self.display_surface.blit(card_4, self.card_4)

        elif (len(player.cards) == 5):

            card_1 = player.cards[0].card_graphic()
            self.card_1 = card_1.get_rect(topleft = (270, 600))
            if (self.card_1.collidepoint(pos[0], pos[1])):
                self.card_1 = card_1.get_rect(topleft = (270, 495))
            
            card_2 = player.cards[1].card_graphic()
            self.card_2 = card_2.get_rect(topleft = (420, 600))
            if (self.card_2.collidepoint(pos[0], pos[1])):
                self.card_2 = card_2.get_rect(topleft = (420, 495))

            card_3 = player.cards[2].card_graphic()
            self.card_3 = card_3.get_rect(topleft = (570, 600))
            if (self.card_3.collidepoint(pos[0], pos[1])):
                self.card_3 = card_3.get_rect(topleft = (570, 495))

            card_4 = player.cards[3].card_graphic()
            self.card_4 = card_4.get_rect(topleft = (720, 600))
            if (self.card_4.collidepoint(pos[0], pos[1])):
                self.card_4 = card_4.get_rect(topleft = (720, 495))

            card_5 = player.cards[3].card_graphic()
            self.card_5 = card_5.get_rect(topleft = (870, 600))
            if (self.card_5.collidepoint(pos[0], pos[1])):
                self.card_5 = card_5.get_rect(topleft = (870, 495))

            self.display_surface.blit(card_1, self.card_1)
            self.display_surface.blit(card_2, self.card_2)
            self.display_surface.blit(card_3, self.card_3)
            self.display_surface.blit(card_4, self.card_4)
            self.display_surface.blit(card_5, self.card_5)
        
        """
        x = 640 - (60 * len(player.player_cards))
        for 

        x = 1280
        left = 75 | right = 1205

        # CARD
        x = 140
        y = 200

        border_left = 1130

        #5 =  43 - card (140) - 43
        """



    def display(self, player):
        self.show_menu_play()
        self.show_stats(player)
        self.show_cards(player)


"""
** BET

GAME (3 rounds)

- Start of first round (to join game)
    2 credits 
        -> game pot
    1 credit 
        -> sabacc pot

- Deals cards
    Deals every player 2 cards

- Betting 
    (No bet before)
        Bet
    Call
    Raise
    Fold/Junk
    Check (if no bets before)

- Deals card
    Dealer puts top card on discard pil (Spike)

- Players turn 
    * Draw
        * Swap w/ spike
        * Swap with hand
        * Stand
    * Swap
    * Stand
    * Junk

- Betting 
    (No bet before)
        Bet
    Call
    Raise
    Fold/Junk
    Check (if no bets before)

- Dealer rolls dice

"""
