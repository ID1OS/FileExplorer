import pygame

class SideScreen():
    """Initialize the settings for the side screen."""
    def __init__(self, screen):
        self.screen = screen
        self.bg_color = (60,70,120)
        self.side_rect = pygame.Rect(0, 0, 200, 620)
        self.before_image = pygame.image.load("images/before.png")
        self.before_rect = self.before_image.get_rect()
        self.before_rect.x = 20
        self.before_rect.y = 10
        self.font = pygame.font.Font("font.ttf", 15)
        self.text_color = (255,255,255)
        self.before_text = self.font.render("Before", True, self.text_color)
        self.before_text_rect = self.before_text.get_rect()
        self.before_text_rect.centery = self.before_rect.centery
        self.before_text_rect.left = self.before_rect.right + 10
        self.home_image = pygame.image.load("images/home.png")
        self.home_rect = self.home_image.get_rect()
        self.home_rect.x = 20
        self.home_rect.y = 80
        self.home_text = self.font.render("Home", True, self.text_color)
        self.home_text_rect = self.home_text.get_rect()
        self.home_text_rect.centery = self.home_rect.centery
        self.home_text_rect.left = self.home_rect.right + 10
        self.chess_image = pygame.image.load("images/chess.png")
        self.chess_rect = self.chess_image.get_rect()
        self.chess_rect.x = 20
        self.chess_rect.y = 150
        self.chess_text = self.font.render("Chess", True, self.text_color)
        self.chess_text_rect = self.chess_text.get_rect()
        self.chess_text_rect.centery = self.chess_rect.centery
        self.chess_text_rect.left = self.chess_rect.right + 10
        self.id1fs_image = pygame.image.load("images/id1fs.png")
        self.id1fs_rect = self.id1fs_image.get_rect()
        self.id1fs_rect.x = 20
        self.id1fs_rect.y = 220
        self.id1fs_text = self.font.render("ID1FS", True, self.text_color)
        self.id1fs_text_rect = self.id1fs_text.get_rect()
        self.id1fs_text_rect.centery = self.id1fs_rect.centery
        self.id1fs_text_rect.left = self.id1fs_rect.right + 10
        self.id1fs_logout_image = pygame.image.load("images/logout.png")
        self.id1fs_logout_rect = self.id1fs_logout_image.get_rect()
        self.id1fs_logout_rect.x = 20
        self.id1fs_logout_rect.y = 220
        self.id1fs_logout_text = self.font.render("Logout", True, self.text_color)
        self.id1fs_logout_text_rect = self.id1fs_logout_text.get_rect()
        self.id1fs_logout_text_rect.centery = self.id1fs_logout_rect.centery
        self.id1fs_logout_text_rect.left = self.id1fs_logout_rect.right + 10
        self.ID1FS = False
        
    

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.side_rect)
        self.screen.blit(self.before_image, self.before_rect)
        self.screen.blit(self.before_text, self.before_text_rect)
        self.screen.blit(self.home_image, self.home_rect)
        self.screen.blit(self.home_text, self.home_text_rect)
        self.screen.blit(self.chess_text, self.chess_text_rect)
        self.screen.blit(self.chess_image, self.chess_rect)
        if not self.ID1FS:
            self.screen.blit(self.id1fs_image, self.id1fs_rect)
            self.screen.blit(self.id1fs_text, self.id1fs_text_rect)
        else:
            self.screen.blit(self.id1fs_logout_image, self.id1fs_logout_rect)
            self.screen.blit(self.id1fs_logout_text, self.id1fs_logout_text_rect)