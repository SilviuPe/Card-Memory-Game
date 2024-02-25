import pygame 
from values import FONT_PATH, CARD_IMAGE
from components import Image, Pharagraph

from random import randint
from datetime import datetime, timedelta
import numpy as np
pygame.init()



class Main:
    def __init__(self, screen_size : tuple) -> None:
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Card Memory Game")

        self.running = True 
        self.cards_path = {
            0 : "assets/cards/apple.png",
            1 : "assets/cards/banana.png",
            2 : "assets/cards/car.png",
            3 : "assets/cards/insta.png",
            4 : "assets/cards/katana.png",
            5 : "assets/cards/lion.png"
        }
        self.seconds_count = 0

    def timer(self):
        self.time = self.time - timedelta(seconds=1)
        self.seconds_count += 1

    def initate_positions(self):
        start_pos_x = 863
        start_pos_y = 300
        difference_x = 70
        difference_y = 105
        self.positions = np.ndarray(shape = (4,3), dtype = object)

        for i in range(4):
            for h in range(3):
                self.positions[i][h] = (start_pos_x+difference_x*h, start_pos_y+difference_y*i)
    
    def initiate_cards(self):
        self.cards = np.ndarray(shape = (4,3), dtype = object)
        print(self.positions)
        self.positions_ = list()
        for iter in range(2):
            for id in self.cards_path:
                position_x = randint(0,2)
                position_y = randint(0,3)
                
                while (position_y,position_x) in self.positions_:
                    position_x = randint(0,2)
                    position_y = randint(0,3)

                self.positions_.append((position_y,position_x))
                print(position_y,position_x)
                img = Image(self.cards_path[id],120,None,list(self.positions[position_y][position_x]),self.screen)
                self.cards[position_y][position_x] = img 


    # Gameplay loop
    def gameplay_screen(self) -> None:

        #CUSTOM EVENTS
        
        self.show_cards_time = pygame.USEREVENT + 1
        pygame.time.set_timer(self.show_cards_time,1000)
        
        self.count = pygame.USEREVENT + 0
        pygame.time.set_timer(self.count,1000)


        self.time = datetime.strptime("50:05","%M:%S")
        self.timer_text = Pharagraph(str(self.time)[-5:],FONT_PATH,24,[20,20],(255,255,255),self.screen)
        self.card = Image(CARD_IMAGE,None,None,['center',300],self.screen,255)
        self.initate_positions()
        self.initiate_cards()
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == self.count:
                    self.timer()
                    self.timer_text.change_text(str(self.time)[-5:])
            
            self.display_gameplay_assets()



    # Home screen loop
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

    # Place random cards in the background
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



    # Assets for gameplay and home screen 
    def display_gameplay_assets(self):
        self.screen.fill((0,0,0))
        self.timer_text.display_text()
        

        if self.seconds_count <= 5:
            for row in self.cards:
                for card in row:
                    card.display_image()
        else:
            for row in self.positions:
                for pos in row:
                    self.card.display_image(pos)
        pygame.display.update()


    def display_home_assets(self) -> None:
        self.screen.fill((0,0,0)) # fill the background

        # Place random cards.
        for card in self.cards_background:
            card.display_image()

        self.play_text.display_text()
        self.quit.display_text()
        pygame.display.update()

Main((1900,1000)).home_screen()