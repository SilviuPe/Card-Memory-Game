import pygame 
from PIL import Image as Img
pygame.init()


class Image:
    def __init__(self,image_path : str, size : tuple, rotation_angle : int, position : list, screen : object, opacity = 255) -> None:
        self.size = size 
        self.rotation_angle = rotation_angle
        self.position = position
        self.screen = screen 
        self.opacity = opacity

        # initiate image & its properties

        # Initiate the image and convert it.
        self.image = pygame.image.load(image_path)
        self.image.set_alpha(self.opacity)
        self.get_position()



    """ Set the position. The position could be a string or int. If the pos[0] or pos[1] is a 
    string, the only possible it that the horizontal/vertical pos is in the center otherwise
    it should be an integer with the position """

    def get_position(self) -> None:

        if self.position[0] == "center":
            self.position[0] = self.screen.get_size()[0] // 2 - self.image.get_size()[0] // 2
        if self.position[0] != "center":
            self.position[0] = int(self.position[0])


        if self.position[1] == "center":
            self.position[1] = self.screen.get_size()[1] // 2 - self.image.get_size()[1] // 2
        if self.position[1] != "center":
            self.position[1] = int(self.position[1])

    
    def display_image(self) -> None:
        self.screen.blit(self.image,tuple(self.position))

"""
centerXcenter
centerXvalue
valueXcenter
valueXvalue
"""


class Pharagraph:
    def __init__(self,text_string : str, font : str, size : int, position : list, color : tuple, surface : object) -> None:
        self.text_string = text_string
        self.font = font 
        self.size = size 
        self.position = position
        self.color = color
        self.surface = surface 


        self.text = pygame.font.Font(self.font,self.size).render(self.text_string,True,self.color)
        
        self.set_position()
        self.rect = [self.text.get_size()[0],self.text.get_size()[1]]

    def set_position(self) -> None:

        if self.position[0] == "center":
            self.position[0] = self.surface.get_size()[0] // 2 - self.text.get_size()[0] // 2
        if self.position[0] != "center":
            self.position[0] = int(self.position[0])


        if self.position[1] == "center":
            self.position[1] = self.surface.get_size()[1] // 2 - self.text.get_size()[1] // 2
        if self.position[1] != "center":
            self.position[1] = int(self.position[1])

    def display_text(self) -> None:
        self.surface.blit(self.text,self.position)

    def on_press(self) -> bool:
        x_pos,y_pos = pygame.mouse.get_pos()

        if x_pos >= self.position[0] and x_pos <= self.position[0] + self.rect[0]:
            if y_pos >= self.position[1] and y_pos <= self.position[1] + self.rect[1]:
                return True 
            
        return False 