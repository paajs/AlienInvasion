import random
import time

import pygame

from character import Character


class Alien(Character):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)

        self.time_from_creation = time.time()

        self.init_character(random.randint(0, self.screen_rect.width),
                            random.randint(0, self.screen_rect.height / 2))

        self.want_right = True
        self.want_left = True
        self.want_down = True
        self.want_up = True

        self.speed = 0.25
        self.image = pygame.image.load('images/alien.bmp')

    def random_move(self):
        now = time.time()

        if (now - self.time_from_creation) > 0.35:
            self.moving_down = False
            self.moving_up = False
            self.moving_right = False
            self.moving_left = False

            while not (self.want_right ^ self.want_left):
                if self.rect.right < self.screen_rect.width:
                    self.want_right = bool(random.getrandbits(1))
                else:
                    self.want_right = False

                if self.rect.left > 0:
                    self.want_left = bool(random.getrandbits(1))
                else:
                    self.want_left = False

            while not (self.want_up ^ self.want_down):
                if self.rect.bottom < self.screen_rect.bottom:
                    self.want_down = bool(random.getrandbits(1))
                else:
                    self.want_down = False

                if self.rect.top > 0:
                    self.want_up = bool(random.getrandbits(1))
                else:
                    self.want_up = False

            if self.want_up:
                self.moving_up = True
                self.want_up = bool(random.getrandbits(1))
            if self.want_down:
                self.moving_down = True
                self.want_down = bool(random.getrandbits(1))
            if self.want_right:
                self.moving_right = True
                self.want_right = bool(random.getrandbits(1))
            if self.want_left:
                self.moving_left = True
                self.want_left = bool(random.getrandbits(1))

            # print("want:\t" + "l: " + str(self.want_left) + " r: " + str(self.want_right) + " u: " + str(self.want_up) + " d: " + str(self.want_down))
            # print("do:\t"+ "l: " + str(self.moving_left) + " r: " + str(self.moving_right) + " u: " + str(self.moving_up) + " d: " + str(self.moving_down))
            self.time_from_creation = time.time()
