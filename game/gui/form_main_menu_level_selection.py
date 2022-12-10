import sys
sys.path.append('../game/settings')
from settings import constantes as Const
from gui.gui_button import Button
from gui.gui_label import Label
from gui.form_gui import Form
from gui.sub_form_level_selector import SubFormLevelSelector


class FormMainMenuLevelSelection(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, slave_background, color_border, active, qty_levels, levels, music):
        super().__init__(name, main_surface, x, y, w, h, color_background, color_border, active, slave_background)
        self.music_manager = music
        self.playing_music = False
        self.id_music = 'menu'

        self.qty_levels = qty_levels
        self.levels = levels

        # Widgets & labels
        self.label_title = Label(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,   
            y=self.slave_background_rect.h/6,
            w=500,
            h=50,
            color_background=Const.VIOLET,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/bubble/table.png',
            text='Select level',
            text_pos='center',
            font=Const.PATH_FONT,
            font_size=25,
            font_color='white')
        self.button_back = Button(
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=Const.WIDTH_SCREEN-300,
            y=Const.HEIGHT_SCREEN-200,
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
            font_color='white')

        # Sub-form
        self.sub_form_level_selector = SubFormLevelSelector(
            name='sub_form_level_selector',
            main_surface=self.slave_background,
            main_rect=self.slave_background_rect,
            x=self.slave_background_rect.w/2,
            y=self.slave_background_rect.h/2 - 50,
            w=500,
            h=500,
            color_background=Const.BROWN,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/level_select/table2.png',
            color_border='',
            music=music,
            qty_levels=self.qty_levels,
            levels=self.levels
            )

    def update(self, event_list):
        if self.active and not self.playing_music:
            self.music_manager.update(self.id_music)
            self.music_manager.update('select')
            self.playing_music = True

        super().draw()
        self.draw()

        self.get_key_event(event_list)
        self.sub_form_level_selector.update(event_list)

        self.label_title.draw()
        self.button_back.update(event_list)
        self.button_back.draw()

    def draw(self):
        self.slave_background.blit(
            self.sub_form_level_selector.slave_background,
            self.sub_form_level_selector.slave_background_rect)
