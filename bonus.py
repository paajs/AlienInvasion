################################
#   bonus.py
#   classes: Bonus
################################

import pygame
import random
from pygame.sprite import Sprite


class Bonus(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, ai_settings.bonus_size, ai_settings.bonus_size)

        self.x = random.randint(0, self.screen_rect.width)
        self.y = random.randint(0, self.screen_rect.height / 2)

        self.color = ai_settings.bonus_color
        self.type = 0
        self.set_type(ai_settings)

    def set_type(self, ai_settings):
        self.type = random.choice(("super", "clear", "extra"))
        if self.type == "super":
            self.color = ai_settings.superbullet_color
        elif self.type == "clear":
            self.color = ai_settings.clearaliens_color
        elif self.type == "extra":
            self.color = ai_settings.extralife_color

    def draw_bonus(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.rect.centerx = self.x
        self.rect.centery = self.y