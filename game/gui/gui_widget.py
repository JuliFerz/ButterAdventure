import pygame


class Widget:
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border='', slave_background=''):
        self.main_surface = main_surface
        self.main_rect = main_rect
        self.color_background = color_background
        self.color_border = color_border
        self.x, self.y, self.w, self.h = x, y, w, h

        # slave_widget_surface
        self.slave_widget_surface = pygame.Surface((self.w, self.h))
        self.slave_widget_rect = self.slave_widget_surface.get_rect(
            center=(self.x, self.y))
        self.slave_widget_rect_collide = self.slave_widget_surface.get_rect(
            center=(
                self.x + self.main_rect.x,
                self.y + self.main_rect.y
            ))
        
        self.slave_background = ''
        if slave_background:
            try:
                self.slave_background = pygame.image.load(slave_background).convert_alpha()
            except:
                print('EXCEPT_gui_widget', slave_background)
            self.slave_background = pygame.transform.scale(self.slave_background,(self.w, self.h))
            self.slave_background_rect = self.slave_background.get_rect(
                center=(self.x, self.y))

            self.slave_background_rect_collide = self.slave_background.get_rect(
                center=(
                    self.x + self.main_rect.x, 
                    self.y + self.main_rect.y
                ))

    def get_text_pos(self, pos):
        if self.slave_background:
            if pos == 'left':
                self.text_pos = (15, self.slave_background_rect_collide.h/4)
            elif pos == 'center':
                self.text_pos = (self.slave_background_rect_collide.w/4, self.slave_background_rect_collide.h/4)
            elif pos == 'center_minus':
                self.text_pos = (self.slave_background_rect_collide.w/3 - (self.slave_background_rect_collide.w/8), self.slave_background_rect_collide.h/4)
            elif pos == 'center_plus':
                self.text_pos = (self.slave_background_rect_collide.w/3 + (self.slave_background_rect_collide.w/25), self.slave_background_rect_collide.h/4)
            elif pos == 'right':
                self.text_pos = (self.slave_background_rect_collide.w/4, 0)
        else:
            if pos == 'left':
                self.text_pos = (15, self.slave_widget_rect_collide.h/4)
            elif pos == 'center':
                self.text_pos = (self.slave_widget_rect_collide.w/4, self.slave_widget_rect_collide.h/4)
            elif pos == 'center_plus':
                self.text_pos = (self.slave_widget_rect_collide.w/3 + (self.slave_widget_rect_collide.w/25), self.slave_widget_rect_collide.h/4)
            elif pos == 'right':
                self.text_pos = (self.slave_widget_rect_collide.w/4, 0)
        return tuple(map(lambda el: int(el), self.text_pos))

    def draw(self):
        if self.slave_background:
            self.main_surface.blit(self.slave_background,self.slave_background_rect)
        else:
            self.main_surface.blit(self.slave_widget_surface,self.slave_widget_rect)
