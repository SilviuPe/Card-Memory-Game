import pygame 
from values import FONT_PATH, CARD_IMAGE
from components import Image, Pharagraph
pygame.init()



class Main:
    def __init__(self, screen_size : tuple) -> None:
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Card Memory Game")

        self.running = True 


    def home_screen(self) -> None:
        self.card_image = Image(CARD_IMAGE,None,0,[100,300],self.screen, opacity = 100)
        self.play_text = Pharagraph(">> Test your memory <<", FONT_PATH, 28, ['center','center'],(255,255,255),self.screen)
        self.quit = Pharagraph(">> quit <<", FONT_PATH, 24, ['center',550],(255,255,255),self.screen)
        
        self.image_ = pygame.image.load(CARD_IMAGE)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_text.on_press():
                        print('play')
                    elif self.quit.on_press():
                        pygame.quit()
                        self.running = False

            self.display_home_assets()

    def display_home_assets(self) -> None:
        self.screen.fill((0,0,0))
        self.screen.blit(self.image_,[100,100])
        self.card_image.display_image()
        self.play_text.display_text()
        self.quit.display_text()
        pygame.display.update()


Main((1900,1000)).home_screen()