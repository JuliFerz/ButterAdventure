import pygame
from gui.gui_widget import Widget


class Button(Widget):
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border, on_click, on_click_param, text, text_pos, font, font_size, font_color, on_click_param_aux='', slave_background='', active=True):
        super().__init__(main_surface, main_rect, x, y, w, h, color_background, color_border, slave_background)
        pygame.font.init()
        self.active = active

        self.main_surface = main_surface
        self.main_rect = main_rect

        # fn buttons
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.on_click_param_aux = on_click_param_aux

        # txt
        self._text = text
        self.text_pos = self.get_text_pos(text_pos)
        self.font = pygame.font.Font(font, font_size)
        self.font_color = font_color

    def click_collition(self, mouse_xy):
        if self.slave_background:
            if self.slave_background_rect_collide.collidepoint(mouse_xy) and \
                self.main_rect.collidepoint(mouse_xy):
                
                if self.on_click_param_aux or self.on_click_param_aux == 0:
                    self.on_click(self.on_click_param, self.on_click_param_aux)
                else:
                    self.on_click(self.on_click_param)
        else:
            if self.slave_widget_rect_collide.collidepoint(mouse_xy) and \
                self.main_rect.collidepoint(mouse_xy):
                
                if self.on_click_param_aux or self.on_click_param_aux == 0:
                    self.on_click(self.on_click_param, self.on_click_param_aux)
                else:
                    self.on_click(self.on_click_param)

    def get_mouse_click(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                self.click_collition(event.pos)
            
    def render(self):
        if self.slave_background:
            self.text_render = self.font.render(self._text, True, self.font_color)
            self.slave_background.blit(self.text_render, self.text_pos)
        else:
            self.text_render = self.font.render(self._text, True, self.font_color, self.color_background)
            self.slave_widget_surface.fill(self.color_background)
            self.slave_widget_surface.blit(self.text_render, self.text_pos)
    
    def update(self, event_list):
        self.get_mouse_click(event_list)
    
    def draw(self):
        super().draw()
        self.render()
