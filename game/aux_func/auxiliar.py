import pygame, json, sys
sys.path.append('../game/settings')
from settings import constantes as Const


class Aux:
    @staticmethod
    def get_surface_from_sprite(path, rows, columns, custom_w=0, step=1, custom_btm=0, tile_size=False):
        '''
        It returns a list, which each of elements is a pygame surface

        :param path: str
        :param columns: int
        :param custom_w: int
        :param step: int
        :param custom_btm: int
        :param tile_size: bool
        :returns: A list of pygame surfaces
        '''
        lista = []
        try:
            surface = pygame.image.load(path)
        except:
            print('EXCEPT_IMG-path', path)
            print('EXCEPT_IMG-rows', rows)
            print('EXCEPT_IMG-columns', columns)
        rect = surface.get_rect()
        width_f = int(rect.width / columns)
        height_f = int(rect.height / rows)
        x = 0
        for f in range(0, rows, step):
            for c in range(0, columns, step):
                x = c * width_f
                y = f * height_f
                new_surface = surface.subsurface(x, y, width_f - custom_w, height_f)
                if tile_size:
                    new_surface = pygame.transform.scale(new_surface, (Const.SIZE_TILE, Const.SIZE_TILE))
                lista.append(new_surface)
            x = 0
        return lista

    @staticmethod
    def get_surface_from_files(path, file_name, quantity=0, w=0, h=1, custom_btm=0):
        '''
        It returns a list, which each of elements is a pygame surface
        The files comes from a different files from the other

        :param path: str
        :param file_name: str
        :param quantity: int
        :param w: int
        :param h: int
        :param custom_btm: int
        :returns: A list of pygame surfaces
        '''
        lista = []
        for i in range(quantity):
            surface = pygame.image.load(path+f'{file_name}_00{i}.png').convert_alpha()
            rect = surface.get_rect()
            width_f = rect.width
            height_f = rect.height
            x = 0
            surface = pygame.transform.scale(surface,(w, h))
            
            lista.append(surface)
        return lista


class Json:
    @staticmethod
    def load_json_info(path):
        '''
        It returns a big dictionary which contains all of information from the levels

        :param path: str
        :returns: A dictionary 
        '''
        temp_list = []
        with open(path, 'r') as file:
            temp_list = json.load(file)
        return temp_list
