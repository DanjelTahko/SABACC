import pygame 

class UI:

    def __init__(self) -> None:
        
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont('arial', 20)

        self.button_1 = pygame.Rect(25, 150, 200, 50)
        self.text_1 = self.font.render("Draw", False, 'black')

        self.button_2 = pygame.Rect(25, 210, 200, 50)
        self.text_2 = self.font.render("Discard & Draw", False, 'black')

        self.button_3 = pygame.Rect(25, 270, 200, 50)
        self.text_3 = self.font.render("Swap", False, 'black')

        self.button_4 = pygame.Rect(25, 330, 200, 50)
        self.text_4 = self.font.render("Stand", False, 'black')

        self.button_5 = pygame.Rect(25, 390, 200, 50)
        self.text_5 = self.font.render("Junk", False, 'black')


    def show_choices(self):

        """
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright = (x,y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)
        """

        """
        1. Draw
        2. Discard & Draw
        3. Swap
        4. Stand
        5. Junk
        """

        pygame.draw.rect(self.display_surface, 'grey', self.button_1)
        self.display_surface.blit(self.text_1, (30, 160))
        pygame.draw.rect(self.display_surface, 'grey', self.button_2)
        self.display_surface.blit(self.text_2, (30, 220))
        pygame.draw.rect(self.display_surface, 'grey', self.button_3)
        self.display_surface.blit(self.text_3, (30, 280))

        pygame.draw.rect(self.display_surface, 'grey', self.button_4)
        self.display_surface.blit(self.text_4, (30, 340))

        pygame.draw.rect(self.display_surface, 'grey', self.button_5)
        self.display_surface.blit(self.text_5, (30, 400))

    def display(self):
        self.show_choices()
