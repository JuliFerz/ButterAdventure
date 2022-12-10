import pygame, sys
import sys
sys.path.append('../game/settings')
from settings import constantes as Const
from aux_func import *


class Character:
    def __init__(
            self,
            manager,
            entity,
            c_type,
            name,
            animations,
            mvm_frame_rate,
            anim_frame_rate,
            control_type,
            level_tiles=[],
            x=0,
            y=0,
            speed_walk=1,
            jump_height=0,
            damage=0.1,
            life=50,
            lives=1):
        '''
        This class represents a player that can attack enemies, take items and gain exp

        :param manager: str
        :param entity: str
        :param c_type: str
        :param name: str
        :param animations: list
        :param mvm_frame_rate: int
        :param anim_frame_rate: int
        :param control_type: str
        :param level_tiles: list
        :param x: int
        :param y: int
        :param speed_walk: int
        :param jump_height: int
        :param damage: int
        :param life: int
        :param lives: int
        '''
        self._manager = manager
        
        # Sprites
        self.type = c_type
        self.name = name
        self.get_animations(animations)

        # Platforms
        self.level_tiles = level_tiles
        self.entity = entity

        # fps
        self.frame = 0
        self.frame_sum_mov = 0
        self.frame_sum_anim = 0
        self.mvm_frame_rate = mvm_frame_rate
        self.anim_frame_rate = anim_frame_rate

        # media
        self.animation = self.animations['stay']
        self.flip_x = False
        self.image = pygame.transform.flip(self.animation[self.frame], self.flip_x, False)

        # main rect
        self.rect = self.image.get_rect()

        # spawn
        self.rect.x = x
        self.rect.y = y
        
        self.rect_collition = pygame.Rect(
            self.rect.x + (self.rect.w / 2) - (self.rect.w / 9),
            self.rect.y,
            (self.rect.w / 3) + 5,
            self.rect.h - 24)

        self.rect_collition.centerx = self.rect.centerx

        # movement
        self.control_type = control_type
        self.speed_walk = speed_walk
        self.speed = self.speed_walk
        self.speed_run = self.speed * 3
        # JUMP
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_height = -jump_height

        self.can_jump = True
        self.is_jumping = False
        self.is_on_floor = False
        self.is_falling = False
        self.on_tile_moving = False

        # others
        self.damage = damage
        self.max_life = life
        self.life = self.max_life
        self.lives = lives
        self.score = 0 # json

        self.bullet_group = []
        self.can_shoot = True
        self.max_qty_bullets = 25
        self.qty_bullets = self.max_qty_bullets

    def get_animations(self, animations: list):
        self.animations = {}
        for anim in animations:
            if not anim.get("custom_cut_w"):
                anim["custom_cut_w"] = 0
            if not anim.get("step"):
                anim["step"] = 1

            self.animations.update(
                {anim['action']: Aux.Aux.get_surface_from_sprite(Const.PATH_IMAGE + f'/{self.type}/players/{self.name}/{anim["fileName"]}', anim["rows"], anim["columns"], anim["custom_cut_w"], anim["step"])[anim["f_from"]:anim["f_to"]]})
        return self.animations

    def control(self):
        list_keys = pygame.key.get_pressed()
        mouse_key_pressed = pygame.mouse.get_pressed()

        if self.control_type == 'A':
            ## X MOVEMENT ##
            if list_keys[pygame.K_d] and not list_keys[pygame.K_a]:
                self.do_walk(False)
            elif list_keys[pygame.K_a] and not list_keys[pygame.K_d]:
                self.do_walk(True)
            elif list_keys[pygame.K_d] and list_keys[pygame.K_a]:
                self.direction.x = 0
            else:
                self.direction.x = 0
            if list_keys[pygame.K_LSHIFT]:
                self.do_sprint()
            else:
                self.speed = self.speed_walk

            ## Y MOVEMENT ##
            if list_keys[pygame.K_w] and (self.is_on_floor or self.can_jump):
                self.do_jump()
            
            ## ACTIONS ##
            if (list_keys[pygame.K_j]) and self.can_shoot:
                self.do_shoot()

            elif (not list_keys[pygame.K_j] and not mouse_key_pressed[0]) and not self.can_shoot:
                self.can_shoot = True

        if self.control_type == 'B':
            ## X MOVEMENT ##
            if list_keys[pygame.K_RIGHT] and not list_keys[pygame.K_LEFT]:
                self.do_walk(False)
            elif list_keys[pygame.K_LEFT] and not list_keys[pygame.K_RIGHT]:
                self.do_walk(True)
            elif list_keys[pygame.K_RIGHT] and list_keys[pygame.K_LEFT]:
                self.direction.x = 0
            else:
                self.direction.x = 0
            if list_keys[pygame.K_RCTRL]:
                self.do_sprint()
            else:
                self.speed = self.speed_walk

            ## Y MOVEMENT ##
            if list_keys[pygame.K_UP] and (self.is_on_floor or self.can_jump):
                self.do_jump()

             ## ACTIONS ##
            if list_keys[pygame.K_m] and self.can_shoot:
                self.do_shoot()
            elif not list_keys[pygame.K_m] and not self.can_shoot:
                self.can_shoot = True

    def do_shoot(self):
        if self.qty_bullets > 0:
            self._manager.sound_effect('shoot')
            self.can_shoot = False
            self.qty_bullets -= 1

            self._manager.shoot(self.entity, self, self.rect_collition.center, self.flip_x)

    def do_walk(self, flip=False):
        if flip:
            self.direction.x = -1
        else:
            self.direction.x = 1
        self.flip_x = flip

    def do_jump(self):
        self._manager.sound_effect('jump')
        self.direction.y = self.jump_height
        self.is_jumping = True
        self.is_on_floor = False
        self.can_jump = False

    def do_sprint(self):
        self.speed = self.speed_run

    def move_rect_x(self):
        self.rect.x += self.direction.x * self.speed
        self.rect_collition.x += self.direction.x * self.speed

    def move_rect_y(self):
        self.rect.y += self.direction.y
        self.rect_collition.y += self.direction.y
        self.apply_gravity()

    def apply_gravity(self):
        self.direction.y += Const.GRAVITY
        if self.direction.y > Const.GRAVITY + 2:
            self.is_falling = True
            self.is_on_floor = False

    def horizontal_collide(self):
        self.move_rect_x()
        for tile in self.level_tiles:
            if tile.rect_collition.colliderect(self.rect_collition):
                if self.direction.x < 0:  # moving left
                    self.rect_collition.left = tile.rect_collition.right
                    self.rect.centerx = self.rect_collition.centerx
                if self.direction.x > 0:  # moving right
                    self.rect_collition.right = tile.rect_collition.left
                    self.rect.centerx = self.rect_collition.centerx

    def vertical_collide(self):
        self.move_rect_y()
        self.on_tile_moving = False
        for tile in self.level_tiles:
            if tile.rect_collition.colliderect(self.rect_collition):
                self.is_jumping = False
                if self.direction.y > 0:  # top - on floor
                    self.rect_collition.bottom = tile.rect_collition.top

                    if tile.x_to and tile.direction.x != 0:
                        self.direction.x = tile.direction.x
                        self.on_tile_moving = True
                        if tile.direction.x < 0:
                            self.rect.x += tile.direction.x 
                            self.rect_collition.x += tile.direction.x 
                        else:
                            self.rect.x += tile.direction.x 
                            self.rect_collition.x += tile.direction.x 

                    self.rect.bottom = self.rect_collition.bottom
                    self.is_on_floor = True
                    self.can_jump = True
                    self.is_falling = False
                if self.direction.y < 0:  # bottom - on ceiling
                    self.rect_collition.top = tile.rect_collition.bottom
                    self.rect.bottom = self.rect_collition.bottom
                    self.is_falling = True
                self.direction.y = 0

            

    def get_animation(self, delta_ms):
        if self.direction.y < 0 and self.is_jumping or self.is_falling:
            self.animation = self.animations['jump']
        elif self.direction.y > 1.6 and self.is_jumping or self.is_falling:
            self.animation = self.animations['jump']
        else:
            if self.is_on_floor:
                if self.direction.x != 0:
                    if not self.on_tile_moving:
                        self.animation = self.animations['walk']
                        self.check_frame_index()
                else:
                    self.animation = self.animations['stay']
                    self.check_frame_index()
        self.upd_animation(delta_ms)

    def upd_animation(self, delta_ms):
        self.frame_sum_anim += delta_ms
        if self.frame_sum_anim >= self.anim_frame_rate:
            self.frame_sum_anim = 0

            self.frame += 1
            self.check_frame_index()

    def check_frame_index(self):
        if self.frame + 1 >= len(self.animation):
            self.frame = 0

    def update(self, delta_ms):
        self.frame_sum_mov += delta_ms
        if self.frame_sum_mov >= self.mvm_frame_rate:
            self.frame_sum_mov = 0

            # movement
            self.control()
            self.vertical_collide()
            self.horizontal_collide()
            self._manager.check_outside_map(self.entity)

            # animation
            self.get_animation(delta_ms)
            self.upd_animation(delta_ms)

    def draw(self, surface):
        if Const.DEBUG:
            pygame.draw.rect(surface, Const.RED, self.rect)
            pygame.draw.rect(surface, Const.BLUE, self.rect_collition)
        self.image = pygame.transform.flip(self.animation[self.frame], self.flip_x, False).convert_alpha()

        surface.blit(self.image, self.rect)