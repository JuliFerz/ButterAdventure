import sys
sys.path.append('../game/settings')
from settings import constantes as Const
from entities import *


class PlayerManager():
    def __init__(self, game_manager, bullet_manager, music_manager):
        '''
        This class represents a manager for the player. It allows to player to shoot, play sounds, and more stuff

        :param game_manager: object
        :param bullet_manager: object
        :param music_manager: object
        '''
        self.__game_manager = game_manager
        self.__bullet_manager = bullet_manager
        self.music_manager = music_manager
        self.is_collide_enemy = False

    def sound_effect(self, id):
        self.music_manager.update(id)

    def shoot(self, entity, instance, pos_x, flip, delta_ms=''):
        shoot = Bullets.Bullet(entity, instance, pos_x, flip)
        self.__bullet_manager.bullet_group.append(shoot)

    def check_outside_map(self, entity):
        for player in self.__game_manager.list_pjs:
            if player.rect_collition.top > Const.WIDTH_SCREEN and player.entity == entity:
                player.life = 0
    
    def get_damage(self, entity, enemy_entity):
        for i, player in enumerate(self.__game_manager.list_pjs):
            for enemy in self.__game_manager.list_enemies:
                if player.entity == entity and enemy.entity == enemy_entity:
                    player.life -= 1
                    pass
                if player.life <= 0:
                    self.music_manager.update('explosion')
                    self.__game_manager.eliminate_player(i)
                    break
