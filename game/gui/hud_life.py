import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.gui_widget import Widget


class HudLife(Widget):
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border, max_life, value):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.color_background = color_background
        self.color_border = color_border

        self.main_surface = main_surface
        self.main_rect = main_rect

        # slave
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(center=(self.x, self.y))
        self.slave_rect_collide = self.slave_surface.get_rect(
            center=(
                self.x + self.main_rect.x,
                self.y + self.main_rect.y
            ))

        # image
        self.bg_image = pygame.image.load(
            f'{Const.PATH_IMAGE}/gui/jungle/load_bar/bg.png'
        )
        self.bg_image = pygame.transform.scale(self.bg_image,(self.w, self.h))

        # rect
        self.rect_bg_img = self.bg_image.get_rect()
        self.rect_bg_img.x, self.rect_bg_img.y = self.slave_rect_collide.x, self.slave_rect_collide.y
        self.rect_bg_img.w, self.rect_bg_img.h = self.slave_rect_collide.w, self.slave_rect_collide.h

        # image
        self.image = pygame.image.load(
            f'{Const.PATH_IMAGE}/gui/jungle/load_bar/2.png'
        )
        self.image = pygame.transform.scale(self.image,(self.w, self.h-5))

        # rect
        self.rect_img = self.image.get_rect()
        self.rect_img.x, self.rect_img.y = self.slave_rect_collide.x+4, self.slave_rect_collide.y+4
        self.rect_img.w, self.rect_img.h = self.slave_rect_collide.w, self.slave_rect_collide.h

        # values
        self.max_life = max_life
        self.life = value
        self.amount = self.w / self.max_life
        self.acumulate_amount = 0
        self.percent_life_w = self.max_life / self.w

    def update(self, life):
        self.image = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/load_bar/2.png')
        self.w = life / self.percent_life_w
        self.image = pygame.transform.scale(self.image,(self.w, self.h-5))

    def draw(self):
        self.main_surface.blit(self.bg_image, self.rect_bg_img)
        self.main_surface.blit(self.image, self.rect_img)
