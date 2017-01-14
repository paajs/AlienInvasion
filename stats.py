################################
#   stats.py
#   Stats
################################
import time


class Stats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats(ai_settings)

    def reset_stats(self, ai_settings):
        self.lives = 1
        self.bullet_speed_factor = ai_settings.bullet_speed_factor

        self.game_active = False
        self.alien_timer = time.time()
        self.points = 0
        self.bonus_counter = 0