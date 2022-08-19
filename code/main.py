import pygame, sys
from settings import *

class Game:

    def __init__(self) -> None:
        
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))


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

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
