import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.gui_widget import Widget


class HudBar(Widget):
    def __init__(self, main_surface, main_rect, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

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

        # image BG
        self.bg_image = pygame.image.load(
            f'{Const.PATH_IMAGE}/gui/jungle/match3/down.png'
        )
        self.bg_image = pygame.transform.scale(self.bg_image,(self.w, self.h))

        # rect BG
        self.rect_bg_img = self.bg_image.get_rect()
        self.rect_bg_img.x, self.rect_bg_img.y = self.slave_rect_collide.x, self.slave_rect_collide.y
        self.rect_bg_img.w, self.rect_bg_img.h = self.slave_rect_collide.w/2, self.slave_rect_collide.h

    
    def draw(self):
        self.main_surface.blit(self.bg_image, self.rect_bg_img)
