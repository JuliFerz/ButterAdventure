from settings import *

class GameManager:
    def __init__(self, list_pjs, list_enemies, items, list_platform, list_traps, surface):
        '''
        This class represents a manager for all the game. It can manage if the game ends with player's win, or player's lose

        :param list_pjs: list
        :param list_enemies: list
        :param items: list
        :param list_platform: list
        :param list_traps: list
        :param surface: list
        '''
        self.list_pjs = list_pjs
        self.list_enemies = list_enemies
        self.items = items
        self.required_items = self.get_required_items(items)
        self.list_platform = list_platform
        self.list_traps = list_traps
        self.surface = surface

        self.ok_enemies = False
        self.ok_items = False
        self.ok_fruits = False
        self.finish = False
        self.win = False
        self.lose = False
        self.sql = Sql.Sql()

    def get_required_items(self, items):
        temp_list = []
        for item in items:
            if item.required:
                temp_list.append(item)
        return temp_list

    def check_win(self):
        if len(self.list_enemies) == 0:
            self.ok_enemies = True
        if len(self.required_items) == 0:
            self.ok_items = True

        if self.ok_enemies and self.ok_items:
            self.win = True
            self.finish = True
    
    def check_lose(self):
        if self.list_pjs:
            for player in self.list_pjs:
                if player.life <= 1:
                    self.lose = True
                    self.finish = True
        else:
            self.lose = True
            self.finish = True

    def create_record(self, name, score, time):
        self.sql.create_record(name, score, time)
        
    def eliminate_enemy(self, index):
        del self.list_enemies[index]

    def eliminate_player(self, index):
        del self.list_pjs[index]
