import pygame 

pygame.init()


class Image:
    def __init__(self,image_path : str, size : tuple, rotation_angle : int, position : list, screen : object, opacity = 255) -> None:
        self.size = size 
        self.rotation_angle = rotation_angle
        self.position = position
        self.screen = screen 

        # initiate image & its properties
        self.image = pygame.image.load(image_path).convert_alpha()
        self.get_position()
        pygame.Surface.set_alpha(self.image, opacity)
        
        if self.rotation_angle:
            self.image = pygame.transform.rotate(self.image,self.rotation_angle)

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
        self.screen.blit(self.image,self.position)

"""
centerXcenter
centerXvalue
valueXcenter
valueXvalue
"""
