import pygame
from settings import *
from gui.form_main_menu import FormMainMenu
from gui.form_main_menu_level_selection import FormMainMenuLevelSelection
from gui.form_play_level import FormPlayLevel
from gui.form_settings import FormSettings
from gui.form_finish_level import FormFinishLevel
from gui.form_scores import FormScores
from manager_modules import *


class Menu:
    def __init__(self, screen, game_levels, game_config):
        self.master_surface = screen
        self.game_levels = game_levels
        self.game_config = self.setup_config(game_config)
        self.music_manager = Music_mng.MusicManager(self.music)
        self.sql = Sql.Sql()
        self.start_db()
        self.setup_level()

    def start_db(self):
        self.sql.create_table()

    def setup_config(self, game_config):
        self.config = Sett.get_game_config(game_config)
        self.music = Music.Music(self.config['music'])

    def setup_level(self):
        self.form_main_menu = FormMainMenu(
            name='form_main_menu',
            main_surface=self.master_surface,
            x=50,
            y=50,
            w=Const.WIDTH_SCREEN - 100,
            h=Const.HEIGHT_SCREEN - 100,
            color_background=Const.RED,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/bg.png',
            color_border='',
            active=True,
            music=self.music_manager)
        self.form_main_menu_selection = FormMainMenuLevelSelection(
            name='form_main_menu_selection',
            main_surface=self.master_surface,
            x=50,
            y=50,
            w=Const.WIDTH_SCREEN - 100,
            h=Const.HEIGHT_SCREEN - 100,
            color_background=Const.RED,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/bg.png',
            color_border='',
            active=False,
            qty_levels=len(self.game_levels),
            levels=self.game_levels,
            music=self.music_manager)
        self.form_play_level = FormPlayLevel(
            name='form_play_level',
            main_surface=self.master_surface,
            x=0,
            y=0,
            w=Const.WIDTH_SCREEN,
            h=Const.HEIGHT_SCREEN,
            color_background=Const.RED,
            color_border='',
            active=False,
            running=False,
            music=self.music_manager)
        self.form_settings = FormSettings(
            name='form_settings',
            main_surface=self.master_surface,
            x=50,
            y=50,
            w=Const.WIDTH_SCREEN - 100,
            h=Const.HEIGHT_SCREEN - 100,
            color_background=Const.RED,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/bg.png',
            color_border='',
            active=False,
            music=self.music_manager)
        self.form_finish_level = FormFinishLevel(
            name='form_finish_level',
            main_surface=self.master_surface,
            x=100,
            y=100,
            w=Const.WIDTH_SCREEN - 200,
            h=Const.HEIGHT_SCREEN - 200,
            color_background='',
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/bg.png',
            color_border='',
            active=False,
            music=self.music_manager,
            form_play_level=self.form_play_level)
        self.form_scores = FormScores(
            name='form_scores',
            main_surface=self.master_surface,
            x=100,
            y=100,
            w=Const.WIDTH_SCREEN - 200,
            h=Const.HEIGHT_SCREEN - 200,
            color_background='',
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/bg.png',
            color_border='',
            active=False,
            music=self.music_manager,
            sql=self.sql)

    def run(self, event_list, delta_ms):

        if self.form_main_menu.active:
            self.form_main_menu.update(event_list)
        elif self.form_main_menu_selection.active:
            self.form_main_menu_selection.update(event_list)
        elif self.form_play_level.active:
            self.form_play_level.update(event_list, delta_ms)
        elif self.form_settings.active:
            self.form_settings.update(event_list)
        elif self.form_finish_level.active:
            self.form_finish_level.update(event_list)
        elif self.form_scores.active:
            self.form_scores.update(event_list)

        if Sett.DEBUG:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
