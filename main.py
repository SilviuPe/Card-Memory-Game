import pygame 
from values import FONT_PATH, CARD_IMAGE
from components import Image, Pharagraph

from random import randint
from datetime import datetime, timedelta
pygame.init()



class Main:
    def __init__(self, screen_size : tuple) -> None:
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Card Memory Game")

        self.running = True 


    def home_screen(self) -> None:

        self.play_text = Pharagraph(">> Test your memory <<", FONT_PATH, 28, ['center','center'],(255,255,255),self.screen)
        self.quit = Pharagraph(">> quit <<", FONT_PATH, 24, ['center',550],(255,255,255),self.screen)
        
        self.place_random_cards()
        while self.running:

            self.display_home_assets()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_text.on_press():
                        return self.gameplay_screen()
                    elif self.quit.on_press():
                        self.running = False
                        pygame.quit()


    def timer(self):
        self.time = self.time - timedelta(seconds=1)
        print(str(self.time)[-5:])

    def gameplay_screen(self) -> None:
        self.count = pygame.USEREVENT + 0
        pygame.time.set_timer(self.count,1000)
        self.time = datetime.strptime("01:00","%M:%S")

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == self.count:
                    self.timer()

    def display_home_assets(self) -> None:
        self.screen.fill((0,0,0)) # fill the background

        # Place random cards.
        for card in self.cards_background:
            card.display_image()

        self.play_text.display_text()
        self.quit.display_text()
        pygame.display.update()

    def place_random_cards(self) -> None:
        self.cards_number = 20
        self.random_cards_pos = [[randint(0,1800),randint(0,900)] for random_int in range(self.cards_number)]
        self.random_opacity = [randint(0,255) for i in range(self.cards_number)]
        self.random_sizes = [randint(0,160) for i in range(self.cards_number)]
        self.random_angles = [randint(-60,60) for i in range(self.cards_number)]
        self.cards_background = list()
        for i in range(self.cards_number):
            img = Image(CARD_IMAGE,self.random_sizes[i],self.random_angles[i]
                        ,self.random_cards_pos[i],self.screen,self.random_opacity[i])
            self.cards_background.append(img)

Main((1900,1000)).home_screen()