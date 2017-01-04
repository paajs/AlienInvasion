################################
#   character.py
#   classes: Character
################################

import pygame
from math import sqrt
from pygame.sprite import Sprite


class Character(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # get object's image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # spawn object in top left corner by default
        self.screen_rect = screen.get_rect()
        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left

        # speed of object
        self.speed = 1

        # moving commands flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.rotate_clock = False
        self.rotate_ctrclock = False
        self.dir = 0

        # get cords to operate with
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

    def init_character(self, x, y):
        self.x = x
        self.y = y

    def match_speed(self):
        """Match speed for character's movement"""
        if self.moving_right or self.moving_left:
            if self.moving_down or self.moving_up:
                return (self.speed * sqrt(2)) / 2
            else:
                return self.speed

        if self.moving_up or self.moving_down:
            if self.moving_right or self.moving_left:
                return (self.speed * sqrt(2)) / 2
            else:
                return self.speed

    def turn_left(self):
        self.dir += 45
        if self.dir > 360:
            self.dir = 45

    def turn_right(self):
        self.dir -= 45
        if self.dir < 0:
            self.dir = 315

    def confirm_move(self):
        """Check the movement flags"""
        if self.moving_right:
            if self.rect.right >= self.screen_rect.right:
                self.moving_right = False

        if self.moving_left:
            if self.rect.left <= 0:
                self.moving_left = False

        if self.moving_up:
            if self.rect.top <= 0:
                self.moving_up = False

        if self.moving_down:
            if self.rect.bottom >= self.screen_rect.bottom:
                self.moving_down = False

    def update(self):
        """Update actual placement"""
        self.confirm_move()

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.match_speed()

        if self.moving_left and self.rect.left > 0:
            self.x -= self.match_speed()

        if self.moving_up and self.rect.bottom > self.rect.height:
            self.y -= self.match_speed()

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.match_speed()

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def blitme(self):
        """ Draw actual placement """
        self.screen.blit(self.image, self.rect)