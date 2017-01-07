#!/usr/bin/python

####################################
#   vsaliens.py
#   Game init and mainloop function
####################################

import pygame
from pygame.sprite import Group
import time
import random

from settings import Settings
from ship import Ship
from stats import Stats
from text_utils import TextField, Button

import game_functions as gf


def run_game():
    # Game init
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("vsAliens")

    random.seed = time.time()

    stats = Stats(ai_settings)

    # play button
    play_button = Button(ai_settings, screen, (0, 255, 0),
                            ai_settings.screen_width / 2, ai_settings.screen_height / 2,
                            "Game")

    # score and lives
    score_field = TextField(ai_settings, screen,
                            ai_settings.screen_width / 2, 15, str(stats.points))
    score_field.text_color = (0, 0, 0)

    lives_field = TextField(ai_settings, screen,
                            0, 15, "")
    lives_field.text_color = (10, 10, 250)

    # new ship
    ship = Ship(ai_settings, screen)

    # new alien
    aliens = Group()

    # bullets group
    bullets = Group()

    # bonuses group
    bonuses = Group()

    # Mainloop
    while True:
        if stats.game_active:
            gf.update_ship(ship)
            gf.update_bullets(bullets)
            gf.spawn_alien(ai_settings, screen, aliens, stats)
            gf.update_aliens(aliens)
            gf.spawn_bonus(ai_settings, screen, bonuses, stats)
            gf.collisions(ship, bullets, aliens, bonuses, stats)
            gf.update_bonuses(bonuses)
            gf.update_score(score_field, stats)
            gf.update_lives(lives_field, stats)

        gf.check_game_active(play_button, stats)
        gf.check_events(ai_settings, screen, ship, bullets,
                        aliens, bonuses, stats, play_button)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets,
                         bonuses, stats, play_button, score_field, lives_field)
if __name__ == "__main__":
    run_game()
