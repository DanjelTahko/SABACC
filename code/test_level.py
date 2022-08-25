import pygame

from settings import *
from test_iu import ui
from player import Player


class LEVEL():

    def __init__(self) -> None:

        # Surface setup
        self.display_surface = pygame.display.get_surface()

        # TEST
        self.player = Player()

        # Background setup
        #bg_table_path = pygame.image.load("graphic/table.jpeg").convert_alpha()
        #self.bg_table = pygame.transform.scale(bg_table_path, [1280, 720])

        # Cursor setup
        self.cursor_img = pygame.image.load("graphic/mouse.png").convert_alpha()
        self.cursor_rec = self.cursor_img.get_rect().inflate(-34, -36)
        
        self.UI = ui()

        # Timer 
        self.time = 0
        self.cool_down = 100
        #self.cool_down_animation = 200

    def draw_surface(self):
        
        self.UI.display(self.player)
        

    def input(self):
        pass

    def animation(self):
        pass

    def finish(self):
        pass


    def run(self):

        self.display_surface.fill((152,118,84))
        #self.display_surface.blit(self.bg_table, (0,0))

        self.draw_surface()
        self.input()
        self.animation()
        self.finish()

        self.cursor_rec.topleft = pygame.mouse.get_pos()
        self.display_surface.blit(self.cursor_img, self.cursor_rec)
