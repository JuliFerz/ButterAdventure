'''
This file represents all the functions that allows the level manager to take all the levels from the JSON file
'''
import pygame
from settings.constantes import *
from entities import *
from aux_func import *

game_levels = Aux.Json.load_json_info(PATH_JSON + '/levels.json')
game_config = Aux.Json.load_json_info(PATH_JSON + '/config.json')

def check_name(obj):
    name = None
    if obj['sub_type'] == 'Tiles':
        name = '{}'.format(obj['image'])
    else:
        if obj['image'] > 1:
            name = '{} ({})'.format(obj['name'], obj['image'])
        else:
            name = '{}'.format(obj['name'])
    return name

def get_platforms(platforms):
    temp_list = []
    for obj in platforms:
        name = check_name(obj)
        temp_list.append(Platform.TilePlatform(
            name=name,
            type=obj['type'],
            sub_type=obj['sub_type'],
            x=obj['x'],
            y=obj['y'],
            x_to=obj.get('x_to') or 0,
            mvm_frame_rate=obj.get('mvm_frame_rate') or 0
        ))
    return temp_list
    
def get_traps(traps):
    temp_list = []
    for obj in traps:
        temp_list.append(Trap.Trap(
            manager='',
            name=obj['image'],
            type=obj['type'],
            sub_type=obj['sub_type'],
            anim_frame_rate=obj.get('anim_frame_rate') or 0,
            rows=obj.get('rows') or 1,
            columns=obj.get('columns') or 1,
            x=obj['x'],
            y=obj['y'],
            x_to=obj.get('x_to') or 0
        ))
    return temp_list

def get_players(l_players):
    temp_list = []
    i = 1
    for player in l_players:
        temp_list.append(Character.Character(
                manager = '',
                entity = f'player_{i}',
                c_type = player['type'],
                name = player['name'],
                animations = player['actions'],
                mvm_frame_rate = player['mvm_frame_rate'],
                anim_frame_rate = player['anim_frame_rate'],
                control_type=player['control']['type'],
                level_tiles='',
                x = player['x'],
                y = player['y'],
                speed_walk = player['speed_walk'],
                jump_height = player['jump_height'],
                damage = player['damage'],
                life = player['life'],
                lives = player['lives']
            ))
        i += 1
    return temp_list

def get_enemies(l_enemies):
    temp_list = []
    i = 1
    for enemy in l_enemies:
        temp_list.append(Enemy.Enemy(
                manager='',
                entity=f'enemy_{i}',
                c_type = enemy['type'],
                name = enemy['name'],
                animations = enemy['actions'],
                separate_files=enemy['separate_files'],
                mvm_frame_rate = enemy['mvm_frame_rate'],
                anim_frame_rate = enemy['anim_frame_rate'],
                level_tiles = [],
                x = enemy['x'],
                y = enemy['y'],
                speed_walk = enemy['speed_walk'],
                points = enemy.get('points') or 10,
                damage = enemy['damage'],
                life = enemy['life'],
                lives = enemy['lives']
            ))
        i += 1
    return temp_list

def get_items(l_items):
    temp_list = []
    i = 1
    for item in l_items:
        temp_list.append(Item.Item(
                manager = '',
                entity = f'item_{i}',
                c_type = item['type'],
                sub_type = item['sub_type'],
                name = item['name'],
                mvm_frame_rate = item.get('mvm_frame_rate') or 1,
                anim_frame_rate = item.get('anim_frame_rate') or 1,
                rows=item.get('rows') or 1,
                columns=item.get('columns') or 1,
                points = item.get('points') or 0,
                health = item.get('health') or 0,
                bullets= item.get('bullets') or 0,
                required = item.get('required') or False,
                level_tiles = [],   
                scale=50,
                x = item['x'],
                y = item['y']
            ))
        i += 1
    return temp_list

def get_levels(levels, id):
    return [{
        'id': id,
        'background': levels['background'],
        'platform': get_platforms(levels['platforms']),
        'traps': get_traps(levels['traps']),
        'players': get_players(levels['players']),
        'enemies': get_enemies(levels['enemies']),
        'items': get_items(levels['items']),  
    }]

def get_music(music):
    return pygame.mixer.Sound(f'{PATH_SOUNDS}/{music}')

def get_game_config(config):
    pygame.mixer.init()
    temp_dict = {'music':{}}
    # load music
    for key, value in config['music'].items():
        temp_dict['music'][key] = get_music(value)
    return temp_dict
