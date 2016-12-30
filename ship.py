import pygame

from character import Character


class Ship(Character):
    """ Class Ship """

    def __init__(self, ai_settings, screen, image_url):
        super().__init__(ai_settings, screen, image_url)

        self.init_character(ai_settings.screen_width / 2,
                            ai_settings.screen_height / 2)

        self.speed = ai_settings.ship_speed_factor
