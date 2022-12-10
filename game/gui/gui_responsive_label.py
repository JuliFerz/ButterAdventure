import pygame
from gui.gui_widget import Widget


class ResponsiveLabel(Widget):
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border, text, value, text_pos, font, font_size, font_color):
        super().__init__(main_surface, main_rect, x, y, w, h, color_background, color_border)
        pygame.font.init()
        
        self.main_surface = main_surface
        self.main_rect = main_rect

        # txt
        self.value = value
        self._text = text
        self.text_pos = self.get_text_pos(text_pos)
        self.font = pygame.font.Font(font, font_size)
        self.font_color = font_color

        if self.color_background:
            self.text_render = self.font.render(self._text, True, self.font_color, self.color_background)
        else:
            self.text_render = self.font.render(self._text, True, self.font_color)

    def render(self):
        if self.color_background:
            self.slave_widget_surface.fill(self.color_background)
        try:
            self.slave_widget_surface.blit(self.text_render, self.text_pos)
        except:
            print('EXCEPT_gui_responsive_label', self.text_pos, self._text)

    def update(self, value):
        self.text_render = self.font.render(f'{self._text}{value}', True, self.font_color)

    def draw(self):
        self.main_surface.blit(
            self.slave_widget_surface,
            self.slave_widget_rect_collide)
        self.render()
