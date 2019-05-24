import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def rungame():
    pygame.init()
    # screen = pygame.display.set_mode((1200,800))
    # bg_color = (230,230,230)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group storing a bullet
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)


rungame()