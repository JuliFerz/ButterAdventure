import pygame
import random


class EnemyManager():
    def __init__(self, game_manager, music_manager):
        '''
        This class represents a manager for enemies. It allows to enemy to see and hit damage to player, and more stuff

        :param game_manager: object
        :param music_manager: object
        '''
        self.__game_manager = game_manager
        self.music_manager = music_manager
        self.pj_instance = ''

    def cooldown_action(self):
        self.time = pygame.time.get_ticks()
        self.cooldown = random.randrange(0, 1000, 500)

    def get_damage(self, entity_enemy, rect_pos_pj, pj_instance):
        self.rect_pj = rect_pos_pj[0]
        self.pj_instance = pj_instance

        for i, enemy in enumerate(self.__game_manager.list_enemies):
            if enemy.entity == entity_enemy:
                enemy.in_vision_pj = True
                enemy.is_collide_x = False
                enemy.random_x = self.rect_pj
                enemy.auto_movement()
                enemy.life -= 1
            if enemy.life <= 0:
                self.__game_manager.eliminate_enemy(i)
                self.music_manager.update('explosion')
                self.pj_instance.score += enemy.points
                break

    def horizontal_collide_pj(self, entity):
        for enemy in self.__game_manager.list_enemies:
            if enemy.in_vision_pj and enemy.rect_collition.colliderect(self.rect_pj):
                enemy.collide_pj = True

                if enemy.entity == entity:
                    self.pj_instance._manager.get_damage(self.pj_instance.entity, enemy.entity)
            else:
                enemy.collide_pj = False

    def update_dir_movement(self):
        for enemy in self.__game_manager.list_enemies:
            if enemy.in_vision_pj:
                enemy.random_x = self.rect_pj.centerx

    def detect_vision(self):
        if self.__game_manager.list_enemies and self.__game_manager.list_pjs:
            for enemy in self.__game_manager.list_enemies:
                for player in self.__game_manager.list_pjs:

                    if enemy.rect_detect.colliderect(player.rect_collition):
                        self.rect_pj = player.rect
                        self.pj_instance = player
                        enemy.in_vision_pj = True
                        break
                    else:
                        enemy.in_vision_pj = False
        else:
            for enemy in self.__game_manager.list_enemies:
                enemy.in_vision_pj = False

    def update(self):
        self.detect_vision()
        self.update_dir_movement()
