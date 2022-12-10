import pygame, sys
# from gui.constantes import * # REVISAR
import sys
sys.path.append('../game/settings')
from settings import constantes as Const

from gui.gui_button import Button
from gui.form_gui import Form

# from settings import get_levels
from settings import *


class SubFormLevelSelector(Form):
    def __init__(self, name, main_surface, main_rect, x, y, w, h, color_background, color_border, music, levels=0, qty_levels=0, active=True, slave_background=''):
        # super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active, slave_background)
        self.music_manager = music
        self.playing_music = False
        # self.id_music = 'menu'
        self.active = active

        self.x, self.y, self.w, self.h = x, y, w, h
        self.main_surface = main_surface
        self.main_rect = main_rect
        self.color_background = color_background
        self.color_border = color_border

        # self.slave_surface = pygame.Surface((self.w, self.h))
        # self.slave_rect = self.slave_surface.get_rect(topleft=(self.x, self.y))
    
        # self.background_img = pygame.image.load(f'{Const.PATH_IMAGE}/gui/background.png').convert_alpha()
        # self.background_rect = self.background_img.get_rect(topleft=(0,0))
        # self.background_img = pygame.transform.scale(self.background_img,(WIDTH_SCREEN, HEIGHT_SCREEN))

        if slave_background:
            # image
            self.slave_background = pygame.image.load(slave_background).convert_alpha()
            # resize
            self.slave_background = pygame.transform.scale(self.slave_background,(self.w, self.h))
            # rect
            self.slave_background_rect = self.slave_background.get_rect(center=(self.x, self.y))
            # collide_rect
            self.slave_background_rect_collide = self.slave_background.get_rect(
                center=(
                    self.x + self.main_rect.x, 
                    self.y + self.main_rect.y
                ))

        # levels
        self.qty_levels = qty_levels
        self.game_levels = levels
        self.list_levels = ''
        if self.qty_levels:
            self.list_levels = self.show_levels(self.qty_levels)
        

    def show_levels(self, list_levels):
        temp_list = []
        y = 0
        for i in range(list_levels):
            temp_list.append(
                Button(
                    # inherit_rect=self,
                    main_surface=self.slave_background,
                    main_rect=self.slave_background_rect_collide,
                    x=self.slave_background_rect.w/2 - 10,
                    y=self.slave_background_rect.h/6 + y,
                    w=400,
                    h=60,
                    color_background=Const.BLUE,
                    slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
                    color_border='', # think in how button image works while pressing click on it - animation
                    on_click=self.on_click,
                    on_click_param='form_play_level',
                    on_click_param_aux=f'level_{i+1}',
                    text='Level {}'.format(i+1),
                    text_pos='left',
                    font=Const.PATH_FONT,
                    font_size=25,
                    font_color='white'
                )
            )
            y += 70
        return temp_list


    def instance_level(self, id):
        self.level = Sett.get_levels(self.game_levels[id], id)
    
    def on_click(self, id_form, id):
        self.instance_level(id)
        self.update_view_form(id_form, id)

    
    def update_view_form(self, id_form, id):
        super().update_view_form(id_form) # apaga los forms y activa el actual
        self.dict_forms[id_form].running = True
        self.dict_forms[id_form].change_level(self.level, id)

    def update(self, event_list):
        
        if self.list_levels:
            for i, level in enumerate(self.list_levels):
                level.update(event_list)
                # if i == 2:
                #     print(level.slave_background_rect_collide)
                level.draw()
        
        # self.draw()

    def draw(self):
        pass
