import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.gui_button import Button
from gui.gui_label import Label
from gui.form_gui import Form


class FormSettings(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, slave_background, color_border, active, music, outside=False):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active, slave_background)
        self.main_surface = main_surface
        self.outside = outside

        self.music_manager = music
        self.playing_music = False
        self.id_music = 'menu'

        self.table_img = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/settings/table.png')
        self.table_img = pygame.transform.scale(self.table_img,(self.w - self.w/4, self.h - self.h/5))
        self.rect_table_img = self.table_img.get_rect(center=(self.slave_rect.centerx-50, self.slave_rect.centery-50))
        self.rect_table_img.w, self.rect_table_img.h = self.slave_rect.w, self.slave_rect.h

        self.icon_img = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/settings/92.png')
        self.icon_img = pygame.transform.scale(self.icon_img,(self.w/2 - self.w/5, self.h/2 - self.h/4))
        self.rect_icon_img = self.icon_img.get_rect(center=(self.slave_rect.centerx-50, self.slave_rect.top + (self.h/8)-50))
        self.rect_icon_img.w, self.rect_icon_img.h = self.slave_rect.w, self.slave_rect.h
        
        self.label_volume = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - self.slave_background_rect.w/4,
            y=self.slave_background_rect.h/4,
            w=150,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='Volume',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=18,
            font_color='white'
        )
        self.label_music = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - self.slave_background_rect.w/4,
            y=self.slave_background_rect.h/3 + 15,
            w=200,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='On/Off music',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=18,
            font_color='white'
        )
        self.label_effects = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + self.slave_background_rect.w/3 - 30,
            y=self.slave_background_rect.h/3 + 15,
            w=230,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='On/Off effects',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=18,
            font_color='white'
        )
        self.button_back = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=Const.WIDTH_SCREEN-450,
            y=Const.HEIGHT_SCREEN-250,
            w=150,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_main_menu',
            text='Back',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white'
        )
        self.volume_down_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/4,
            w=50,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/98.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_down_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='black'
        )
        self.volume_up_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/4,
            w=50,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/97.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_up_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='black'
        )
        self.volume_quit_music_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/3 + 15,
            w=150,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/96.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_quit_music_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='black',
            active=True
        )
        self.volume_add_music_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 - (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/3 + 15,
            w=150,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/95.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_add_music_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='black',
            active=False
        )
        self.volume_quit_effects_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/3 + 15,
            w=150,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/96.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_quit_effects_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='black',
            active=True
        )
        self.volume_add_effects_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + (self.slave_background_rect.w/10) + 30,
            y=self.slave_background_rect.h/3 + 15,
            w=150,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/95.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_add_effects_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='black',
            active=False
        )
        self.change_controls_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + 30,
            y=self.slave_background_rect.h/3 + 15 + 90,
            w=350,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_main_menu',
            text='Change controls',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white'
        )

        self.label_list = [self.label_volume, self.label_music, self.label_effects]
        self.button_list = [self.button_back, self.volume_down_button, self.volume_up_button]


    def on_click(self, id):
        if id == 'form_main_menu':
            super().on_click(id)
        else:
            if id == 'volume_down_button':
                if Const.DEBUG: print('➖', id)
                self.music_manager.change_volume(-1)
            elif id == 'volume_up_button':
                if Const.DEBUG: print('➕', id)
                self.music_manager.change_volume(1)
            
            
            elif id == 'volume_quit_music_button':
                if Const.DEBUG: print('❌', id)
                self.music_manager.change_play_music('menu')
            elif id == 'volume_add_music_button':
                if Const.DEBUG: print('✅', id)
                self.music_manager.change_play_music('menu')

            elif id == 'volume_quit_effects_button':
                if Const.DEBUG: print('❌', id)
                self.music_manager.change_play_effects()
            elif id == 'volume_add_effects_button':
                if Const.DEBUG: print('✅', id)
                self.music_manager.change_play_effects()

            self.music_manager.update('select')
        
    def get_key_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.on_click('form_main_menu')

    def update(self, event_list):
        if self.active and not self.playing_music:
            self.music_manager.update(self.id_music)
            self.music_manager.update('select')
            self.playing_music = True
        
        self.get_key_event(event_list)

        for label in self.label_list:
            label.draw()

        for button in self.button_list:
            button.draw()
            button.update(event_list)

        if self.music_manager.play_music:
            self.volume_quit_music_button.draw()
            self.volume_quit_music_button.update(event_list)
        elif not self.music_manager.play_music:
            self.volume_add_music_button.draw()
            self.volume_add_music_button.update(event_list)

        if self.music_manager.play_effects:
            self.volume_quit_effects_button.draw()
            self.volume_quit_effects_button.update(event_list)
        elif not self.music_manager.play_effects:
            self.volume_add_effects_button.draw()
            self.volume_add_effects_button.update(event_list)

        super().draw()
        self.draw()

    def draw(self):
        self.slave_background.blit(self.table_img, self.rect_table_img)
        self.slave_background.blit(self.icon_img, self.rect_icon_img)
