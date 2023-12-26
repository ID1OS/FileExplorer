import pygame
import subprocess

class Settings():
    """A class to store all settings for the Desktop env."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.installing_path = "/usr/"
        self.screen_width = 800
        self.screen_height = 620
        self.bg_color = (230, 230, 230)
        self.selected_folder = None
        self.selected_file = None
        self.text_color = (30, 30, 30)
        self.hover_color = (30,40,120)
        self.hover_icon = None
        self.hover_count = 0
        self.name_color = (100,120,50)
        self.name_bg = (230, 230, 230)
        self.name = None
        self.ctrl = False
        self.shift = False
        self.clicked = False
        self.clicked_count = 0
        self.changing_name = False
        self.changing_name_icon = None
        self.login = False
        self.password = ""
        self.username = ""
        self.ID1FS = False
        result = subprocess.run("whoami",capture_output = True, text = True,check = True)
        if result.stdout.strip() == "root":
            self.home_dir = "/root"
        else:
            self.home_dir = "/home/" + result.stdout.strip()