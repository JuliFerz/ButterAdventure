import pygame, sys
from menu import Menu
from settings import *

screen = pygame.display.set_mode((Const.WIDTH_SCREEN, Const.HEIGHT_SCREEN))
pygame.display.set_caption('Butter Adventure ')
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

level = Menu(screen, Sett.game_levels, Sett.game_config)

pygame.mouse.set_visible(False)
cursor = Cursor.Cursor()
running = True

while running:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    delta_ms = clock.tick(Const.FPS)
    cursor.update(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

    # Execute level
    level.run(event_list, delta_ms)
    
    cursor.draw(screen)
    pygame.display.flip()
    
pygame.quit()
sys.exit()