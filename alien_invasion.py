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
    new_enemy1 = Alien(ai_settings, screen, 'images/alien.bmp')
    new_enemy2 = Alien(ai_settings, screen, 'images/alien.bmp')
    new_enemy3 = Alien(ai_settings, screen, 'images/alien.bmp')
    enemies = []
    enemies.append(new_enemy1)
    enemies.append(new_enemy2)
    enemies.append(new_enemy3)

    # bullets group
    bullets = Group()

    # Mainloop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        for enemy in enemies:
            enemy.random_move()
            enemy.update()

        bullets.update()

        # delete old bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        gf.update_screen(ai_settings, screen, ship, enemies, bullets)

run_game()
