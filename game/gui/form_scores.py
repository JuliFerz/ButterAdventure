import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.gui_button import Button
from gui.form_gui import Form
from gui.gui_label import Label


class FormScores(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, slave_background, color_border, active, music, sql):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active, slave_background)
        self.music_manager = music
        self.playing_music = False
        self.id_music = 'menu'
        self.sql = sql
        self.sorted = False
        self.list_scores=''
        self.list_scores_buttons=''

        # table background
        self.table_img = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/settings/table.png')
        self.table_img = pygame.transform.scale(self.table_img,(self.w - self.w/4, self.h - self.h/5))
        self.rect_table_img = self.table_img.get_rect(center=(self.slave_rect.centerx-100, self.slave_rect.centery-100))
        self.rect_table_img.w, self.rect_table_img.h = self.slave_rect.w, self.slave_rect.h

        # icon win
        self.icon_rating_img = pygame.image.load(f'{Const.PATH_IMAGE}/gui/jungle/rating/header.png')
        self.icon_rating_img = pygame.transform.scale(self.icon_rating_img,(self.w/2 - self.w/5, self.h/2 - self.h/4))
        self.rect_icon_rating_img = self.icon_rating_img.get_rect(center=(self.slave_rect.centerx-100, self.slave_rect.top + (self.h/8)-100))
        self.rect_icon_rating_img.w, self.rect_icon_rating_img.h = self.slave_rect.w, self.slave_rect.h

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

    def show_scores(self, list_scores):
        temp_list_label = []
        temp_list_buttons = []
        y = 0
        for i, score in enumerate(list_scores):
            temp_list_label.append(
                    Label(
                        main_surface=self.slave_background,
                        main_rect=self.slave_background_rect,
                        x=self.slave_background_rect.w/2,
                        y=self.slave_background_rect.h/5 + y,
                        w=600,
                        h=30,
                        color_background=Const.VIOLET,
                        slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
                        text='[{}] {} -> {} points ({}p {}sec)'.format(
                            i+1, score[1], score[2]-score[3], score[2], score[3]
                        ),
                        text_pos='left',
                        font=Const.PATH_FONT,
                        font_size=18,
                        font_color='white'
                    ))
            temp_list_buttons.append(
                    Button(
                        main_surface=self.slave_background,
                        main_rect=self.slave_background_rect,
                        x=self.slave_background_rect.w/2 + 300,
                        y=self.slave_background_rect.h/5 + y,
                        w=30,
                        h=30,
                        color_background=Const.VIOLET,
                        slave_background=f'{Const.PATH_IMAGE}/gui/jungle/rating/close_2.png',
                        color_border='',
                        on_click=self.on_click,
                        on_click_param=score[0],
                        text='',
                        text_pos='left',
                        font=Const.PATH_FONT,
                        font_size=25,
                        font_color='white'
                    ))
            y += 40
        return temp_list_label, temp_list_buttons

    def get_scores(self):
        self.sorted = True
        
        cursor = self.sql.select_all_record()
        temp_list = []
        for score in cursor:
            temp_list.append(score)
        temp_list.sort(key=lambda el: el[2]-el[3], reverse=True)

        self.list_scores = temp_list
        self.list_scores, self.list_scores_buttons = self.show_scores(self.list_scores)

    def on_click(self, id):
        if id == 'exit':
            sys.exit()
        elif id == 'form_main_menu':
            self.sorted = False
            super().on_click('form_main_menu')
        else:
            self.music_manager.update('select')
            self.sql.delete_table_where(id)
            self.get_scores()

    def get_key_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.on_click('form_main_menu')
                    self.sorted = False

    def update(self, event_list):
        if self.active and not self.playing_music:
            self.music_manager.update(self.id_music)
            self.music_manager.update('select')
            self.playing_music = True
        
        if not self.sorted:
            self.get_scores()
        
        self.get_key_event(event_list)

        if self.list_scores:
            for score in self.list_scores[:7]:
                score.draw()
        if self.list_scores_buttons:
            for button in self.list_scores_buttons[:7]:
                button.draw()
                button.update(event_list)

        self.exit_button.draw()
        self.exit_button.update(event_list)
        self.main_menu_button.draw()
        self.main_menu_button.update(event_list)
        
        self.draw()

    def draw(self):
        super().draw()
        
        self.slave_background.blit(self.table_img, self.rect_table_img)
        self.slave_background.blit(self.icon_rating_img, self.rect_icon_rating_img)
