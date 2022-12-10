import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.form_gui import Form
from gui.hud_life import HudLife
from gui.hud_bullets import HudBullets
from gui.hud_time import HudTime
from gui.hud_static_bar import HudBar
from gui.hud_score import HudScore


class SubFormGameHud(Form):
    def __init__(self, name, main_surface, main_rect, x, y, w, h, image_background, color_border, levels=0, qty_levels=0, active=True, score=0, max_life=10, life=10, bullets=0, time=0):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.name = name
        self.image_background = image_background
        self.color_border = color_border
        self.active = active

        # main
        self._main_surface = main_surface
        self._main_rect = main_rect

        # slave
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(topleft=(self.x, self.y))
        self.slave_rect_collide = self.slave_surface.get_rect(
            topleft=(
                self.x + self._main_rect.x,
                self.y + self._main_rect.y
            ))
        
        # PJ
        self.score = -1
        self.max_life = max_life
        self.life = life
        self.bullets = bullets
        self.current_time = time

        # levels
        self.qty_levels = qty_levels
        self.game_levels = levels
        self.list_levels = ''
        if self.qty_levels:
            self.list_levels = self.show_levels(self.qty_levels)
       
        self.gui_bar = HudBar(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=Const.WIDTH_SCREEN/2,
            y=Const.HEIGHT_SCREEN-5,
            w=Const.WIDTH_SCREEN + Const.WIDTH_SCREEN/5,
            h=150,
        )
        self.gui_life = HudLife(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=Const.HEIGHT_SCREEN-25,
            w=500,
            h=30,
            color_background=Const.VIOLET,
            color_border='white', 
            max_life=self.max_life,
            value=self.life,
            )
        self.gui_bullets = HudBullets(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=Const.WIDTH_SCREEN-200,
            y=Const.HEIGHT_SCREEN-25,
            w=300,
            h=30,
            color_background=Const.VIOLET,
            color_border='white', 
            max_bullets=self.bullets,
            value=self.bullets,
            )
        self.gui_score = HudScore(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=200,
            y=Const.HEIGHT_SCREEN-25,
            w=200,
            h=40,
            color_background=Const.VIOLET,
            color_border='white', 
            value=self.score,
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.gui_time = HudTime(
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=Const.WIDTH_SCREEN-120,
            y=35,
            w=200,
            h=40,
            color_background=Const.VIOLET,
            color_border='white', 
            value=self.current_time,
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        
        self.list_hud = [self.gui_bar,self.gui_life,self.gui_bullets,self.gui_score,self.gui_time]

    def update(self, score, life, bullets, time):
        if score != self.score:
            self.score = score
            self.gui_score.update(self.score)

        if life != self.life:
            self.life=life
            self.gui_life.update(self.life)
        if bullets != self.bullets:
            if bullets > self.bullets:
                self.bullets = bullets
                self.gui_bullets.update_bullets(self.bullets)
            else:
                self.bullets = bullets
                self.gui_bullets.update()

        self.gui_time.update(time)
        self.draw()

    def draw(self):
        self.slave_surface.blit(self.image_background, self.slave_rect)
        for hud in self.list_hud:
            hud.draw()
