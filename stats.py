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
        self.b_width = ai_settings.bullet_width
        self.b_height = ai_settings.bullet_height

        self.game_active = False
        self.alien_timer = time.time()
        self.points = 0
        self.bonus_counter = 0