import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from level import Level
from gui.form_gui import Form
from gui.sub_form_pause_game import SubFormPauseGame
from gui.sub_form_game_hud import SubFormGameHud
import time


class FormPlayLevel(Form):
    def __init__(self, name, main_surface, x, y, w, h, color_background, color_border, active, running, music):
        super().__init__(name, main_surface, x, y, w, h, color_background,  color_border, active,)
        self.music_manager = music
        self.playing_music = False
        self.id_music = 'background'
        self.win = False
        self.lose = False

        self.main_surface = main_surface
        self.running = running
        self.finish_time = '---'
        self.finish_score = '---'
        self.finish = False

        self.sub_form_pause_game = SubFormPauseGame(
            name='sub_form_pause_game',
            main_surface=self.slave_surface,
            main_rect=self.slave_rect,
            x=self.slave_rect.w/2,
            y=self.slave_rect.h/2,
            w=500,
            h=500,
            color_background=Const.BROWN,
            slave_background=f'{Const.PATH_IMAGE}/gui/jungle/settings/table.png',
            color_border='',
            active=False,
            music=music
            )

    def get_background(self, l_image):
        self.background_image = pygame.image.load(
            '{}/locations/{}/{}/{}.png'.format(
                Const.PATH_IMAGE,
                l_image['set'],
                l_image['type'],
                l_image['image']
            ))
        self.background_image = pygame.transform.scale(
            self.background_image, 
            (self.w, self.h)
            )
        return self.background_image.convert_alpha()
    
    def get_key_event(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.running:
                        self.running = False
                        self.level.running = False
                        self.sub_form_pause_game.active=True
                        self.playing_music = False
                    else:
                        self.running = True
                        self.level.running = True
                        self.sub_form_pause_game.active=False

    def change_level(self, level, id):
        self.restart_time = time.perf_counter()
        self.running = True 
        self.finish = False
        self.win = False
        self.lose = False

        self.id = id
        self.game_level = level
        self.level = Level(
            level_data=self.game_level[0],
            running=self.running,
            surface=self.slave_surface,
            music_manager=self.music_manager
        )
        self.background_image = self.get_background(self.game_level[0]['background'])

        self.sub_form_game_hud = SubFormGameHud(
            name='sub_form_game_hud', 
            main_surface=self.slave_surface, 
            main_rect=self.slave_rect, 
            x=0, 
            y=0, 
            w=self.slave_rect.w, 
            h=self.slave_rect.h, 
            image_background=self.background_image, 
            color_border='', 
            levels=0, 
            qty_levels=0, 
            active=True,
            score=self.level.level_data['players'][0].score,
            max_life=self.level.level_data['players'][0].max_life,
            life=self.level.level_data['players'][0].life,
            bullets=self.level.level_data['players'][0].qty_bullets,
            time=time.perf_counter()
        )

    def update_pj_info(self, player):
        self.score = player.score
        self.life = player.life
        self.bullets = player.qty_bullets

    def update(self, event_list, delta_ms):
        if self.active and not self.playing_music:
            self.music_manager.update(self.id_music)
            self.music_manager.update('select')
            self.playing_music = True
        
        self.update_pj_info(self.level.level_data['players'][0])

        if self.level.game_manager.finish:
            if self.level.game_manager.win:
                self.win = True
            elif self.level.game_manager.lose:
                self.lose = True
            self.finish_time = self.current_time
            self.finish_score = self.score
                
            self.running = False
            self.finish = True
            self.active = False
        else:
            self.current_time = time.perf_counter() - self.restart_time
            if self.current_time >= 60.2:
                self.finish_time = self.current_time
                self.finish_score = self.score
                self.finish = True
                self.lose = True
                self.active = False
                super().on_click('form_finish_level')

        self.draw()
    
        if not self.running and self.finish:
            self.level.run(delta_ms)
        elif not self.running:
            self.sub_form_pause_game.update(event_list)
        elif self.running:
            self.sub_form_game_hud.update(self.score, self.life, self.bullets, self.current_time)
            self.level.run(delta_ms)
            
        self.get_key_event(event_list)


    def draw(self): 
        super().draw()
        if self.sub_form_pause_game.active:
            self.main_surface.blit(
                self.sub_form_pause_game.slave_background,
                self.sub_form_pause_game.slave_background_rect)
                
            self.sub_form_pause_game.draw()
        elif self.running:
            self.slave_surface.blit(
                self.sub_form_game_hud.slave_surface,
                self.sub_form_game_hud.slave_rect
            )
        elif self.finish:
            self.on_click('form_finish_level')
