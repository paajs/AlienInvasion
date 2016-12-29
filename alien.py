import pygame
import random
import time
from character import Character


class Alien(Character):
    def __init__(self, ai_settings, screen, image_url):
        super().__init__(ai_settings, screen, image_url)

        self.time_from_creation = time.time()

    def random_move(self):
        now = time.time()
        if (now - self.time_from_creation) > 0.25:
            self.moving_left = bool(random.getrandbits(1))
            self.moving_right = bool(random.getrandbits(1))
            self.moving_up = bool(random.getrandbits(1))
            self.moving_down = bool(random.getrandbits(1))
            self.time_from_creation = time.time()