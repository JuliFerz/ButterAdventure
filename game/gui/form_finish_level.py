import pygame, sys
sys.path.append('../game/settings')
from gui.gui_button import Button
from gui.form_gui import Form
from gui.gui_label import Label
from settings import (
    constantes as Const,
    settings as Sett
)


class FormFinishLevel(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, slave_background, color_border, active, music, form_play_level, levels):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active, slave_background)
        self.music_manager = music
        self.playing_music = False
        self.id_music = 'menu'
        self.form_play_level = form_play_level
        self.game_levels = levels

        # table background
        self.table_img = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/settings/table.png')
        self.table_img = pygame.transform.scale(self.table_img,(self.w - self.w/4, self.h - self.h/5))
        self.rect_table_img = self.table_img.get_rect(center=(self.slave_rect.centerx-100, self.slave_rect.centery-100))
        self.rect_table_img.w, self.rect_table_img.h = self.slave_rect.w, self.slave_rect.h

        # icon win
        self.icon_img_win = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/you_win/header.png')
        self.icon_img_win = pygame.transform.scale(self.icon_img_win,(self.w/2 - self.w/5, self.h/2 - self.h/4))
        self.rect_icon_img_win = self.icon_img_win.get_rect(center=(self.slave_rect.centerx-100, self.slave_rect.top + (self.h/8)-100))
        self.rect_icon_img_win.w, self.rect_icon_img_win.h = self.slave_rect.w, self.slave_rect.h

        # score table
        self.score_table_img = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/you_lose/bg.png')
        self.score_table_img = pygame.transform.scale(self.score_table_img,(self.w/2 , self.h/2 + self.h/8))
        self.rect_score_table_img = self.score_table_img.get_rect(center=(self.slave_rect.centerx-100, self.slave_rect.top + (self.h/3)+30))
        self.rect_score_table_img.w, self.rect_score_table_img.h = self.slave_rect.w, self.slave_rect.h

        self.icon_img_lose = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/you_lose/header.png')
        self.icon_img_lose = pygame.transform.scale(self.icon_img_lose,(self.w/2 - self.w/5, self.h/2 - self.h/4))
        self.rect_icon_img_lose = self.icon_img_lose.get_rect(center=(self.slave_rect.centerx-100, self.slave_rect.top + (self.h/8)-100))
        self.rect_icon_img_lose.w, self.rect_icon_img_lose.h = self.slave_rect.w, self.slave_rect.h

        # text
        self.font = pygame.font.Font(Const.PATH_FONT, 25)
        self.input_user_name = ''
        self.text_surface = self.font.render(self.input_user_name, True, 'white')

        # text score
        self.text_score_surface = self.font.render('', True, 'white')
        # text time
        self.text_time_surface = self.font.render('', True, 'white')

        self.static_label = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,
            y=self.slave_background_rect.h/5,
            w=500,
            h=40,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='Save score?',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.name_label = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/3,
            y=self.slave_background_rect.h/3-50,
            w=120,
            h=40,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='Name',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.score_label = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/3,
            y=self.slave_background_rect.h/3,
            w=120,
            h=40,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='Score',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.time_label = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/3,
            y=self.slave_background_rect.h/3 + 50,
            w=120,
            h=40,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='Time',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.exit_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/3,
            y=self.slave_background_rect.h/3 + 235,
            w=300,
            h=40,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='exit',
            text='Exit to desktop',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.main_menu_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + 235,
            y=self.slave_background_rect.h/3 + 235,
            w=300,
            h=40,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='form_main_menu',
            text='Main menu',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.submit_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2 + 235,
            y=self.slave_background_rect.h/2 ,
            w=150,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/rating/btn.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='submit_record',
            text='',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.retry_button = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/3,
            y=self.slave_background_rect.h/3 + 145,
            w=150,
            h=40,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            color_border='',
            on_click=self.on_click,
            on_click_param='retry',
            text='Retry',
            text_pos='left',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')

    def instance_level(self, id):
        self.level = Sett.get_levels(self.game_levels[id], id)
    
    def update_view_form(self, id, id_form=''):
        if id == 'form_main_menu':
            super().update_view_form(id)
        else:
            super().update_view_form(id_form)
            self.dict_forms[id_form].running = True
            self.dict_forms[id_form].change_level(self.level, id)

    def on_click(self, id):
        if id == 'submit_record':
            self.form_play_level.level.game_manager.create_record(
                self.input_user_name,
                self.form_play_level.finish_score,
                int(self.form_play_level.finish_time)
                )
            self.input_user_name = ''
            super().on_click('form_main_menu')
        elif id == 'retry':
            self.instance_level(self.form_play_level.game_level_id)
            self.update_view_form(self.form_play_level.game_level_id, 'form_play_level')

        else:
            super().on_click(id)

    def get_key_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_user_name = self.input_user_name[:-1]
                else:
                    if len(self.input_user_name) >= 20:
                        return
                    else:
                        self.input_user_name += event.unicode
    
    def update(self, event_list):
        if self.active and not self.playing_music:
            self.music_manager.update(self.id_music)
            self.music_manager.update('select')
            self.playing_music = True
    
        self.get_key_event(event_list)

        # text
        if self.form_play_level.win:
            self.text_surface = self.font.render(self.input_user_name, True, 'white')
            # label
            self.static_label.draw()
            self.name_label.draw()

            # buttons
            self.submit_button.draw()
            self.submit_button.update(event_list)
        
        self.retry_button.draw()
        self.retry_button.update(event_list)

        self.score_label.draw()
        self.time_label.draw()
        self.text_score_surface = self.font.render(f'{self.form_play_level.finish_score} points', True, 'white')
        self.text_time_surface = self.font.render(f'{int(self.form_play_level.finish_time)} seconds', True, 'white')

        self.exit_button.draw()
        self.exit_button.update(event_list)
        self.main_menu_button.draw()
        self.main_menu_button.update(event_list)
        
        self.draw()

    def draw(self):
        super().draw()
        if self.form_play_level.finish:
            self.slave_background.blit(self.table_img, self.rect_table_img)
            self.slave_background.blit(self.score_table_img, self.rect_score_table_img)

            # text blits
            if self.form_play_level.win:
                self.slave_background.blit(self.text_surface, (self.name_label.slave_widget_rect.x + 150,self.name_label.slave_widget_rect.y+10))
            self.slave_background.blit(self.text_score_surface, (self.score_label.slave_widget_rect.x + 150,self.score_label.slave_widget_rect.y+10))
            self.slave_background.blit(self.text_time_surface, (self.time_label.slave_widget_rect.x + 150,self.time_label.slave_widget_rect.y+10))

            if self.form_play_level.win:
                self.slave_background.blit(self.icon_img_win, self.rect_icon_img_win)
            elif self.form_play_level.lose:
                self.slave_background.blit(self.icon_img_lose, self.rect_icon_img_lose)
