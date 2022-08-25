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
 

    def display(self, player):
        self.show_menu_bet()
        self.show_stats(player)


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
