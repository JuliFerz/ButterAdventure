import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.gui_widget import Widget


class HudBullets(Widget):
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border, max_bullets, value):
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
            f'{Const.PATH_IMAGE}/gui/set_gui_01/Data_Border/Bars/Bar_Background01.png'
        )
        self.bg_image = pygame.transform.scale(self.bg_image,(self.w, self.h))

        # rect BG
        self.rect_bg_img = self.bg_image.get_rect()
        self.rect_bg_img.x, self.rect_bg_img.y = self.slave_rect_collide.x, self.slave_rect_collide.y
        self.rect_bg_img.w, self.rect_bg_img.h = self.slave_rect_collide.w/2, self.slave_rect_collide.h

        # image 
        self.bullet_image = pygame.image.load(
            f'{Const.PATH_IMAGE}/gui/set_gui_01/Data_Border/Bars/Bar_Segment01.png'
        )

        # rect
        self.rect_img = self.bullet_image.get_rect()
        self.rect_img.x, self.rect_img.y = self.slave_rect_collide.x, self.slave_rect_collide.y
        self.rect_img.w, self.rect_img.h = self.slave_rect_collide.w, self.slave_rect_collide.h

        # values
        self.max_bullets = max_bullets
        self.bullets = value

        self.qty_bullets = self.get_bullets(self.bullets)
        

    def get_bullets(self, qty_bullets):
        bullet_list = []
        w_bullet = 0
        x = self.rect_img.x + 2
        y = self.rect_img.y
        for i in range(qty_bullets):
            surface = self.bullet_image
            x += w_bullet
            
            w_bullet = self.rect_img.w / qty_bullets
            h_bullet = self.slave_rect_collide.h
            surface = pygame.transform.scale(surface,(w_bullet, h_bullet))
            rect = surface.get_rect(topleft=(x, y))
            
            bullet_list.append({'surface':surface, 'rect':rect})
        return bullet_list

    def update_bullets(self, bullets):
        self.qty_bullets = self.get_bullets(bullets)

    def update(self):
        print(len(self.qty_bullets))
        try:
            del self.qty_bullets[-1]
        except:
            print('EXCEPT_hud_bullets',self.qty_bullets)
    
    def draw(self):
        self.main_surface.blit(self.bg_image, self.rect_bg_img)
        for bullet in self.qty_bullets:
            self.main_surface.blit(bullet['surface'], bullet['rect'])
