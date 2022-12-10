import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.gui_button import Button
from gui.form_gui import Form
from gui.gui_label import Label


class SubFormPauseGame(Form):
    def __init__(self, name, main_surface, main_rect, x, y, w, h, color_background, slave_background, color_border, active, music):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active, slave_background)
        self.music_manager = music
        self.playing_music = False
        self.id_music = 'background'

        self.x, self.y, self.w, self.h = x, y, w, h
        self.name = name
        self.color_background = color_background
        self.color_border = color_border
        self.active = active

        # main
        self._main_surface = main_surface
        self._main_rect = main_rect

        # slave
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(center=(self.x, self.y))
        self.slave_rect_collide = self.slave_surface.get_rect(
            center=(
                self.x + self._main_rect.x,
                self.y + self._main_rect.y
            ))
        
        self.slave_background_rect = self.slave_background.get_rect(
            center=(
                self.x + self._main_rect.x,
                self.y + self._main_rect.y
            ))

        self.label_title = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/8,
            w=500,
            h=150,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/pause/header.png',
            text='',
            text_pos='center_plus',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.label_volume = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2 - self.slave_rect.w/4,
            y=self.slave_rect.h/2 + self.slave_rect.h/5 + 10,
            w=130,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='Volume',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=18,
            font_color='white'
            )
        self.volume_down_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/2 + self.slave_rect.h/5 + 10,
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
            font_color='white'
        )
        self.volume_up_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2 + self.slave_rect.w/4,
            y=self.slave_rect.h/2 + self.slave_rect.h/5 + 10,
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
            font_color='white'
        )
        self.volume_quit_music_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2 - self.slave_rect.w/8,
            y=self.slave_rect.h/2 + self.slave_rect.h/3 + 10,
            w=80,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/btn/music_on.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_quit_music_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white',
            active=True
        )
        self.volume_add_music_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2 - self.slave_rect.w/8,
            y=self.slave_rect.h/2 + self.slave_rect.h/3 + 10,
            w=80,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/btn/music_off.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_add_music_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white',
            active=False
        )
        self.volume_quit_effects_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2 + self.slave_rect.w/8,
            y=self.slave_rect.h/2 + self.slave_rect.h/3 + 10,
            w=80,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/btn/effects_on.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_quit_effects_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white',
            active=True
        )
        self.volume_add_effects_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2 + self.slave_rect.w/8,
            y=self.slave_rect.h/2 + self.slave_rect.h/3 + 10,
            w=80,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/btn/effects_off.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='volume_add_effects_button',
            text='',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white',
            active=False
        )
        self.continue_game = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6 + 70,
            w=400,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_play_level',
            text='Continue',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white',
            on_click_param_aux=''
        )
        self.main_menu = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6 + 70 + 70,
            w=400,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_main_menu',
            text='Main menu',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white',
            on_click_param_aux=''
        )
        self.exit_game = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/6 + 70 + 70 + 70,
            w=400,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='exit',
            text='Exit to desktop',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white',
            on_click_param_aux=''
        )
        
        self.button_list = [self.continue_game,self.main_menu,self.exit_game,self.volume_down_button,self.volume_up_button]
    
    def on_click(self, id):
        if id in ['volume_down_button', 'volume_up_button', 'volume_quit_music_button', 'volume_add_music_button', 'volume_quit_effects_button', 'volume_add_effects_button']:
            if id == 'volume_down_button':
                if Const.DEBUG: print('➖', id)
                self.music_manager.change_volume(-1)

            elif id == 'volume_up_button':
                if Const.DEBUG: print('➕', id)
                self.music_manager.change_volume(1)
            
            elif id == 'volume_quit_music_button':
                if Const.DEBUG: print('❌', id)
                self.music_manager.change_play_music('background')

            elif id == 'volume_add_music_button':
                if Const.DEBUG: print('✅', id)
                self.music_manager.change_play_music('background')

            elif id == 'volume_quit_effects_button':
                if Const.DEBUG: print('❌', id)
                self.music_manager.change_play_effects()

            elif id == 'volume_add_effects_button':
                if Const.DEBUG: print('✅', id)
                self.music_manager.change_play_effects()

            self.music_manager.update('select')
        else: 
            super().on_click(id)


    def update_view_form(self, id_form):
        super().update_view_form(id_form)
        self.dict_forms[id_form].running = True
        self.active = False
        if id_form == 'form_play_level':
            self.dict_forms[id_form].level.running = True

    def update(self, event_list):
        if self.active and not self.playing_music:
            self.music_manager.update('select')
            self.playing_music = True
        
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

        for button in self.button_list:
            button.update(event_list)

    def draw(self):
        self.label_title.draw()
        self.label_volume.draw()
        self.volume_down_button.draw()
        self.volume_up_button.draw()

        for button in self.button_list:
            button.draw()
