import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from aux_func import *


class TilePlatform(pygame.sprite.Sprite):
    def __init__(self, name, type, sub_type, x, y, x_to, mvm_frame_rate):
        super().__init__()
        '''
        This class represents a platform that can move in a certain position, or not

        :param name: str
        :param type: str
        :param sub_type: str
        :param x: int
        :param y: int
        :param x_to: int
        :param mvm_frame_rate: int
        '''
        self.name = name
        self.type = type
        self.sub_type = sub_type
        self.x = x
        self.y = y
        self.image = pygame.image.load(
            Const.PATH_IMAGE+'/tileset/{}/{}/{}.png'.format(
                self.type, self.sub_type, self.name
            )).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Const.SIZE_TILE, Const.SIZE_TILE))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.rect_collition = pygame.Rect(
            self.rect.x, self.rect.y + Const.GROUND_RECT_BOTTOM, self.rect.w, self.rect.h - Const.GROUND_RECT_BOTTOM)

        self.x_from = self.rect.x
        self.x_to = x_to
        self.direction = pygame.Vector2(0,0)
        self.moving_r = True
        self.moving_l = False
        self.platform_time = pygame.time.get_ticks()
        self.frame_sum_mov = 0
        self.mvm_frame_rate = mvm_frame_rate

    

    def check_point(self):
        if self.direction.x > 0:
            if self.rect.x == self.x_to:
                self.moving_r = False
                self.direction.x = 0
                self.platform_time = pygame.time.get_ticks()
        else:
            if self.rect.x == self.x_from:
                self.moving_l = False
                self.direction.x = 0
                self.platform_time = pygame.time.get_ticks()


    def move_rect_x(self):
        self.rect.x += self.direction.x
        self.rect_collition.x += self.direction.x
        self.check_point()

    def update(self, delta_ms):
        self.frame_sum_mov += delta_ms
        if self.frame_sum_mov >= self.mvm_frame_rate:
            self.frame_sum_mov = 0

            if self.rect.x != self.x_to or self.rect.x != self.x_from:

                self.current_time = pygame.time.get_ticks()

                if self.current_time > self.platform_time + 500:
                    if self.rect.x < self.x_to and (not self.moving_l): 
                        self.moving_r = True
                        self.direction.x = 2
                    # moving left
                    if self.rect.x > self.x_from and (not self.moving_r): 
                        self.moving_l = True
                        self.direction.x = -2
                    self.move_rect_x()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
