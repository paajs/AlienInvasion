#!/usr/bin/python

####################################
#   vsaliens.py
#   Game init and mainloop function
####################################

import pygame
from pygame.sprite import Group, GroupSingle
import time
import random

from settings import Settings
from ship import Ship
from alien import Alien
from bonus import Bonus
import stats
import game_functions as gf


def run_game():
    # Game init
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("vsAliens")

    random.seed = time.time()

    # new ship
    ship = Ship(ai_settings, screen)

    # new alien
    aliens = Group()

    # bullets group
    bullets = Group()

    bonuses = Group()

    # Mainloop
    timer = time.time()
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.check_lives(ship)
        gf.update_aliens(ship, aliens)
        gf.update_bonuses(ship, aliens, bullets, bonuses)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, bonuses)

        now = time.time()
        if (now - timer) > 0.75:
            new_alien = Alien(ai_settings, screen)
            aliens.add(new_alien)
            timer = time.time()

        if stats.bonus_counter == ai_settings.bonus_frags:
            new_bonus = Bonus(ai_settings, screen)
            bonuses.add(new_bonus)
            stats.bonus_counter = 0

if __name__ == "__main__":
    run_game()
