from re import A
import pygame, sys
from settings import *
from level import Level

from test_level import LEVEL

class Game:

    def __init__(self) -> None:
        
        pygame.init()
        self.clock = pygame.time.Clock()

        # Change this to something better
        self.icon = pygame.image.load("graphic/DICE/1.png")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CARD GAME FROM ANOTHER GALAXY")
        pygame.display.set_icon(self.icon)
        pygame.mouse.set_visible(False)

        self.corellian_spike = LEVEL()

    def run(self): 

        while (True):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            #self.screen.fill('black')

            self.corellian_spike.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()

# Add more sabacc variants when done 