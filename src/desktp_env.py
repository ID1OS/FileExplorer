#!/bin/python3
import pygame
import subprocess
import desktop_functions as df
from desktop_settings import Settings
from desktop import Desktop
from side_screen import SideScreen
from login_screen import LoginScreen
settings = Settings()
def run_env():
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Desktop Environment")
    desktop = Desktop(screen, settings,".")
    side_screen = SideScreen(screen)
    login_screen = LoginScreen(screen)
    while True:
        if not settings.ID1FS:
            pygame.display.set_caption(desktop.path)
        else:
            fs = f"{settings.home_dir}/.id1fs/ID1FS"
            pygame.display.set_caption(desktop.path.replace(fs,""))
        df.check_events(desktop, settings,side_screen, login_screen)
        df.moving_icons(settings)
        df.hover_icon(desktop, settings)
        df.inhover_icon(desktop, settings)
        df.check_double_click(settings)
        df.change_mouse_cursor(desktop, settings,side_screen)
        df.draw_screen(screen, settings, desktop, side_screen, login_screen)


run_env()