import pygame.ftfont


class Button:
    def __init__(self, ai_settings, screen, bg_color, x, y, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 40
        self.bg_color = bg_color
        self.text_color = (255, 255, 255)
        self.font = pygame.ftfont.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.centerx = x
        self.rect.centery = y

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True,
                            self.text_color, self.bg_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_text_field(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class TextField:
    def __init__(self, ai_settings, screen, x, y, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.x = x
        self.y = y
        self.text_color = (255, 255, 255)
        self.font = pygame.ftfont.SysFont(None, 48)
        self.bg_color = ai_settings.bg_color

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_disp = self.font.render(msg, True,
                            self.text_color, self.bg_color)

    def draw_text_field(self):
        self.screen.blit(self.msg_disp, (self.x, self.y))