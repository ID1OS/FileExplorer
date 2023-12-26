import pygame
import os

class Folder():
    """A class that contains the settings of a folder."""
    def __init__(self, path):
        """Initialize a folder."""
        self.path = path
        self.name = os.path.basename(path)
        self.reduced_name = self.name[:10]
        self.image = pygame.image.load("images/folder.png")
        if os.path.dirname(self.path) == "C:\\Users":
            self.image = pygame.image.load("images/personal.png")
        self.rect = self.image.get_rect()
        self.pos = None
        self.text_color = (30, 30, 30)
        self.bg_color = (230, 230, 230)
        self.font_path = "font.ttf"
        self.font = pygame.font.Font(self.font_path, 9)
        self.get_name_rect()


    def __str__(self):
        return "Folder"
    def get_name_rect(self):

        self.name_image = self.font.render(self.reduced_name, True, self.text_color, self.bg_color)
        self.name_rect = self.name_image.get_rect()

    def get_name_pos(self):
        self.name_rect.centerx = self.rect.centerx
        self.name_rect.top = self.rect.bottom

    
