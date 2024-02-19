import pygame 
from values import FONT_PATH, CARD_IMAGE
from components import Image
pygame.init()



class Main:
    def __init__(self, screen_size : tuple) -> None:
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Card Memory Game")

        self.running = True 


    def home_screen(self) -> None:
        self.card_image = Image(CARD_IMAGE,None,0,[100,300],self.screen, opacity = 2)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
            print(pygame.display.get_active())
            self.display_home_assets()
            pygame.display.update()
    def display_home_assets(self) -> None:
        self.card_image.display_image()


Main((1900,1000)).home_screen()