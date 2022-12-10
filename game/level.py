import pygame
from settings import *
from manager_modules import *


class Level:
    def __init__(self, level_data, running, surface, music_manager):
        ## Level config ##
        self.display_surface = surface
        self.display_rect = self.display_surface.get_rect()

        self.running = running
        self.music_manager = music_manager
        self.level_data = level_data
        self.setup_level(self.level_data)
    
    def _subscribe_instance(self, list_ent, instance):
        for entity in list_ent:
            entity._manager = instance

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.tiles_movement = pygame.sprite.Group()
        self.traps = []
        self.players = []
        self.enemies = []
        self.items = []

        ## Platforms ##
        for platform in layout['platform']:
            self.tiles.add(platform)
        
        ## Traps ##
        for trap in layout['traps']:
            self.traps.append(trap)

        ## Players ##
        for player in layout['players']:
            player.level_tiles = self.tiles
            self.players.append(player)
        
        ## Enemies ##
        for enemy in layout['enemies']:
            enemy.level_tiles = self.tiles
            self.enemies.append(enemy)
        
        ## Items ##
        for item in layout['items']:
            self.items.append(item)

        ## Managers ##
        self.game_manager = Game_mng.GameManager(self.players, self.enemies, self.items, self.tiles, self.traps, self.display_surface)
        self.bullet_manager = Bullet_mng.BulletManager(self.game_manager, self.music_manager)
        self.enemy_manager = Enemy_mng.EnemyManager(self.game_manager, self.music_manager)
        self.player_manager = Player_mng.PlayerManager(self.game_manager, self.bullet_manager, self.music_manager)
        self.item_manager = Item_mng.ItemManager(self.game_manager, self.music_manager)

        ## Manager subscription (to instances) ##
        self._subscribe_instance(self.players, self.player_manager)
        self._subscribe_instance(self.enemies, self.enemy_manager)
        self._subscribe_instance(self.items, self.item_manager)
        self._subscribe_instance(self.traps, self.game_manager)

    def run(self, delta_ms):
        if Const.DEBUG:
            for tile in self.tiles:
                pygame.draw.rect(self.display_surface, Const.RED, tile.rect)
                pygame.draw.rect(self.display_surface, Const.GREEN, tile.rect_collition)
            for trap in self.traps:
                pygame.draw.rect(self.display_surface, Const.GREEN, trap.rect)

        if self.running:
            self.update(delta_ms)
        self.draw()

    def update(self, delta_ms):
        self.game_manager.check_win()
        self.game_manager.check_lose()
        
        ## Tiles ## 
        for tile in self.tiles:
            if tile.x_to:
                tile.update(delta_ms)
        
        ## Traps ##
        for trap in self.traps:
            trap.update(delta_ms)

        if not self.game_manager.finish:
            ## Enemies ## 
            for i, enemy in enumerate(self.enemies):
                enemy.update(delta_ms)
            
            ## Drop items ##
            for item in self.items:
                item.update(delta_ms)

            ## Players ##
            for i, player in enumerate(self.players):
                player.update(delta_ms)

            ## Manager ##
            self.bullet_manager.update()
            self.enemy_manager.update()

    def draw(self):
        ## Level tiles ##
        self.tiles.draw(self.display_surface)

        ## Traps ##
        for trap in self.traps:
            trap.draw(self.display_surface)

        ## Enemies ## 
        for i, enemy in enumerate(self.enemies):
            enemy.draw(self.display_surface)
        
        ## Drop items ##
        for item in self.items:
            item.draw(self.display_surface)

        ## Players ##
        for i, player in enumerate(self.players):
            player.draw(self.display_surface)
