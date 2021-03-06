################################
#   game_functions.py
#   game functions
################################

import sys
import time
import pygame

from bullet import Bullet
from alien import Alien
from bonus import Bonus
from text_utils import TextField


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True

    if event.key == pygame.K_w:
        ship.moving_up = True
    elif event.key == pygame.K_s:
        ship.moving_down = True

    if event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship, stats)
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


def check_events(ai_settings, screen, ship, bullets, aliens, bonuses, stats, play_button):
    """Reaction for events generated using kb or mouse"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, aliens, bullets, bonuses, stats, play_button, mouse_x, mouse_y)


def check_play_button(ai_settings, aliens, bullets, bonuses, stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.reset_stats(ai_settings)
        stats.game_active = True

        aliens.empty()
        bullets.empty()
        bonuses.empty()


def update_ship(ship):
    ship.update()


def update_bullets(bullets):
    bullets.update()

    # delete old bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def spawn_alien(ai_settings, screen, aliens, stats):
    now = time.time()

    if (now - stats.alien_timer) > 0.75:
        new_alien = Alien(ai_settings, screen)
        aliens.add(new_alien)
        stats.alien_timer = time.time()


def update_aliens(aliens):
    for alien in aliens.sprites():
        alien.random_move()
        alien.update()


def spawn_bonus(ai_settings, screen, bonuses, stats):
    if stats.bonus_counter == ai_settings.bonus_frags:
        new_bonus = Bonus(ai_settings, screen)
        bonuses.add(new_bonus)
        stats.bonus_counter = 0


def update_bonuses(bonuses):
    for bonus in bonuses:
        bonus.update()


def update_score(score_field, ai_settings, screen, stats):
    score_field.empty()
    new_score_field = TextField(ai_settings, screen,
                                ai_settings.screen_width / 2, 15, str(stats.points))
    new_score_field.text_color = (0, 0, 0)
    score_field.add(new_score_field)


def update_lives(lives_field, ai_settings, screen, stats):
    lives_field.empty()
    new_lives_field = TextField(ai_settings, screen,
                                0, 15, "L: " + str(stats.lives))
    lives_field.add(new_lives_field)


def collisions(ai_settings, screen, ship, bullets, aliens, bonuses, stats, score_field, lives_field):
    if pygame.sprite.spritecollideany(ship, aliens):
        ship.center_ship()
        stats.lives -= 1
        update_lives(lives_field, ai_settings, screen, stats)

    hitByBullet = pygame.sprite.groupcollide(aliens, bullets, True, True)

    if hitByBullet:
        stats.points += 5
        stats.bonus_counter += 1
        update_score(score_field, ai_settings, screen, stats)

    for bonus in pygame.sprite.spritecollide(ship, bonuses, True):
        if bonus.type == "super":
            stats.bullet_speed_factor *= 1.2
        elif bonus.type == "clear":
            aliens.empty()
        elif bonus.type == "extra":
            stats.lives += 1
            update_lives(lives_field, ai_settings, screen, stats)


def check_game_active(play_button, stats):
    if stats.lives <= 0:
        play_button.prep_msg("Once again?")
        stats.game_active = False


def update_screen(ai_settings, screen, ship, aliens, bullets,
                  bonuses, stats, play_button, score_field, lives_field):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    for alien in aliens:
        alien.blitme()

    for bonus in bonuses.sprites():
        bonus.draw_bonus()

    for sc_f in score_field:
        sc_f.draw_text_field()

    for lv_f in lives_field:
        lv_f.draw_text_field()

    if not stats.game_active:
        play_button.draw_text_field()

    pygame.display.flip()