import pygame
class Settings:
    def __init__(self):
        self.bg_color = (60, 47, 86)
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_speed = 1.5
        pygame.display.set_caption('Alien Invasion')
