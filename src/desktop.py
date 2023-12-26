import pygame
import os
from folder import Folder
from file import File
class Desktop():
    """A class to manage the desktop environment."""
    def __init__(self, screen, settings, path):
        """Initialize the desktop environment."""
        self.installing_path = "/usr/FileExplorer"
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.path = os.path.abspath(path)
        self.icon_size = 100
        self.icon_color = (0, 0, 0)
        self.folders = []
        self.files = []
        self.icon_places = []
        self.icons = []
        with open(f"{self.installing_path}/system/log","w"):
            pass
        self.Initialize_desktop()


    def Initialize_desktop(self):
        with open("system/log","a") as f:
            f.write(self.path+"\n")
        self.folders = []
        self.files = []
        self.icon_places = []
        self.icons = []
        self.get_rect_places()
        self.get_content()
        self.get_icons()
        self.icons_get_pos()

    def get_content(self):
        """Get the content of the file"""
        count = 0
        for file in os.listdir(self.path):
            file = os.path.join(self.path,file)
            if os.path.isdir(file):
                if os.path.basename(file)[0] != ".":
                    count+=1
                    self.folders.append(Folder(file))
            if os.path.isfile(file):
                if os.path.basename(file)[0] != ".":
                    count+=1
                    self.files.append(File(file))
        self.icon_places = self.icon_places[0:count]
        
    
    def get_rect_places(self):
        """Get the rect of the icons."""
        self.icon_number = len(os.listdir(self.path))
        self.icon_rows = self.icon_number // 6 + 1
        for i in range(self.icon_rows):
            for j in range(6):
                icon_rect = (pygame.Rect(200 + self.icon_size * j, self.icon_size * i, self.icon_size, self.icon_size))
                self.icon_places.append(icon_rect)
        self.icon_places = self.icon_places[0:self.icon_number]
        
    
    def get_icons(self):
        """display the icons"""
        index = 0
        for folder in self.folders:
            folder.x = index
            index = index + 1
        for file in self.files:
            file.x = index
            index = index + 1
    
    def icons_get_pos(self):
        for folder in self.folders:
            folder.rect.center = self.icon_places[folder.x].center
        for file in self.files:
            file.rect.center = self.icon_places[file.x].center


    def blitme(self):
        """draw the folder on the screen"""
        for folder in self.folders:
            folder.get_name_pos()
            self.screen.blit(folder.image, folder.rect)
            self.screen.blit(folder.name_image, folder.name_rect)
        for file in self.files:
            file.get_name_pos()
            self.screen.blit(file.image, file.rect)
            self.screen.blit(file.name_image, file.name_rect)
    

            
    
