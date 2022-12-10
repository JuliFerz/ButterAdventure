import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.gui_widget import Widget
import time


class HudTime(Widget):
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border, value,font,font_size,font_color):
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

        # image BG
        self.bg_image = pygame.image.load(
            f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png'
        )
        self.bg_image = pygame.transform.scale(self.bg_image,(self.w, self.h))

        # rect BG
        self.rect_bg_img = self.bg_image.get_rect()
        self.rect_bg_img.x, self.rect_bg_img.y = self.slave_rect_collide.x, self.slave_rect_collide.y
        self.rect_bg_img.w, self.rect_bg_img.h = self.slave_rect_collide.w/2, self.slave_rect_collide.h

        # image 
        self.clock_img = pygame.image.load(
            f'{Const.PATH_IMAGE}/gui/jungle/bubble/clock.png'
        )
        self.clock_img = pygame.transform.scale(self.clock_img,(self.w/2 - self.w/4, self.h+self.h/4))
        # rect
        self.rect_img = self.clock_img.get_rect()
        self.rect_img.x, self.rect_img.y = self.slave_rect_collide.x, self.slave_rect_collide.y-5
        self.rect_img.w, self.rect_img.h = self.slave_rect_collide.w, self.slave_rect_collide.h

        # text
        self.font = pygame.font.Font(font, font_size)
        self.font_color = font_color

        # values
        self.text_render = self.font.render(time.strftime('%M:%S', time.gmtime(value)), True, self.font_color)
        

    def update(self, time_play):
        self.text_render = self.font.render(time.strftime('%M:%S', time.gmtime(time_play)), True, self.font_color)

        if int(time_play) >= 50:
            self.font_color = Const.RED
    
    def draw(self):
        self.main_surface.blit(self.bg_image, self.rect_bg_img)
        self.main_surface.blit(self.clock_img, self.rect_img)
        self.main_surface.blit(self.text_render, (self.rect_img.x+70, self.rect_img.y+10))
