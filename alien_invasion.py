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

    pygame.display.set_caption("Inwazja obcych")

    # new ship
    ship = Ship(ai_settings, screen, 'images/ship.bmp')

    # new enemy
    enemy = Alien(ai_settings, screen, 'images/alien.bmp')

    # bullets group
    bullets = Group()

    # Mainloop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        enemy.update()
        enemy.random_move()
        bullets.update()

        # delete old bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, enemy, bullets)

run_game()
