################################
#   settings.py
#   classes: Settings
################################


class Settings:
    """Settings Class"""

    def __init__(self):
        """Settings initialization"""

        # Screen
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_speed_factor = 1.5

        # Bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
