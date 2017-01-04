import pygame

from character import Character


################################
#   ship.py
#   classes: Ship
################################

class Ship(Character):
    """ Class Ship """

    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)

        self.lives = 3

        self.speed = ai_settings.ship_speed_factor
        self.image = pygame.image.load('images/ship.bmp')

        self.center_ship()

    def center_ship(self):
        self.init_character(self.screen_rect.centerx,
                            self.screen_rect.bottom - 24)
