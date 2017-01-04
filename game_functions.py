################################
#   game_functions.py
#   game functions
################################

import sys
import pygame

import stats
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True

    if event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True

    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

    if event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False

    elif event.key == pygame.K_a:
        ship.moving_left = False

    elif event.key == pygame.K_w:
        ship.moving_up = False

    elif event.key == pygame.K_s:
        ship.moving_down = False


def update_bullets(aliens, bullets):
    bullets.update()

    # delete old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(aliens, bullets, True, True)

    if collisions:
        stats.points += 5


def update_aliens(ship, aliens):
    for alien in aliens.sprites():
        alien.random_move()
        alien.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship.center_ship()
        ship.lives -= 1


def check_lives(ship):
    if ship.lives == 0:
        print(stats.points)
        sys.exit()


def check_events(ai_settings, screen, ship, bullets):
    """Reaction for events generated using kb or mouse"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    for alien in aliens:
        alien.blitme()

    pygame.display.flip()