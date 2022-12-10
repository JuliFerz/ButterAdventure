import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from aux_func import *


class Bullet:
    def __init__(self, entity, instance, pos_x, flip):
        self.bullet = Aux.Aux.get_surface_from_sprite(Const.PATH_IMAGE+'/assets/bullet/bullet_4.png',1,1)
        '''
        This class represents a bullet where it is instantiated from the player

        :param entity: str
        :param instance: object
        :param pos_x: tuple
        :param flip: bool
        '''
        # entity
        self.entity = entity # NUEVO
        self.pj_instance = instance

        # FPS
        self.anim_frame_rate = 85
        self.frame_sum_anim = 0

        # media
        self.flip_x = flip
        self.frame = 0
        self.image = pygame.transform.flip(self.bullet[self.frame], self.flip_x, False)
        self.rect_pj = pos_x
        self.rect = self.image.get_rect(center = self.rect_pj)
        self.rect.h += 1

        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.is_shooting = False
        self.speed = 17


    def move_rect_x(self):
        self.is_shooting = True
        if self.flip_x:
            self.direction.x = -1
        else:
            self.direction.x = 1
        self.rect.x += self.direction.x * self.speed


    def update(self):
        self.move_rect_x()
    
    def draw(self, surface):
        if self.is_shooting:
            if Const.DEBUG: 
                pygame.draw.rect(surface, Const.RED, self.rect)

            self.image = pygame.transform.flip(self.bullet[self.frame], self.flip_x, False)
            surface.blit(self.image, self.rect)
