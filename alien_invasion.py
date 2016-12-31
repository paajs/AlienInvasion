import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # Game init
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("vsAliens")

    # new ship
    ship = Ship(ai_settings, screen, 'images/ship.bmp')

    # new alien
    aliens = Group()

    # bullets group
    bullets = Group()

    # Mainloop
    loopcounter = 0
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        loopcounter += 1
        while loopcounter == 350:
            new_alien = Alien(ai_settings, screen, 'images/alien.bmp')
            aliens.add(new_alien)
            loopcounter = 0

run_game()
