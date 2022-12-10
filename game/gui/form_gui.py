import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const


class Form:
    dict_forms = {}
    def __init__(self, name, main_surface, x, y, w, h, color_background, color_border, active, slave_background=''):
        self.dict_forms[name] = self

        self.__main_surface = main_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
        if Const.DEBUG:
            print('⭕ Form_gui instance')

        # slave surface
        self.slave_surface = pygame.Surface((self.w, self.h))
        self.slave_rect = self.slave_surface.get_rect(topleft=(self.x, self.y))
        self.active = active
    
        self.background_img = pygame.image.load(f'{Const.PATH_IMAGE}/gui/background.png').convert_alpha()
        self.background_rect = self.background_img.get_rect(topleft=(0,0))
        self.background_img = pygame.transform.scale(self.background_img,(Const.WIDTH_SCREEN, Const.HEIGHT_SCREEN))

        self.slave_background=''
        if slave_background:
            try:
                self.slave_background = pygame.image.load(slave_background).convert_alpha()
            except:
                print('EXCEPT_form_gui', slave_background, name)
            self.slave_background_rect = self.slave_background.get_rect(topleft=(self.x, self.y))
            self.slave_background = pygame.transform.scale(self.slave_background,(self.w, self.h))

    def get_key_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.on_click('form_main_menu')

    def update_view_form(self, id):
        for form in self.dict_forms.values():
            form.active = False
            form.playing_music = False
        self.dict_forms[id].active = True

    def on_click(self, id):
        if id == 'exit':
            sys.exit()
        else:
            self.update_view_form(id)

    def draw(self):
        self.__main_surface.blit(self.background_img, self.background_rect)
        
        if self.slave_background:
            self.__main_surface.blit(self.slave_background, self.slave_background_rect)
        else:
            self.__main_surface.blit(self.slave_surface, self.slave_rect)
