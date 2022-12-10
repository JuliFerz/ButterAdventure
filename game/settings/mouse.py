import pygame
from constantes import *


class Cursor:
    def __init__(self):
        '''
        This class represents the cursor on the screen in all the game
        '''
        self.cursor_0 = pygame.image.load(PATH_IMAGE + '/tileset/cursor/cursor_0.png')
        self.cursor_1 = pygame.image.load(PATH_IMAGE + '/tileset/cursor/cursor_1.png')
        self.image = pygame.transform.scale(self.cursor_0, (17, 18))
        self.rect = self.image.get_rect()

    def update(self, pos, click):
        if click[0]:
            self.image = pygame.transform.scale(self.cursor_1, (17, 18))
        else:
            self.image = pygame.transform.scale(self.cursor_0, (17, 18))
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw(self, surface):
        surface.blit(self.image, self.rect)
