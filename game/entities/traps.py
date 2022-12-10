import pygame, sys
sys.path.append('../game/settings')
from settings import constantes as Const
from aux_func import auxiliar

class Trap(pygame.sprite.Sprite):
    def __init__(
            self, 
            manager,
            name,
            type, 
            sub_type, 
            anim_frame_rate, 
            rows, 
            columns,
            x, 
            y, 
            x_to):
        super().__init__()
        '''
        This class represents a trap that can hit damage to players

        :param manager: str
        :param name: str
        :param type: str
        :param sub_type: str
        :param anim_frame_rate: int
        :param rows: int
        :param columns: int
        :param x: int
        :param y: int
        :param x_to: int
        '''
        self._manager = manager

        self.name = name
        self.type = type
        self.sub_type = sub_type
        self.x = x
        self.y = y
        self.animation = auxiliar.Aux.get_surface_from_sprite(
            path=Const.PATH_IMAGE+'/tileset/{}/{}/{}.png'.format(
                self.type, self.sub_type, self.name
            ),
            rows=rows,
            columns=columns,
            tile_size=True)

        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.x_from = self.rect.x
        self.x_to = x_to
        self.direction = pygame.Vector2(0,0)
        self.moving_r = True
        self.moving_l = False
        self.platform_time = pygame.time.get_ticks()
        self.frame_sum_anim = 0
        self.anim_frame_rate = anim_frame_rate

    def upd_animation(self, delta_ms):
        self.frame_sum_anim += delta_ms
        if self.frame_sum_anim >= self.anim_frame_rate:
            self.frame_sum_anim = 0

            self.frame += 1
            self.check_frame_index()

    def check_frame_index(self):
        if self.frame + 1 >= len(self.animation):
            self.frame = 0
        
    def rect_collide_pj(self):
        for player in self._manager.list_pjs:
            if self.rect.colliderect(player.rect_collition):
                player.life = 0

    def update(self, delta_ms):
        self.upd_animation(delta_ms)
        self.rect_collide_pj()

    def draw(self, surface):
        self.image = self.animation[self.frame].convert_alpha()
        surface.blit(self.image, self.rect)
