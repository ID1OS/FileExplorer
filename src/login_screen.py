import pygame

class LoginScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_color = (60,70,120)
        self.field_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.rect = pygame.Rect(0, 0, 300, 200)
        self.rect.center = self.screen_rect.center
        self.font = pygame.font.Font("font.ttf", 20)
        self.field_username_rect = pygame.Rect(0, 0, 200, 30)
        self.field_password_rect = pygame.Rect(0, 0, 200, 30)
        self.username = ""
        self.username_image = self.font.render(self.username, True, self.text_color, self.field_color)
        self.username_image_rect = self.username_image.get_rect()
        self.username_image_rect.centerx = self.screen_rect.centerx
        self.username_image_rect.top = 100
        self.password = ""
        self.password_image = self.font.render(self.password, True, self.text_color, self.field_color)
        self.password_image_rect = self.password_image.get_rect()
        self.password_image_rect.centerx = self.screen_rect.centerx
        self.password_image_rect.top = 150
        self.login_button = "Login"
        self.login_button_image = self.font.render(self.login_button, True, self.text_color, self.bg_color)
        self.login_button_image_rect = self.login_button_image.get_rect()
        self.register_button = "Register"
        self.register_button_image = self.font.render(self.register_button, True, self.text_color, self.bg_color)
        self.register_button_image_rect = self.register_button_image.get_rect()
        self.login = False
        self.register = False
        self.entering_username = False
        self.entering_password = False

    def render_username(self):
        self.username_image = self.font.render(self.username, True, self.text_color, self.field_color)
        self.username_image_rect = self.username_image.get_rect()

    def render_password(self):
        self.password_image = self.font.render(self.password, True, self.text_color, self.field_color)
        self.password_image_rect = self.password_image.get_rect()
    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.rect)
        if not self.login and not self.register:
            self.login_button_image_rect.centerx = self.screen_rect.centerx
            self.login_button_image_rect.top = self.rect.top + 50
            self.register_button_image_rect.centerx = self.screen_rect.centerx
            self.register_button_image_rect.bottom = self.rect.top + 150
            self.screen.blit(self.login_button_image, self.login_button_image_rect)
            self.screen.blit(self.register_button_image, self.register_button_image_rect)
        if self.login:
            self.draw_login()
        if self.register:
            self.draw_register()
        
        
    def draw_login(self):
        self.login_button_image_rect.centerx = self.rect.centerx
        self.login_button_image_rect.top = self.rect.top + 10
        self.screen.blit(self.login_button_image, self.login_button_image_rect)
        self.field_username_rect.centerx = self.rect.centerx
        self.field_username_rect.top = self.rect.top + 50
        # Draw username field
        pygame.draw.rect(self.screen, self.field_color, self.field_username_rect)
        self.field_password_rect.centerx = self.rect.centerx
        self.field_password_rect.bottom = self.rect.bottom -50
        # Draw password field
        pygame.draw.rect(self.screen, self.field_color, self.field_password_rect)

        self.username_image_rect.center = self.field_username_rect.center
        self.password_image_rect.center = self.field_password_rect.center
        # Draw username and password
        self.screen.blit(self.username_image, self.username_image_rect)
        self.screen.blit(self.password_image, self.password_image_rect)

    
    def draw_register(self):
        self.register_button_image_rect.centerx = self.rect.centerx
        self.register_button_image_rect.top = self.rect.top + 10
        self.screen.blit(self.register_button_image, self.register_button_image_rect)
        self.field_username_rect.centerx = self.rect.centerx
        self.field_username_rect.top = self.rect.top + 50
        # Draw username field
        pygame.draw.rect(self.screen, self.field_color, self.field_username_rect)

        self.field_password_rect.centerx = self.rect.centerx
        self.field_password_rect.bottom = self.rect.bottom -50
        # Draw password field
        pygame.draw.rect(self.screen, self.field_color, self.field_password_rect)

        self.username_image_rect.center = self.field_username_rect.center
        self.password_image_rect.center = self.field_password_rect.center
        # Draw username and password
        self.screen.blit(self.username_image, self.username_image_rect)
        self.screen.blit(self.password_image, self.password_image_rect)

    def update(self):
        self.username_image = self.font.render(self.username, True, self.text_color, self.bg_color)